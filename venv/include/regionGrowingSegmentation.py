import cv2 as cv
import numpy as np

tableOfSeeds = []


def getCoordinates(x, y, shape):
    outTable = []
    maximumOfX = shape[1] - 1
    maximumOfY = shape[0] - 1

    # left  top
    coordinatesOfX = min(max(x - 1, 0), maximumOfX)
    coordinatesOfY = min(max(y - 1, 0), maximumOfY)
    outTable.append((coordinatesOfX, coordinatesOfY))

    # left bot
    coordinatesOfX = min(max(x - 1, 0), maximumOfX)
    coordinatesOfY = min(max(y + 1, 0), maximumOfY)
    outTable.append((coordinatesOfX, coordinatesOfY))

    # left mid
    coordinatesOfX = min(max(x - 1, 0), maximumOfX)
    coordinatesOfY = y
    outTable.append((coordinatesOfX, coordinatesOfY))

    # center top
    coordinatesOfX = x
    coordinatesOfY = min(max(y - 1, 0), maximumOfY)
    outTable.append((coordinatesOfX, coordinatesOfY))

    # center bot
    coordinatesOfX = x
    coordinatesOfY = min(max(y + 1, 0), maximumOfY)
    outTable.append((coordinatesOfX, coordinatesOfY))

    # right top
    coordinatesOfX = min(max(x + 1, 0), maximumOfX)
    coordinatesOfY = min(max(y - 1, 0), maximumOfY)
    outTable.append((coordinatesOfX, coordinatesOfY))

    # right mid
    coordinatesOfX = min(max(x + 1, 0), maximumOfX)
    coordinatesOfY = y
    outTable.append((coordinatesOfX, coordinatesOfY))

    # right bot
    coordinatesOfX = min(max(x + 1, 0), maximumOfX)
    coordinatesOfY = min(max(y + 1, 0), maximumOfY)
    outTable.append((coordinatesOfX, coordinatesOfY))

    return outTable


def mouseClicked(event, x, y, flags, params):
    if event == cv.EVENT_FLAG_LBUTTON:
        print('Starting point: ' + str(x) + ', ' + str(y))
        tableOfSeeds.append((y, x))


def regionGrowing(image, startPoint):
    tempList = []
    outImage = np.zeros_like(image)
    tempList.append((startPoint[0], startPoint[1]))
    processed = []
    bright = image[startPoint[0], startPoint[1]]
    difference = 256 * 0.07
    print("Base brightness: " + str(bright))
    while len(tempList) > 0:
        pixel = tempList[0]
        outImage[pixel[0], pixel[1]] = 255  #color of base pixel
        for coord in getCoordinates(pixel[0], pixel[1], image.shape):
            if (image[coord[0], coord[1]] >= bright - difference) & (image[coord[0], coord[1]] <= bright + difference):
                print(image[coord[0], coord[1]]) #show brightness of pixel
                outImage[coord[0], coord[1]] = 255 #set brigthness for out image
                if not coord in processed:
                    tempList.append(coord)
                processed.append(coord)
        tempList.pop(0)
        cv.imshow("Progress window", outImage)
        cv.waitKey(1)

    return outImage


def main(imageToSeg, x, y, use):

    image = cv.imread(imageToSeg, 0)
    cv.namedWindow('Initial segmentation')

    if use == 1:
        cv.setMouseCallback('Initial segmentation', mouseClicked, 0, )

    if use == 2:
        tableOfSeeds.append((y, x))

    cv.imshow('Initial segmentation', image)
    cv.waitKey()
    startingPoint = tableOfSeeds[-1]
    out = regionGrowing(image, startingPoint)
    cv.imshow('Region Growing', out)
    cv.waitKey()
    cv.destroyAllWindows()