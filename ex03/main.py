import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from scipy.spatial import distance

# Manually input the data
data = {
    'Ehitis': [
        '120801759', '120801756', '120801732',
        '120847092', '120847091', '120847090',
        '101019312', '101014868', '101019344',
        '120857076', '120791952', '120857095'
    ],
    'maxKorrusteArv': [2, 2, 2, 2, 2, 2, 9, 9, 9, 12, 14, 12],
    'ehitisalunePind': [640.4, 640.4, 640.4, 433.1, 433.1, 433.1, 598.0, 598.0, 674.0, 521.3, 521.3, 521.3],
    'korgus': [7.1, 7.1, 7.1, 7.2, 7.2, 7.2, 0, 29.8, 0, 38.8, 44.8, 38.8],
    'pikkus': [52.4, 52.4, 52.4, 37.7, 37.7, 37.7, 0, 0, 0, 28.3, 29.5, 28.3],
    'laius': [11.1, 11.1, 11.1, 11.4, 11.4, 11.4, 0, 0, 0, 21.2, 21.2, 21.2,],
    'lift': [0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2],
    'esmaneKasutus': [2018, 2018, 2018, 2019, 2019, 2019, 1974, 1974, 1974, 0, 2020, 2023]
}

# Create a DataFrame from the manually input data
df = pd.DataFrame(data)

# Extract the 'Ehitis' column for building names
buildings = df['Ehitis']

# Initialize MinMaxScaler
scaler = MinMaxScaler()

# Select numerical columns for scaling
numerical_columns = ['maxKorrusteArv', 'ehitisalunePind', 'korgus', 'pikkus', 'laius', 'lift', 'esmaneKasutus']
df_scaled = df[numerical_columns]

# Scale the numerical columns
df_scaled = pd.DataFrame(scaler.fit_transform(df_scaled), columns=numerical_columns)

# Calculate Euclidean distances
distances = pd.DataFrame(index=buildings, columns=buildings)

for i in range(len(buildings)):
    for j in range(len(buildings)):
        distances.iloc[i, j] = distance.euclidean(df_scaled.iloc[i], df_scaled.iloc[j])

# Add headers to the distances DataFrame
distances.columns.name = 'Ehitis'
distances.index.name = 'Ehitis'

# Write results to a new CSV file
distances.to_csv('similarity_matrix.csv')

# Display the distances DataFrame as a table
print(distances)
