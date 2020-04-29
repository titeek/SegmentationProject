import cv2
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
    if event == cv2.EVENT_FLAG_LBUTTON:
        print('Starting point: ' + str(x) + ', ' + str(y))
        tableOfSeeds.append((y, x))


def regionGrowing(image, startPoint):
    tempList = []
    outImage = np.zeros_like(image)
    tempList.append((startPoint[0], startPoint[1]))
    processed = []
    while len(tempList) > 0:
        pixel = tempList[0]
        outImage[pixel[0], pixel[1]] = 255
        for coord in getCoordinates(pixel[0], pixel[1], image.shape):
            if image[coord[0], coord[1]] != 0:
                outImage[coord[0], coord[1]] = 255
                if not coord in processed:
                    tempList.append(coord)
                processed.append(coord)
        tempList.pop(0)
        cv2.imshow("Progress window", outImage)
        cv2.waitKey(1)

    return outImage


def main(imageToSeg, x, y, use):

    image = cv2.imread(imageToSeg, 0)
    ret, imageAfterInitialSegmentation = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
    cv2.namedWindow('Initial segmentation')

    if use == 1:
        cv2.setMouseCallback('Initial segmentation', mouseClicked, 0, )

    if use == 2:
        tableOfSeeds.append((y, x))

    cv2.imshow('Initial segmentation', imageAfterInitialSegmentation)
    cv2.waitKey()
    startingPoint = tableOfSeeds[-1]
    out = regionGrowing(imageAfterInitialSegmentation, startingPoint)
    cv2.imshow('Region Growing', out)
    cv2.waitKey()
    cv2.destroyAllWindows()
