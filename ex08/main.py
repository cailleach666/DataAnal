import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# Step 1: Prepare the Dataset
data = {
    "Piim": [1, 1, 0, 0, 0, 1],
    "Sai": [1, 1, 0, 0, 0, 0],
    "Leib": [0, 0, 1, 1, 1, 0],
    "Banaan": [0, 0, 1, 1, 1, 1],
    "Näts": [0, 0, 1, 1, 1, 0],
    "Huulepuna": [0, 0, 0, 0, 0, 1]
}
df = pd.DataFrame(data, index=['Ostja1', 'Ostja2', 'Ostja3', 'Ostja4', 'Ostja5', 'Ostja6']).T

# Step 2: Compute the Distance Matrix using Euclidean Distance
# This is implicitly done in the linkage function

# Step 3: Perform Hierarchical Clustering using UPGMA
Z = linkage(df, method='average', metric='euclidean')

# Step 4: Plot the Dendrogram
plt.figure(figsize=(10, 7))
dendrogram(Z, labels=df.index, leaf_rotation=90)
plt.title("Hierarchical Clustering Dendrogram (UPGMA)")
plt.xlabel("Product")
plt.ylabel("Distance")
plt.show()
