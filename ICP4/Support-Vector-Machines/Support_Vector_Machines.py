from sklearn import datasets

irisdataset = datasets.load_iris()

print ("Features:", irisdataset.feature_names)
print("Labels:", irisdataset.target_names)

print(irisdataset.data.shape)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(irisdataset.data, irisdataset.target, test_size=0.3, random_state=0)

from sklearn import svm
clf = svm.SVC(kernel='linear')
clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)

from sklearn import metrics
print("Accuracy", metrics.accuracy_score(y_test,y_pred))
print("Precision:",metrics.precision_score(y_test, y_pred,pos_label='positive',average='micro'))
print("Recall:",metrics.recall_score(y_test, y_pred,pos_label='positive',average='micro'))
