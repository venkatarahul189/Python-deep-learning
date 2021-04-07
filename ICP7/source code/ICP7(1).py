#Here first i import all the libraries
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
#Here i loaded the files by using twenty_train
twenty_train = fetch_20newsgroups(subset='train', shuffle=True)
#Here i take TfidfVectorizer that can be used as input to estimator
tfidf_Vect = TfidfVectorizer()
tfidf_Vect1 = TfidfVectorizer(ngram_range=(1, 2))
tfidf_Vect2 = TfidfVectorizer(stop_words='english')
#To transform the data
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)
X_train_tfidf1 = tfidf_Vect1.fit_transform(twenty_train.data)
X_train_tfidf2 = tfidf_Vect2.fit_transform(twenty_train.data)
#here i used the classifier model for the term frequency
clf = MultinomialNB()
clf.fit(X_train_tfidf, twenty_train.target)
#here i used the classifier model for the term frequency1
clf1 = MultinomialNB()
clf1.fit(X_train_tfidf1, twenty_train.target)
#here i used the classifier model for the term frequency2
clf2 = MultinomialNB()
clf2.fit(X_train_tfidf2, twenty_train.target)

twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)
#here i run the test data
predicted = clf.predict(X_test_tfidf)
score = round(metrics.accuracy_score(twenty_test.target, predicted), 3)
#here i loaded the data score to find the MultinomialNB accuracy
print("MultinomialNB accuracy is: ", score)

#setting the tfidf vectorizer parameter to use bigram
twenty_test1 = fetch_20newsgroups(subset='test', shuffle=True)
#Here i transform the data into tfidf1 vectors
X_test_tfidf1 = tfidf_Vect1.transform(twenty_test.data)
#here i take predicted1 as p1 and to find the docs state and to run the test data
P1 = clf1.predict(X_test_tfidf1)
#Here i take score1 as s1
s1 = round(metrics.accuracy_score(twenty_test1.target, P1), 4)
#Loaded the data with the score1 to find MultinomialNB accuracy
print("Accuracy of bigram is: ", s1)
#setting the vectorizer argument to use stop words
twenty_test2 = fetch_20newsgroups(subset='test', shuffle=True)
#Here i transform the data into tfidf2 vectors
X_test_tfidf2 = tfidf_Vect2.transform(twenty_test.data)
#Here i run the test data into the model as predicted2
P2 = clf2.predict(X_test_tfidf2)
#This is the score2 accuracy
s2 = round(metrics.accuracy_score(twenty_test2.target, P2), 5)
#Loaded the data with the score2 to find MultinomialNB accuracy
print("Accuracy by adding the stop-words is: ", s2)
#Here i used svc implementation to find the accuracy of SVM
svc = SVC(kernel='linear')
#Here i used svc classifier to fit the data
svc.fit(X_train_tfidf, twenty_train.target)
#here i take k nearest to use the data and classify the data points
acc_knn = round(svc.score(X_train_tfidf, twenty_train.target) * 100, 3)
#here i loaded the knn classifier
print("SVM accuracy is:", acc_knn / 100)