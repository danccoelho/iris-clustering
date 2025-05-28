# %%
from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram


# %%
iris = datasets.load_iris()
iris

# %%
def plot_clusters(data, labels, title):
    colors = ['red','green','purple','black']
    plt.figure(figsize=(8,4))
    for i,c,l in zip(range(-1,3), colors, ['Noise', 'Setosa', 'Versicolor', 'Virginica']):
        if i == -1:
            plt.scatter(data[labels == i, 0], data[labels == i, 3], c = colors[i], label = l, alpha=0.5, s=50, marker='x')
        else:
            plt.scatter(data[labels == i, 0], data[labels == i, 3], c = colors[i], label = l, alpha=0.5, s=50,)

    plt.legend()
    plt.title(title)
    plt.xlabel("Comprimento Sépala")
    plt.ylabel("Largura da pétala")
    plt.show


# %%
iris.target

# %%
kmeans = KMeans(n_clusters=3,n_init='auto')
kmeans.fit(iris.data)
print(kmeans.labels_)

resultado = confusion_matrix(iris.target, kmeans.labels_)
print(resultado)

plot_clusters(iris.data, kmeans.labels_, 'Cluster Kmeans')

# %%
dbscan = DBSCAN(eps=0.5, min_samples=3)
dbscan_labels = dbscan.fit_predict(iris.data)
print(dbscan_labels)

resultado = confusion_matrix(iris.target, dbscan.labels_)
print(resultado)

plot_clusters(iris.data,dbscan.labels_, 'Cluster DBSCAN')

# %%
agglo = AgglomerativeClustering(n_clusters=3,)
agglo_labels = agglo.fit_predict(iris.data)
print(agglo_labels)

resultado = confusion_matrix(iris.target, agglo_labels)
print(resultado)

plot_clusters(iris.data, agglo_labels,'Cluster Hierárquico')

# %%
plt.figure(figsize=(12,6))
plt.title('Cluster Hierárquico: Dendrograma')
plt.xlabel('Índice')
plt.ylabel('Distância')
linkage_matrix = linkage(iris.data, method='ward')
dendrogram(linkage_matrix, truncate_mode='lastp', p=15)
plt.axhline(y=7, c='gray', lw=1, linestyle='dashed')
plt.show()


