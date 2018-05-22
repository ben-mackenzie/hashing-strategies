'''
Created on Mar 18, 2018

@author: benjaminmackenzie
'''

class LinearProbingHash(object):
    '''
    Private:
    _table: data member (hash table) where records are stored.
    _collisions: data member that tracks the number of collisions.
    _hashIndex: uses hash formula to calculate the index for a particular record based on the key.
    _lookUp: returns index of record with inputed key or index appropriate for new record with given key.
    
    Methods:
    get: returns the value at the given key.
    put: stores a <key, value> record in the hash table.
    del: removes a <key, value> record from the hash table.
    collisions: returns the number stored in the _collisions private data member.
    '''  
    class Record(object):
        '''
        A <key, value> pair with two directly accessible data members: "key" and "value."
        '''
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, initialSize):
        '''
        Constructor for the LinearProbingHash object.  
        self._table begins pre-populated with values of "None" at each position
        and self._collisions begins at zero.
        '''
        #constructs empty table
        self._table = [None] * initialSize
        self._collisions = 0
        
    def _hashIndex(self, key):
        index = key
        return index % len(self._table)
    
    def _lookUp(self, key):
        startIndex = self._hashIndex(key)
        index = startIndex
        while True:
            p = self._table[index]
            if p == None:
                return index
            elif p.key == key:
                return index
            #linear probing
            self._collisions += 1
            index += 1
            index = index % len(self._table)
            if index == startIndex:
                print("Table is full")
                return len(self._table)
            
    def get(self, key):
        index = self._lookUp(key)
        if index > len(self._table): 
            return None
        p = self._table[index]
        if p:
            return p.value
        else:
            return None
    
    def put(self, key, value):
        index = self._lookUp(key)
        if index > len(self._table):
            print("Table is full")
        p = self._table[index]
        if not p:
            self._table[index] = self.Record(key, value) #new key-value pair (record)
        else:
            p.value = value
            
    def collisions(self):
        return self._collisions
    
    
