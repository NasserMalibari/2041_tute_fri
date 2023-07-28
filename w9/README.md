# Week 9

# Admin

- Labs and Weekly tests as usual
- myExperience is out !
- Assignment 2 is out

# 1

Discuss how Python can be generated for the supplied examples for subsets 0-3

# 2

Discuss the assignment specification and possible strategies for the assignment. 

# 3

 Write a Python program, tags.py which given the URL of a web page fetches it by running wget and prints the HTML tags it uses.

The tag should be converted to lower case and printed in alphabetical order with a count of how often each is used.

Don't count closing tags.

Make sure you don't print tags within HTML comments
```
$ ./tags.py https://www.cse.unsw.edu.au
a 141
body 1
br 14
div 161
...
```

# 4

Add an -f option to tags.py which indicates the tags are to be printed in order of frequency. 

```
$ ./tags.py -f https://www.cse.unsw.edu.au
head 1
noscript 1
html 1
form 1
title 1
footer 1
header 1
body 1
h2 2

```

# 5

Modify tags.py to use the requests and beautifulsoup4 modules

# 6



If you fell like a harder challenge after finishing the challenge activity in the lab this week have a look at the following websites for some problems to solve using regexp:

    https://regex101.com/quiz
    https://alf.nu/RegexGolf

