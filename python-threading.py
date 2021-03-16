#coding:utf-8
# import threading
# import time

# def run(n):
# 	print(f"thread:{n}")

# def main():
# 	for i in range(4):
# 		para="t"+str(i)
# 		threads.append(threading.Thread(target=run,args=(para,)))

	
# if __name__ =='__main__':
# 	threads=[]
# 	main()
# 	for thread in threads:
# 		thread.start() 



# class MyThread(threading.Thread):
# 	def __init__(self,n):
# 		super(MyThread,self).__init__()
# 		self.n=n
# 	def run(self):
# 		print(f"thread:{self.n}")

# if __name__=="__main__":
# 	threads=[]
# 	for i in range(4):
# 		threads.append(MyThread(i))

# 	for thread in threads:
# 		thread.start()



# def run(n):
# 	print(f"thread{n}")
# 	print("休眠两秒")
# 	time.sleep(2)
# 	print("休眠十秒")
# 	time.sleep(10)

# if __name__=="__main__":
# 	t=threading.Thread(target=run,args=("1",))
# 	t.setDaemon(True)   #设置子线程为守护线程，主线程退出，子线程退出
# 	t.start()
# 	#t.join()
# 	print("end")



# def run(n):
# 	print(f"thread{n}")
# 	print("休眠两秒")
# 	time.sleep(2)
# 	print("休眠十秒")
# 	time.sleep(10)

# if __name__=="__main__":
# 	t=threading.Thread(target=run,args=("1",))
# 	t.setDaemon(True)   #设置子线程为守护线程，主线程退出，子线程退出
# 	t.start()
# 	t.join()  #主线程等待子线程结束
# 	print("end")


#线程共享全局变量
# g_num=100
# def work1():
# 	global g_num
# 	for i in range(3):
# 		g_num+=1
# 	print("g_num %d" % g_num)
# def work2():
# 	global g_num
# 	print("g_num work2 %d" % g_num )
# if __name__=="__main__":
# 	t1=threading.Thread(target=work1)
# 	t1.start()
# 	time.sleep(1)
# 	t2=threading.Thread(target=work2)
# 	t2.start()
# 	t2=threading.Thread(target=work2)


#互斥锁
# from threading  import Thread,Lock
# import os,time
# def work():
# 	global n
# 	lock.acquire()
# 	temp=n
# 	time.sleep(1)
# 	n=temp-1
# 	print(n)
# 	lock.release()
# if __name__=="__main__":
# 	lock=Lock()
# 	n=100
# 	l=[]
# 	for i in range(20):
# 		p=Thread(target=work)
# 		l.append(p)
# 		p.start()
# 	for p in l:
# 		p.join()

#递归锁
# import threading 
# import time

# def work(lock):
# 	global g_num
# 	lock.acquire()
# 	g_num +=1
# 	time.sleep(1)
# 	print(g_num)
# 	lock.release()

# if __name__ =="__main__":
# 	g_num=0
# 	lock=threading.RLock()
# 	for i in range(10):
# 		t=threading.Thread(target=work,args=(lock,))
# 		t.start()

#信号量
#同时允许一定数量的线程修改数据

# import threading
# import time

# def run(n,semaphore):
# 	semaphore.acquire()
# 	time.sleep(1)
# 	print("run the thread %s" % n)
# 	semaphore.release()

# if __name__=="__main__":
# 	num=0
# 	semaphore=threading.BoundedSemaphore(5)
# 	for i in range(10):
# 		t = threading.Thread(target=run,args=("t-%s" % i,semaphore))
# 		t.start()
# 	while threading.active_count() != 1:
# 		#print(threading.active_count)
# 		pass
# 	else:
# 		print("----all thread done----")

#事件
import threading
import time
event=threading.Event()

def lighter():
	count=0
	event.set()  #将flag设置为true
	while True:
		if 5<count<=10:
			event.clear()  #将flag设置为false
			print("\033[41;1m read light is on...\033[0m")
		elif count >10:
			event.set()  
			count=0
		else:
			print("\033[42;1m green light is on...\033[0m")

		time.sleep(1)
		count +=1

def car(name):
	while True:
		if event.is_set():
			print("[%s] running..."% name)
			time.sleep(1)
		else:
			print("[%s] see red light ,waitting..."% name)
			event.wait()  #监听flag，如果没有检测到就一直处于阻塞状态
			print("[%s] green light is on ,start going..." % name)

light=threading.Thread(target=lighter)
light.start()

car=threading.Thread(target=car,args=("MINI",))
car.start()
