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

## Severance 
### 6, 8, 9, 10