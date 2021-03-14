#coding:UTF-8
#
#while else 循环
# num=0
# while num < 3:
# 	print(f'num < 3')
# 	num += 1
# else:
# 	print(f'num > 3')
# print('循环结束')

#for  -- else 循环
# names = ['xiaoming','xiaoshi']
# for name in names:
# 	if name == 'xiao':
# 		print(f'名称{name}')
# 		break
# 	print(f'循环列表数据:{name}')
# else:
# 	print("循环没数据了")
# print("结束循环")
# 
# pass 占位符
# name='xiaozzhi'
# if name == 'xiaozzhi':
# 	print('hello')
# elif name == 'li':
# 	pass   #
# else:
# 	print('nothing')

##game
# import random  导入random包

# rand_num = random.randint(1,100)   生成随机数
# guess=0
# while True:
# 	num_input=input("请输入一个数字:")
# 	guess+=1
# 	if not num_input.isdigit():
# 		print("输入有误，请重新输入")
# 	elif int(num_input)<0 or int(num_input) > 100:
# 		print('请输入1-100之间的数字')
# 	else:
# 		if int(num_input)>rand_num:
# 			print('数据过大')
# 		elif int(num_input)<rand_num:
# 			print("数据过小")
# 		else:
# 			print('恭喜您，猜对了')
# 			print(f'随机数为 {rand_num}')
# 			break
## 头部加 #!/usr/bin/env python3
#
#
#
###函数
# def hello():
# 	print("hello")
# hello()  #调用函数

# def get_student_info(name,age):  #带参数的函数
# 	print(f'name:{name},age={age}')
# get_student_info('tom',20)


# def get_message(name,age=20):    #age默认值为20，当age不给定值是，则为20
# 	print(f'name={name},age={age}')
# get_message('jerry')

# #参数可变函数
# def get_more_args(name,*args):
# 	print(f'{name}')
# 	print(f'{args}')    #返回元组数据
# 	for val in args:
# 		print(f'遍历数据:{val}')
# get_more_args('boy','girl',34)

# #参数可变二
# others={'city':'xian','home':'xichgn'}
# def per_info(name,**kw):   #**kw 接收键值对形式的参数
# 	print(f'name:{name},other:{kw}')
# per_info('tom',city=others['city'],home=others['home'])
# per_info('tom',city='kk',home='ff')

#全局变量
# num = 200   #全局变量
# def global_exercise():
# 	num = 10  #局部变量
# 	print(f'{num}')
# global_exercise()

# def global_exercise_second():
# 	#如果要使用全局变量，则在变量前加global关键字
# 	global num
# 	print(f'{num}')
# global_exercise_second()
# 
#函数返回函数示例
# def get_sum(*args):
# 	def get_sum():
# 		sum=0
# 		for n in args:
# 			sum=sum+n
# 		return sum
# 	return get_sum
# print(f'函数调用{get_sum(1,2,3)}')
# result=get_sum(1,2,3)
# print(f'{result()}')



#闭包
# def func_close():
# 	fs=[]
# 	for i in range(1,4):
# 		def f():
# 			return i*i
# 		fs.append(f)
# 	return fs
# f1,f2,f3 = func_close()
# print(f1(),f2(),f3())



#闭包正确
# def func_close():
# 	def f(j):
# 		def g():
# 			return j*j
# 		return g
# 	fs=[]
# 	for  i in range(1,4):
# 		fs.append(f(i))   #f(i) 立即执行
# 	return fs

# f1,f2,f3=func_close()

# print(f1())
# print(f2())
# print(f3())



#类

# class  Person(object):
# 	#构造方法
# 	def __init__(self,name,score):
# 		self.name=name
# 		self.__score=score  #变量添加__代表私有属性
# 		print(f'我是带参数的构造方法{name}')

# 	def show(self):
# 		print(f'调用show方法{self.name}')
# 	def getScore(self):
# 		print(f'{self.__score}')
# 		#读取私有属性
# 	def get_score(self):
# 		return self.__score

# 	def set_score(self,score):
# 		if 0<score <100:
# 			self.__score=score
# 		else:
# 			print("输入参数有误")
#     #私有方法不能在类外部调用
# 	def __info(self):
# 		print("我是私有方法")


# person = Person("zhangsan",10)  #声明类
# person.show()   #调用方法
# person.getScore()
# print(f'分数为{person.get_score()}')
# person.set_score(20)
# print(f'修改后分数为{person.get_score()}')
# person.set_score(-20)


