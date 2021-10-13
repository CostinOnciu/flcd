# **git repo branch lab2**
    https://github.com/CostinOnciu/flcd

The SymbolTable class has a size (self.__m)
the hashTable (self.__st), and an occupancy that tells when to resize the hashTable.
It has a method named hash that returns a key for the token given. When adding a token 
if it is in the list at the index returned by the hash(token) then the method returns a tuple 
(key, position) without adding anymore the token, if it's not then it adds the token and returns
a new (key, position) tuple, also if the occupancy of the hash table is more than 0.8 after
adding we resize the hash table and recalculate the hash for the token and after this we return 
the new tuple
