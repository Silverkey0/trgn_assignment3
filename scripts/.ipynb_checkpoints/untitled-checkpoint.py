import sys,re

file = "mytextfile.txt"

if __name__ == '__main__':
	content=""
	argv_len=len(sys.argv)
	if argv_len>1:
		for line in open(sys.argv[1],"r"):
			text=line
			phoneNumRegex = re.compile("(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}")
			content = re.findall(phoneNumRegex,text)
			print(content)