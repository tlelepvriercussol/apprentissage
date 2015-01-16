import numpy as np
from sklearn import svm
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC


#pourcent learn/test (50 means that we calculate the model on 50/100 of the datas
pourcent = 75

#---------------------- Learning Data ----------------------#

#Create a 2D array containing the data about mammos and a 1D array about the actual results
def parse_data(data_file_name):
    inputfile = open(data_file_name)

    listmammo = []
    listgoal = []

    for line in inputfile:
        strings = line.split(",")

        #Avoiding non-complete data
        if check_missing_arg(strings[0], strings[1], strings[2], strings[3], strings[4], strings[5]):
            temp_mam = np.array([int(strings[0]),int(strings[1]),int(strings[2]),int(strings[3]),int(strings[4])]) #Attributes
            listmammo.append(temp_mam) #Data Set
            listgoal.append(int(strings[5])) #Result

    array_mammo = np.vstack(listmammo)

    inputfile.close()
    return array_mammo,listgoal
    
#Look for missing attributes in the dataset
def check_missing_arg(data0,data1,data2,data3,data4,data5):
    result = True
    if(data0 == "?" or data1 =="?" or data2 =="?" or data3 =="?" or data4 =="?" or data5 =="?"):
        result = False
    return result

#---------------------- Evaluation ----------------------#

#Error rate. Difference between expected and obtained results.
def compare(true, result):
    errors=0.0
    for i in range (len(result)):
        if(true[i]!=result[i]):
            errors +=1.0
    print (errors/len(result))*100

#---------------------- Running ----------------------#

data, target = parse_data("../mammographic_masses.data")

print "Data"
print data

print "Target"
print target

clf = svm.SVC(gamma=0.001, C=100.)
svm_pred = clf.fit(data[:pourcent*len(target)/100], target[:pourcent*len(target)/100])
result_svm = svm_pred.predict(data[pourcent*len(target)/100:])

gnb = GaussianNB()
gnb_pred = gnb.fit(data[:pourcent*len(target)/100], target[:pourcent*len(target)/100])
result_bayes = gnb_pred.predict(data[pourcent*len(target)/100:])

iris = datasets.load_iris()
gnb = GaussianNB()
y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)

#---------------------- Checking ----------------------#
print "*" * 100
print "Last 20 patients of the dataset"
print "Real"
print target[len(target)-21:]
print "SVM"
print svm_pred.predict([[4,48,4,4,1],
                        [4,58,4,3,3],
                        [5,58,3,4,3],
                        [4,70,1,1,1],
                        [5,70,1,4,3],
                        [4,59,2,1,3],
                        [4,57,2,4,3],
                        [4,53,4,5,3],
                        [4,54,4,4,3],
                        [4,53,2,1,3],
                        [0,71,4,4,3],
                        [5,67,4,5,3],
                        [4,68,4,4,3],
                        [4,56,2,4,3],
                        [4,35,2,1,3],
                        [4,52,4,4,3],
                        [4,47,2,1,3],
                        [4,56,4,5,3],
                        [4,64,4,5,3],
                        [5,66,4,5,3],
                        [4,62,3,3,3]])
print "Gaussian Naive Bayes"
print gnb_pred.predict([[4,48,4,4,1],
                        [4,58,4,3,3],
                        [5,58,3,4,3],
                        [4,70,1,1,1],
                        [5,70,1,4,3],
                        [4,59,2,1,3],
                        [4,57,2,4,3],
                        [4,53,4,5,3],
                        [4,54,4,4,3],
                        [4,53,2,1,3],
                        [0,71,4,4,3],
                        [5,67,4,5,3],
                        [4,68,4,4,3],
                        [4,56,2,4,3],
                        [4,35,2,1,3],
                        [4,52,4,4,3],
                        [4,47,2,1,3],
                        [4,56,4,5,3],
                        [4,64,4,5,3],
                        [5,66,4,5,3],
                        [4,62,3,3,3]])
print "*" * 100
print " "
print "SVM error rate"
compare( target[len(target)-len(result_svm):],result_svm)
print " "
print "Gaussian Naive Bayes error rate"
compare( target[len(target)-len(result_bayes):],result_bayes)
print " "
print "Gaussian Naive Bayes error rate using sklearn database"
compare( iris.target,y_pred )
