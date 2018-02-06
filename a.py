#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#s1 = 72
#s2 = 85
#r = (s2 - s1) / s1 * 100
#print ('百分比: %.1f%%' % r)

#---59页练习-------
#L = [
#	['Apple','Google','Microsoft'],
#	['Java','Python','Ruby','Php'],
#	['Adam','Bart','Lisa']
#]
#打印 Apple
#print ('L[0][0] = ',L[0][0])
#打印 Python
#print (L[1][1])
#打印 Lisa
#print (L[2][2])
#a = input ('你的年龄是啥？')
#a = int(a)
#age = a
#if age >= 18:
#	print ('你的年龄是',age)
#	print ('老人')
#elif age >= 10:
#	print ('你的年龄是',age)
#	print ('年轻人')
#else:
#	print ('你的年龄是',age)
#	print ('婴儿')

# ----63页test----
#g = input ('你的身高：')
#g = float (g)
#z = input ('你的体重：')
#z = float (z)
#bmi = z/(g*g)
#if bmi < 18.5:
#	print ('过轻',bmi)
#elif bmi >= 18.5 and bmi < 25:
#	print ('正常')
#elif bmi >= 25 and bmi < 28:
#	print ('过重')
#elif bmi <= 28 and bmi < 32:
#	print ('肥胖')
#else:
#	print ('严重肥胖',bmi)
#-----------------------



#n = ['Michael','Bob','Tracy']
#for name in n:
#	print (name)
#-----数列累计---
#sum = 0
#for x in [1,2,3,4,5,6,7,8,9,10]:
#	sum = sum + x
#	print (sum)
#---------
#sum = 0
#for b in range(101):
#	sum = sum + b
#	print (sum)



#------while循环----
#sum = 0
#n = 99
#while n > 0:
#	sum = sum +n
#	n = n - 2
#	print (sum)

#----66页练习---
#L = ['Bart','Lisa','Adam']
#for b in L:
#	print ('Hello',b,'!:')

#names = ['Michael','Bob','Tracy']
#scores = [95,75,85]
#d = {'Michael':95,'Bob':75,'Tracy':85}
#print ('Michael\'s scores:',d['Michael'])
#d ['Kew'] = 95
#print (d)

#---函数---
#x = input ('请输入一个数字：')
#def my_abs (x):
#	if x >= 0:
#		pass
#		return x
#	else:
#		return -x

#print ('绝对值是：',x)


#import math
#def move (x,y,step,angle=0):
#	nx = x+step*math.cos(angle)
#	ny = y-step*math.sin(angle)
#	return nx,ny
#x, y = move(100, 100, 60, math.pi / 6)
#print (x,y)


#import math
#def enroll(name, gender):
#print('name:', name)
#def quadratic(a,b,c):
#    if not isinstance(a,(int,float)):
#        raise TypeError('a is not a number')
#    if not isinstance(b,(int,float)):
#        raise TypeError('b is not a number')
#    if not isinstance(c,(int,float)):
#        raise TypeError('c is not a number')
#    d=b*b-4*a*c #求根公式
#    if a==0:
#        if b==0:
#            if c==0:
#                return '方程根为全体实数'
#            else:
#                return '方程无根'
#        else:
#            x1=-c/b
#            x2=x1
#            return x1,x2
#    else:
#        if d<0:
#            return '方程无根'
#        else:
#            x1 = (-b + math.sqrt(d))/2/a 
#            x2 = (-b - math.sqrt(d))/2/a
#            return x1,x2        
#print(quadratic(0,0,0))
#print(quadratic(1,3,-4))

#q = input ('输入一个数字：')
#q = int (q)
#def kew (q):
#	if not isinstance(q,(int,float)):
#		raise TypeError("错的")
#	if q >= 15:
#		return q*q
#	else:
#		return q+q


#print ('运算后得出',kew(q))

#x = input ("数字:")
#x = int (x)
#n = input ('平方数:')
#n = int (x)
#def kew (x,n):
#	s = 1
#	while n > 0:
#		n = n - 1
#		s = s * x
#	return s
#print ("运算后得出:",kew(x,n))
#print (kew(5,3))
#print (kew(5))
#print (s)


