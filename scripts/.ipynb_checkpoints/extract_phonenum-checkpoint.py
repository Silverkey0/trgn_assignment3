import os,sys,re,getopt

if __name__ == '__main__': #runs blocks of code only when our Python script is being executed directly from a user.
	content="" #content=""的意思和用法是什么？
	argv_len=len(sys.argv) #len()- function is used to count the number of arguments passed to the command line. Since the iteration starts with 0, it also counts the name of the program as one argument. The first argument, sys.argv[0], is always the name of the program as it was invoked,and sys.argv[1] is the first argument you pass to the program.
	if argv_len>1: #if the argument I pass to the program>1
		for line in open(sys.argv[1],"r"): #open the file contain this argument in row.
			p = re.compile(r'(\+\d{2}){0,1}(\-){0,1}(\d{2,3})-(\d{3,4})-(\d{3,4})' ) #re.compile() method is used to compile a regular expression pattern provided as a string into a regex pattern object (re.Pattern). Later we can use this pattern object to search for a match inside different target strings using regex methods such as a re.findall() or re.search().
			for v in  p.findall(line): #use defined p to find all matched numbers in line. 
				# print(v)，v在这里的意思是？
				if v[0] is not None:
					result=v[0]+" ("+v[2]+") "+v[3]+v[4] #能解释下这个result的意思吗？
					print(result)
				else:
					result="("+v[2]+")"+v[3]+v[4]
					print(result)