import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('fakeStudent.csv')

df['Rank each skill on the list first to last. [Problem Solving]'] = df['Rank each skill on the list first to last. [Problem Solving]'].astype(str).str[0]
df['Rank each skill on the list first to last. [Creativity]'] = df['Rank each skill on the list first to last. [Creativity]'].astype(str).str[0]
df['Rank each skill on the list first to last. [Research]'] = df['Rank each skill on the list first to last. [Research]'].astype(str).str[0]
df['Rank each skill on the list first to last. [Time Management]'] = df['Rank each skill on the list first to last. [Time Management]'].astype(str).str[0]
df['Rank each skill on the list first to last. [Communication]'] = df['Rank each skill on the list first to last. [Communication]'].astype(str).str[0]
# df['[Critical Thinking]'] = df['[Critical Thinking]'].astype(str).str[0]






if __name__ == '__main__':
    print('bruh')