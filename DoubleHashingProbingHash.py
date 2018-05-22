'''
Created on Mar 18, 2018

@author: benjaminmackenzie
'''

from LinearProbingHash import LinearProbingHash

class DoubleHashingProbingHash(LinearProbingHash):
    '''
    Set as subclass of LinearProbingHash class in order to maximize code re-use.
    The private "_lookUp" method will be rewritten here to meet the criteria for Double Hashing,
    and a second hashing private method "_hash2" will be written to increment the hashing index 
    after collisions in conjunction with the "_hashIndex" method from LinearProbingHash.
    '''

    def _hash2(self, key):
        R = 181
        return R - (key % R)
        
    def _lookUp(self, key):
        i = 0
        startIndex = self._hashIndex(key)
        index = startIndex
        while True:
            p = self._table[index]
            if p == None:
                return index
            elif p.key == key:
                return index
            #double hash probing
            self._collisions += 1
            i += 1
            index = startIndex + i * self._hash2(key)
            #if we re-check any position, we have traversed the entire table and it is full.
            if index == startIndex:
                print("Table is full")
                return len(self._table)
            #if the end of the table is reached, take modulo of index and table size
            elif index >= len(self._table):
                index = index % len(self._table)