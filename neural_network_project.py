import numpy as np
import math
import random
#from data_parser import *

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


#---------------------- Neuralis Class ----------------------#
class neuron:

    learning_rate = 1
    
    def __init__(self):
        self.entries=[1.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.weights=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
        self.threshold=1.0
        self.output=0.0

    def init_weights(self):
        for i in range(len(self.weights)):
            self.weights[i]=random.uniform(-10.0,10.0)
        self.threshold=1.0

    def calculate(self):
        length = len(self.weights)
        not_even_my_final_form=0.0
        
        for i in range(length):
            not_even_my_final_form += self.entries[i]*self.weights[i]

        if(not_even_my_final_form > self.threshold):
            self.output=1.0
        else:
            self.output=0.0
        
                  
    def calculate_output(self, attr1, attr2, attr3, attr4, attr5):
        self.entries[1]=attr1
        self.entries[2]=attr2
        self.entries[3]=attr3
        self.entries[4]=attr4
        self.entries[5]=attr5
        
        self.calculate()

#---------------------- Learning Master ----------------------#

def perceptron(listmammos, neuronLambda):
    nb_errors=12
    ite=0
    output=0.0

    while (nb_errors > 0 and ite < 1000):
        nb_errors = 0

        for mammo in listmammos:
            neuronLambda.calculate_output(mammo.bi_rads, mammo.age, mammo.shape, mammo.margin, mammo.density)
            output = neuronLambda.output
            true_answer = mammo.get_response()


            for j in range(len(neuronLambda.weights)):
                neuronLambda.weights[j] += neuron.learning_rate*(true_answer - output)*neuronLambda.entries[j]
                """if true_answer - output != 0:
                print mammo.size, mammo.weight
                print neuron.learning_rate*(true_answer - output)*neuronLambda.entries[j]
                print neuronLambda.weights"""
            nb_errors += math.fabs(true_answer - output)
            
        ite += 1
        
    print(nb_errors)
    print(ite)
#---------------------- Learning Data ----------------------#

def parse_data(data_file_name):
    inputfile = open(data_file_name)

    listmammo = []

    for line in inputfile:
        temp_mammo = mammo()
        strings = line.split(",")

        temp_mammo.set_characteristics(strings[0], strings[1], strings[2], strings[3], strings[4], strings[5])

        if check_missing_arg(temp_mammo):
            listmammo.append(temp_mammo)


    print len(listmammo)

    inputfile.close()
    return listmammo
    
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

#Initalizing listmammos with real data:

listmammos = parse_data("mammographic_masses.data")


print ("-" * 100)

#---------------------- Creating Neurons ----------------------#

neuronLambda = neuron()
neuronLambda.init_weights()


#---------------------- Testing string comparison ----------------------#
#print("A"=="B") # false
#print("A"=="A") # true
#print("A"==listmammos[0].name) # true
#print("A"==listmammos[6].name) # false

#All working well with ==

#---------------------- Using Neural Network ----------------------#

print(neuronLambda.weights)
perceptron(listmammos, neuronLambda)
print(neuronLambda.weights)

