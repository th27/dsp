# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

>> pwd - print working directory
   mkdir - make directory
   cd  - change directory
   ls - list directory
   rmdir - remove directory
   touch - make an empty file
   pushd - push directory
   popd - pop directory
   cp - copy a file or directory
   mv - move a file or directory
   less - page through a file
   cat - print the whole file
   find - find files
   grep - find things inside files
   exit - exit the shell

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

>>`ls` lists files and folders in current directory  
`ls -a` lists all entries, including names beginning with a period (.)
`ls -l` displays the long format listing
`ls -lh` lists long format with readable file size
`ls -lah` displays long format listing; for all entries including names beginning with a period (.); with readable file size
`ls -t` sort by time & date  
`ls -Glp`lists long format with readable file size; but do not list owner name; and displays directories with slash (/)

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

>> 'ls -d' displays only directories
   'ls -l' displays the long format listing
   'ls -m' displays the names as a comma separated list
   'ls -p' displays directories with /
   'ls -t' displays newest files first based on timestamp

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

>> xargs is a command used to build and execute command lines from standard input. While some commands (e.g. grep) can accept the standard input as a parameter via a  pipe some others (e.g. cp) do not accept the standard input stream. These others rely on arguments found after the command. xargs breaks the list of arguments into sublists small enough to be acceptable.

  An example is finding files and then looking for a specific keyword on that file using grep.

  find . -name "*.txt" | xargs grep "hello"