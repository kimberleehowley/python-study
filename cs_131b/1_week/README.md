# Week 1: Expressions 

## Interpreter  
### [Python for Everybody](https://fog.ccsf.edu/~abrick/Severance.pdf)
### 1: Why should you learn to write programs? 
* Computers contain: 
  * Central processing unit (CPU): The part of the computer that executes programs (asks "What's next?").
  * Main memory: Stores information the CPU needs quickly; info disappears if computer off.
  * Secondary memory: Slower than main memory, but can store info even if computer off. 
  * Input/output: keyboard, mouse, mic, etc. 
  * Network connection: Way to retrieve data. 
* Programmers write instructions for "What's next?" that are stored in a computer's main memory. 
* Reserved words in Python are like words that humans can use to communicate with dogs: a dog won't understand everything, but knows keywords like "sit" or "stay". Those words can't be used to make the dog understand anything but their first understanding, or, we can't use reserved words for anything other than reserved words' purposes in Python. They have only one meaning. 
* "Python is a way for creators of programs to express how the conversation is supposed to proceed." 
* Python is a "high-level" languages for humans. 
* The actual CPU does not understand high-level languages, and instead understands "machine language". 
* Interpreters or Compilers translate high-level languages to machine language. 
  * _Interpreter_: Reads the programmer's high-level code, parses it, and interprets the instructions on the fly (interactive). Python is an interpreter. 
  * _Compiler_: Needs to be handed an entire program in a file, and then runs a process to translate high-level code into machine language code. Then, the machine language code is put in a file for later execution. 
* The Python interpreter is written in 'C'. 
* "When you installed Python on your computer (or
the vendor installed it), you copied a machine-code copy of the translated Python program onto your system." 

```python
# Program prints the name of my representative in the California Assembly 

print('Kimberlee lives in State Assembly District 11, so her Assembly Member is David Chiu.')
```

## Types
### [Python for Everybody](https://fog.ccsf.edu/~abrick/Severance.pdf)
### 2. Variables, Expressions, and Statements 