# Week 2: Numbers 

## Conditionals 
* Full colons and indentations demonstrate loops in Python 
* They end when their indentations end 
* `elifs` and `else` can be distinct branches within 
* A bool value controls each conditional 
* Instead of `if len(name)>0`, we can write `if len(name)` or `if name` to do the same. 
* Order of conditions matter because each one is exclusive (not dependent on each other). 
* "Nested ternary conditionals" can synthesize some conditionals. 

## Math 
* `//` is different than `/`! The former just returns an int. 
* The math and random libraries are useful. 

## Video 

### [Python for Everybody](https://fog.ccsf.edu/~abrick/Severance.pdf)
### 3: Conditional Execution 
* I can use the `is` operator in Python, e.g. `x is y` or `x is not y`. 
* `==` is my comparison operator. Not `=`. That's an assignment! 
* Logical operators: `and`, `or`, and `not`. 
* `pass` statement can be used as a placeholder for code that does nothing. 
* _Alternative execution_: basically an else statement.
* _Chained conditions_: `elif` and `else` statements.  
* Conditionals can also be _nested_. 
* Try/except are built into conditionals in Python and handle expected and unexpected errors, like an "insurance policy" 
  * If all goes well, Python executes the `try` block of code; otherwise, it goes to `except` if there is a mistake
* _Short circuiting_: When overall value is already known in a program, so it stops the evaluation and doesn't finish the rest 
  * Short circuiting can lead to _the guardian pattern_, where we construct a logical expression with additional comparisons to take advantage of short circuit behavior 
* _Traceback_: A list of functions that are executing, printed when an exception occurs. 