# #继承
# class Animal(object):
# 	def __init__(self):
# 		print("我是animal类")
# 	def run(self):
# 		print("Animal is running...")

# class Dog(Animal):
# 	pass
# class Pig(Animal):
# 	pass

# dog = Dog()
# dog.run()   #子类执行继承来自父类的方法
# #子类不能继承父类的私有成员及方法


# #多态
# class Car(object):
# 	def run(self):
# 		print("Car is running...")

# class littleCar(Car):
# 	def run(self):
# 		print("littleCar is running...")
# little = littleCar();
# little.run()
# #isinstance 判断是否是同一种类型
# print(f'判断little是否是littleCar的示例{isinstance(little,littleCar)}')


# def run_animal(animal):
# 	animal.run()
# run_animal(Animal())


# #8.6封装

# class Person(object):
# 	pass
# class Runnle(object):
# 	pass
# #该类表示多继承
# class Student(Person,Runnle):
# 	pass

# #使用type方法获取类型
# print(f'获取变量类型{type(Student)}')




# def fn():
# 	print("this is a test function")
# import types   #引入types模块
# #判断fn的类型
# print(type(fn)==types.FunctionType) #通过常量去判断


# dir('abc')  #获取对象属性和方法




# #类的特有方法
# class Lawyer():
# 	def __init__(self,name):
# 		self.name = name
# 		print("__init__ methods")
# 	#重写__str__方法
# 	def __str__(self):
# 		return f'student name {self.name}'
# 	#当调用的属性不存在是则会调用该方法
# 	def __getattr__(self,attr):
# 		if attr == 'score':
# 			return 98
# 	def __call__(self):
# 		print(self.name)
# law = Lawyer('zhangsan')
# print(law)
# print(law.score)

# law()  #添加__call__可以用这个调用



# #异常
# #python 异常处理实例
# def exp_exception(x,y):
# 	try:
# 		a=x/y
# 		print('a=',a)
# 		return a
# 	except Exception:
# 		print("程序出现异常")
# exp_exception(2,0)

# #抛出异常
# def exp_exception_second():
# 	try:
# 		raise NameError("name is error")
# 	except NameError:
# 		print("抛出自定义异常")
# 		#raise  抛出异常
# 	#except err:   指定多个异常
# 		pass
# exp_exception_second()

# #在意个块中抛出多个异常
# def exp_exception_third(x,y):
# 	try:
# 		a=x/y
# 		b=name
# 	except (ZeroDivisionError,NameError,TypeError):
# 		print("one of error is happen")
# exp_exception_third(10,0)

# #抛出真正的异常信息

# def exp_exception_four(x,y):
# 	try:
# 		b=name
# 		a=x/y
# 	except (ZeroDivisionError,NameError,TypeError) as e:  #添加as e
# 		print(e)
# exp_exception_four(10,0) 

# #抛出所有异常信息
# def exp_exception_five(x,y):
# 	try:
# 		a=x/y
# 	except Exception as e:
# 		print(e)
# exp_exception_five(20,0)


# #使用else告知程序未发生异常
# def exp_exception_six(x,y):
# 	try:
# 		a=x/y
# 	except Exception as e:
# 		print(e)
# 	else:
# 		print("程序执行完成，未出现错误信息")

# exp_exception_six(10,2)


# #实现自定义异常
# class MyError(Exception):
# 	def __init__(self):
# 		pass

# 	def __str__(self):
# 		return ("thi is my personal error")
# def my_error_test():
# 	try:
# 		raise MyError()
# 	except MyError as e:
# 		print(e)

# my_error_test()

# #finally  
# def my_exception(x,y):
# 	try:
# 		a = x/y
# 	except Exception as e:
# 		print(e)
# 		#不困怎么样都会执行该语句
# 	finally:
# 		print("over")
# my_exception(10,0)



# #时间和日期
# import time
# print(f"当前时间戳{time.time()}")
# print(f'time.localtime():{time.localtime()}')
# print(f'time.gmtime:{time.gmtime()}')
# t=time.localtime()
# print(f'time.asctiome():{time.asctime(t)}')  #返回字符串
# #将时间戳转为time.asctime()
# print(f'time.ctime():{time.ctime()}')
# #进程休眠时间  time.sleep(seconds)
# print(time.ctime())
# #time.sleep(2)
# print(time.ctime())

