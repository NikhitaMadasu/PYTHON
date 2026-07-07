Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#single key number of values
a={"idnos":[10,20,30],"names":["nikhita","tulasi","geethu"],"marks":[60,70,80]}
print(a)
{'idnos': [10, 20, 30], 'names': ['nikhita', 'tulasi', 'geethu'], 'marks': [60, 70, 80]}
type(a)
<class 'dict'>
a.keys()
dict_keys(['idnos', 'names', 'marks'])
>>> a.values()
dict_values([[10, 20, 30], ['nikhita', 'tulasi', 'geethu'], [60, 70, 80]])
>>> a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['nikhita', 'tulasi', 'geethu']), ('marks', [60, 70, 80])])
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> b=a[-5:]
>>> a
[9, 1, 5, 2, 8, 4, 6, 3, 7, 0]
>>> b
[4, 6, 3, 7, 0]
>>> a1=a[0:5]
>>> a1
[9, 1, 5, 2, 8]
>>> a2=a[5:10]
>>> a2
[4, 6, 3, 7, 0]
>>> a1.sort()
>>> a1
[1, 2, 5, 8, 9]
>>> a2.sort()
>>> a2
[0, 3, 4, 6, 7]
>>> a1.reverse()
>>> a1
[9, 8, 5, 2, 1]
>>> a2.reverse()
>>> a2
[7, 6, 4, 3, 0]
>>> a.merge(a1,a2)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.merge(a1,a2)
AttributeError: 'list' object has no attribute 'merge'
>>> a=a1+a2
>>> print(a)
[9, 8, 5, 2, 1, 7, 6, 4, 3, 0]
>>> b=a1+a2
>>> print(b)
[9, 8, 5, 2, 1, 7, 6, 4, 3, 0]
>>> c=a1+a2
>>> print(c)
[9, 8, 5, 2, 1, 7, 6, 4, 3, 0]
>>> c=a2+a1
>>> print(c)
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
