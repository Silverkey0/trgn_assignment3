import sys,getopt,os
import pandas as pd  
import numpy as np   
import matplotlib.pyplot as plt

if sys.argv[:1] == '-f' :
    n= str((column_selection[2]))
    
data = pd.read_tsv(sys.argv(2), sep='\t', header=0)
data.head()
    df = pd.Dataframe(data)
        n = [1,2,3,4]
        df = df[str(df.columns[4])]
        ax = df.plot.hist()
        plt.xlabel('Number Ranges')
        plt.title('Histogram')
        plt.legend()
        plt.show()
        plt.saveas(gcf,'histogram.png')