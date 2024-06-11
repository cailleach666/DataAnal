import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import openpyxl

df = pd.read_excel('Apartment_Building_Dataset.xlsx')

drop_columns = ['ID', 'EHR_kood', 'Korgus_Umardatud', 'MaaAluste_Korruste_Arv']
df.drop(drop_columns, axis=1, inplace=True)

df['Laius'] = df['Laius'].fillna(np.sqrt(df['EhitusAlune_Pindala']))
df['Pikkus'] = df['Pikkus'].fillna(np.sqrt(df['EhitusAlune_Pindala']))

df = df.fillna(df.mode().iloc[0])

encoder = LabelEncoder()
for col in df.select_dtypes(include=['object']):
    df[col] = encoder.fit_transform(df[col])

X = df.drop("Hooneosade_Arv", axis=1)
y = df["Hooneosade_Arv"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

classifier = RandomForestClassifier(random_state=42)
# classifier = GradientBoostingClassifier(random_state=42)

classifier.fit(X_train, y_train)

# for feature, importance in zip(X.columns, clf.feature_importances_):
#     print(f"{feature}: {importance}")

y_pred = classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
