import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
import seaborn as sns
sns.set(style='white', color_codes=True)
import warnings
warnings.filterwarnings("ignore")

#QUESTION 1
#Apply K means clustering in the data set provided
data = pd.read_csv('./CC.csv')
print(data['TENURE'].value_counts())
#Remove any null values by the mean
nulls = pd.DataFrame(data.isnull().sum().sort_values(ascending=False)[:23])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)
#Here the MINIMUM_PAYMENTS and CREDIT_LIMIT have nulls, below replacing them by the mean
data.loc[(data['MINIMUM_PAYMENTS'].isnull()==True), 'MINIMUM_PAYMENTS'] = data['MINIMUM_PAYMENTS'].mean()
data.loc[(data['CREDIT_LIMIT'].isnull()==True), 'CREDIT_LIMIT'] = data['CREDIT_LIMIT'].mean()
#Deviding data into x, y where y is TENURE
x = data.iloc[:, 1:]
print(x.shape)
#Use the elbow method to find a good number of clusters with the KMeans algorithm
wcss = []
print()
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
#Display of the graph
print(wcss)
plt.plot(range(1, 11), wcss)
plt.title('THE ELBOW METHOD')
plt.xlabel('NO.OF CLUSTERS')
plt.ylabel('WCSS')
plt.show()
#Silhouette score before clustering
km = KMeans(n_clusters=3)
km.fit(x)
y_cluster_kmeans = km.predict(x)
score = metrics.silhouette_score(x, y_cluster_kmeans)
print()
print('Silhouette score for', 3, 'clusters before scaled', score)

###QUESTION 2###
#feature scaling and then apply KMeans on the scaled features
from sklearn import preprocessing
scaler = preprocessing.StandardScaler()
scaler.fit(x)
X_scaled_array = scaler.transform(x)
X_scaled = pd.DataFrame(X_scaled_array, columns = x.columns)
#This is the silhouette score after clustering
km = KMeans(n_clusters=3)
km.fit(X_scaled)
y_cluster_kmeans = km.predict(X_scaled)
from sklearn import metrics
score = metrics.silhouette_score(X_scaled, y_cluster_kmeans)
print('Silhouette score for', 3, 'clusters after scaled', score)

###QUESTION 3###
#Here i applied PCA on the same dataset
scaler = StandardScaler()
scaler.fit(x)
x_scaler = scaler.transform(x)
#Apply kMeans algorithm on the PCA result
pca = PCA(1)
x_pca = pca.fit_transform(x_scaler)
#Here i combined data
df = pd.DataFrame(data=x_pca)
wcss=[]
for i in range(1, 7):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(x_pca)
    wcss.append(kmeans.inertia_)
print()
print(wcss)
plt.plot(range(1, 7), wcss)
plt.title('THE ELBOW METHOD')
plt.xlabel('NUMBER OF CLUSTERS')
plt.ylabel('WCSS')
plt.show()
#Silhouette score after applying PCA
km = KMeans(n_clusters=4)
km.fit(x_pca)
y_cluster_kmeans = km.predict(x_pca)
score = metrics.silhouette_score(x_pca, y_cluster_kmeans)
print('Silhouette score after applying PCA', score)