# WEEK 4

# Admin

- Week 3 weekly test is due Thursday 21:00

- Next week we will talk about the assignment, git and testing with shell


# Q1

COMP2041 student wrote this script, named start_lab04.sh, to run before the Week 4 lab. 

```
cat start_lab04.sh
#! /bin/dash

cd ~/labs/04

ex1=jpg2png
ex2=email_image
ex3=date_image
ex4=tag_music`
```

```
$ pwd
/home/z1234567
$ ./start_lab04.sh
pwd
/home/z1234567
$ echo $ex1 $ex2 $ex3 $ex4

```

Why not? How can the sctipy be fixed? 


# Q2

Write a shell script, is_business_hours which exits with a status of 0 if the current time is between 9am - 5pm, and otherwise exits with a status of 1. 

Hint: The `date` command prints the current time in a format like this

# Q3

 COMP2041 student Shruti has a 'friends' subdirectory in her home directory that contains images of her many friends.
Shruti likes to view these images often and would like to have them appear in other directories within her CSE account so she has written a shell script to symlink them to the current directory:

```
for image_file in $(ls ~/friends); do
    ln -s "~/friends/$image_file" .
done
```

The links created by Shruti's script are broken.

Why? How can she fix her script? 


# Q4

The course code for COMP2041 has been changed to COMP2042 and the course code for COMP9044 has been changed to COMP9042.

Write a shell script, update_course_code.sh which appropriately changes the course code in all the files it is given as arguments. 

# Q5

Modify update_course_code.sh so if given a directory as an argument it updates the course codes in files found in that directory and its sub-directories. 

 CSE systems have a command, mlalias, which prints information about a specified mail alias.
For example:
```
$ mlalias cs2041.23T2.tutors
        Alias: cs2041.23T2.tutors
  Description: Maling List For COMP(2041|9044) 2023 T2 Tutors
        Flags: personal, public, unprivileged, members_can_post, closed
    Addresses:
               andrewt
               z9300162
               dylanb
               z5115658
               ...
               z5316004
               z5363586
               z5360319
               z3540752
       Owners: cs2041
      Senders: @COMP2041_Lecturer, @COMP2041_Supervisor
```
Convert the output of the mlalias command into a new line separated list of UNSW zIDs,
like this:
```
z9300162
z5115658
...
z5316004
z5363586
z5360319
z3540752
```

# Q7

 CSE system have a command, acc, which prints information about a specified user.
For example:
```
$ acc z5555555
            User Name : z5555555              Aliases :
                  Uid : 25068                     Gid : 25068
              Expires : 19Dec 2023

               Groups :
        Group classes :
         User classes : 3978_Student, COMP1521t1_Student[10may2022]
                      : COMP1531t1_Student[10may2022], COMP2041t2_Student[26sep2022]
                      : COMP2121t2_Student[26sep2022], COMP2511t1_Student[26sep2022]
                      : COMP1511t1_Tutor[10may2022], COMP2041t2_Tutor[26sep2022]
         Misc classes :

                 Name : Mr Doe, John (John Doe)
             Position : Casual Academic (Sch: Computer Science & Eng)
          UNSW Number : 5555555
            UNSW Mail : z5555555@unsw.edu.au
            UNSW Home : //INFPWFS219.ad.unsw.edu.au/Student038$/z5555555
             CSE Home : /import/kamen/3/z5555555
```
Write a pipeline which converts the output of acc into a new line separated list of courses the person is enrolled as a student in,
like this:
```
COMP1521
COMP1531
COMP2041
COMP2121
COMP2511
```

# Q8

Use the pipeines from the above 2 questions to write shell commands which print a list of courses taken by COMP2041 students with counts of how many COMP2041 students take each,
like this: 

```
7 COMP6771
4 COMP3511
3 COMP4952
3 COMP4951
3 COMP3141
2 COMP9417
...
```

# Q9
 Write a shell script named is_prime.sh which given an integer as an argument, tests whether it is prime and prints a suitable message:
```
$ is_prime.sh 42
42 is not prime
$ is_prime.sh 113
113 is prime
```
Your script should exit with a non-zero exit status if its argument is not prime.

Write a second script named primes.sh which uses the first script to print all primes less than a specified value, e.g:
```
$ primes.sh 100
2
3
5
7
11
13
17
...
79
83
89
97
```

# Q10


# Q11

 The shell variable $PATH contains a colon-separated list of directories. which will be searched when executing a command.

Write a shell script named which.sh which given a program name as argument, uses to ls to print details of matching files in directories in $PATH

For example:
```
$ ./which.sh cat
-rwxr-xr-x 1 root root 43936 Sep 24 18:36 /bin/cat
$ ./which.sh clang
llrwxrwxrwx 1 root root 24 Jan 12 01:49 /usr/bin/clang -> ../lib/llvm-11/bin/clang
$ ./which.sh lost
lost not found
```

The shell builtin which does something similar:
```
which cat
/bin/cat
which clang
/usr/bin/clang
which lost
```

but don't try using which. Use the usual programs we've been using to write scripts such as tr and test.

Think about if any characters in directory names migh break your answer, e.g spaces. 