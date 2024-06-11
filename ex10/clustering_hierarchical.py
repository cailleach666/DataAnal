import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.stats import mode
import matplotlib.pyplot as plt

# Read data from CSV file
data = pd.read_csv('buildings.csv')  # Ensure this path matches the location of your CSV file

# Standardizing the features to have mean=0 and variance=1
scaler = StandardScaler()
features_scaled = scaler.fit_transform(
    data[['MaksKorrust', 'EhitisealunePind', 'Kõrgus', 'Pikkus', 'Laius', 'LiftideArv', 'Aasta']])

# Perform Agglomerative Hierarchical Clustering
k = 3  # Desired number of clusters
agg_clust = AgglomerativeClustering(n_clusters=k, metric='euclidean', linkage='ward')
data['Cluster'] = agg_clust.fit_predict(features_scaled)

# Optionally, plot the dendrogram for visual analysis (requires linkage matrix from scipy)
linked = linkage(features_scaled, 'ward')

# Generating the dendrogram with rotated labels
plt.figure(figsize=(10, 7))
dendrogram(linked, orientation='top', labels=data['EHV'].astype(str).values, distance_sort='descending',
           show_leaf_counts=True, leaf_rotation=90)  # Rotate labels
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Building')
plt.ylabel('Distance')
plt.tight_layout()  # Adjust layout to make room for the rotated labels
plt.show()

# Print out clusters and their descriptions
for cluster in range(k):
    cluster_data = data[data['Cluster'] == cluster]
    print(f'Cluster {cluster + 1}')
    buildings = cluster_data['EHV'].tolist()
    print('Buildings:', buildings)

    # Calculate mean for numerical data
    print('Average Values:')
    for column in ['MaksKorrust', 'EhitisealunePind', 'Kõrgus', 'Pikkus', 'Laius', 'LiftideArv', 'Aasta']:
        print(f'{column}: {cluster_data[column].mean():.2f}')

    print('')  # For better readability
