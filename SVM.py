import sklearn
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import unicodedata
import nltk 
import time
from io import StringIO
import csv
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics

with open("resource/question.csv", "r") as ins:
    data = []
    for line in ins:
        data.append(line.replace("\n","").replace("\r",""))

dataTrain = data[:int(0.7*len(data))]
dataTest = data[int(0.7*len(data)):]

with open("resource/category.csv", "r") as ins:
    target = []
    for line in ins:
        target.append(line.replace("\n","").replace("\r",""))

targetName = list(set(target))

targetEnc=[]
for i in target:
	targetEnc.append(targetName.index(i))


targetTrain = np.array(targetEnc[:int(0.7*len(targetEnc))])
targetTest = np.array(targetEnc[int(0.7*len(targetEnc)):])

#print(dataTest[0],"============",data[int(0.7*len(data))])


count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(dataTrain)
tfidf_transformer = TfidfTransformer(use_idf=True)
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
t0 = time.time()
clf = svm.SVC(kernel='linear', C=1,gamma='auto').fit(X_train_tfidf, targetTrain)
train_time = time.time() - t0
print("train time: %0.3fs" % train_time)

docs_new = dataTest
X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)
t0 = time.time()
predicted = clf.predict(X_new_tfidf)
test_time = time.time() - t0
print("test time:  %0.3fs" % test_time)
# print(clf.score(X_new_tfidf,targetTest))
print(metrics.accuracy_score(targetTest,predicted))

