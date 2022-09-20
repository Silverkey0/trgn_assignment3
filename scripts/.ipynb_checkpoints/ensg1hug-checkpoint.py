import sys,re

if __name__ == '__main__':
	content=""
	with open('1.tsv','a') as filewrite:
		filewrite.write("\"gene_id\",\"gene_biotype\",\"transcript_name\",\"exon.id\"\r\n")
		print("\"gene_id\",\"gene_biotype\",\"transcript_name\",\"exon.id\"")
		for line in open("Homo_sapiens.GRCh37.75.formatted.gtf","r"):
			n=line.split('	')
			l=n[8].split(";")
			data={}
			for v in l:
				m=v.strip().split(" ")
				if len(m)==2:
					data[m[0]]=m[1]
			print(data['gene_id']+","+data['gene_biotype']+","+data['transcript_name']+","+data['exon_id'])
			filewrite.write(data['gene_id']+","+data['gene_biotype']+","+data['transcript_name']+","+data['exon_id']+"\r\n")