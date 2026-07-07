Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#escape sequence
#\n->new line
#\t->tab space
a="name\nmobile\temailid\nclg"
print(a)
name
mobile	emailid
clg
b="name:nikhita\nmobile:9515532455\temailid:nikhita3535@gmail.com\nclg
SyntaxError: unterminated string literal (detected at line 1)
b="name:nikhita\nmobile:9515532455\temailid:nikhita3535@gmail.com\nclg"
b=print(b)
name:nikhita
mobile:9515532455	emailid:nikhita3535@gmail.com
clg
#replace
c="wait until you succeed"
c.replace("wait","work")
'work until you succeed'
c.replace("until","let")
'wait let you succeed'
d="wait wait until you succeed"
d.replace("wait","wait","work")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    d.replace("wait","wait","work")
TypeError: 'str' object cannot be interpreted as an integer
d.replace("wait","work")
'work work until you succeed'
d.replace("wait","work",2)
'work work until you succeed'
#upper()
e="nikhita"
e.upper()
'NIKHITA'
f="NIKHITA"
f.lower()
'nikhita'
#lower
f="NIKHITA"
f.lower()
'nikhita'
g="python"
g[0].upper
<built-in method upper of str object at 0x00007FFB11E18BC8>
g[0].upper()
'P'
g.capitalize()
'Python'
#all letters capital we use capitalize
g.capitalize()
'Python'
#title all words first letter capital
h="my name is nikhita"
h.title()
'My Name Is Nikhita'
'My Name Is Nikhita'
'My Name Is Nikhita'
#true false checking
i="java"
i.isupper()
False
i.islower()
True
i.isdigit()
False
i.isalnum()
True
i.isalnum()
True
j="python course"
j.isdigit()
False
j.isalpha()
False
j.isalnum()
False
k="1234"
k.isdigit()
True
k.isalnum()
True
l="nikhita1234"
k.isdigit()
True
k.isalnum()
True
k.isalpha()
False
l="nikhita@1234"
l.isdigit()
False
l.isalmum()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    l.isalmum()
AttributeError: 'str' object has no attribute 'isalmum'. Did you mean: 'isalnum'?
l.isalnum()
False
m="hello python"
m.startswith("h")
True
m.endswith("n")
True
#strip()is used to remove the white space
#lstrip is used to remove left space
#rstrip() is used to remove right space
n="       nikhita       "
n.strip()
'nikhita'
o="   nikhita"
n.lstrip()
'nikhita       '
p="nikhita    "
p.rstrip()
'nikhita'
#split()
q="python java c c++)
SyntaxError: unterminated string literal (detected at line 1)
q="python java c c++"
q.split()
['python', 'java', 'c', 'c++']
r="i am in vijayawada"
r.split()
['i', 'am', 'in', 'vijayawada']
s="codegnan"
s.split()
['codegnan']
#join
t="my name is nikhita"
t.join()
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    t.join()
TypeError: str.join() takes exactly one argument (0 given)
u="vja hyd vzg"
"".join(u)
'vja hyd vzg'
v="vja","hyd","vzg"
"".join(v)
'vjahydvzg'
"k".join(v)
'vjakhydkvzg'
" ".join(v)
'vja hyd vzg'
#concatination
fname="nikhita"
lname="madasu"
print(fname+lname)
nikhitamadasu
print(fname+" "+lname)
nikhita madasu
print(fname.title()+" "+lname.title())
Nikhita Madasu
print((fname+lname).title())
Nikhitamadasu
print((fname+" "+lname).title())
Nikhita Madasu
#formatting
a=2
b=6
print(a+b)
8
print("the sum is",a+b)
the sum is 8
x="vja"
print("city is",vja)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    print("city is",vja)
NameError: name 'vja' is not defined
>>> print("city is",x)
city is vja
>>> #format method
>>> a="motu
SyntaxError: unterminated string literal (detected at line 1)
>>> a="motu"
>>> b="patlu"
>>> print(a+b)
motupatlu
>>> print("hello",a+b)
hello motupatlu
>>> print("hello {}{}".format(a,b))
hello motupatlu
>>> print("hello {} {}".format(a,b))
hello motu patlu
>>> print("hello {}+hello{}".format(a,b))
hello motu+hellopatlu
>>> print("hello {}  hello{}".format(a,b))
hello motu  hellopatlu
>>> print("hello {} hello {}".format(a,b))
hello motu hello patlu
>>> #fsting
>>> a="sita"
>>> b="ram"
>>> print(f"hello {a}{b}")
hello sitaram
>>> print(f"hello {a} {b}")
hello sita ram
>>> print(f"hello {a} hello {b}")
hello sita hello ram
>>> #format
>>> a=5
>>> b=p=8
>>> a=5
>>> b=6
>>> print(a*b)
30
>>> print("product is".format(a,b))
product is
>>> print("product is {}".format(a*b))
product is 30
>>> print(f"product is {a*b}")
product is 30
