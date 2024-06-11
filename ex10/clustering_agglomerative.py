import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from scipy.stats import mode

# Read data from CSV file
data = pd.read_csv('buildings.csv')

# Configuration
k = 4  # Number of clusters

# Perform Agglomerative Clustering
agg_clust = AgglomerativeClustering(n_clusters=k, metric='euclidean', linkage='ward')
data['Cluster'] = agg_clust.fit_predict(
    data[['MaksKorrust', 'EhitisealunePind', 'Kõrgus', 'Pikkus', 'Laius', 'LiftideArv', 'Aasta']])


# Plotting the clustered data
plt.figure(figsize=(8, 6))
for cluster in range(k):
    cluster_data = data[data['Cluster'] == cluster]
    plt.scatter(cluster_data['Kõrgus'], cluster_data['EhitisealunePind'], label=f'Cluster {cluster + 1}')

plt.title('Agglomerative Clustering')
plt.xlabel('Kõrgus')
plt.ylabel('EhitisealunePind')
plt.legend()
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
