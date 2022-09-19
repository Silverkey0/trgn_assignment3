import sys,re
if __name__ == '__main__':
	content=""
	argv_len=len(sys.argv)
	if argv_len==2:
		for line in open(sys.argv[1],"r"):
			content=content+line

	res = re.search('(?P<countryCode>\d{2})-(?P<AreaCode>\d{2})-(?P<localPhoneNumber1>\d{4})-(?P<localPhoneNumber2>\d{4})(?P<msg>.*)(?P<a>\d{3})-(?P<b>\d{3})-(?P<c>\d{4})',content)
	result=res.groupdict()

	print("+"+result['countryCode']+" ("+result['AreaCode']+") "+result['localPhoneNumber1']+result['localPhoneNumber2'])
	print("("+result['a']+") "+result['b']+result['c'])