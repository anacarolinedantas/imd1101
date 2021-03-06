import pandas as pd
from sklearn.model_selection import RepeatedKFold
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neural_network import MLPClassifier

dados = pd.read_csv('../Bases/diabetes.csv')

X = dados.iloc[:,:-1].values
y = dados.iloc[:,-1].values

rkf = RepeatedKFold(n_splits=10, n_repeats=10, random_state=990)

for train, test in rkf.split(X, y):
    X_train = X[train]
    X_test = X[test]
    y_train = y[train]
    y_test = y[test]

mlp = MLPClassifier(solver='sgd', momentum=0.8, hidden_layer_sizes=(300), learning_rate='constant', learning_rate_init=0.01, max_iter=500, random_state=1)

mlp.fit(X_train, y_train)

y_pred = mlp.predict(X_test)

acc = str(accuracy_score(y_test, y_pred))

print("Acurácia:", acc)

cm = confusion_matrix(y_test, y_pred)

print("Matriz de confusão")
print(cm)