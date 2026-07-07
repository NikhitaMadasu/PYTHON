Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[2,5.6,"python",6+9j,True,False]
print(a)
[2, 5.6, 'python', (6+9j), True, False]
type(a)
<class 'list'>
b=5
type(b)
<class 'int'>
c=[5]
type(c)
<class 'list'>
#append
a=["python","java","c","c++"]
a.append("DSA")
a
['python', 'java', 'c', 'c++', 'DSA']
a.append("ml","ai")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ml","ai"])
a
['python', 'java', 'c', 'c++', 'DSA', ['ml', 'ai']]
#extend
a=["ml","ai","dsa"]
a.extend(["c","c++","python"])
a
['ml', 'ai', 'dsa', 'c', 'c++', 'python']
#insert
b=["vja","hyd"]
b.insert(1,"vzg")
b
['vja', 'vzg', 'hyd']
#index
a=["black","blue","pink","white"]
a.index("white")
3
#copy
a.copy()
['black', 'blue', 'pink', 'white']
b=a.copy()
b
['black', 'blue', 'pink', 'white']
#count
b.count("pink")
1
b.count("white")
1
#sort
a=["grapes","apple","orange","mango","banana"]
a.sort()
a
['apple', 'banana', 'grapes', 'mango', 'orange']
b=[8,5,7,6,9,2,1,0]
b.sort()
b
[0, 1, 2, 5, 6, 7, 8, 9]
#reverse
a=[7,8,6,5,4,9,5,2,]
a.reverse()
a
[2, 5, 9, 4, 5, 6, 8, 7]
b=["nikhita","tulasi","geethika","pooja","happi"]
b.reverse()
b
['happi', 'pooja', 'geethika', 'tulasi', 'nikhita']
b.remove()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    b.remove()
TypeError: list.remove() takes exactly one argument (0 given)
b.remove(3)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    b.remove(3)
ValueError: list.remove(x): x not in list
b.remove("nikhita")
b
['happi', 'pooja', 'geethika', 'tulasi']
#pop()
#either empty list or index
a=["ml","ai","c++"]
a.pop()
'c++'
a.pop(2)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a.pop(2)
IndexError: pop index out of range
a.pop(1)
'ai'
#remove
a.remove("c++")
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a.remove("c++")
ValueError: list.remove(x): x not in list
a.remove("ml")
a
[]
a.remove("ai")
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a.remove("ai")
ValueError: list.remove(x): x not in list
>>> b=["nikki","tulasi","geethika","pooj","happi"]
>>> b.pop()
'happi'
>>> b.pop(3)
'pooj'
>>> b.remove("pooj")
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    b.remove("pooj")
ValueError: list.remove(x): x not in list
>>> b.remove("nikki")
>>> b
['tulasi', 'geethika']
>>> a["pooja","nikki","tulasi","geethu"]
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a["pooja","nikki","tulasi","geethu"]
TypeError: list indices must be integers or slices, not tuple
>>> a=["pooja","nikki","tulasi","geethu"]
>>> len(a)
4
>>> b="pooja"
>>> len(b)
5
>>> c="nikki"
>>> len(c)
5
>>> a.clear()
>>> a
[]
>>> b={}
>>> b.append("hi")
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    b.append("hi")
AttributeError: 'dict' object has no attribute 'append'
>>> b.append()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    b.append()
AttributeError: 'dict' object has no attribute 'append'
>>> b=[]
>>> b.append("hi")
>>> b
['hi']