#-----------87 page

#def kew (name,gender,age=15,city='shenzhen'):
#	print ('name:',name)
#	print ('gender:',gender)
#	print ('age:',age)
#	print ('city:',city)
#	print ('...\n')
#kew ('ben','F',18,'shenzhne')
#kew ("wen","W")
#kew ('cco','W','29','nanshan')
#kew ('wen','W')

#--------------89 page----------
#def add_end (l = [1,2]):
#	l.append ('add')
#	return l 
#	add_end ([1,2,3])
#print (add_end())
#print (add_end())
#print (add_end())
#print ('\n')

#def add_end1 (l = None):
#	if l is None:
#		l = []
#	l.append ('end')
#	return l
#print (add_end1())
#print (add_end1())
#print (add_end1())


#------91 page-----------
#def kew (shuzi):
#	sum = 0
#	for n in shuzi:
#		sum = sum + n * n
#	return sum 

#kew([1,2])
#print (kew([1,2,3]))
#print (kew([1,3,5,7]))
#print (kew([]))
#print ('......\n')

#def kew (*shuzi):
#	sum = 0
#	for n in shuzi:
#		sum = sum + n * n
#	return sum 
#shuzi = [1,2,5,7]
#shuzi = [1,2,3]
#print (kew(*shuzi))


#def kew (name,age,**ke):
#	print ('name:',name,'age:',age,'other:',ke)

#kew = input ("name:,age:,oth:")
#kew ('cfo',40,citu = '111',job = 'ert')
#ke = ['2']
#print ('name:',name,'age:',age,'other:',ke)
#print ('....\n')

#def kew1 (name,age,**ke):
#	if 'city' in ke:
#		pass
#	if 'job' in ke:
#	pass	
#	print ('name:',name,'age:',age,'other:',ke)

#b = {'city':'shenzhne','job':'ther'}
#n = input ("name:")
#a = input ('age:')
#c = input ('city:')
#j = input ('job:')
#kew1 (n,a,op = b['city'],oi = b['job'])
#kew1 (n,a,c,j)

#def kew1 (name,age,*,city = 'shenz',job = 'eng'):
#	if 'city' in ke:
#		pass
#	if 'job' in ke:
#	pass	
#	print (name,age,city,job)

#b = {'city':'shenzhne','job':'ther'}
#n = input ("name:")
#a = input ('age:')
#c = input ('city:')
#j = input ('job:')
#kew1 (n,a,op = b['city'],oi = b['job'])
#kew1 (n,a,c,j)
#print (kew1(n,a,))
#print (kew1(name,age,city,job))

#def kew (a,b,c = 0,*d,**e):
#	print ('a:',a,'b:',b,'c:',c,'d:',d,'e:',e)
#kew (1,2,3,'a = 22','ddd',llk= 233)
#kew (1,2,d=99,ext = None)
#a = input ('a is :')
#b = input ('b is :')
#c = input ('c is :')
#d = input ('d is :')
#e = input ('e is :')
#kew (a,b)
#d = (1,2,3,4,5,6)
#e = {'qq:':99,'xx:':'#'}
#kew(*d,**e)
#---------------98 page-------------

#n = input ('enter a number:')
#n = int ()
#def kew (n):
#	if n == 1:
#		return 1
#	return n * kew (n - 1)
#n = input ('enter a number:')
#n = int (n)
#print (kew (n))
#kew (1) 

#def kew (n):
#	return kew_one(n,1)
#def kew_one(num,product):
#	if num == 1:
#		return product
#	return kew_one(num - 1,num * product)
#n = input ('enter a num:')
#n = int (n)
#print (kew(n))


