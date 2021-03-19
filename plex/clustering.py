import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.preprocessing import MinMaxScaler


def cluster(csv, num_clusters, etc=None):
    df = pd.read_csv(csv)
    # print(df['Rank each skill on the list first to last. [Problem Solving]'])
    df['Problem Solving'] = df['Rank each skill on the list first to last. [Problem Solving]'].astype(str).str[0]
    df['Creativity'] = df['Rank each skill on the list first to last. [Creativity]'].astype(str).str[0]
    df['Research'] = df['Rank each skill on the list first to last. [Research]'].astype(str).str[0]
    df['Time Management'] = df['Rank each skill on the list first to last. [Time Management]'].astype(str).str[0]
    df['Communication'] = df['Rank each skill on the list first to last. [Communication]'].astype(str).str[0]
    # df['Critical Thinking'] = df[' [Critical Thinking]'].astype(str).str[0]

    newdf = df[['Problem Solving', 'Creativity', 'Research', 'Time Management', 'Communication']]
    # print(newdf)


    scaler = MinMaxScaler()
    # print(df)
    new_df = pd.DataFrame(scaler.fit_transform(newdf), columns=newdf.columns[:], index=newdf.index)

    # print(new_df)

    clustering = AgglomerativeClustering(num_clusters)

    # Fitting
    clustering.fit(new_df)

    # Getting cluster assignments
    cluster_assignments = clustering.labels_

    # Unscaling the categories then replacing the scaled values
    if csv == "fakeStudent.csv":
        df = df[['Best email to reach you']].join(pd.DataFrame(scaler.inverse_transform(newdf), columns=newdf.columns[:], index=newdf.index))
    else:
        df = df[['Company Name']].join(pd.DataFrame(scaler.inverse_transform(newdf), columns=newdf.columns[:], index=newdf.index))
    # Assigning the clusters to each profile
    df['Cluster #'] = cluster_assignments

    # Viewing the dating profiles with cluster assignments
    # print(df)
    return df

if __name__ == "__main__":
    csv = input("Enter csv file (with datapath): ")
    num_clusters = int(input("Enter number of clusters you wish to cluster into: "))
    cluster(csv, num_clusters)


