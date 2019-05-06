from Library.utils import *
import Library.networkStructure as Network

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
# print(circleInputs[1].swapaxes(0,1).shape)
for x in circleInputs:
    tupleTest = (x, circleResults)
    testArrayCricles.append(tupleTest)

validationData = (testArrayCricles[:4], 'circle')

# Test

net = Network.Network([784, 16, 16, 9])

net.SGD(testArrayCricles, 30, 9, 3.0, test_data=validationData)


# print(len(readElements('Circle')))
# print(len(readElements('Egg')))
# print(len(readElements('House')))
# print(len(readElements('MickeyMouse')))
# print(len(readElements('QuestionMark')))
# print(len(readElements('SadFace')))
# print(len(readElements('Square')))
# print(len(readElements('Tree')))
# print(len(readElements('Triangle')))

