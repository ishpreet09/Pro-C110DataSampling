from os import stat
import plotly.figure_factory as ff
import statistics
import random
import pandas as pd

df=pd.read_csv("D:/DATA DESKTOP/Notes Of Code/Python/Homework/Pro-C110DataSampling/medium_data.csv")
data=df["reading_time"].to_list()

fig=ff.create_distplot([data],["Reading Time"], show_hist=False)
fig.show()

mean=statistics.mean(data)
print("Mean of the population is", mean)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0, counter):
        random_index=random.radint(0, len(data))
        value=data[random_index]
        dataset.append(value)

    mean=statistics.mean(dataset)
    return(mean)

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(10)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    print("Sampling mean:- ", statistics.mean(mean_list))
setup()