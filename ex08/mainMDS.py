import numpy as np
import pandas as pd
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

# Prepare the Dataset (same as before)
data = {
    "Piim": [1, 1, 0, 0, 0, 1],
    "Sai": [1, 1, 0, 0, 0, 0],
    "Leib": [0, 0, 1, 1, 1, 0],
    "Banaan": [0, 0, 1, 1, 1, 1],
    "Näts": [0, 0, 1, 1, 1, 0],
    "Huulepuna": [0, 0, 0, 0, 0, 1]
}
df = pd.DataFrame(data, index=['Ostja1', 'Ostja2', 'Ostja3', 'Ostja4', 'Ostja5', 'Ostja6']).T

# Perform MDS
mds = MDS(n_components=2, dissimilarity="euclidean")
mds_coords = mds.fit_transform(df)

# Plot MDS
plt.figure(figsize=(10, 7))
plt.scatter(mds_coords[:, 0], mds_coords[:, 1])
for label, x, y in zip(df.index, mds_coords[:, 0], mds_coords[:, 1]):
    plt.annotate(label, (x, y))
plt.title("Multidimensional Scaling (MDS)")
plt.xlabel("MDS Dimension 1")
plt.ylabel("MDS Dimension 2")
plt.show()
