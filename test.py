from Library.utils import *
import Library.networkStructure as Network
import numpy as np

# results = [circle, egg, house, mickey, question, sadface, square, tree, triangle]
circleResults     = np.array([1,0,0,0,0,0,0,0,0,0])
eggResult         = np.array([0,1,0,0,0,0,0,0,0,0])
houseResults      = np.array([0,0,1,0,0,0,0,0,0,0])
mickeyResults     = np.array([0,0,0,1,0,0,0,0,0,0])
questionResults   = np.array([0,0,0,0,1,0,0,0,0,0])
sadfaceResults    = np.array([0,0,0,0,0,1,0,0,0,0])      
squareResults     = np.array([0,0,0,0,0,0,1,0,0,0])
treeResults       = np.array([0,0,0,0,0,0,0,1,0,0])
triangleResults   = np.array([0,0,0,0,0,0,0,0,1,0])
happyfaceResults  = np.array([0,0,0,0,0,0,0,0,0,1])      


# TestTuples (input, output)
circleInputs = readElements('Circle')
testArrayCricles = []

for x in circleInputs:
    tupleTest = (x, circleResults)
    testArrayCricles.append(tupleTest)

validationData = (testArrayCricles[:4], 'circle')

# Test

net = Network.Network([784, 16, 16, 9])

net.SGD(testArrayCricles[0], 30, 9, 3.0, test_data=validationData[0])



# print(len(readElements('Circle')))
# print(len(readElements('Egg')))
# print(len(readElements('House')))
# print(len(readElements('MickeyMouse')))
# print(len(readElements('QuestionMark')))
# print(len(readElements('SadFace')))
# print(len(readElements('Square')))
# print(len(readElements('Tree')))
# print(len(readElements('Triangle')))