# #time.clock() 返回当前cpu的执行时间  ,3.7无此属性
# def get_time():
# 	time.sleep(2)
# #t1=time.clock()
# #get_time()
# #print(f'cost {(time.clock()-t1)}')
# t1=time.time()
# #get_time()
# print(f'cost {(time.time()-t1)}')

# #格式化日期输出
# now= (2018,3,11,16,50,39,5,48,0)
# now_n = time.mktime(now)
# print(time.strftime('%Y %H:%M:%S',time.gmtime(now_n)))

# #time.strptime() 将时间字符解析为时间元组
# strct_time=time.strptime("11 Mar 18","%d %b %y")
# print(strct_time)
'''
格式之间的转换
format -> struct_time  =strptime
struct_time -> format = strftime
struct_time -> timestamp = mktime
timestamp -> struct_time = localtime | gmtime

#datetime 模块
'''
# import datetime
# print("获取当前时间",datetime.datetime.today())
# print(f"当前时间是{datetime.datetime.now()}")
# print(f'获取utc时间{datetime.datetime.utcnow()}')
# #创建一个datetime对象
# print(f'{datetime.datetime.fromtimestamp(time.time())}')
# print(f'{datetime.datetime.utcfromtimestamp(time.time())}')
# print('将格式字符串转为datetime对象')
# dt=datetime.datetime.now()
# print(f'{dt.strptime(str(dt),"%Y-%m-%d %H:%M:%S.%f")}')
# print(f'{dt.strftime("%Y-%m-%d %H:%M:%S")}')


#日历模块
# import calendar as c
# print("============================calendar")
# #print(c.calendar(2021,w=2,l=1,c=6))
# #3个月一行 间隔距离为c 每日宽度间隔为 w l是每星期的行数
# print(c.firstweekday())  #0代表星期1
# print(c.isleap(2021)) #如果是true则是闰年 否则是false
# print(c.leapdays(2021,2023))  #返回两个年之间的闰年总数
# print(c.month(2021,6,w=2,l=1))
# print(c.monthcalendar(2021,6))
# print(c.monthrange(2021,6))


#正则表达式
'''
\d  [0-9]
\D  f非数字字符
\s  任意空白字符
\S  非空白字符
\w  包括下划线的任意字符
\W  任意非单词字符
'''

#正则表示模块  re
# import re
# print(re.match('hello','hello world').span())  #在起始位置匹配
# print(re.match('world','hello world'))  #不在起始位置匹配

# print(re.search('hello','hello world').span())
# print(re.search('world','hello world').span())

# print(re.match(r'^(\d+)(0*)$','102300').groups())
# print(re.match(r'^(\d+?)(0*)$','102300').groups())

#re.sub 替换匹配字符串的匹配项
#re_telephone=re.compile(r'~(\d{3})-(\d{3,8})$')
#print(re.match(re_telephone,'010-5640').groups())


#python操作文件 (文件模式)
#path="d:/hello.txt"
#f_name = open(path,'r')  #r 表示只读模式
#f_name=open(path,'r') #读写的方式打开
#print(f_name.write('hello python'))
#print(f_name.name)
#print(f_name.read())  #读取12个字符,不指定则会读取所有内容




# #带有close的打开文件
# path = "./hello.txt"
# try:
# 	f_name=open(path,'w')
# 	print(f'{f_name.write("hello\n")}')
# finally:
# 	if f_name:
# 		f_name.close()
#name_f = open(path,'r')
#print(name_f.write('hello python'))
#print(name_f.read())
#name_f = open(path,'a')
#name_f.write("hello go\n")
#name_f = open(path,'r')
#print(name_f.read())


#如果需要读取特定格式额文件，则需要传入编码
#f_name=open(path,'r',encoding='gbk')   读取gbk编码方式的文件

#读写行操作
# name_f = open(path,'r')
# print(name_f.readline())
# print(name_f.readlines())
# str_list=["name","lisis\n"]
# name_f = open(path,'a')
# #将列表写入文件中
# name_f.writelines(str_list)
# name_f = open(path,'r')
# print(name_f.read())
# 关闭文件   name_f.close()


# #使用 with打开文件,自带关闭操作，不需要人为手动去关闭
# path="./hello.txt"
# with open(path,'w') as f:
# 	f_name=open(path,'w')
# 	print(f_name.write("gg"))

# #文件改名
# import os 
# open("./hello.txt",'w')
# os.rename('hello.txt','hello.txt')

#删除文件
# try:
# 	os.remove("./hello.json")
# except Exception as e:
# 	print(e)
#f_name = open('./hello.txt','w')
#f_name.write("hello go \n")

