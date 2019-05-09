from Library.NetworkArquitecture import NetworkArquitecture
from Library.utils import *

test = fromImageToArray('test.jpg')

net = NetworkArquitecture()
net.predict(test)
predicted = net.predict(fromImageToArray('test.jpg'))
tmp = 0
for idx, element in enumerate(predicted):
    if element > tmp:
        tmp = element
        index = idx

labelResult = {
    0: "It's a Cricle! I'm {} precente sure".format(tmp),
    1: "It's a Egg! I'm {} precente sure".format(tmp),
    2: "It's a House! I'm {} precente sure".format(tmp),
    3: "It's Mickey! I'm {} precente sure".format(tmp),
    4: "It's a QuestionMark! I'm {} precente sure".format(tmp),
    5: "It's a Sad Face! I'm {} precente sure".format(tmp),
    6: "It's a Square! I'm {} precente sure".format(tmp),
    7: "It's a Tree! I'm {} precente sure".format(tmp),
    8: "It's a Triangle! I'm {} precente sure".format(tmp),
    9: "It's a Happy Face! I'm {} precente sure".format(tmp),
}
print(predicted)
print('Result: {}'.format(labelResult.get(index)))