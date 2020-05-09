import cv2 as cv
import numpy as np
import time

tableOfSeeds = []
difference = 0
colorOfOutImage = 255


def getCoordinates(x, y, shape, outimg):
    global colorOfOutImage
    outTable = []

    valueXmin1 = (min(max(x - 1, 0), shape[1] - 1))
    valueXplus1 = (min(max(x + 1, 0), shape[1] - 1))
    valueYmin1 = (min(max(y - 1, 0), shape[0] - 1))
    valueYplus1 = (min(max(y + 1, 0), shape[0] - 1))

    # left  top
    if outimg[valueXmin1, valueYmin1] != colorOfOutImage:
        outTable.append((valueXmin1, valueYmin1))

    # left bot
    if outimg[valueXmin1, valueYplus1] != colorOfOutImage:
        outTable.append((valueXmin1, valueYplus1))

    # left mid
    if outimg[valueXmin1, y] != colorOfOutImage:
        outTable.append((valueXmin1, y))

    # center top
    if outimg[x, valueYmin1] != colorOfOutImage:
        outTable.append((x, valueYmin1))

    # center bot
    if outimg[x, valueYplus1] != colorOfOutImage:
        outTable.append((x, valueYplus1))

    # right top
    if outimg[valueXplus1, valueYmin1] != colorOfOutImage:
        outTable.append((valueXplus1, valueYmin1))

    # right mid
    if outimg[valueXplus1, y] != colorOfOutImage:
        outTable.append((valueXplus1, y))

    # right bot
    if outimg[valueXplus1, valueYplus1] != colorOfOutImage:
        outTable.append((valueXplus1, valueYplus1))

    return outTable


def mouseClicked(event, x, y, flags, params):
    if event == cv.EVENT_FLAG_LBUTTON:
        print('Starting point: ' + str(x) + ', ' + str(y))
        tableOfSeeds.append((y, x))


def regionGrowing(image, startPoint):
    global difference
    global colorOfOutImage
    start = time.time()
    tempList = []
    outImage = np.zeros_like(image)
    tempList.append((startPoint[0], startPoint[1]))
    processed = []
    bright = image[startPoint[0], startPoint[1]]
    # print("Base brightness: " + str(bright))
    while len(tempList) > 0:
        pixel = tempList[0]
        for coord in getCoordinates(pixel[0], pixel[1], image.shape, outImage):
            if coord not in processed and bright + difference >= image[coord[0], coord[1]] >= bright - difference:
                tempList.append(coord)
                outImage[coord[0], coord[1]] = colorOfOutImage  # set brigthness for out image
                processed.append(coord)
                # print(image[coord[0], coord[1]])  # show brightness of pixel

        tempList.pop(0)
        # cv.imshow("Progress window", outImage)
        # cv.waitKey(1)

    stop = time.time()
    t = stop - start
    print("Time: " + str(t))

    return outImage


def main(imageToSeg, x, y, use, differenceP):
    image = cv.imread(imageToSeg, 0)
    cv.namedWindow('Initial segmentation')

    if use == 1:
        cv.setMouseCallback('Initial segmentation', mouseClicked, 0, )

    if use == 2:
        tableOfSeeds.append((y, x))

    global difference
    difference = 256 * differenceP * 0.01
    cv.imshow('Initial segmentation', image)
    cv.waitKey()
    startingPoint = tableOfSeeds[-1]
    out = regionGrowing(image, startingPoint)
    cv.imwrite("/home/krystian/Pulpit/ImagesPAMM/edited/out.bmp", out)
    cv.imshow('Region Growing', out)
    cv.waitKey()
    cv.destroyAllWindows()
