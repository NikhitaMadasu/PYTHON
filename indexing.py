Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a="nikhita"
a[2]
'k'
a[5]
't'
>>> a[3]+a[4]+a[5]
'hit'
>>> b="my name is nikhita"
>>> b[3]
'n'
>>> b[7]
' '
>>> b[3]+b[4]+b[5]+b[6]
'name'
>>> b[0]+b[3]
'mn'
>>> b[2]+b[7]+b[10]
'   '
>>> c="i am learning python course"
>>> c[14]+c[15]+c[16]+c[17]+c[18]+c[19]
'python'
>>> c[5]+c[6]+c[7]+c[8]+c[9]
'learn'
>>> c[21]+c[22]+c[23]+c[24]+c[25]+c[26]
'course'
>>> d="time is very precious"
>>> d[13]+d[14]+d[15]+d[16]+d[17]+d[18]+d[19]+d[19]+d[20]
'preciouus'
>>> d[8]+d[9]+d[10]+d[11]
'very'
>>> d[0]+d[1]+d[2]+d[3]
'time'
>>> e="'simple is is better than complex"
>>> f="simple is better than comlex"
>>> n="simple is better than complex"
>>> n[-29]+n[-28]+n[-26]+n[-25]+n[-24]
'siple'
>>> n[-29]+n[-28]+n[-27]+n[-26]+n[-25]+n[-24]
'simple'
>>> n[-12]+n[-11]+n[-10]+n[-9]
'than'
>>> n[-19]+n[-18]+n[-17]+n[-16]+n[-15]+n[-14]
'better'
>>> n[-7]+n[-6]+n[-5]+n[-4]+n[-3]+n[-2]+n[-1]
'complex'
>>> s="i love python"
>>> s[-11]+s[-10]+s[-9]+s[-8]
'love'
>>> s[-6]+s[-5]+s[-4]+s[-3]+s[-2]+s[-1]
'python'
