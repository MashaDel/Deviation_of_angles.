import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


class Plot:
    def draw_plots(self,link):
        file_json=pd.read_json(link)
        if 'plots' not in os.listdir(os.getcwd()):
            os.makedirs('plots')
        else:
            file_plot=sns.pairplot(data=file_json.iloc[:,3:])
            file_plot.savefig('plots/file_plot.png')
            plots_path=[]
            plots_path.append(os.getcwd()+'plots/file_plot')
        return plots_path

test=Plot()
print(*test.draw_plots('https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json'))



