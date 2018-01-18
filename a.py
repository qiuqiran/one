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


#------------

def kew (name,gender,age=15,city='shenzhen'):
	print ('name:',name)
	print ('gender:',gender)
	print ('age:',age)
	print ('city:',city)
kew ('ben','F',18,'shenzhne')
kew ("wen","W")
#kew ('wen','W')
