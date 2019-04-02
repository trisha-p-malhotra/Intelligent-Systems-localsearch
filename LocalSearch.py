"""
file: FIS-HW2.py
language: python3
description: FIS HW 2, evaluating local search algorithms
author: tpm6421@rit.edu (Trisha Malhotra)
"""
__author__ = "Trisha Malhotra"

import math
import random

successor = None


def main():
    """
    Starts at random point , takes file as input, stores it as array
    calls other functions for further evaluation.
    :return: pass
    """
    rowRandom = random.randint(0, 499)
    columnRandom = random.randint(0, 399)

    with open("elevation.txt") as terrain:
            myArray = [line.split() for line in terrain]
    fivebyfive(myArray,successor)
    randowmstartpoint = myArray[rowRandom][columnRandom]
    findingsuccessors(myArray,currentx=rowRandom,currenty=columnRandom)




def Value(fivebyfivelist) :
    """
    Gets difference between min and max values
    i.e. Variation
    :param fivebyfivelist: list of 5x5 matrix
    :return: pass
    """
    maximum = max(fivebyfivelist)
    minimum = min(fivebyfivelist)
    Differencevalue = maximum-minimum
    print("Variation:")
    print(Differencevalue)


def findingsuccessors (myArray,currentx,currenty):
    """
    Finds neighbours for current point
    :param myArray: list input
    :param currentx: x
    :param currenty: y
    :return:
    """

    successors = ((currentx,currenty+1),(currentx-1,currenty),(currentx+1,currenty),(currentx,currenty-1))

    print("Successors of current point:")
    print(successors)
    #print(hillclimb(myArray,successors))

    return successors



def fivebyfive(myArray,successor):
    """
    generates 5x5 matrix
    :param myArray: input list
    :param successor: neighbours
    :return:
    """
    rowRandom = random.randint(0,499)
    columnRandom =  random.randint(0,399)

    fivebyfivelist = []
    startpointformatrix = myArray[rowRandom-2][columnRandom-2]
    print(startpointformatrix)
    for i in range (5):
        fivebyfivelist.append(float(myArray[rowRandom - (2 + i)][columnRandom-2]))

    secondpointformatrix = myArray[rowRandom-2][columnRandom-1]
    for i in range (5):
        fivebyfivelist.append(float(myArray[rowRandom - (2 + i)][columnRandom-1]))

    thirdpointformatrix = myArray[rowRandom][columnRandom]
    for i in range(5):
        fivebyfivelist.append(float(myArray[rowRandom + i][columnRandom]))

    fourthpointformatrix = myArray[rowRandom - 2][columnRandom + 1]
    for i in range(5):
        fivebyfivelist.append(float(myArray[rowRandom -(2+i)][columnRandom + 1]))

    fifthpointformatrix = myArray[rowRandom -2][columnRandom + 2]
    for i in range(5):
        fivebyfivelist.append(float(myArray[rowRandom-(2+i)][columnRandom + 2]))

    print("5x5 matrix for current point:")
    print(fivebyfivelist)
    Value(fivebyfivelist)



def hillclimb(myArray,successors ):
    """
    Hill climb algorithm
    :param myArray:
    :param successors:
    :return:
    """
    rowRandom = random.randint(0, 499)
    columnRandom = random.randint(0, 399)

    currentx = rowRandom
    currenty = columnRandom

    bestval = myArray[rowRandom][columnRandom]
    best_step = None
    for successor in findingsuccessors(myArray):
         for i in successor:
             currentx = successor[1]
             currenty = successor[2]
             newsuccessor = (currentx,currenty)
         fivebyfive(myArray,newsuccessor)

         val = Value(successor)
         if bestval > val:
            best_step = successor
            bestval = val

    if best_step > Value(successor):
        return successor

    return hillclimb(best_step)



def rrhc(myArray,bestval,val):
    """
    Repeatedly calls hillclimb for 50 times
    :param myArray: array made from input text file
    :return: maximum and average
    """
    evalcount = 0
    max_eval = 50
    totalval = 0
    while evalcount < max_eval:
        remaining_eval = max_eval - evalcount
        hillclimb(myArray)

        if val > bestval or bestval is None:
            val = bestval
            totalval = totalval + bestval
        evalcount =+ 1

        avgrrhc = totalval / max_eval
        maxrrhc = bestval

    print(avgrrhc)
    print(maxrrhc)

def sa(myArray):
    """
    sa algorithm
    :param myArray:
    :return:
    """
    rowRandom = random.randint(0, 499)
    columnRandom = random.randint(0, 399)

    currentx = rowRandom
    currenty = columnRandom

    state =(currentx,currenty)
    T = 2
    Tmin = 0.1
    while(T> Tmin):
        findingsuccessors(currentx,currenty)
        snew = successor[random.randint(0,3)]
        if Value(snew) > Value(state):
            state = snew
        elif (random.rand(0,1) < (math.e)^(Value(state)-Value(snew))):
            state = snew

        else:
            state = (random.randint(0, 499),random.randint(0,399))

        T *= 0.999



def rrsa(myArray,bestval,val):
    """
    Repeatedly calls hillclimb for 50 times
    :return: max and avg of values
    """
    sacount = 0
    max_eval = 50
    totalval = 0
    while sacount < max_eval:
        remaining_eval = max_eval - sacount
        sa(myArray)
        if val > bestval or bestval is None:
            val = bestval
            totalval = totalval+ bestval
        sacount = + 1
        avgrrsa = totalval / max_eval
        maxrrsa = bestval

    print(avgrrsa)
    print(maxrrsa)



if __name__ == '__main__':
    main()