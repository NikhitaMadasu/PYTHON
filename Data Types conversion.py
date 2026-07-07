Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
int(7)
7
>>> int(4.5)
4
>>> int("code")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    int("code")
ValueError: invalid literal for int() with base 10: 'code'
>>> int(4+5j)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(4+5j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(True)
1
>>> INt(False)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    INt(False)
NameError: name 'INt' is not defined. Did you mean: 'int'?
>>> int(False)
0
>>> float(5)
5.0
>>> float(4.5)
4.5
>>> float("code")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    float("code")
ValueError: could not convert string to float: 'code'
>>> float(4+5j)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float(4+5j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float(True)
1.0
>>> float(False)
0.0
>>> str(7)
'7'
>>> str(4.5)
'4.5'
>>> str("code")
'code'
>>> str(4+5j)
'(4+5j)'
str(True)
'True'
str(False)
'False'
complex(55)
(55+0j)
complex(5)
(5+0j)
complex(4.5)
(4.5+0j)
complex("code")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    complex("code")
ValueError: complex() arg is a malformed string
complex(4.5j)
4.5j
complex(True)
(1+0j)
complex(False)
0j
bool(5)
True
bool(66)
True
bool(-1)
True
bool(5.5)
True
bool("code")
True
bool('''code''')
True
bool(0)
False
bool(True)
True
bool(False)
False
