from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
iris = datasets.load_iris()

print iris
X = iris.data
y = iris.target
rf = RandomForestClassifier(n_estimators=80)
# print rf.fit(X, y)
