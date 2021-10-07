from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

data = load_breast_cancer()
X = data.data
Y = data.target

x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.2)
# define classifier (support_vector_machine)
clf = SVC(kernel='linear', C=3)
clf.fit(x_train,y_train)
# classifier number 2 (k-neighbors)
clf2 = KNeighborsClassifier(n_neighbors=3)
clf2.fit(x_train,y_train)
# test classifier 1 (support_vector_machine)
print(clf.score(x_test,y_test))
# test classifier 2 (k-neighbors)
print(clf2.score(x_test,y_test))