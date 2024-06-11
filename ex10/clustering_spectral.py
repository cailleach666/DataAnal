import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import SpectralClustering
from sklearn.preprocessing import StandardScaler
from scipy.stats import mode

# Read data from CSV file
data = pd.read_csv('buildings.csv')  # Ensure this path matches the location of your CSV file

# Configuration
k = 4  # Number of clusters

# Prepare data for clustering
numerical_columns = ['MaksKorrust', 'EhitisealunePind', 'Kõrgus', 'Pikkus', 'Laius', 'LiftideArv', 'Aasta']
x = data[numerical_columns].values

# Standardize the numerical data
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# Perform Spectral Clustering
spectral_clust = SpectralClustering(n_clusters=k, affinity='nearest_neighbors', random_state=42)
data['Cluster'] = spectral_clust.fit_predict(
    data[['MaksKorrust', 'EhitisealunePind', 'Kõrgus', 'Pikkus', 'Laius', 'LiftideArv', 'Aasta']])

# Visualize the clusters
plt.figure(figsize=(10, 8))
# Define colors/markers for plotting each cluster
colors = plt.cm.tab20.colors  # Use a colormap for distinct colors
markers = ['o', 's', '^', 'x', '+', '*', 'D', 'v', '<', '>', 'P', 'H']  # Marker styles

# Plot each cluster separately
for cluster in range(k):
    cluster_data = data[data['Cluster'] == cluster]
    plt.scatter(cluster_data['MaksKorrust'], cluster_data['EhitisealunePind'],
                label=f'Cluster {cluster + 1}', color=colors[cluster % len(colors)], marker=markers[cluster % len(markers)])

# Plot centroids if needed (uncomment the following lines)
# centroids = scaler.inverse_transform(kmeans.cluster_centers_)
# plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=300, c='r', label='Centroids')
plt.title(f'Spectral Clustering Results (k={k})')
plt.xlabel('MaksKorrust')
plt.ylabel('EhitisealunePind')
plt.legend()
plt.grid(True)
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