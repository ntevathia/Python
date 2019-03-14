class HashTable:
    def __init__(self, nbuckets):                      
        """
        Constructor : Initializes the attributes for the class
        """
        self.nbuckets = nbuckets
        self.table = [[] for n in range(nbuckets)]       # create a list of buckets (lists)

    def __len__(self):
        """
        Return : count of elements in all of the buckets in hashtable
        """
        count = 0
        for i in range(self.nbuckets):
            count += len(self.table[i])
        return count
        

    def __setitem__(self, key, value):
        """
        Inserts a (key, value) pair if not present, otherwise replace it with new entry.
        """
        bucket = self.table[self.hashcode(key) % self.nbuckets]
        position = self.bucket_indexof(key)
        if position == -1:                             # if value not present, append it
            bucket.append((key, value))
        else:
            bucket[position] = (key, value)            # if value present already, replace with new one.
        
        return self.table

    def __getitem__(self, key):
        bucket = self.table[self.hashcode(key) % self.nbuckets]    # get the bucket for the key
        position = self.bucket_indexof(key)
        if position != -1:
            return bucket[position][1]                  # get the value for the key, if not found return none

        return None
        

    def __contains__(self, key):         # checks for presence of the key in table
        for i in range(self.nbuckets):
            for elm in self.table[i]:
                if key==elm[0]:
                    return True   
        return False

    def __iter__(self):                   # return the iterator for keys only.
        keys = []
        for i in range(self.nbuckets):
            for elm in self.table[i]:
                keys.append(elm[0])
        return iter(keys)

    def keys(self):
        key_list = []
        for i in range(self.nbuckets):
            for elm in self.table[i]:
                key_list.append(elm[0])
        return key_list

    def items(self):                    # returns a list of all (key, value) pairs
        item_list = []
        for i in range(self.nbuckets):
            for elm in self.table[i]:
                item_list.append(elm)
        return item_list

    def __repr__(self):
        ind = ""
        str = ""
        for i in range(self.nbuckets):
            ind = f'{i:04}' + '->'
            for j in range(len(self.table[i])):
                if j == len(self.table[i]) - 1:
                    ind = ind + "%s:%s" % (self.table[i][j][0], self.table[i][j][1])
                else:
                    ind = ind + "%s:%s" % (self.table[i][j][0], self.table[i][j][1]) + ', '
            str = str + '\n' + ind
        str = str + '\n'
        return str.lstrip()
    
    def __str__(self):
        count = 0
        for i in range(self.nbuckets):
            for j in range(len(self.table[i])):
                count = count + 1
        if self.table == []:
            stri = '{' + '}'
        else:
            stri = ""
            for i in range(self.nbuckets):
                for j in range(len(self.table[i])):
                    count = count - 1
                    if count == 0:
                        stri = stri + "%s:%s" % (self.table[i][j][0], self.table[i][j][1])
                    else:
                        stri = stri + "%s:%s" % (self.table[i][j][0], self.table[i][j][1]) + ', '

            stri = '{' + stri + '}'

        return stri

    def hashcode(self, o):
        if type(o) == int:
            return o
        elif type(o) == str:
            h = 0
            for c in o:
                h = h*31+ord(c)
            return h
        else:
            return None
    
    def bucket_indexof(self, key):
        bucket = self.table[self.hashcode(key) % self.nbuckets]
        for i in range(len(bucket)):
            if key in bucket[i]:  
                return i
        return -1