#f_name = open('./hello.txt','r')
# #print(f_name.read())
# while True:
# 	c_str = f_name.read(1)
# 	if not c_str:
# 		break
# 	print(c_str)
# #f_name.close()


# while True:
# 	c_line = f_name.readline(1)
# 	if not c_line:
# 		break
# 	print(c_line)
# f_name.close()


# #使用fileinput迭代
# import fileinput
# for  line in fileinput.input('./hello.txt'):
# 	print(f'{line}')

#使用文件迭代
# path='./hello.txt'
# f_name = open(path)
# for line in f_name:
# 	print("使用文件的方式迭代文件",line)
# f_name.close()   #关闭文件

#StringIO函数
# from io import StringIO
# io_val = StringIO()
# io_val.write('hello')
# print(f'{io_val.getvalue()}')

# fo_val=StringIO('hello\nworld\ngo\n')
# while True:
# 	line=fo_val.readline()
# 	if line == '':
# 		break
# 	print(line.strip())  #去掉行前后的空格

#序列化
# import pickle
# #d= dict(name='xiaohong',num=10022)
# #print(pickle.dumps(d))  #将对象转为 bytes
# try:
# 	#将序列化的数据写入文件
# 	d=dict(name="xiaoming",age=20)
# 	f_name=open('dump.txt','wb')
# 	pickle.dump(d,f_name)
# finally:
# 	f_name.close()
#反序列化
# import pickle
# try:
# 	f_name=open('./dump.txt','rb')
# 	print(pickle.load(f_name))
# finally:
# 	f_name.close()
#json 序列化
# import json
# data={'name':'xiaoming','age':'10'}
# json_str= json.dumps(data)   #对数据进行编码
# print(f'原始数据{data}')
# print(f'json {json_str}')

# data2=json.loads(json_str)   #对数据进行解码
# print(f"data2['name']:{data2['name']}")
# print(f"data2['age']:{data2['age']}")



# #写入json数据
# with open('dump.txt','w') as f:
# 	json.dump(data,f)
# #读取json数据
# with open('dump.txt','r') as f:
# 	data=json.load(f)
# print(data)

#多线程
# import _thread
# from time  	import sleep
# from datetime import datetime

# datetime_format="%y-%M-%d %H:%M:%S"

# def date_time_str(date_time):
# 	return datetime.strftime(date_time,datetime_format)

# def loop_one():
# 	print(f'线程开始于:{date_time_str(datetime.now())}')
# 	print("线程休眠4秒")
# 	time.sleep(4)
# 	print(f'线程结束于:{date_time_str(datetime.now())}')

# def loop_two():
# 	print(f'线程二开始于:{date_time_str(datetime.now())}')
# 	print("线程休眠2秒")
# 	time.sleep(2)
# 	print(f'线程二结束于：{date_time_str(datetime.now())}')

# def main():
# 	print('开始所线程',date_time_str(datetime.now()))
# 	_thread.start_new_thread(loop_one,())
# 	_thread.start_new_thread(loop_two,())
# 	sleep(6)
# 	print('进程结束时间',date_time_str(datetime.now()))

# if __name__ == '__main__':
# 	main()


#防止主进程终止导致所有线程终止，添加锁
# import  _thread,time
# from datetime import datetime
# #定义时间格式
# date_format= "%y-%M-%d %H:%M:%S"
# loops=[4,2]
# def datetime_str(date_time):
# 	return datetime.strftime(date_time,date_format)

# def loop(n_loop,n_sec,lock):
# 	print(f'线程{n_loop}开始执行：{datetime_str(datetime.now())}，先休眠n_sec秒')
# 	time.sleep(n_sec)
# 	print(f'线程{n_loop}结束：{datetime_str(datetime.now())}，线程退出')
# 	lock.release()   #执行完毕后释放线程锁

# def main():
# 	print('开始执行所有进程')
# 	locks=[]
# 	n_loops=range(len(loops))
# 	print(f'n_loops:{n_loops}')

# 	for i in n_loops:    #添加线程锁
# 		lock=_thread.allocate_lock()
# 		lock.acquire()
# 		locks.append(lock)

# 	for i in n_loops:   #启动多线程
# 		_thread.start_new_thread(loop,(i,loops[i],locks[i]))

# 	for i in n_loops:
# 		while locks[i].locked():   #判断状态
# 			pass

# 	print('所有线程执行完毕')

# if __name__ == '__main__':
# 	main()

