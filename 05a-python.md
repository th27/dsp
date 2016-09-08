# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are similar in that they can be any type and they are indexed by integers. However, they are different in that tuples are immutable, whereas lists are mutable. The notation for lists are square brackets e.g. [], whereas tuples are notated in normal brackets e.g.().  
Tuples are commonly used as keys in dictionaries. In fact you can not use lists as keys. This is because dictionaries are implemented using a hashtable, which means that the keys in a dictionary must be hashable. Dictionaries use integers generated via hash functions to look up key-value pairs. This system works only if the keys are immutable (like tuple but not lists). If the key was mutable, a modified key that is hashed would go to a different location and there would be cases where there are multiple entries for the same key.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>>Lists and sets are both a type of built-in data structure. Lists are ordered sequence of objects, that can contain any type of object and they are mutable.  While a list will keep order, sets are unordered sequence of unique elements that can be mutable or immutable (in the case of frozen sets).  
An example of a list: 
```python
l = [1, 2.0, 'three']  
```  
An example of a set:  
```python
s = set([1, 2, 3])  
```  
Sets perform faster than lists for search functions. This is because sets are implemented using hash tables. When testing for membership within 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> lambda in Python is a tool for building function objects without using 'def'i.e. an 'anonymous' function, without a name. It is often used in situations where a shorthand, one-off version of a function is desirable to make code writing easier and the written code clearer.  
An example of a simple lambda application:  
```python
g = lambda x: x ** 2  
print g(x)
```
An example of using a lambda to sort:     
```python
three_tup = [(1,2,3),(6,5,4),(-1,2,5)]    
print sorted(three_tup, key = lambda tup: tup[2])     
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>>
List comprehensions are an easy and elegant way to define and create lists. List comprehensions can be a complete substitute for the lambda function as well as for map() and filter() and are typically a more intuitive syntax that closely resembles mathematical notations.

Two examples of list comprehensions:
```
# convert celsius to fahrenheit usng a list comprehension
celsius = [10, 15, 20, 25, 30, 35]
fahrenheit_list_comp = [((float(9)/5) * x + 32) for x in celsius]
print fahrenheit_list_comp

# get even from fib using a list comprehension
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
even_fib_list_comp = [f for f in fib if f % 2 == 0]
print even_fib_list_comp
```

An equivalent of the first example with a map():
```
# convert celsius to fahrenheit usng a map
celsius = [10, 15, 20, 25, 30, 35]
fahrenheit_map = map(lambda x: ((float(9)/5) * x + 32), celsius)
print fahrenheit_map
```

An equivalent of the second example with a filter():
```
# get even from fib using a filter()
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
even_fib_filter = filter(lambda x: x % 2 == 0, fib)
print even_fib_filter
```

An example of a set comprehension:
```
# return a set (of unique entries) by using a set comprehension
my_list = [10, 10, 20, 20, 30, 30, 40, 40]
l_set = {l for l in my_list if l <= 30}
print l_set
```

An example of a dictionary comprehension:
```
# return an indexed dictionary using a dictionary comprehension
l = ['a', 'b', 'c', 'd']
my_dict = {letter: i for i, letter in enumerate(l, start = 1)}
print my_dict
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days	

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





