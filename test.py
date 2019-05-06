from Library.utils import *
from Library.networkStructure as Network

# results = [circle, egg, house, mickey, question, sadface, square, tree, triangle]
circleResults   = [1,0,0,0,0,0,0,0,0]
eggResult       = [0,1,0,0,0,0,0,0,0]
houseResults    = [0,0,1,0,0,0,0,0,0]
mickeyResults   = [0,0,0,1,0,0,0,0,0]
questionResults = [0,0,0,0,1,0,0,0,0]
sadfaceResults  = [0,0,0,0,0,1,0,0,0]
squareResults   = [0,0,0,0,0,0,1,0,0]
treeResults     = [1,0,0,0,0,0,0,1,0]
triangleResults = [1,0,0,0,0,0,0,0,1]

# TestTuples (input, output)
circleInputs = readElements('Circle')
testArrayCricles = []
for x in circleInputs:
    tupleTest = (x, circleResults)
    testArrayCricles.append(tupleTest)

validationData = (testArrayCricles[:4], 'circle')

# Test

net = Network.Network([784, 30, 9])

net.SGD(training_data, 30, 10, 3.0, test_data=test_data)


# print(len(readElements('Circle')))
# print(len(readElements('Egg')))
# print(len(readElements('House')))
# print(len(readElements('MickeyMouse')))
# print(len(readElements('QuestionMark')))
# print(len(readElements('SadFace')))
# print(len(readElements('Square')))
# print(len(readElements('Tree')))
# print(len(readElements('Triangle')))

