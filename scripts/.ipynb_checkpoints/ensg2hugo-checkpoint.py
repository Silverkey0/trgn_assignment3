import os,sys,re,getopt

def get_value(keyname,content):
	p = re.compile(r''+keyname+' \"(.*?)\"' )#'+keyname+'和\"(.*?)\"的意思是什么？
	for v in  p.findall(content):
	    return v#为什么要用return，return的作用是什么？在什么情况下用？


def main(argv): #这里的main(argv)有具体含义吗？还是只是字符
	argv_count=len(argv) #这里是数参数的意思吗？
	if argv_count>1:
		content="" #content=""的意思和用法是什么？
		dicts={} #这是建dictionary的意思吗？
		number = '' #同上，不知道这个的意思和用法
		try:
		  opts, args = getopt.getopt(argv,"f:",["number="]) #opts is a simple python library which allows you to easiely parse command line arguments.args is the argument list to be parsed, without the leading reference to the running program. Typically, this means sys.argv[1:]. f is the string of the option column that the script wants to recognize, with options that require an argument followed by a colon (':'; i.e., the same format that Unix getopt() uses)."number" is a list of strings with numbers.
		except getopt.GetoptError:#This module helps scripts to parse the command line arguments in sys.argv. It supports the same conventions as the Unix getopt() function (including the special meanings of arguments of the form ‘-’ and ‘--‘).
#opts, args = getopt.getopt(argv,"f:",["number="])怎么用？getopt.GetoptError在这里是什么意思？
		  print('python3 ensg2hugo.py -f<number> <output>')
		  sys.exit(2) #在这里是什么意思？
		for opt, arg in opts:
		  if opt in ("-f", "--ifile"):
		     number = arg
#for opt, arg in opts:
#if opt in ("-f", "--ifile"):
#number = arg
#这块儿我都没懂


		i=0
		for content in open("Homo_sapiens.GRCh37.75.gtf","r"):
			i=i+1 #i=i+1是啥意思？我看后面i都没出现过了。
			# print(content)
			gene_id=get_value("gene_id",content)
			transcript_id=get_value("transcript_id",content)
			exon_number=get_value("exon_number",content)
			gene_name=get_value("gene_name",content)
			gene_source=get_value("gene_source",content)
			gene_biotype=get_value("gene_biotype",content)
			transcript_name=get_value("transcript_name",content)
			transcript_source=get_value("transcript_source",content)
			exon_id=get_value("exon.id",content)

			if  gene_id is not None:
				dicts[gene_id]={} #extract gene_id into dictionary.
				dicts[gene_id]['gene_id']=gene_id; #这儿的意思我不确定，是在建立对应关系吗？就是用gene_id建立dictionary后，根据不同的gene_id来对应其他的数据?
				if  transcript_id is not None:
					dicts[gene_id]['transcript_id']=transcript_id;

				if  exon_number is not None:
					dicts[gene_id]['exon_number']=exon_number;

				if  gene_name is not None:
					dicts[gene_id]['gene_name']=gene_name;

				if  gene_source is not None:
					dicts[gene_id]['gene_source']=gene_source;

				if  gene_biotype is not None:
					dicts[gene_id]['gene_biotype']=gene_biotype;

				if  transcript_name is not None:
					dicts[gene_id]['transcript_name']=transcript_name;

				if  transcript_source is not None:
					dicts[gene_id]['transcript_source']=transcript_source;

				if  exon_id is not None:
					dicts[gene_id]['exon_id']=exon_id;

		if os.path.exists(sys.argv[2]): #check whether the csv document exists or not. 
			if int(number)==2: #The int() converts number to integer and returns.
                #int(number)==2是啥意思？int()的用法是？
				print('"","gene_name","gene_type","logFC","AveExpr"')
			else:
				print('"","gene_id","gene_type","logFC","AveExpr"')
			for csv in open(sys.argv[2],"r"):
				p=csv.split(",") #splits a string into a list with a seperator ",".
				n2=p[1]
				# and n2 !="\"gene_id\""
				if n2.find('.') != -1 :
					gene_id=n2.split(".")
					gene_id=gene_id[0].replace("\"","") #从n2=p[1]到这儿都没懂

					if int(number)==2:
						if gene_id in dicts:
							result =p[0]+",\""+dicts[gene_id] #这个result的内容我没看懂。
['gene_name']+"\","+p[2]+","+p[3]+","+p[4].replace("\n","") #这一行代码为什么跳出了前一个逻辑？为什么要把空格替换成\n？\n不是一行末尾的意思吗？
							print(result)
					else:
						result =p[0]+p[1]+","+p[2]+","+p[3]+","+p[4].replace("\n","")
						print(result)
					
		else:
			print(sys.argv[2]+" not exist")
	else:
		print('python3 ensg2hugo.py -f<number> <output>')

if __name__ == '__main__':
	main(sys.argv[1:]) #这里的意思是该脚本从第一个导入的参数开始处理吗？这能放在脚本的开头吗？