#使用threading模块实现多线程
# import threading
# import time
# from datetime  import datetime

# loops=[4,2]
# date_time_format="%y-%M-%d %H:%M:%S"

# def date_time_str(date_time):
# 	return datetime.strftime(date_time,date_time_format)

# def loop(n_loop,n_sec):
# 	print(f'线程 {n_loop} 开始执行{date_time_str(datetime.now())}')
# 	time.sleep(n_sec)
# 	print(f'线程执行结束{date_time_str(datetime.now())}')

# def main():
# 	print(f'所有线程开始执行{date_time_str(datetime.now())}')
# 	threads = []
# 	n_loops=range(len(loops))
# 	print('n_loops',n_loops)

# 	for i in n_loops:
# 		t=threading.Thread(target=loop,args=(i,loops[i]))  #创建线程
# 		threads.append(t)

# 	for i in n_loops:
# 		threads[i].start()  #启动线程

# 	for i in  n_loops:
# 		threads[i].join()

# 	print(f'所有线程执行完毕{date_time_str(datetime.now())}')

# if __name__=='__main__':
# 	main()


#使用类创建多线程
#多线程面相对象方法
# import threading
# import time
# from datetime import datetime
# loops=[2,4,5]
# date_time_format="%y-%M-%d %H:%M:%S"

# def get_date_str(date_time):
# 	return datetime.strftime(date_time,date_time_format)

# class ThreadFunc(object):
# 	def __init__(self,func,args,name=""):
# 		self.name=name
# 		self.func=func
# 		self.args=args
# 	def __call__(self):
# 		self.func(*self.args)

# def loop(n_loop,n_sec):
# 	print(f"线程{n_loop}开始执行{get_date_str(datetime.now())}")
# 	time.sleep(n_sec)
# 	print(f'线程{n_loop}执行结束{get_date_str(datetime.now())}')

# def main():
# 	print(f'执行所有线程{get_date_str(datetime.now())}')
# 	threads=[]
# 	nloops=range(len(loops))
# 	for i in nloops:
# 		t=threading.Thread(target=ThreadFunc(loop,(i,loops[i]),loop.__name__))
# 		threads.append(t)

# 	for i in nloops:
# 		threads[i].start()

# 	for i in nloops:
# 		threads[i].join()
# 	print(f"所有线程执行完毕{get_date_str(datetime.now())}")

# if __name__=='__main__':
# 	main()


#__call__方法的使用
# class Person(object):
# 	def __call__(self,name,add):
# 		print("调用__call__方法",name,add)
# per = Person()
# per("参数1","参数二")   #像调用方法一样使用

#线程同步
# import threading
# import time
# from datetime import datetime

# date_time_format='%y-%M-%d %H:%M:%S'

# class MyThread(threading.Thread):
# 	def __init__(self,threadID,name,counter):
# 		threading.Thread.__init__(self)
# 		self.threadID=threadID
# 		self.name=name
# 		self.counter=counter

# 	def run(self):
# 		print(f"开启线程{self.name}")
# 		threadLock.acquire() #获取锁
# 		print_time(self.name,self.counter,3)  #执行的代码
# 		threadLock.release() #释放锁

# def print_time(threadName,delay,counter):
# 	while counter:
# 		time.sleep(delay)
# 		print(f'{threadName}:{datetime.strftime(datetime.now(),date_time_format)}')
# 		counter-=1
# def main():
# 	thread1=MyThread(1,"thread-1",1)
# 	thread2=MyThread(2,"thread-2",2)
# 	#启动线程
# 	thread1.start()
# 	thread2.start()

# 	threads.append(thread1)
# 	threads.append(thread2)

# 	for t in threads:
# 		t.join()  #退出主线程s
# 	print("退出主线程")

# if __name__=='__main__':
# 	threadLock=threading.Lock()
# 	threads=[]
# 	main()

# #线程优先级队列 Queue 实现线程之间的通信
# import threading
# import queue
# from time import sleep

# class MyThread(threading.Thread):
# 	def __init__(self,threadID,name,q):
# 		threading.Thread.__init__(self)
# 		self.threadID=threadID
# 		self.name=name
# 		self.q=q
# 	def run(self):
# 		print(f'开启线程{self.name}')
# 		process_data(self.name,self.q)
# 		print(f'退出线程{self.name}')
# def process_data(threadName,q):
# 	while not exitFlag:
# 		queueLock.acquire()
# 		if not workQueue.empty():  #队列为空返回true，否则返回false
# 			data=q.get()  #获取队列
# 			queueLock.release()
# 			print(f'{threadName}processing{data}')
# 		else:
# 			queueLock.release()
# 		sleep(1)
# def main():
# 	global exitFlag
# 	exitFlag=0
# 	threadList=['thread-1','thread-2','thread-3']
# 	nameList=['one','two','three','four']
# 	threads=[]
# 	threadID=1

