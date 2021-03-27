import pygame
from math import sqrt, acos, atan2, radians, degrees, pi
from random import randint, choice
from cmath import exp


def writeToFileFromList(listToRightFrom, filename):
    openedFile = open(filename, 'w')
    for item in listToRightFrom:
        openedFile.write(item)
    openedFile.close()


def toggle(boolean):
    if boolean:
        return False
    else:
        return True


def convexHull(pts):  # Graham's scan.
    xleftmost, yleftmost = min(pts)
    by_theta = [(atan2(x-xleftmost, y-yleftmost), x, y) for x, y in pts]
    by_theta.sort()
    as_complex = [complex(x, y) for _, x, y in by_theta]
    chull = as_complex[:2]
    for pt in as_complex[2:]:
        # Perp product.
        while ((pt - chull[-1]).conjugate() * (chull[-1] - chull[-2])).imag < 0:
            chull.pop()
        chull.append(pt)
    return [(pt.real, pt.imag) for pt in chull]


def dft(xs):
    return [sum(x * exp(2j*pi*i*k/len(xs))
                for i, x in enumerate(xs))
            for k in range(len(xs))]


def calculateAngle(pointA, pointB):
    x = pointB[0] - pointA[0]
    y = pointB[1] - pointA[1]
    return 180 - degrees(float(atan2(float(y), float(x))))


def distance(pointA, pointB):
    x = pointA[0] - pointB[0]
    y = pointA[1] - pointB[1]
    return int(sqrt(x ** 2 + y ** 2))


def isOutside(point, rectToCheckIfOutside):
    if point[0] < rectToCheckIfOutside[0] or point[0] > (rectToCheckIfOutside[0]+rectToCheckIfOutside[2]) or \
            point[1] < rectToCheckIfOutside[1] or point[1] > (rectToCheckIfOutside[1]+rectToCheckIfOutside[3]):
        return True
    else:
        return False


def moves(t0, t1, psx, psy, speed):
    speed = speed
    distance = [t0 - psx, t1 - psy]
    norm = sqrt(distance[0] ** 2 + distance[1] ** 2)
    direction = [distance[0] / norm, distance[1] / norm]

    bullet_vector = [direction[0] * speed, direction[1] * speed]
    return bullet_vector


def getCoordinatesToCenterTextMiddle(textToCenter, desiredCenter):
    dimensionsOfText = textToCenter
    desiredCenter = [desiredCenter[0] - (dimensionsOfText[0]/2),
                     desiredCenter[1] - (dimensionsOfText[1]/2), dimensionsOfText[0], dimensionsOfText[1]]
    return desiredCenter


def getCoordinatesForCenteredTextTopLeft(textToCenter, desiredTopLeft):
    dimensionsOfText = textToCenter
    desiredTopLeft = [desiredTopLeft[0] + (dimensionsOfText[0] / 2.0),
                      desiredTopLeft[1] + (dimensionsOfText[1] / 2.0), dimensionsOfText[0], dimensionsOfText[1]]
    return desiredTopLeft


def getCoordinatesForCenteredTextBottomRight(textToCenter, desiredBottomRight):
    dimensionsOfText = textToCenter
    desiredBottomRight = [desiredBottomRight[0]-(dimensionsOfText[0]),
                          desiredBottomRight[1]-(dimensionsOfText[1]), dimensionsOfText[0], dimensionsOfText[1]]
    return desiredBottomRight


def createListOfStars():
    listOfStars = []
    for i in range(0, 110):
        listOfStars.append([randint(0, 640), randint(0, 640)])
    return listOfStars


def drawRectanglesFromList(listToDrawFrom, placeToDrawOn):
    for rectangleToDraw in listToDrawFrom:
        pygame.draw.rect(placeToDrawOn, (255, 255, 255), [rectangleToDraw[0], rectangleToDraw[1], 2, 2])


def oddlySpecificListReformatting(listToReformat):
    if listToReformat is not None:
        newList = []
        for i in listToReformat:
            newList.append(int(str(i).replace('\n', '')))
        return newList


def listSplit(listToSplit):
    newList = []
    for i in listToSplit:
        temporaryList = []
        listElement = i.split("|")
        for subListElement in listElement:
            temporaryList.append(subListElement.replace("\n", ""))
        newList.append(temporaryList)
    return newList


def readFromFile(filename=""):
    if filename != "":
        toReturn = []
        try:
            fileToReadFrom = open(filename, 'r')
        except:
            return ["aaaaa|0|Loss", "aaaaa|0|Loss"]
        
        while True:
            try:
                newLine = fileToReadFrom.readline()
                if newLine.strip() == "":
                    break
                toReturn.append(newLine)
            except EOFError:
                return toReturn
        return toReturn


def reformat(new, old, frame):
    reformed = pygame.PixelArray(new)
    r2 = pygame.PixelArray(old)
    reformed[:, ::(frame+2)] = r2[:, ::(frame+2)]
    return reformed.surface


def range2(start, stop=None, step=1.0):
    if stop is None:
        stop = start
        start = 0
    x = []
    while start <= stop:
        x.append(start)
        start += step
    return x


def dotProduct(v1, v2):
    return sum((a*b) for a, b in zip(v1, v2))


def length(v):
    return sqrt(dotProduct(v, v))


def angle(v1, v2):
    return acos(dotProduct(v1, v2) / (length(v1) * length(v2)))
