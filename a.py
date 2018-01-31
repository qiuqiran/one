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


import math
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

d = {'a':1,'b':2,'c':3}
for key in d:
	print (key)

for values in d.values():
	print (values)
for i,value in enumerate ({'a','b','c'}):
	print (i,value)
print ('shuiji[(1,1),(2,4),(3,6)]:')
for x, y in [(1,1),(2,4),(3,6)]:
	print (x,y)