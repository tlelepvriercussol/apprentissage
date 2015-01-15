import numpy as np
import math
import random

#---------------------- Data Class ----------------------#
class rodent:
    

    def __init__(self):
        self.name=""
        self.size=0.0
        self.weight=.0

    def set_characteristics(self, name, size, weight):
        self.name=name
        self.size=size
        self.weight=weight

    def get_response(self):
        if self.name == "A":
            return 1
        else:
            return 0

#---------------------- Neuralis Class ----------------------#
class neuron:

    learning_rate = 1
    
    def __init__(self):
        self.entries=[1.0,0.0,0.0]
        self.weights=[1.0,1.0,1.0]
        self.threshold=1.0
        self.output=0.0

    def init_weights(self):
        self.weights[0]=random.uniform(-100.0,100.0)
        self.weights[1]=random.uniform(-100.0,100.0)
        self.weights[2]=random.uniform(-100.0,100.0)
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
        
                  
    def calculate_output(self, attr1, attr2):
        self.entries[1]=attr1
        self.entries[2]=attr2
        
        self.calculate()

#---------------------- Learning Master ----------------------#

def perceptron(listrodents, neuronLambda):
    nb_errors=12
    ite=0
    output=0.0

    while (nb_errors > 0 and ite < 100000):
        nb_errors = 0
        
#        print neuronLambda.weights

        for rodent in listrodents:
            neuronLambda.calculate_output(rodent.size, rodent.weight)
            output = neuronLambda.output
            true_answer = rodent.get_response()


            for j in range(len(neuronLambda.weights)):
                neuronLambda.weights[j] += neuron.learning_rate*(true_answer - output)*neuronLambda.entries[j]
                """            if true_answer - output != 0:
                print rodent.size, rodent.weight
                print neuron.learning_rate*(true_answer - output)*neuronLambda.entries[j]
                print neuronLambda.weights"""
            nb_errors += math.fabs(true_answer - output)
            
        ite += 1
        
    print(nb_errors)
    print(ite)
#---------------------- Learning Data ----------------------#

listrodents = [ rodent() for i in range(12)]

#Initalizing listrodents with real data:

listrodents[0].set_characteristics("A", 36, 17)
listrodents[1].set_characteristics("A", 41, 16)
listrodents[2].set_characteristics("A", 48, 18)
listrodents[3].set_characteristics("A", 47, 18)
listrodents[4].set_characteristics("A", 50, 22)
listrodents[5].set_characteristics("A", 48, 21)
listrodents[6].set_characteristics("B", 48, 12)
listrodents[7].set_characteristics("B", 56, 16)
listrodents[8].set_characteristics("B", 62, 13)
listrodents[9].set_characteristics("B", 60, 24)
listrodents[10].set_characteristics("B", 65, 18)
listrodents[11].set_characteristics("B", 66, 21)


#print(listrodents[5].weight)

#---------------------- Creating Neurons ----------------------#

neuronLambda = neuron()
neuronLambda.init_weights()


#---------------------- Testing string comparison ----------------------#
#print("A"=="B") # false
#print("A"=="A") # true
#print("A"==listrodents[0].name) # true
#print("A"==listrodents[6].name) # false

#All working well with ==

#---------------------- Using Neural Network ----------------------#

print(neuronLambda.weights)
perceptron(listrodents, neuronLambda)
print(neuronLambda.weights)