#--------------101 page-------
#Python利用递归函数移动汉诺塔:
# 汉诺塔思想笔记
# 认识汉诺塔的目标：把A柱子上的N个盘子移动到C柱子
# 递归的思想就是把这个目标分解成三个子目标
# 子目标1：将前n-1个盘子从a移动到b上
# 子目标2：将最底下的最后一个盘子从a移动到c上
# 子目标3：将b上的n-1个盘子移动到c上
# 然后每个子目标又是一次独立的汉诺塔游戏，也就可以继续分解目标直到N为1
#def move(n, a, b, c):
#    if n == 1:
#        print(a, '-->', c)
#    else:
#        move(n-1, a, c, b)# 子目标1
#        move(1, a, b, c)# 子目标2
#        move(n-1, b, a, c)# 子目标3
#n = input('enter the number:')
#n = int (n)
#move(n,'A','B','C')


#------------------
#有一个很通俗易懂的例子，把大象放到冰箱需要几步：
#第一步：打开冰箱门(把n-1个先放到B柱上)
#也就是move(n-1, a, c, b)
#第二步：把大象装进去(把最大的一个放到C柱上)
#也就是move(1, a, b, c)
#第三步：关上冰箱门(把n-1)个放到C柱上也就是move(n-1,b,a,c)
#你说的当n=3时
#move(2,a,c,b)这个会继续向下递归直到n-1 = 1()
#move(1,a,b,c)
#3move(2,b,a,c)同理这个会继续向下递归直到n-1 = 1#
#也就是move(n-1,a,c,b), move(n-1,b, a,c)会继续递归


#l = []
#n = input ('ent:')
#n = int (n)
#while n <= 99:
#	l.append (n)
#	n = n + 2
#n = input ('enter a number:')
#n = int (n)
#print (l)

#l = ['ben','wen','ooo','kkk','oiy','kas']
#print (l[2])
#print (l[0:3])
#print (l[2:3])
#print (l[4:5])
#print (l[-2:-1])
#print (l[-3:-1])

#b = list(range(100))
#print (b)
#n = input ('chu kaishi :')
#n = int (n)
#m = input ('chu jiewei :')
#m = int (m)
#print (b[n:m:2])
#print (b[::5])

#l = (0,1,2,3,4,5)[2:3]
#print ('l[2:3] =',l)
#a = ('ashdkjshakdhjkasd')[3:5]
#print (a)

#d = {'a':1,'b':2,'c':3}
#for key in d:
#	print (key)

#for values in d.values():
#	print (values)
#for i,value in enumerate ({'a','b','c'}):
#	print (i,value)
#print ('shuiji[(1,1),(2,4),(3,6)]:')
#for x, y in [(1,1),(2,4),(3,6)]:
#	print (x,y)


#l = list (range(1,11))#生成 list  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print (l)

#o = []
#for x in range (1,11):#生成 [1x1, 2x2, 3x3, ..., 10x10] 
#	o.append (x * x)
#print (o)

#a = [x / x for x in range (1,11)]#生成 [1/1, 2/2, 3/3, ..., 10/10] 
#print (a)

#q = [x*x for x in range(1,11) if x %2 == 0]
#print (q)

#w = [m + n for m in '1234' for n in '5678']#使用两层循环，可以生成全排列
#print (w)

#d = {'ben':'23','wemn':'18','wene':'30'}#for 循环其实可以同时使用两个甚至多个变量，比如 dict 的 items() 可以同时迭代 key 和 value：
#for k , v in d.items ():
#	print (k , '年龄:' , v)

#s = [k + '=' + v for k , v in d.items ()]#for 循环其实可以同时使用两个甚至多个变量，比如 dict 的 items() 可以同时迭代 key 和 value：
#print (s)

#l = ['Hello','Worls','Ibm','HJJKK']#把一个 list 中所有的字符串变成小写
#a = [s.lower () for s in l]
#print (a)


#l = ['Hello','Worls',18,'Ibm',5555555,'333333','HJJKK',None]#---------------110page test-------------------
#a = [s.lower () for s in l if isinstance (s,str)]
#print (a)


#l = [x * x for x in range (10)]
#print (l)
#g = (x * x for x in range (10))
#for n in g:
#	print (n)

#-----------------斐波拉契数列------------------------------
#v = input ('enter a number:')
#v = int(v)
#def kew (v):
#	n,a,b = 0,0,1
#	while n <v:
#		yield b
#		a,b = b,a+b
#		n = n +1
#	return 'done'

