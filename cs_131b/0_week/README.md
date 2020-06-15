# CS131B: Week 0 
_Background, tools, and Unix. 

## Background  
* Guido van Rossum, a Dutch computer scientist, developed Python. 
* Make comments in Python with the `#` symbol. Anything between the hash and the new line becomes a comment. 
* Complementary triple quotes, `'''` or `"""` also disable program execution between them. 

## Tools 
* Linux server `hills.ccsf.edu` is where programming for this course takes place. I'll need to login with an `ssh`. 
* Submiting homework: `abrick/send`
* Seeing what to peer review: `abrick/tally` 
* Names of programs I write should end in `.py` 
* Peer reviews end in `.pr`. My comments here cannot be wrapped, but should include long lines (no linebreaks).

## Unix Tutorial (via [Kevin Heard](https://people.ischool.berkeley.edu/~kevin/unix-tutorial/toc.html))
### Intro 
* All UNIX programs are portable, multi-user, and multi-tasking 
### Logging in 
* `ssh username@UNIXhost`
* Then, enter password when prompted 
* `whoami`: returns username 
* `passwd`: change password 
* `logout` 
### Looking around ([full tutorial](https://people.ischool.berkeley.edu/~kevin/unix-tutorial/section3.html))
* `pwd`: print working directory 
* `ls -F`: list fancy: show distinction between files and directories (though sometimes is included in alias)
* Learn about all your files by adding `-a` option, e.g. `ls -aF`  
* Get even more with `ls -alF`, like date modified 
#### Managing files 
* `rmdir`: remove directory, only if it's empty 
* `mv`: move (rename) files  
* `rm -r` can be used to delete files recursively (so rmdir can be used), but is dangerous
- `chmod`: change modes, can manipulate who has permissions to read directories 
#### Viewing and editing 
* `cat` to display contents 
* `more` allows you to sccroll through files one screen at a time (pager)
* The program `pico` can be used for editing files within the terminal 