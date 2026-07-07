Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a="work until you succeed"
>>> a[4:10]
' until'
>>> a[11:14]
'you'
>>> a[0:4]
'work'
>>> a[14:23]
' succeed'
>>> b="codegnan it solutions"
>>> b[9:11]
'it'
>>> b[12:21]
'solutions'
>>> b[0:7]
'codegna'
>>> b[0:8]
'codegnan'
>>> #slicing
>>> c="codegnan"
>>> c[0:3]
'cod'
>>> c[0:4]
'code'
>>> c[4:8]
'gnan'
>>> #negative slicing
>>> d="vijayawada is a royal city"
>>> d[-10:-6]
'roya'
>>> d[-10:-5]
'royal'
>>> d[-16:-26]
''
>>> d[-26:-16]
'vijayawada'
>>> d[-4:0]
''
>>> d[-4:-1]
'cit'
>>> d[-4:]
'city'
>>> e="vizag is city of Destiny"
>>> e[-15:-11]
'city'
[-24:-19]
SyntaxError: invalid syntax
e[-24:-19]
'vizag'
e[-7:]
'Destiny'
