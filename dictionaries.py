Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict{}
a={"name":"nikhita","city","vijayawada"}
SyntaxError: ':' expected after dictionary key
a={"name":"nikhita","city":"vijayawada"}
print(a)
{'name': 'nikhita', 'city': 'vijayawada'}
type(a)
<class 'dict'>
b={5,6,7,8,9,"name"}
type(b)
<class 'set'>
print(b)
{'name', 5, 6, 7, 8, 9}
a={"name":"nikhita","city":"vijayawada","emailid":"sainikhitamadasu"}
print(a)
{'name': 'nikhita', 'city': 'vijayawada', 'emailid': 'sainikhitamadasu'}
type(a)
<class 'dict'>
a.keys()
dict_keys(['name', 'city', 'emailid'])
a.values()
dict_values(['nikhita', 'vijayawada', 'sainikhitamadasu'])
a.items()
dict_items([('name', 'nikhita'), ('city', 'vijayawada'), ('emailid', 'sainikhitamadasu')])
a={"course":"python","institute":"codegnan"}
print(a)
{'course': 'python', 'institute': 'codegnan'}
a.update({"year":"2026"})
a
{'course': 'python', 'institute': 'codegnan', 'year': '2026'}
a.update({"name":"nikhita"},{"month":"july"})
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.update({"name":"nikhita"},{"month":"july"})
TypeError: update expected at most 1 argument, got 2
a.update({"name":"nikhita","month":"july"})
a
{'course': 'python', 'institute': 'codegnan', 'year': '2026', 'name': 'nikhita', 'month': 'july'}
#setdefault
a={"year":2026,"month":"july"}
a.setdefault("date":2)
SyntaxError: invalid syntax
a.setdefault("date",2)
2
a
{'year': 2026, 'month': 'july', 'date': 2}
#pop
a={"time":12,"hour":1,"minute":3}
a.pop()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("time")
12
a
{'hour': 1, 'minute': 3}
#pop is used to delete one perticular item
#popitem() is used to delete last item
a.popitem()
('minute', 3)
a
{'hour': 1}
#get() means read
a={"college":"klu","branch":'cse"}
   
SyntaxError: unterminated string literal (detected at line 1)
a={"college":"klu","branch":"cse"}
   
a.get("college")
   
'klu'
a["branch']
  
SyntaxError: unterminated string literal (detected at line 1)
a["branch"]
  
'cse'
a.get("cse")
  

#copy()
  
KeyboardInterrupt
KeyboardInterrupt

a={"hour":12,"min":3,"sec":60}
  
a.copy()
  
{'hour': 12, 'min': 3, 'sec': 60}


a
  
{'hour': 12, 'min': 3, 'sec': 60}
>>> a.clear()
...   
>>> a
...   
{}
>>> b={}
...   
>>> b.update({"name":"nikhita"})
...   
>>> b
...   
{'name': 'nikhita'}
>>> KeyboardInterrupt
>>> KeyboardInterrupt
>>> 
>>> 
>>> #dictionary not allow duplicates
...   
>>> #keys are differebnt it will execute
...   
>>> a={"name":"nikhita","course":"python","year":2026}
...   
>>> len(a)
...   
3
>>> a.count("name")
...   
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a.count("name")
AttributeError: 'dict' object has no attribute 'count'
>>> a={"name":"nikhita","city":"vijayawada","name":"nikhita"}
...   
>>> print(a)
...   
{'name': 'nikhita', 'city': 'vijayawada'}
>>> a={"name":"nikhita","city":"vijayawada","name":"tulasi"}
...   
>>> print(a)
...   
{'name': 'tulasi', 'city': 'vijayawada'}
>>> a={"name1":"nikhita","city":"vijayawada","name2":"nikhita"}
...   
>>> print(a)
...   
{'name1': 'nikhita', 'city': 'vijayawada', 'name2': 'nikhita'}
