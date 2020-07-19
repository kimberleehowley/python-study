# Week 3: Collections

## Containers I 
* In Python, integer indices apply to any ordered collection 
* `len` reveals the number of items in that collection 
* `list` and `tuple` are class types that can store objects of any type 
  * `list`: mutable, can be resized as needed. Supports `find` and `append()` and `pop()`.  
    * Create one with `list()` 
  * `tuple`: immutable, which can be useful for performance. 
    * Create one with `tuple()` 
* `sys.argv`: produces command line arguments in a list of strings.  
  * `import sys` to access  
* `max`: max of a collection 
* `sum`: adds values 
* `any`: True if any value returns true, vs. 
* `all`: only True if all values are true 
* `in`: searches through a collection for a certain value 
* Slicing: `group[n:m:o]` retrieves every `oth` value from group between indices n (included) and m (excluded)

## Containers II 
* `set` and `dict` container classes are unordered and exclude duplicate entries. 
  * `dict`: key-value store, can access like `events[California]`
* `.sort()` can sort lists in place. We can sort the key values of a dictionary. 
* Instances of `set` and `dict` can only contain hashable objects; to be hashable they must be immutable
* `frozenset`: immutable set providing the same benefits as a tuple over a list

## Video Notes 
* Lists and sets are collections 
* Lists has indices and order
  * This means we can use Python's slicing and striding syntax 
  * sys.argv will be a particuar list we focus on 
* Sets are not in any order; just a grab bag 
* Both support the "in" operator, for checking if an element is "in" the collection 


### [Python for Everybody](https://fog.ccsf.edu/~abrick/Severance.pdf)
### 6: Strings 
* A string is a sequence; characters can be accessed one at a time with the bracket operator, using indices 
  * Indices must be integers! 
* `len` gives us the built-in length of a string (starts counting at 1, not 0 like indices)
* You can use negative indices to get last/first letters in strings 
* _Traversal_: Starting at the beginning of something and continuing through each item through to the end 
  * _while_ loops 
  * _for_ loops 

### 8:  
### 9:  
### 10: 