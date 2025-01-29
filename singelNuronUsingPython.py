#Singel Nuron Implementation

inputs = [1,1]

def singleNuron(inputs,weights, bias):
  weightedSum = 0
  for i in range(len(inputs)):
    weightedSum += inputs[i] * weights[i]
  weightedSum += bias
  #step activation function
  if(weightedSum > 0):
    print(f"Inputs:{inputs} then Single Nuron Output is: 1")
  else:
    print(f"Inputs:{inputs} then Single Nuron Output is: 0")

weights = [1,1]
bias = -1.5
singleNuron(inputs,weights,bias)


# AND gate implementation using Single Nuron
def ANDGateUsingSingelNuron(inputs,weights, bias):
  weightedSum = 0
  for i in range(len(inputs)):
    weightedSum += inputs[i] * weights[i]
  weightedSum += bias
  #step activation function
  if(weightedSum > 0):
    print(f"Inputs:{inputs} then AND Gate Output is: 1")
  else:
    print(f"Inputs:{inputs} then AND Gate Output is: 0")

weights = [1,1]
bias = -1.5
ANDGateUsingSingelNuron(inputs,weights, bias)


# OR gate implementation using Single Nuron
def ORGateUsingSingelNuron(inputs,weights, bias):
  weightedSum = 0
  for i in range(len(inputs)):
    weightedSum += inputs[i] * weights[i]
  weightedSum += bias
  #step activation function
  if(weightedSum > 0):
    print(f"Inputs:{inputs} then OR Gate Output is: 1")
  else:
    print(f"Inputs:{inputs} then OR Gate Output is: 0")

weights = [2,2]
bias = -1.5
ORGateUsingSingelNuron(inputs,weights, bias)


# NOT gate implementation using Single Nuron
def NOTGateUsingSingelNuron(inputs,weights, bias):
  weightedSum = 0
  weightedSum += inputs[0] * weights[0]
  weightedSum += bias
  #step activation function
  if(weightedSum > 0):
    print(f"Inputs:[{inputs[0]}] then NOT Gate Output is: 1")
  else:
    print(f"Inputs:[{inputs[0]}] then NOT Gate Output is: 0")

weights = [-1.5]
bias = 1
NOTGateUsingSingelNuron(inputs,weights, bias)


# NAND gate implementation using Single Nuron
def NANDGateUsingSingelNuron(inputs,weights, bias):
  weightedSum = 0
  for i in range(len(inputs)):
    weightedSum += inputs[i] * weights[i]
  weightedSum += bias
  #step activation function
  if(weightedSum > 0):
    print(f"Inputs:{inputs} then NAND Gate Output is: 1")
  else:
    print(f"Inputs:{inputs} then NAND Gate Output is: 0")

weights = [-1,-1]
bias = 1.5
NANDGateUsingSingelNuron(inputs,weights, bias)


# NOR gate implementation using Single Nuron
def NORGateUsingSingelNuron(inputs,weights, bias):
  weightedSum = 0
  for i in range(len(inputs)):
    weightedSum += inputs[i] * weights[i]
  weightedSum += bias
  #step activation function
  if(weightedSum > 0):
    print(f"Inputs:{inputs} then NOR Gate Output is: 1")
  else:
    print(f"Inputs:{inputs} then NOR Gate Output is: 0")

weights = [-2,-2]
bias = 1
NORGateUsingSingelNuron(inputs,weights, bias)

#   inputs, weights and bias are adjested for every function in the program 