import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd
import numpy as np

plt.style.use('seaborn-whitegrid')

def preprocess_df(path):
    df = pd.read_csv(path, na_values=["no graph", "no trends"])
    df.rename(columns={'susp/con ZIKV cases':'year', "Unnamed: 1": "date", "Unnamed: 2": "epi week"}, inplace=True)
    df = df.drop(0)
    df = df.dropna(how="all")
    df = df.dropna(how="all", axis = 1)    
    return df

def fill_date(df):
    year = 0
    for i in df.index:
        if not pd.isnull(df["year"][i]):
            year = df["year"][i]
        else:
            df.loc[i,"year"] = year
    df["date"]=pd.to_datetime(df["date"]+"-"+df["year"])
    df = df.drop("year",axis=1)
    return df

def plot_continent(df, colors, name):
    df = fill_date(df)
    df = df.set_index("date")
    df.sort_index(inplace=True)
    fig = plt.figure(figsize=(12,7))
    ax = plt.subplot(111)
    df.plot(ax=ax, color=colors)
    # Shrink current axis by 20%
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    # Put a legend to the right of the current axis    
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.subplots_adjust(bottom=0.2, left=0.1,right=0.8,top=None)
    ax.set_title(name.replace("_"," "))
    ax.set_xlabel("Time")
    ax.set_ylabel("ZIKV cases per week")
    plt.savefig("../plots/"+name+".png", dpi=300)
    plt.clf()
    plt.close()

if __name__=="__main__":
    _c = list(mpl.colors.cnames.values())    
    df = preprocess_df("../caribbean.csv")
    colors = _c[7:]
    plot_continent(df.drop("epi week", axis =1), colors, "Caribbean")
    df = preprocess_df("../south_america.csv")
    colors = _c[7:]
    plot_continent(df, colors, "South_America")  
    df = preprocess_df("../central_america.csv")
    colors = _c[8:]
    plot_continent(df, colors, "Central_America")
