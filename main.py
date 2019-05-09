from Library.NetworkArquitecture import NetworkArquitecture
from Library.utils import *
import numpy as np



# results = [circle, egg, house, mickey, question, sadface, square, tree, triangle]
circleResults     = np.array([1,0,0,0,0,0,0,0,0,0]).reshape(10,1)
eggResults        = np.array([0,1,0,0,0,0,0,0,0,0]).reshape(10,1)
houseResults      = np.array([0,0,1,0,0,0,0,0,0,0]).reshape(10,1)
mickeyResults     = np.array([0,0,0,1,0,0,0,0,0,0]).reshape(10,1)
questionResults   = np.array([0,0,0,0,1,0,0,0,0,0]).reshape(10,1)
sadfaceResults    = np.array([0,0,0,0,0,1,0,0,0,0]).reshape(10,1)
squareResults     = np.array([0,0,0,0,0,0,1,0,0,0]).reshape(10,1)
treeResults       = np.array([0,0,0,0,0,0,0,1,0,0]).reshape(10,1)
triangleResults   = np.array([0,0,0,0,0,0,0,0,1,0]).reshape(10,1)
happyfaceResults  = np.array([0,0,0,0,0,0,0,0,0,1]).reshape(10,1)

# results = [circle, egg, house, mickey, question, sadface, square, tree, triangle]
print('[*] Reading all images')
circleInputs  = readElements('Circle')
circleResults = np.array([circleResults] * len(circleInputs))

houseInputs  = readElements('House')
houseResults = np.array([houseResults] * len(houseInputs))

eggInput  = (np.load('Images/Test/egg.npy'))
eggInput = eggInput.reshape(len(eggInput), 784, 1)
eggResults = np.array([eggResults] * len(eggInput))

questionInputs = np.array(np.load('Images/Test/questionmark.npy')).reshape(3060, 784, 1)
questionResults = np.array([questionResults] * (3060))

mickeyInputs  = (np.load('Images/Test/mickeymouse.npy'))
mickeyInputs = mickeyInputs.reshape(len(mickeyInputs), 784, 1)
mickeyResults = np.array([mickeyResults] * len(mickeyInputs))

sadfaceInputs = (np.load('Images/Test/sadface.npy'))
sadfaceInputs = sadfaceInputs.reshape(len(sadfaceInputs), 784, 1)
sadfaceResults = np.array([sadfaceResults] * len(sadfaceInputs))

squareInputs  = readElements('Square')
squareResults = np.array([squareResults] * len(squareInputs))

treeInputs  = readElements('Tree')
treeResults = np.array([treeResults] * len(treeInputs))

triangleInputs  = readElements('Triangle')
triangleResults = np.array([triangleResults] * len(triangleInputs))

happyfaceInputs  = readElements('SmileyFace')
happyfaceResults = np.array([happyfaceResults] * len(happyfaceInputs))


print('[*] Training Start')


input = np.append(circleInputs, houseInputs ,axis=0 )
input = np.append(input, happyfaceInputs    ,axis=0 )
input = np.append(input, triangleInputs     ,axis=0 )
input = np.append(input, treeInputs         ,axis=0 )
input = np.append(input, squareInputs       ,axis=0 )
input = np.append(input, sadfaceInputs      ,axis=0 )
input = np.append(input, mickeyInputs       ,axis=0 )
input = np.append(input, questionInputs     ,axis=0 )
input = np.append(input, eggInput           ,axis=0 )
output = np.append(circleResults, eggResults,axis=0 )
output = np.append(output, houseResults     ,axis=0 )
output = np.append(output, mickeyResults    ,axis=0 )
output = np.append(output, questionResults  ,axis=0 )
output = np.append(output, sadfaceResults   ,axis=0 )
output = np.append(output, squareResults    ,axis=0 )
output = np.append(output, treeResults      ,axis=0 )
output = np.append(output, triangleResults  ,axis=0 )
output = np.append(output, happyfaceResults ,axis=0 )

np.random.seed(0)
np.random.shuffle(np.transpose(input))
np.random.seed(0)
np.random.shuffle(np.transpose(output))


predictionValue = 0
nerual = NetworkArquitecture()
predictionTemp = 0

nerual.train_network(input, output, 10)