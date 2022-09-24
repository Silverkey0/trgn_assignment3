import os,sys,re,getopt

if __name__ == '__main__':
	content=""
	argv_len=len(sys.argv)
	if argv_len>1:
		for line in open(sys.argv[1],"r"):
			p = re.compile(r'(\+\d{2}){0,1}(\-){0,1}(\d{2,3})-(\d{3,4})-(\d{3,4})' )
			for v in  p.findall(line):
				# print(v)
				if v[0] is not None:
					result=v[0]+" ("+v[2]+") "+v[3]+v[4]
					print(result)
				else:
					result="("+v[2]+")"+v[3]+v[4]
					print(result)