# 	for tName in threadList:
# 		thread=MyThread(threadID,tName,workQueue)
# 		thread.start()
# 		threads.append(thread)
# 		threadID+=1
# 	queueLock.acquire()
# 	for word in nameList:
# 		workQueue.put(word)  #写入队列
# 	queueLock.release()

# 	while not workQueue.empty():
# 		pass

# 	exitFlag=1

# 	for t in  threads:
# 		t.join()
# 	print('线程退出')

# if __name__=='__main__':
# 	queueLock=threading.Lock()
# 	workQueue=queue.Queue(10)
# 	main()

# import threading ,queue,time,urllib
# from urllib import request

# base_url='https://www.yyfeiye.com/guocanju/zx20/1-'
# url_queue=queue.Queue()
# for item in range(1,36):
# 	url=base_url+str(item)+'.html'
# 	url_queue.put(url)

# def fetch_url(url_queue):
# 	while True:
# 		try:
# 			url_val=url_queue.get_nowait()
# 			url_queue.qsize()  #返回队列大小
# 		except Exception as e:
# 			print(f'err1 :{e}')
# 			break
# 		curr_thread_name=threading.currentThread().name
# 		print(f'{curr_thread_name}:{url_val}')
# 		try:
# 			response=urllib.request.urlopen(url_val)
# 			response_code=response.getcode()
# 		except Exception as e:
# 			print(f'error:{e}')
# 			continue

# 		if response_code == 200:
# 			time.sleep(1)

# if __name__=='__main__':
# 	start_time=time.time()
# 	threads=[]
# 	thread_num=4
# 	for num in range(0,thread_num):
# 		thread=threading.Thread(target=fetch_url,args=(url_queue,))
# 		threads.append(thread)
# 	for item in threads:
# 		item.start()
# 	for thread_t in threads:
# 		thread_t.join()
# 	print(f'all thread donw spend{time.time()-start_time}')


# for item in range(0,10):   #返回0-9，不包含10
# 	print(f'thread-{item}')
#使用python发送电子邮件



#python 网络编程
#客户端
# import socket
# #创建一个socket
# s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# host=socket.gethostname() #获取本地主机名
# print(host)
# port=9000
# s.connect(('www.baidu.com',80))
# s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
# buffer=[]
# while  True:
# 	d= s.recv(1024)
# 	if d:
# 		buffer.append(d)
# 	else:
# 		break
# 	data=b''.join(buffer)
# 	print(data) 
# s.close()  #关闭连接

# header,html=data.split(b'\r\n\r\n',1)
# print(header.decode('utf-8'))
# with open('baidu.html','wb') as f:
# 	f.write(html)

#服务端
# import socket
# import threading
# import time
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #创建socket
# host=socket.gethostname()
# port=9999
# s.bind((host,port))
# #设置最大连接数
# s.listen(5)  

# def tcplink(sock,addr):
# 	print(f'access tcp link%s{addr}')
# 	sock.send("欢迎学习python网络编程".encode('utf-8'))
# 	while True:
# 		data=sock.recv(1024)
# 		time.sleep(1)
# 		if not data or data.decode('utf-8')=='exit':
# 			break
# 		sock.send(('hello %s'% data.decode('utf-8')).encode('utf-8'))
# 		sock.close()
# 		print('connection from %s:%s closed' % addr)

# while True:
# 	print("等待客户端连接...")
# 	sock,addr=s.accept()
# 	t=threading.Thread(target=tcplink,args=(sock,addr))
# 	t.start()

#urllib模块
#get请求
# from urllib  import request

# def get_request():
# 	with request.urlopen("http://www.baidu.com") as f:
# 		data=f.read()
# 		print(f'{f.status} {f.reason}')
# 		for k,v in f.getheaders():
# 			print(f'{k}:{v}')
# 	#print(f"Data:{data.decode('utf-8')}")
# def main():
# 	get_request()
# if __name__=='__main__':
# 	main()

#post请求
from urllib import request,parse

def login_post():
	print('login qq.com')
	account=input('account:')
	passwd=input('passwd:')
	login_data=parse.urlencode