import os,sys,re,getopt

def get_value(keyname,content):
	p = re.compile(r''+keyname+' \"(.*?)\"' )
	for v in  p.findall(content):
	    return v


def main(argv):
	argv_count=len(argv)
	if argv_count>1:
		content=""
		dicts={}
		number = ''
		try:
		  opts, args = getopt.getopt(argv,"f:",["number="])
		except getopt.GetoptError:
		  print('python3 ensg2hugo.py -f<number> <output>')
		  sys.exit(2)
		for opt, arg in opts:
		  if opt in ("-f", "--ifile"):
		     number = arg




		i=0
		for content in open("Homo_sapiens.GRCh37.75.gtf","r"):
			i=i+1
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
				dicts[gene_id]={}
				dicts[gene_id]['gene_id']=gene_id;
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

		if os.path.exists(sys.argv[2]):
			# print('"","gene_id","gene_type","logFC","AveExpr"')
			for csv in open(sys.argv[2],"r"):
				p=csv.split(",")
				n2=p[1]
				# and n2 !="\"gene_id\""
				if n2.find('.') != -1 :
					gene_id=n2.split(".")
					gene_id=gene_id[0].replace("\"","")

					if int(number)==2:
						if gene_id in dicts:
							result =p[0]+",\""+dicts[gene_id]['gene_name']+"\","+p[2]+","+p[3]+","+p[4].replace("\n","")
							print(result)
					else:
						result =p[0]+p[1]+","+p[2]+","+p[3]+","+p[4].replace("\n","")
						print(result)
					
		else:
			print(sys.argv[2]+" not exist")
	else:
		print('python3 ensg2hugo.py -f<number> <output>')

if __name__ == '__main__':
	main(sys.argv[1:])