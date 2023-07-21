# Week 8



# 1

What types are avalible as inbuilt types in Python? 

# 2

What other useful types are available with Python's standard library? 

# 3

Write a Python function print_dict() that displays the contents of a dict in the format below:

# 4

Write a Python program, times.py which prints a table of multiplications.

Your program will be given the dimension of the table and the width of the columns to be printed. For example

```
$ ./times.py 5 5 5
    1     2     3     4     5
    2     4     6     8    10
    3     6     9    12    15
    4     8    12    16    20
    5    10    15    20    25
```

# 5

Write a Python program missing_words.py which given two files as arguments prints, in sorted order, all the words found in file1 but not file2.

You can assume words occur one per line in each file

# 6

Write a Python program source_count.py which prints the number of lines of C source code in the current directory. In other words, this Python program should behave similarly to wc -l *.[ch]. (Note: you are not allowed to use wc or other Unix programs from within the Perl script). For example: 

```
./source_count.py
    383 cyclorana.c
    280 cyclorana.h
     15 enum.c
    194 frequency.c
    624 model.c
    293 parse.c
    115 random.c
     51 smooth.c
    132 util.c
     16 util.h
    410 waveform.c
   2513 total
```


# 7

 Write a Python program, phone_numbers.py which given the URL of a web page fetches it by running wget and prints any strings that might be phone numbers in the web page.

Assume the digits of phone numbers may be separated by zero or more spaces or hyphens ('-') and can contain between 8 and 15 digits inclusive.

You should print the phone numbers one per line with spaces & hyphens removed. 

```
./phone_numbers.py https://www.unsw.edu.au
20151028
11187777
841430912571345
413200225
61293851000
57195873179
```
