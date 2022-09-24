import sys,getopt,os
import pandas as pd  
import numpy as np   
import matplotlib.pyplot as plt





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

    if os.path.exists(sys.argv[2]):
        Titanic = pd.read_csv(sys.argv[2])

        if int(number)==4:
            Titanic.AveExpr.plot(kind = 'hist', bins = 20, color = 'steelblue', edgecolor = 'black', label ='AveExpr')
        else:

            Titanic.logFC.plot(kind = 'hist', bins = 20, color = 'steelblue', edgecolor = 'black', label = 'logFC')
        plt.xlabel('Number Ranges')
        plt.title('Histogram')
        plt.legend()
        plt.show()
    else:
        print(sys.argv[2]+" not exist")
        plt.saveas(gcf,'histogram.png')

if __name__ == '__main__':
    main(sys.argv[1:])