#print(kew(v))

#print (next(kew(v)))
#def kew ():
#	print ('step one ')
#	yield 1
#	print ('step two ')
#	yield (3)
#	print ('step three ')
#	yield (5)
#n = input ('ssss')
#n = int (n)
#o = kew()
#for n in o:
#	print (n)


#g = kew (6)
#while True:
#	try:
#		x = next(g)
#		print ('g:',x)
#	except StopIteration as e:
#		print ('Generation return value:',e.value)
#		break



#-----------------------118 page 没有做练习--------------
#a = abs 
#f = a (-122)
#x = -5
#y = 6
#print (f)
#def kew (x,y,a):
#	return a(x) + a(y)

#print (kew(x,y,a))
#def f(x):
#	return x*x
#a = f
#l = []
#for n in [1,2,3,4,5,6,7,8,9]:
#	l.append (a(n))
#print (l)

#r = map (a,[1,2,3,4,5,6,7,8,9])
#print (list(r))

#from functools import reduce
#def kew(x,y):
#	return x * 10 +y
#b = reduce (kew,[1,2,3,4])
#print (b)

#def wen (z,s):
#	return z * 10 + s
#c = reduce (wen,[1,2,3,4])
#print (c) 

#def kew1(s):
#	return {'0':0,'1':1,'2':2,'3':3,'5':5,'7':7,'9':9}[s]

#k = reduce (kew,map(kew1,'12579'))
#print (k)

#--------------130 test -------------------
#利用 map() 函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
#输入： ['adam', 'LISA', 'barT'] ，输出： ['Adam','Lisa', 'Bart'] 
#n = input ('enter name1 :')
#m = input ('enter name2 :')
#b = input ('enter name3 :')
#x = [n,m,b]

#L = []
#for n in list(map(str.lower,x)):
#    L.append(n[:1].upper()+n[1:].lower())#没看懂
#print(L)

#def kew (n):
#	return n % 2 == 1
#l = list (filter(kew,[1,2,3,4,5,6,9,10,15]))#在一个 list 中，删掉偶数，只保留奇数，
#print (l)


#---------134 page ----------------------
#def is_palindrome(n):
#    nn=int(str(n)[::-1])
#    return n==nn
#output = filter(is_palindrome, range(1, 1000))
#print('1~1000:', list(output))
#if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#    print('测试成功!')
#else:
#    print('测试失败!')

#l = sorted([36,5,-12,9,-21])
#print (l)

#l = [('Bob', 75), ('Adam', 92), ('Zart', 66), ('Lisa', 88)]
#def shunxu (t):
#	return t [0]

#l1 = sorted (l,key = shunxu)
#print (l1)	

#print(sorted(l,key=lambda x:x[0].lower()))
#print(sorted(l,key=lambda x:x[1],reverse=True))

#def calc_sum(*args):
#	ax = 0
#	for n in args:
#		ax = ax + n
#		return ax

#f = calc_sum
#print (f)

#def lazy_sum(*args):
#	def sum():
#		ax = 0
#		for n in args:
#			ax = ax + n
#		return ax
#	return sum
#g = lazy_sum(1,3,5,7,9)
#print (g)
#pritn (g())

#def count():
#	fs = []
#	for i in range(1, 4):
#		def f():
#			return i*i
#		fs.append(f)
#	return fs
#f1, f2, f3 = count()

#print (f1)
#def now():
#	print ('2018-2-6')

#f = now
#print (f)

#print(now.__name__)
#print (f.__name__)

#def kew (f):
#	def wen (*args,**kw):
#		print ('call %s():'% f.__name__)
#		return f (*args,**kw)
#	return wen

#@log
def int2(x,base=2):
	return int(x,base)
a = int2

print (a('1000000'))


import functools
int3= functools.partial (int,base =2 )#把一个函数的某些参数给固定住（也就是设置默认值）
c = int3
print (c('1010101'))
print (c('1000000',base = 10))

#-----------------------------------------------

' a test module '#任何模块代码的第一个字符串都被视为模块的文档注释
__author__ = 'Kew Qiran'#使用 __author__ 变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名

