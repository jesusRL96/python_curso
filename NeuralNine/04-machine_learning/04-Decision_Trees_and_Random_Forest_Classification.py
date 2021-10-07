from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


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
# classifier number 3 (decision tree classifier)
clf3 = DecisionTreeClassifier()
clf3.fit(x_train,y_train)
# classifier number 4 (random forest classifier)
clf4 = RandomForestClassifier()
clf4.fit(x_train,y_train)

# test classifier 1 (support_vector_machine)
print(f"SVM: {clf.score(x_test,y_test)}")
# test classifier 2 (k-neighbors)
print(f"k-Neighbors: {clf2.score(x_test,y_test)}")
# test classifier 3 (decision tree classifier)
print(f"decision tree: {clf3.score(x_test,y_test)}")
# test classifier 4 (random forest classifier)
print(f"Random forest: {clf4.score(x_test,y_test)}")