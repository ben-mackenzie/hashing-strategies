'''
Created on Mar 18, 2018

@author: benjaminmackenzie
'''

from LinearProbingHash import LinearProbingHash

class QuadraticProbingHash(LinearProbingHash):
    '''
    Set as subclass of LinearProbingHash class in order to maximize code re-use.
    The private "_lookUp" method will be rewritten here to meet 
    the criteria for Quadratic Hash Probing.
    '''
    
    def _lookUp(self, key):
        startIndex = self._hashIndex(key)
        i = 0
        index = startIndex + i*i
        while True:
            p = self._table[index]
            if p == None:
                return index
            elif p.key == key:
                return index
            #quadratic probing
            self._collisions += 1
            i += 1
            index = startIndex + i*i
            index = index % len(self._table) 
            if index == startIndex: #index and startIndex are both 10 when value = 16
                print("Table is full")
                return len(self._table)
            

        