import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


dataset_url = '/Users/charankottapalli/Desktop/py_ICP5/data/College.csv'
data = pd.read_csv(dataset_url)

x = data.iloc[:,[2,3,4,5,6,7,8,9]]
print(x)

from sklearn import preprocessing

scaler = preprocessing.StandardScaler()

scaler.fit(x)

X_scaled_array = scaler.transform(x)
print(X_scaled_array)
X_scaled = pd.DataFrame(X_scaled_array, columns = x.columns)

from sklearn.cluster import KMeans
nclusters = 3 # this is the k in kmeans
seed = 42

km = KMeans(n_clusters=nclusters, random_state=seed)
km.fit(X_scaled)

# predict the cluster for each data point
y_cluster_kmeans = km.predict(X_scaled)

from sklearn import metrics
wcss = []
##elbow method to know the number of clusters
print(metrics.silhouette_score(X_scaled_array,y_cluster_kmeans))
for i in range(1,11):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,11),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()

sns.FacetGrid(data, hue="Outstate", size=4).map(plt.scatter, "Accept", "Outstate")
# do same for petals
sns.FacetGrid(data, hue="Accept", size=4).map(plt.scatter, "Books", "Accept")
plt.show()
