#coding:utf-8
import threading
import time

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


g_num=100
def work1():
	global g_num
	for i in range(3):
		g_num+=1
	print("g_num %d" % g_num)
def work2():
	global g_num
	print("g_num work2 %d" % g_num )
if __name__=="__main__":
	t1=threading.Thread(target=work1)
	t1.start()
	time.sleep(1)
	t2=threading.Thread(target=work2)
	t2.start()
	t2=threading.Thread(target=work2)
