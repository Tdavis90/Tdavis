Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 14 2019, 23:09:19) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> temp =70
>>> temp
70
>>> temp = input("Please enter a temperature: ")
Please enter a temperature: 70
>>> temp
'70'
>>> if temp > 70: print ("no jacket")
temp
SyntaxError: invalid syntax
>>> temp = int(temp)
>>> input
<built-in function input>
>>> 
==== RESTART: C:/Users/jerzf/Documents/Intro Problem Solving/conditions 2.py ===
Please enter the current temperature: 70
>>> 
==== RESTART: C:/Users/jerzf/Documents/Intro Problem Solving/conditions 2.py ===
Please enter the current temperature: 70
>>> 
==== RESTART: C:/Users/jerzf/Documents/Intro Problem Solving/conditions 2.py ===
Please enter the current temperature: 
Traceback (most recent call last):
  File "C:/Users/jerzf/Documents/Intro Problem Solving/conditions 2.py", line 4, in <module>
    temp = int(temp)
ValueError: invalid literal for int() with base 10: ''
>>> temp
''
>>> 
==== RESTART: C:/Users/jerzf/Documents/Intro Problem Solving/conditions 2.py ===
Please enter a temperature 70