#以上就是 Python 模块的标准文件模板，当然也可以全部删掉不写，但是，按标准办事肯定没错。
import sys

def test():
	args = sys.argv
	if len(args)==1:
		print('Hello, world!')
	elif len(args)==2:
		print('Hello, %s!' % args[1])
	else:
		print('Too many arguments!')
if __name__=='__main__':
	test()


def _private_1(name):
	return 'Hello, %s' % name
def _private_2(name):
	return 'Hi, %s' % name
def greeting(name):
	if len(name) > 3:
		return _private_1(name)
	else:
		return _private_2(name)



from PIL import Image#有了 Pillow，处理图片易如反掌。随便找个图片生成缩略图：
im = Image.open ('E:\kew\dock\mac-os-x-yosemite-pack\Spark Alt.png')
print (im.format,im.size,im.mode)

im.thumbnail ((200,100))
im.save ('a1aa.png','PNG')

#--------------------------------------------------------------
std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

print('bart.name =', bart.name)
print('bart.score =', bart.score)
bart.print_score()

print('grade of Bart:', bart.get_grade())
print('grade of Lisa:', lisa.get_grade())

#-------------------------------------
print('\n')
std3 = { 'name': 'kew', 'score': 98 }
std4 = { 'name': 'wen', 'score': 81 }

class Fuqi(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def qqq(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

k = Fuqi('邱', 59)
w = Fuqi('文', 87)

print('k de name =', k.name)
print('k de score =', k.score)
k.qqq()
w.qqq()

print('kew 枫树:', k.get_grade())
print('wen 枫树:', w.get_grade())

#-----------------------------------------------------

class Animal(object):
	"""docstring for Animal"""
	def run(self):
		print ('Animal is run...')
class Dog(Animal):
	def run (self):
		print ('Dog is run...')

dog = Dog ()
dog.run()

animal = Animal()
animal.run()

a = list()
b = Animal()
c = Dog()

print ('a is a list?',isinstance (a, list))
print ('b is animal?',isinstance (b, Animal))
print ('c is a dog?',isinstance (c, Dog))
print ('c is animal?',isinstance (c, Animal))
print ('b is dog?',isinstance(b, Dog))

#---------------
def run_twice (animal):
	animal.run()
	animal.run()

print (run_twice(Animal()))
print (run_twice(Dog()))

class Tortoise(Animal):
	def run(self):
		print ('Tortoise is run...slowly')

print (run_twice(Tortoise()))

class Kewkk(Animal):
	def run (self):
		print ('Kewkk is conming...')

print (run_twice(Kewkk()))

		
print ('123\'s type is :',type (123))
print ('kew\'s type is :',type ('kew'))
print ('None\'s type is :',type (None))
print (type (123) == type (456))

print ('dog is in animal ?',isinstance (c, Animal))
print ('\n')
print (dir('ABC'))
print ('len\'ABC\' is :',len('ABC'))
print ('len\'ABC\' is :','ABC'.__len__())
print ('ABNJJJJ de 小写字符串：','ABNJJJJ'.lower())

class MyObject (object):
	def __init__(self):
		self.x = 9
	def power (self):
		return self.x * self.x

obj = MyObject()

print ('have x ?',hasattr (obj,'x'))
print ('MyObject x num is :',obj.x)
setattr (obj,'y',19)
print ('have y ?',hasattr (obj,'y'))
print ('MyObject y num is :',obj.y)
print ('MyObject y num is :',getattr (obj,'y'))

def ppp (MyObject):
	if hasattr (obj,'x'):
		return 300
	return 100
#etattr (ppp,'x',12)
p = ppp(MyObject)
print (p)

#*----------------184page-------------
#std1 = { 'name': 'Michael', 'score': 98 }
#std2 = { 'name': 'Bob', 'score': 81 }

class Student(object):
	def __init__(self, name):
		self.name = name

s = Student('Bob')
s.score = 90
i = Student ('Michael')
i.score = 60


print (s,'\'s score is :',s.score)
print (s.name,'\'s score is',s.score)
print (i.name,i.score)
#del s.name
print (i.name)

		
