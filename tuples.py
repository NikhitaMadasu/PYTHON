Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#tuple
a=(4,5.6,"code",5+9J,True,False)
print(a)
(4, 5.6, 'code', (5+9j), True, False)
type(a)
<class 'tuple'>
a.count(5+9j)
1
a.index(True)
4
len(a)
6
#sets
#doesnt allow duplicate values,it is semi mutable,set is an unordered collection,represented with{}
a={3,2,1,6,5,7,8,9}
print(a)
{1, 2, 3, 5, 6, 7, 8, 9}
type(a)
<class 'set'>
b={5,8.9,"nikki",5+9j,True,False}
print(b)
{False, True, (5+9j), 5, 8.9, 'nikki'}
type(b)
<class 'set'>
#subset
a={3,4,5,6,7,8,9}
b=[5,6,7,8}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
b={5,6,7,8}
b.issubset(a)
True
a.issubset(b)
False
#superset
a={3,4,5,6,7,8,9}
b={5,6,7,8}
a.issuperset(b)
True
b.issuperset(a)
False
#union
a={3,4,5,6,7,8,9}
b={5,6,7,8}
a.union(b)
{3, 4, 5, 6, 7, 8, 9}
c={1,2,3,4,5,6,7,8,9}
print(c)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
d={1,2,3,5,5,6,6}
print(c)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
print(d)
{1, 2, 3, 5, 6}
#intersection
#print common values
a={3,4,5,6,7,8,9}
b={6,7,8,9,10,11}
a.intersection(b)
{8, 9, 6, 7}
#update
a={10,20,30,40,50}
b={40,50,60,70,80}
a
{50, 20, 40, 10, 30}
a.update(b)
a
{70, 40, 10, 80, 50, 20, 60, 30}
b
{80, 50, 70, 40, 60}
b.update(a)
b
{70, 40, 10, 80, 50, 20, 60, 30}
#difference
a={4,5,6,7,8,9,10,11}
b={3,4,5,6,7,11,12,13}
a.differnce(b)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a.differnce(b)
AttributeError: 'set' object has no attribute 'differnce'. Did you mean: 'difference'?
a.difference(b)
{8, 9, 10}
b.difference(a)
{3, 12, 13}
#symmetric difference
a={3,4,5,6,7,8,9}
b={1,3,5,7,8,11,13}
a.symmetric_difference(b)
{1, 4, 6, 9, 11, 13}
b.symmetric_difference(a)
{1, 4, 6, 9, 11, 13}
#difference update
a={1,3,5,7,9,11,13}
b={2,3,4,6,7,9,11,12}
a.intersection_update(b)
a
{11, 9, 3, 7}
b
{2, 3, 4, 6, 7, 9, 11, 12}
b.intersection_update(a)
b
{3, 9, 11, 7}
#this is intersection update
#differece update
a={2,3,4,5,6,7}
b={9,8,7,5,6,4,2}
a.difference_update(b)
a
{3}
b
{2, 4, 5, 6, 7, 8, 9}
b.difference_update(a)
b
{2, 4, 5, 6, 7, 8, 9}
#symmetric difference update
a={11,12,13,14,15,16,17}
b={13,14,15,16,17,18}
a.symmetric_difference_update(b)
a
{18, 11, 12}
b
{16, 17, 18, 13, 14, 15}
b.symmetric_difference_update(a)
b
{16, 17, 11, 12, 13, 14, 15}
#pop
a={4,5,6,7,8,9,10}
a.pop()
4
a
{5, 6, 7, 8, 9, 10}
a.remove(5)
a
{6, 7, 8, 9, 10}
a.discard(7)
a
{6, 8, 9, 10}
>>> a.copy()
{8, 9, 10, 6}
>>> b={5,6}
>>> a.copy(b)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    a.copy(b)
TypeError: set.copy() takes no arguments (1 given)
>>> b.copy(a)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    b.copy(a)
TypeError: set.copy() takes no arguments (1 given)
>>> a
{6, 8, 9, 10}
>>> a.copy()
{8, 9, 10, 6}
>>> a.clear()
>>> a
set()
>>> b=set()
>>> b.add(20)
>>> b
{20}
>>> #set doesnot have count which  there is no repeated,there is no atribute index because there is no order
>>> a={3,4,5,6,7}
>>> len(a)
5
>>> a.cout(5)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    a.cout(5)
AttributeError: 'set' object has no attribute 'cout'
>>> a.index(4)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    a.index(4)
AttributeError: 'set' object has no attribute 'index'
>>> #isdisjoint
>>> a={3,4,5,6,7}
>>> b={5,6,7,9,2}
>>> a.isdisjoint(b)
False
>>> b.isdisjoint(a)
False
