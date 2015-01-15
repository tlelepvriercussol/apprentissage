import numpy as np
from sklearn import svm

#---------------------- Data Class ----------------------#
class mammo:
    
    def __init__(self):
        self.bi_rads = 0
        self.age=0
        self.shape=0
        self.margin=0
        self.density=0
        self.severity=0

    def set_characteristics(self, bi_rads, age, shape, margin, density, severity):
        self.bi_rads=bi_rads
        self.age=age
        self.shape=shape
        self.margin=margin
        self.density=density
        self.severity=severity

    def get_response(self):
        return self.severity

#---------------------- Learning Data ----------------------#

#Create a 2D array containing the data about mammos
def parse_data(data_file_name):
    inputfile = open(data_file_name)

    listmammo = []

    for line in inputfile:
        temp_mammo = mammo()
        strings = line.split(",")

        temp_mammo.set_characteristics(strings[0], strings[1], strings[2], strings[3], strings[4], strings[5])

        if check_missing_arg(temp_mammo):
            temp_mam = np.array([int(strings[0]),int(strings[1]),int(strings[2]),int(strings[3]),int(strings[4]),int(strings[5])])
            listmammo.append(temp_mam)


    print len(listmammo)
    array_mammo = np.vstack(listmammo)

    #print array_mammo
    inputfile.close()
    return array_mammo
    
def check_missing_arg(mammo):
    result = True
    if(mammo.bi_rads == "?"):
        mammo.bi_rads = -1
        result = False
    else:
        mammo.bi_rads = int(mammo.bi_rads)

    if(mammo.age == "?"):
        mammo.age = -1
        result = False
    else:
        mammo.age = int(mammo.age)

    if(mammo.shape == "?"):
        mammo.shape = -1
        result = False
    else:
        mammo.shape = int(mammo.shape)

    if(mammo.margin == "?"):
        mammo.margin = -1
        result = False
    else:
        mammo.margin = int(mammo.margin)

    if(mammo.density == "?"):
        mammo.density = -1
        result = False
    else:
        mammo.density = int(mammo.density)

    if(mammo.severity == "?"):
        mammo.severity = "NONSENSEGETOUTOFMYLAWN"
        result = False
    else:
        mammo.severity = int(mammo.severity)

    return result


clf = svm.SVC(gamma=0.001, C=100.)
data_array = parse_data("mammographic_masses.data")
"""TODO: the last characteristic is our goal field in each 1D array.
it should be removed from data and passed to target, which is a 1D array
We can then call clf.fit(digits.data[:-1], digits.target[:-1]) """
#Si j'ai bien compris, ofc.
