from LinearProbingHash import LinearProbingHash
from QuadraticProbingHash import QuadraticProbingHash
from DoubleHashingProbingHash import DoubleHashingProbingHash
import sys

#parses and formats increaseRandom.txt file
fiR = open("increaseRandom.txt", "r")
unparsed = fiR.read().splitlines()
iRandom = []
for i in range(1, len(unparsed)):
    for e in unparsed[i].split(' '):
        if e != '':
            iRandom.append(int(e.strip()))
fiR.close()

#parses and formats decreaseRandom.txt file
fdR = open("decreaseRandom.txt", "r")
unparsed = fdR.read().splitlines()
dRandom = []
for i in range(1, len(unparsed)):
    for e in unparsed[i].split(' '):
        if e != '':
            dRandom.append(int(e.strip()))
fdR.close()

#parses and formats unordered r100.txt file
fuR = open("rin100.txt", "r")
unparsed = fuR.read().splitlines()
uRandom = []
for i in range(1, len(unparsed)):
    for e in unparsed[i].split(' '):
        if e != '':
            uRandom.append(int(e.strip()))
fuR.close()

#parses and formats in.txt file
fR = open("in.txt", "r")
unparsed = fR.read().split(' ')
random = [int(e) for e in unparsed]
fR.close()

def driver(ints, outFile): #takes list of numbers for hashing and a text file for storing test results as inputs
    
    #initializes hash objects
    linear = LinearProbingHash(191)
    quadratic = QuadraticProbingHash(191)
    double = DoubleHashingProbingHash(191)
    
    #opens output file in write mode and redirects print statements to given output file
    sys.stdout = open(outFile, "w")
    
    #iterates over given number lists, performs probing operations, and writes value/collision data to output file
    for i in range(0, len(ints)):
        value = i + 1
        
        #performs tests for linear probing and prints to output file
        print("Before linear key = " + str(ints[i]) + " got value = " + str(value))
        print("1.before put LinearProbingHash.collisions = " + str(linear.collisions()))
        linear.put(ints[i], value)
        print("2.after put LinearProbingHash.collisions = " + str(linear.collisions()))
        val = linear.get(ints[i])
        print("3.after get LinearProbingHash.collisions = " + str(linear.collisions()))
        print("After linear key = " + str(ints[i]) + " got value(*p) = " + str(val))
        print("\n")
        
        #performs tests for quadratic probing and prints to output file
        print("Before quadratic key = " + str(ints[i]) + " got value = " + str(value))
        print("1.before put QuadraticProbingHash.collisions = " + str(quadratic.collisions()))
        quadratic.put(ints[i], value)
        print("2.after put QuadraticProbingHash.collisions = " + str(quadratic.collisions()))
        val = quadratic.get(ints[i])
        print("3.after get QuadraticProbingHash.collisions = " + str(quadratic.collisions()))
        print("After quadratic key = " + str(ints[i]) + " got value(*pq) = " + str(val))
        print("\n")
        
        #performs tests for double hash probing and prints to output file
        print("Before double hashing key = " + str(ints[i]) + " got value = " + str(value))
        print("1.before put DoubleHashingProbingHash.collisions = " + str(double.collisions()))
        double.put(ints[i], value)
        print("2.after put DoubleHashingProbingHash.collisions = " + str(double.collisions()))
        val = double.get(ints[i])
        print("3.after get DoubleHashingProbingHash.collisions = " + str(double.collisions()))
        print("After double hashing key = " + str(ints[i]) + " got value(*pdh) = " + str(val))
        print("\n")
    
if __name__ == '__main__':
    driver(iRandom, "increaseRandomOut.txt")
    driver(dRandom, "decreaseRandomOut.txt")
    driver(uRandom, "rout100.txt")
    driver(random, "out.txt")
    
    
