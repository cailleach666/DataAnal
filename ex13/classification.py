import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Laadige andmed
df = pd.read_excel('Apartment_Building_Dataset.xlsx')

# Veergude kustutamine
drop_columns = ['ID', 'TaisAadress', 'Maakond', 'KOV_voi_LinnaOsa', 'Tänav_Hoone_Nr', 'Korgus_Umardatud', 'MaaAluste_Korruste_Arv']
df.drop(drop_columns, axis=1, inplace=True)

# Puuduvate väärtuste täitmine
df['Laius'] = df['Laius'].fillna(np.sqrt(df['EhitusAlune_Pindala']))
df['Pikkus'] = df['Pikkus'].fillna(np.sqrt(df['EhitusAlune_Pindala']))
df = df.fillna(df.mode().iloc[0])

# Kategooriliste muutujate kodeerimine
encoder = LabelEncoder()
for col in df.select_dtypes(include=['object']):
    df[col] = encoder.fit_transform(df[col])

# Funktsioonide ja sihitud tunnuse valimine
X = df.drop("Katusekatte materjal", axis=1)
y = df["Katusekatte materjal"]

# Andmete jagamine treening- ja testandmeteks
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# K-nearest neighbors (KNN) klassifikaatori loomine ja koolitamine
classifier = RandomForestClassifier(random_state=42)
classifier.fit(X_train, y_train)

# Testandmete ennustamine
y_pred = classifier.predict(X_test)

# Täpsuse arvutamine
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
