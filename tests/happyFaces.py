from PIL import Image, ImageDraw
import random
 
# Global
MIN_POS = 0
MAX_POS = 28 - MIN_POS
RAND_SIZE_MAX = 28

def main():
    for i in range(0,250):
        nameOfFile = "face" + str(i) + ".bmp"
        DrawFace(nameOfFile)


def DrawFace(nameOfFile):
    img = Image.new('RGB', (28, 28), color = 'white')
    draw = ImageDraw.Draw(img)

    # get the center of the face
    centerx = 13 + random.randint(0, 3)
    centery = 13 + random.randint(0, 3)

    # top left and bottom right
    randomSize = random.randint(10,RAND_SIZE_MAX)
    while ((randomSize + centery) > MAX_POS or (randomSize + centerx) > MAX_POS or \
        (centery - randomSize) < 0 or (centerx - randomSize) < 0):
        randomSize = random.randint(10,RAND_SIZE_MAX)

    # Draw Head
    draw.ellipse((centerx - randomSize, centery - randomSize, centerx + randomSize, centery + randomSize), fill = None, outline ='black')

    # # Eyes 
    print(nameOfFile)
    randomSpace = random.randint(1,5)
    while (randomSize /  2 < randomSpace):
        randomSpace = random.randint(2,5)

    upRandom = random.randint(0,2)
    randomBig = random.randint(2, 5)

    topLeft = (centerx - randomSpace, (centery - randomBig) - upRandom)
    bottomLeft = (centerx - randomSpace, (centery + randomBig) - upRandom)

    topRight = (centerx + randomSpace, (centery - randomBig) - upRandom)
    bottomRight = (centerx + randomSpace, (centery + randomBig) - upRandom)

    draw.line([topLeft, bottomLeft], fill='black' )
    draw.line([topRight, bottomRight], fill='black' )

    # Mouth
    mouthRandY = random.randint(0,30) - 10
    mouthSizeRand = random.randint(int(randomSize/6), int(randomSize/2))

    pointLeft = (centerx - mouthSizeRand, centery + mouthRandY-2)
    pointRight = (centerx + mouthSizeRand, centery + mouthRandY+2)

    while (bottomRight[1] >= pointLeft[1] or (pointLeft[1]+5)> (centery + randomSize)):
            mouthRandY = random.randint(0,30) - 10
            pointLeft = (centerx - mouthSizeRand, centery - mouthRandY-2)
            pointRight = (centerx + mouthSizeRand, centery - mouthRandY+2)
    
    mouthSizeRand = random.randint(int(randomSize/6), int(randomSize/2))
    draw.arc([pointLeft, pointRight], 0, 180 , fill='black')

    # AQUI
    img.save('Images/CarasFelices/'+nameOfFile)

main()