import numpy as np
import math
import random

#---------------------- Data Class ----------------------#
class mammo:
    

    def __init__(self):
        self.BI-RADS = 0
        self.age=0
        self.shape=0
        self.margin=0
        self.density=0
        self.severity=0

    def set_characteristics(self, BI-RADS, age, shape, margin, density, severity):
        self.BI-RADS=BI-RADS
        self.age=age
        self.shape=shape
        self.margin=margin
        self.density=density
        self.severity=severity

    def get_response(self):
        return severity


#---------------------- Neuralis Class ----------------------#
class neuron:

    learning_rate = 1
    
    def __init__(self):
        self.entries=[1.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.weights=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
        self.threshold=1.0
        self.output=0.0

    def init_weights(self):
        for i in range(len(weights)):
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
            #print(self.weights)
        
                  
    def calculate_output(self, attr1, attr2, attr3, attr4):
        self.entries[1]=attr1
        self.entries[2]=attr2
        self.entries[3]=attr3
        self.entries[4]=attr4
        
        self.calculate()

#---------------------- Learning Master ----------------------#

def perceptron(listmammos, neuronLambda):
    nb_errors=12
    ite=0
    output=0.0

    while (nb_errors > 0 and ite < 100000):
        nb_errors = 0
        
#        print neuronLambda.weights

        for mammo in listmammos:
            neuronLambda.calculate_output(mammo.size, mammo.weight)
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

listmammos = [ mammo() for i in range(12)]

#Initalizing listmammos with real data:

listmammos[0].set_characteristics("A", 36, 17)
listmammos[1].set_characteristics("A", 41, 16)
listmammos[2].set_characteristics("A", 48, 18)
listmammos[3].set_characteristics("A", 47, 18)
listmammos[4].set_characteristics("A", 50, 22)
listmammos[5].set_characteristics("A", 48, 21)
listmammos[6].set_characteristics("B", 48, 12)
listmammos[7].set_characteristics("B", 56, 16)
listmammos[8].set_characteristics("B", 62, 13)
listmammos[9].set_characteristics("B", 60, 24)
listmammos[10].set_characteristics("B", 65, 18)
listmammos[11].set_characteristics("B", 66, 21)


#print(listmammos[5].weight)

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

