# Week 4: Flow 

## Exceptions 
* Runtime errors happen during execution 
* Errors are objects extend from the Exception class
* Common error types: 
  * ValueError 
  * IndexError 
  * TypeError 
* To _except_ an error is to provide a procedural alternativ for a potential failure 
  * We _try_ what we want to do, and _except_ what we do otherwise  

## Files 
* Key terms: _with_ _open_ _read_ _write_ _close_ _bytes_
* Files are inherently sequential storage; they return one line at at time. 
* As a best practice, it's not often necessary to read a file more than once. For continual access, we can store in memory. 
* Calling `open()` yields a wrapper for dealing with a file on a disk 
* `with` can be a context manager that closes the file for us 
* Wrapper object has methods: `read()`, `write()`, and `seek()` 
* It's important to use try and except with file access, because lots of things can go wrong: 
  * The file might not be found 
  * The file might not be readable 
  * The file could be a directory 

## Loops
* Key terms: _for_, _while_ 
* _while_ loops continue until a condition becomes false  
* _for_ iterates over a set list, so it's a little bit safer because there is a set list of things (prevents infinite loops if there is a bad condition)
* When possible, it's good to try to do built-in iteration, like using the `max()`, `min()`, etc. methods 
 * `min()`, for example, can take a second key parameter, e.g. `shortest = min(sys.argv, key=len)`

## [Exceptional Logging of Exceptions in Python](https://www.loggly.com/blog/exceptional-logging-of-exceptions-in-python/)

* The "Big Tarp" pattern 
```python 
try:
    main_loop()
except Exception:
    logger.exception("Fatal error in main loop")
```
  * The `logger.exception` here returns the full stack trace in the context of the except block 

* The "Pinpoint" pattern 
* Looks for a very specific exception type, which has semantic relevance at that particular place in the code.
* Like for the specific conflict when the burrito criteria you're looking for isn't available at a restaurant: 
```python 
from openburrito import find_burrito_joints, BurritoCriteriaConflict
# "criteria" is an object defining the kind of burritos you want.
try:
    places = find_burrito_joints(criteria)
except BurritoCriteriaConflict as err:
    logger.warn("Cannot resolve conflicting burrito criteria: {}".format(err.message))
    places = list()
``` 
  * `logger.warn` is used here to log a particular message, instead of logging the whole stack trace 
* The "Transformer" Pattern 
* Raises a different error from the exception caught 
```python 
try:
    something()
except SomeError as err:
    logger.warn("...")
    raise DifferentError() from err
``` 
* A practical example is when a particular kind of error is not provided in an SDK, so you have to create your own: 
```python
from myexceptions import NoMatchingRestaurants
try:
    places = find_burrito_joints(criteria)
except BurritoCriteriaConflict as err:
    logger.warn("Cannot resolve conflicting burrito criteria: {}".format(err.message))
    raise NoMatchingRestaurants(criteria) from err 
```
* This means you can chain exceptions and errors in python3! 

* "Message and Raise" Pattern 
* Useful when you're dealing with an error at a higher level in the code and want to fall back on that: 
```python 
try:
    something()
except SomeError:
    logger.warn("...")
    raise
```

* Anti patterns and best practices: 
* At least pass an error like the below, to make sure information is passed about where the event happened: 
```python 
try:
    something()
except Exception:
    logger.error("something bad happened", exc_info=True)
``` 
* Never, ever, just `except Exception: pass`. That provides no info and hides errors! 

## [You probably don't need for loops](https://medium.com/python-pandemonium/never-write-for-loops-again-91a5a4c84baf)
* Python has List Comprehension, e.g.: 
```python 
result = [do_something_with(item) for item in item_list]
```
* Generator Expression: 
```python 
result = (do_something_with(item) for item in item_list)
```
* Can also use built-in `.map` and `.reduce` functions 
* Or you can write your own functions to be more efficient! 
* The `itertools` module can also do a lot of things you want for loops to do! 

## [Unicode HOWTO](https://docs.python.org/3/howto/unicode.html)
* Unicode is: a specification that aims to list every character used by human languages and give each character its own unique code.
* "The Unicode standard describes how characters are represented by code points. A _code point_ value is an integer in the range 0 to 0x10FFFF"
* "...Code points needs to be represented in memory as a set of code units, and code units are then mapped to 8-bit bytes. The rules for translating a Unicode string into a sequence of bytes are called a character encoding, or just an encoding." 

## Video Notes