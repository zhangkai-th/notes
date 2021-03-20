#coding:utf-8
import time
import math
'''
@description 建议服务信息登记
@version 1.0
'''

def menu():
	print("\t\t服务器信息登记管理系统\t\t")
	print("\t\t1、添加服务信息\t\t")
	print('\t\t2、查询服务信息\t\t')
	print('\t\t3、输入[q|Q]退出系统\t\t')
def write_disk(data,config_dir):
	'''
	该方法将数据写入
	'''
	try:
		with open(config_dir,'w') as file:
			file.write(str(data)+'\n')
	except Exception as e:
		print("写入文件失败:",e)
	finally:
		print("文件写入方法执行完")

def main():
	config_dir='./config.cfg'+str(math.ceil(time.mktime(time.localtime())))
	#server_dic={}
	server_list=[]
	servers={}
	while True:
		menu()

		server_dic={}
		#servers={}
		answer=str(input("请输入操作选项："))
		if answer == '1':
			server_name=str(input("请输入服务名称："))
			ip=str(input("请输入服务器ip："))
			port=str(input('请输入端口号：'))
			path=str(input("请输入服务启动路径:"))
			server_dic=dict(ip=ip,port=port,path=path)
			#print(server_dic)
			#server_list.append(server_dic)
			servers[server_name]=server_dic
			#with open(config_dir,'a') as file:
				#for k,v in server_dic.items():
				#	file.write(k+':'+v+'\n')
			#	file.write(str(servers)+'\n')

		elif answer == '2':
			write_disk(servers,config_dir)
			print("数据写入成功")
			with open(config_dir,'r') as file:
				while True:
					line=file.readline()
					print(line,end='')
					if line == '':
						break
					#print(file.readline())

		elif answer == 'q' or answer == 'Q':
			print("系统将在两秒后退出...")
			time.sleep(2)
			break
		else:
			print("输入有误,请重新输入")
if __name__=='__main__':
	main()