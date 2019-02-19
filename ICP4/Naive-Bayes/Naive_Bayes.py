from sklearn import datasets
from sklearn import svm

irisdataset = datasets.load_iris()
print(irisdataset.feature_names)
print(irisdataset.target_names)
print(irisdataset.data.shape)

print(irisdataset.data[0:5])
print(irisdataset.target)

from sklearn.model_selection import train_test_split
#70% training and 30% testing
x_train, x_test, y_train, y_test = train_test_split(irisdataset.data,irisdataset.target,test_size=0.3,random_state=0)


from sklearn.model_selection import cross_val_score
clf = svm.SVC(kernel='linear', C=1)
#cross Validation with 5 dataset splits
scores = cross_val_score(clf, irisdataset.data, irisdataset.target, cv=5)
from sklearn import metrics
scores = cross_val_score(clf, irisdataset.data, irisdataset.target, cv=5, scoring='f1_macro')
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()
gnb.fit(x_train,y_train)
y_pred = gnb.predict(x_test)

from sklearn import metrics

print("Accuracy", metrics.accuracy_score(y_test,y_pred))
print("Precision", metrics.precision_score(y_test,y_pred,pos_label='positive',average='micro'))
print("Recall", metrics.recall_score(y_test,y_pred,pos_label='positive',average='micro'))

