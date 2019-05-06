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

    # save
    img.save('Images/CarasFelices/'+nameOfFile)

main()