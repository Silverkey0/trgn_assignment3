
# extract_phonenum.py

## USAGE
python3 extract_phonenum.py mytextfile.txt

## DESCRIPTION
Extracts phone numbers from a text file, and prints formatted phone numbers.
One-line per phone number formatted as [+][country code] ([AreaCode]) [local phone number]. [+][country code] optional output if number is international. Create a script called extract_phonenum.py which extracts phone numbers from text file.

## KNOWN ISSUES
It seems like there isn't too many issues. The only problem is that you don't upload the file, mytextfile.txt. So, I creat another file, example1.txt, and test my program on it. It works well.

# ensg2hugo.py

## USAGE
python3 ensg2hugo.py [-f][0-9] [file]

## DESCRIPTION
Key hints. You need to read the Homo_sapiens.GRCh37.75.gtf to create a dictionary, whereby you lookup the Ensembl name and replace it with the HUGO name.

## KNOWN ISSUES
You didn't upload the file, Homo_sapiens.GRCh37.75.gtf, either. So, I found a .gtf file, named Homo_sapiens.GRCh37.75.formatted.gtf, and downloaded it. I tried to extract four columns from this file, and altered the first column from gene_id to gene_name. But I could only extract columns from this file. So, I still need to figure out how to build the dictionary and to replace columns. Though my program is totally wrong, I still pushed my work to Github to prove my efforts. 

# histogram.py

## USAGE
python3 histogram.py [-f][0-9] [file]

## DESCRIPTION
Creates a histogram as a png from a file using the specified column in a tab delimited file.

## KNOWN ISSUES
I can't understand what this homework asks me to do. I will figure it out on Tuesday class.