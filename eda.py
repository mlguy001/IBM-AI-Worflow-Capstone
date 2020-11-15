import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plotCompareDistrubutions(over, to_compare, dist_of, data):
    n=len(dist_of)
    
    fig, axes = plt.subplots(nrows=n,ncols=1,figsize=(10,10))
    for var, ax in zip(dist_of, axes):
        for v in to_compare:
            t = data[(data[over]==v)][var]
            sns.distplot(t,bins=10,kde=True,hist_kws={"alpha":0.3}, kde_kws={"bw":0.5},ax=ax,label=v)
            
        t = data[(data[over]==v)][var]
        sns.distplot(t,bins=10,kde=True,hist_kws={"alpha":0.3}, kde_kws={"bw":0.5},ax=ax,label="ALL")
        
        ax.set_xlabel("")
        ax.legend()
        ax.set_title(var)