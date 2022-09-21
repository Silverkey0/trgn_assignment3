
# extract_phonenum.py

## USAGE
python3 extract_phonenum.py mytextfile.txt

## DESCRIPTION
Extracts phone numbers from a text file, and prints formatted phone numbers.
One-line per phone number formatted as [+][country code] ([AreaCode]) [local phone number]. [+][country code] optional output if number is international. Create a script called extract_phonenum.py which extracts phone numbers from text file.

## KNOWN ISSUES


# ensg2hugo.py

## USAGE
python3 ensg2hugo.py [-f][0-9] [file]

## DESCRIPTION
Use ensg2hugo.py to read the Homo_sapiens.GRCh37.75.gtf to create a dictionary, and lookup the Ensembl name and replace it with the HUGO name.
To get Homo_sapiens.GRCh37.75.gtf, download the file below and unzip it.
```
curl ftp://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz -O / --remote-name
```

## KNOWN ISSUES
I tried to extract two columns, gene_id and gene_name from this file, and altered the first column from gene_id to gene_name. But I could only extract columns from this file. So, I still need to figure out how to build the dictionary and to replace columns. 

# histogram.py

## USAGE
python3 histogram.py [-f][0-9] [file]

## DESCRIPTION
Creates a histogram as a png from a file using the specified column in a tab delimited file.

## KNOWN ISSUES
Still work on ensg2hugo.py, so I didn't start this part, yet. But I will complete it soon.