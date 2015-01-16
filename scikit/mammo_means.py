"""The idea here is to try keeping all values from the data set even those with missing atrributes "?", replacing these missing attributes by the average."""

import numpy as np
from sklearn import svm
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC


#Sums
sum_data=[0.0, 0.0, 0.0, 0.0, 0.0]

#Numbers
nb_elt=[0, 0, 0, 0, 0]

#Means
means = [0.0, 0.0, 0.0, 0.0, 0.0]

#list_data
datas = []

#pourcent learn/test (50 means that we calculate the model on 50/100 of the datas
pourcent = 75


#---------------------- Learning Data ----------------------#




def compute_means(matrix):
    for line in matrix[:pourcent*len(matrix)/100]:
        for i in range(5):
            if line[i] != "?":
                sum_data[i] += int(line[i])
                nb_elt[i] += 1


    for i in range(5):
        means[i] = sum_data[i] / nb_elt[i]


#Create a 2D array containing the data about mammos and a 1D array about the actual results
def parse_data(data_file_name):
    inputfile = open(data_file_name)

    #First we create a global matrix with all values
    for line in inputfile:
        strings = line.split(",")
        data = [strings[0], strings[1], strings[2], strings[3], strings[4], strings[5]]
        datas.append(data)

    inputfile.close()
    
    #We compute means
    compute_means(datas)

    #We seperate the data and the result in the good format for sklearn
    listmammo = []
    listgoal = []
    i=0
    for line in datas:

        #Avoiding non-complete data
        temp_mam = np.array([check(line[0],0), check(line[1],1), 
                             check(line[2],2), check(line[3],3),
                             check(line[4],4)]) #Attributes
        listmammo.append(temp_mam) #Data Set
        listgoal.append(int(line[5])) #Result
        
    array_mammo = np.vstack(listmammo)

    
    return array_mammo,listgoal
    
#Look for missing attributes in the dataset
def check(data, i):
    if data=="?":
        return means[i]
    else:
        return int(data)

#---------------------- Evaluation ----------------------#

#Error rate. Difference between expected and obtained results.
def compare(true, result):
    errors=0.0
    for i in range (len(result)):
        if(true[i]!=result[i]):
            errors +=1.0
    print (errors/len(result))*100


def compute_false_positive(true, result):
    false_positive = 0.0
    positive_result = 0.0
    for i in range (len(result)):
        if(result[i]):
            if(not(true[i])):
                 false_positive += 1
            positive_result += 1
    print (false_positive/positive_result)*100


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

#---------------------- Checking ----------------------#
print "*" * 100
print " "
print "SVM error rate"
compare( target[len(target)-len(result_svm):],result_svm)
print " "
print "Gaussian Naive Bayes error rate"
compare( target[len(target)-len(result_bayes):],result_bayes)

print "*" * 100
print " "
print "SVM false positive rate"
compute_false_positive( target[len(target)-len(result_svm):],result_svm)
print " "
print "Gaussian Naive Bayes false positive rate"
compute_false_positive( target[len(target)-len(result_bayes):],result_bayes)


