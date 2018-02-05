# -*- coding: utf-8 -*-
import os, optparse, datetime, time, dns.resolver, csv
from pytz import timezone

resolver = dns.resolver.Resolver()
resolver.nameservers = ['8.8.8.8'] #google
subnameservers = ['208.67.222.222'] #opendns

def setCsv(cnt, domain, ip):
	if not os.path.isfile('./reverseip.csv'):
		f = open('./reverseip.csv', 'w', newline='')
		wr = csv.writer(f)
		title = ['연변', '시간정보(GMT+9)', '대상 도메인', 'IP주소', '조회한 DNS 서버 IP 주소']
		wr.writerow(title)
		f.close()
	f = open('./reverseip.csv', 'a', newline='')
	wr = csv.writer(f)
	fread = open('./reverseip.csv', 'r')
	lines = fread.readlines()
	
	if len(lines) > 1:
		last_line = lines[len(lines)-1]
		cnt = int(last_line.split(',')[0]) + 1

	ctime = datetime.datetime.now(timezone('Asia/Seoul'))
	datas = [cnt, ctime, domain, ip, resolver.nameservers[0]]
	wr.writerow(datas)

def checkDns(domain):
	try:
		ip = []
		answers = resolver.query(domain, 'A')
		for rdata in answers:
			ip.append(rdata.address)
		return ip
	except (dns.exception.Timeout, dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
		resolver.nameservers = subnameservers
		answers = resolver.query(domain, 'A')
		for rdata in answers:
			ip.append(rdata.address)
		return ip

def parseDomain(url):
	domain = url.replace('http://','')
	domain = domain.replace('https://','')
	idx = domain.find('/')
	if idx > 0:
		domain = domain[:idx]
	return domain

def main():
	parser = optparse.OptionParser('usage dns_query.py --target domain_name')
	parser.add_option('--target', dest="target", help="Input Domain")

	(options, args) = parser.parse_args()

	target = options.target

	if target == None:
		print (parser.usage)
		exit(0)
    
	cnt = 1
	while True:
		domain = parseDomain(target)
		ips = checkDns(domain)
		ip = str(ips[0])
		setCsv(cnt, domain, ip)
		cnt += 1
		time.sleep(1)

if __name__ == '__main__':
	main()
