Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arithmetic
a=5
b=9
print(a+b)
14
print(a-b)
-4
prin(*b)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    prin(*b)
NameError: name 'prin' is not defined. Did you mean: 'print'?
print(a*b)
45
print(a//b)
0
print(a/b)
0.5555555555555556
print(a**b)
1953125
print(a%b)
5
#assignment operator
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
14
a=8
b=9
b+=a
b+a
25
b+=a
b
25
b-=a
b
17
b*=a
b
136
b//=a
b
17
b/=a
b
2.125
b**=a
b
415.7875443100929
b%=a
b
7.787544310092926
a=7
b=6
a+=
SyntaxError: invalid syntax
a+=b
a
13
a-=b
b
6
a*=b
a
42
a//=b
a
7
a/=b
a
1.1666666666666667
a**=b
a
2.5216263717421135
a%=b
a
2.5216263717421135
#comparsion operator
a=6
b=9
a<b
True
b>a
True
b<a
False
b>a
True
a<=b
True
a>=b
False
b<=a
False
b>=a
True
a!=b
True
b!=a
True
a==b
False
b==a
False
#logical operator
a=5
b=4
a<b and b>a
False
b<a and a>b
True
a<=b and b>=a
False
a<b or b>a
False
a!=b or b!=a
True
a<=b or b<=a
True
not True
False
not False
True
#identity operator
a=4
a is int
False
type (a) is int
True
type(a) is not int
False
type (a) is float
False
type (a) is not float
True
>>> type(a) is str
False
>>> type(a) is compex
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    type(a) is compex
NameError: name 'compex' is not defined. Did you mean: 'complex'?
>>> 
>>> type(a) is complex
False
>>> type(a) is boolean
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    type(a) is boolean
NameError: name 'boolean' is not defined
>>> type(a) is bool
False
>>> type (a) is not str
True
>>> type(a) is not complex
True
>>> type(a) is not bool
True
>>> a=3,5,8,6,9
>>> 8 in type(a)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    8 in type(a)
TypeError: argument of type 'type' is not a container or iterable
>>> 8 in a
True
>>> 8 not in a
False
>>> 23 in a
False
>>> 23 is not in a
SyntaxError: invalid syntax
>>> 23 not in a
True
