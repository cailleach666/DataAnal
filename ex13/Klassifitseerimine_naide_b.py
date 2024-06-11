import pandas as pd  # Impordib pandas teeki lühendatud nimetusega "pd".
from sklearn.model_selection import train_test_split  # Impordib funktsiooni andmekogumi jagamiseks treening- ja testandmeteks.
from sklearn.preprocessing import StandardScaler  # Impordib klassi muutujate ümberskaleerimiseks.
from sklearn.metrics import accuracy_score  # Impordib funktsiooni mudeli ennustuste täpsuse hindamiseks.
from sklearn.linear_model import LogisticRegression  # Impordib LogisticRegression klassifikaatori.
from sklearn.neighbors import KNeighborsClassifier  # Impordib KNeighborsClassifier klassifikaatori.
from sklearn.svm import SVC  # Impordib SVC (Support Vector Machine) klassifikaatori.
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier  # Impordib RandomForest ja GradientBoosting klassifikaatorid.
from sklearn.tree import DecisionTreeClassifier  # Impordib DecisionTreeClassifier klassifikaatori.

# Laeb andmekogumi
file_path = 'bank-data.csv'  # Määratakse muutuja file_path väärtuseks faili asukoht
data = pd.read_csv(file_path)  # Loeb CSV-faili pandas DataFrame'i.

# Andmete ettevalmistamine
data.drop('id', axis=1, inplace=True)  # Eemaldab 'id' veeru.
data['pep'] = data['pep'].map({'YES': 1, 'NO': 0})  # Teisendab 'pep' väärtused numbrilisteks.

# Teisendab kategoorilised tunnused one-hot kodeeringuks.
data = pd.get_dummies(data, columns=['sex', 'region', 'married', 'car', 'save_act', 'current_act', 'mortgage'])

# Jagab andmekogumi treening- ja testkomplektideks.
X = data.drop('pep', axis=1)  # Eraldab iseseisvad tunnused (X).
y = data['pep']  # Eraldab väljundmuutuja/sihtmuutuja (y).
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # Jagab andmed.

# Skaalib funktsioonid.
scaler = StandardScaler()  # Loob ümberskaleerimise objekti.
X_train = scaler.fit_transform(X_train)  # skaleerib treeningandmed ümber
X_test = scaler.transform(X_test)  # skaleerib testandmed ümber

# Klassifikaatorite valik (ise kommenteeri välja ja sisse, mida soovid!)
clf = DecisionTreeClassifier(random_state=42) # Kasutab DecisionTree (otsustuspuu) klassifikaatorit.
# clf = KNeighborsClassifier()
# clf = LogisticRegression(random_state=42)
# clf = SVC(random_state=42)
# clf = RandomForestClassifier(random_state=42)
# clf = GradientBoostingClassifier(random_state=42)

# Koolitab valitud klassifikaatori.
clf.fit(X_train, y_train)

# Teeb ennustused testandmete kohta.
y_pred = clf.predict(X_test)

# Hindab mudeli ennustuste täpsust.
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy of {clf.__class__.__name__}: {accuracy:.2f}')  # Prindib välja klassifikaatori nime ja täpsuse.

# print("\nActual outcomes (y_test):")
# print(y_test.to_numpy())  # Teisendab y_test pandas seeria numpy massiiviks parema loetavuse jaoks ja prindib selle välja.
# print("\nPredicted outcomes (y_pred):")
# print(y_pred)  # Prindib välja mudeli poolt ennustatud tulemused (y_pred).

# Milline tunnus omab tugevat ennustusväärtust? Kas antud klassifikaator toetab feature_importances_?
feature_names = X.columns
if hasattr(clf, 'feature_importances_'):
    # Print the feature importances
    print("Feature Importances:")
    for name, importance in zip(feature_names, clf.feature_importances_):
        print(f"{name}: {importance:.4f}")
else:
    print(f"{clf.__class__.__name__} does not support feature importance directly.")
