# hashing-strategies
An exploration of linear probing, quadratic probing, and double-hash probing.


Purpose

    This project is designed to explore hashing in general and specifically
    three methods for resolving collisions in hash tables:
    linear probing, quadratic probing, and double hash probing.

    This has been done by creating 3 classes for these probing techniques
    using the LinearProbingHash class as a base class and a nested Record
    class within LinearProbingHash for tracking the <key, value> pairs 
    being inserted into the hash tables.

    A driver is included to parse 4 text files, test the hash class methods
    on the data contained within the parsed lists, and track the collisions
    that occur when records are inserted into hash tables.

Input

    A text file containing numbers.

Output

    Data on collisions, record keys, and record values is written to the output file listed in the driver call.

Bugs or Implemented Test Cases

    Linear probing, quadratic probing, and double hash probing methods are tested on lists containing random 
    increasing, random decreasing, and just plain random numbers.
    

Ben Mackenzie - March 19, 2018


