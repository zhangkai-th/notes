#coding:utf-8
# height=float(input("请输入身高"))

# if height > 170:
# 	print("\033[41;1m 中等 %s\033[0m"% height)
# elif height <= 170:
# 	print("\033[42;1m 较低 %s\033[0m"% height)

# s=("如果一个字符串不能再一行完全显示，可以使用（）将其分行显示"
# 	"第二行内容")
"""
使用单个下划线_的模块变量或者函数，是受保护的，不能通过from  xxx import xxx 引入
使用双下划线的实例变量的的方法属于私有的
推荐导入方法
import os
import sys
nickname="小红"
type(nickname)   #判断变量的类型
"""
hello="world"
 #获取变量地址
print(id(hello))
#常量由大写字母与下划线组成
"""
str() 将数字转为字符串
常见的转义字符
\
\n 换行符
\0 空
\t 水平制表符
\" 双引号
\f 换页
int()
float()
repr()
eval()
chr()
逻辑运算符
and or not
age=int(input("请输入年龄"))
"""
#print("hello","world")
# print("欢迎登陆身高测试系统")
# father_height=float(input("请输入父亲的身高:"))
# mom_height=float(input("请输入母亲的身高:"))
# print("您儿子的身高是",(father_height+mom_height)*0.54)
# num=5
# if num == 5:print("num is 5")

# print("欢迎登陆过考试成绩查询系统")
# coures=str(input("请输入需要查询的科目[english|chinese]:"))
# if coures=="english":
# 	print("您的语文成绩是 47分")
# elif coures=="chinese":
# 	print("您的英文成绩是 67分")
# else:
# 	print("输入有误，请重新输入")

# print("\t酒驾检测系统\t")
# proof=float(input("请输入每毫升血液酒精含量:"))
# if proof <20:
# 	print("未酒驾")
# else:
# 	if 80>proof>=20:
# 		print("您已涉嫌酒驾")
# 	else:
# 		print("醉酒标准，已达")

#条件表达式
# a=10
# b=6
# if a>b:
# 	r=a
# 	print(r)
# else:
# 	r=b
# 	print(r)

# a=10
# b=6
# r=a if a>b else b
#
'''
while 循环
'''
# num=0
# flag=True
# while flag:
# 	num += 1
# 	if num == 10:
# 		print("恭喜你，中奖了")
# 		flag=False

#for 循环用来迭代字符串 列表 元组
# print("从1加到100")
# result=0
# for i in range(101):
# 	result=result+i
# print(result)

# for i in range(1,10,2): #start end 步长
# 	print(i,end=' ')  #end 表示分隔符

# str_list='不要再说我不能'
# for ch in str_list:
# 	print(ch)

#打印99乘法表
# for  i in range(1,10):
# 	for j in range(1,i+1):
# 		print(str(j)+"*"+str(i)+"="+str(i*j)+"\t",end=" ")
# 	print('')

#模拟10086查询模块
# print("\t10086查询功能\t")
# print("输入1，查询流量\n"
# 	"输入2，查询话费\n"
# 	"输入3，退出系统")
# while True:
# 	result=int(input("请输入"))
# 	if result==1:
# 		print("您当前余额为50G")
# 	elif result==2:
# 		print("您当前余额为50￥")
# 	elif result==3:
# 		print("即将退出系统...")
# 		break
# 	else:
# 		print("error")
#序列 ：列表 元组 集合 字典 字符串
#-1表示最后一个元素
#切片 name=[start:end:step]
# names=['小明','小白','笑话','晓明','老徐','失败']
# print(names[1:5])  #2-5的元素
# print(names[0:5:2])  #1 3 5 元素
# print(names[:]) #复制整个序列
# #序列相加
# name1=['docker','k8s']
# name2=['javascript','java']
# print(name1+name2) #['docker', 'k8s', 'javascript', 'java']
# print(name1*3)  #['docker', 'k8s', 'docker', 'k8s', 'docker', 'k8s']

# namelist=[None]*5  #声明一个有五个元素的列表
# print(namelist)  

# print('docker' in name1) #判断docker是否在序列中  not in 用法相同
'''
len(name1) 返回列表的长度
max(name1) 返回列表中的最大值
min(name1)  返回最小值
list() 将序列在转换为列表
str()  将序列转化为字符串
sum() 计算元素和
sorted()  对元素进行排序
reversed() 反向序列中的元素
enumerate() 将序列组合为一个索引序列
列表
name=['name1','name2']
1、列表中的元素类型可以不同

'''
# print(list(range(10,20,2)))  #[10, 12, 14, 16, 18]
# numlist=list(range(1,10))
# print(numlist[2]) #获取list元素
# print(numlist)
# del numlist   #删除列表
# print(numlist)
# 

# #遍历列表
# for i in range(10,20):
# 	print(i)
# names=['tom','jerry','marry']
# #使用enumerate获取列表的元素及索引
# for i,v in enumerate(names):
# 	print(i,v)
# #列表添加元素
# names.append('henry')
# print(names)
# names.insert(1,'mmmm')
# print(names)
# names2=['shshhshs','shark']
# names.extend(names2)  #追加元素
# print(names)
# names[2]="readhat"
# print(names)
# #根据索引删除元素
# del names[1]
# print(names)
# names.remove('tom')  #根据名字删除元素
# print(names)
# #删除元素前先判断元素是否存在
# if names.count('tom')>0:
# 	names.remove('tom')
# 	print(names)
# else:
# 	print('元素不存在')

# #列表统计函数
# print(names)
# print(names.count('shark')) #统计元素出现的次数
# print(names.index('shark')) #获取元素首次出现的下标

# nums=list(range(10))
# print(nums)
# totatl=sum(nums)  #列表元素求和
# print(totatl)
# nums2=[1,5,3,4,9,100,34]
# nums2.sort()
# print(nums2) #升序排列
# nums2.sort(reverse=True) #逆序排序
# print(nums2)
'''
char=['cat','dog',mow]
char.sort()
char.sort(key=str.lower) 不区分大小写
使用该方法排序，源列表顺序不变,新生成一个副本
sorted(listname,key=None,reverse=True)
'''
#列表推导式生成列表
# import random
# numss=[random.randint(10,200) for i in range(10)]
# print(numss)
# price=[100,200,300,400]
# sale=[int(x*0.5) for x in price]
# print(sale)
# sale2=[x for x in price if x >100]  #根据指定条件生成列表
# print(sale2)

# #创建二维列表
# listname=[[j for j in range(5)] for i in range(4)]
# print(listname)

#元组  （），不可变
# books=('红楼鞥','水浒传','西游记','鹿鼎记','赘婿')
# print(books)
# num=tuple(i for i in range(10))
# print(num)
# print(books[0])  #访问元组元素
# #del num  #删除元组
# #元组的遍历
# for book in books:
# 	print(book)

# for i,book in enumerate(books):
# 	print(i,book)

# #元组不支持修改操作
# #元组推到式
# import random
# #tuple()  转换为元组
# mytuple=tuple(random.randint(10,100)  for i in range(10))
# print(mytuple)

#__next__() 遍历生成器
# number=(i for i in range(10))
# print(number.__next__()) #输出第一个元素
# print(number.__next__()) #输出第二个元素
# nmber=tuple(number)
# print(number)
'''
元组与列表区别
1、列表可变，元组不可变，且不可修改
2、元组处理速度比列表快
'''
'''
字典
1、键值必须唯一
2、键不可变
'''
# dictionary={'name':'zhangsan','age':20,'height':170}
# print(dictionary)
# list1=[1,2,3,4]
# list2=['name','age','height','weight']
# dic=dict(zip(list1,list2))  #zip函数将两个列表合并为一个键值对
# print(dic)
# #通过给定键值对创建字典
# dic1=dict(name='tom',age=10)
# print(dic1)
# #创建为空的字典
# list3=['name','age']
# dic3=dict.fromkeys(list3)
# print(dic3)
#del dic3  删除字典
#dic3.clear()  清空字典
#pop()  删除指定键元素
#popitem() 删除并返回字典中的一个元素
#dictionary('name') 返回指定的值
#print(dictionary['name'] if 'name' in dictionary else 'no this result')
#print(dictionary.get('name','no this result'))
# for item in dictionary.items():   #获取键值对
# 	print(item)

# for k,v in dictionary.items():
# 	print(k,v)
#values() 和 keys()  获取字典的键和值

# print("\t操作字典\t")
# dictionary=dict((('name','小明'),('age',20),('height',170)))
# dictionary['hello']='红薯'
# if 'name' in dictionary:  #判断是否存在该键
# 	del dictionary['name']
# print(dictionary)

#字典推导式
# import random
# ra={i:random.randint(10,100) for i in range(1,5)}
# print(ra)
# name=['晓明','李四','张三']
# job=['钢琴家','警察','医生']

# ra1={i:j for i,j in zip(name,job)}
# print(ra1)

#集合
#保存不重复的元素
# set1={'红楼梦','田龙龙八部','你好河流咯','哈喽','牛皮'}
# print(set1)

# #使用set函数创建集合
# set2=set([1,2])
# print(set2)
# set3=set(('sss','vvv'))
# print(set3)

# #集合操作
# books={'红楼梦','田龙龙八部','你好河流咯','哈喽','牛皮'}
# books.add('夜班敲门')  #添加元素
# print(books)
'''
remove('红楼梦') 删除指定元素
pop() 删除第一个元素
clear()   清空集合
del books  删除集合
'''



'''
字符串及正则表达式

'''
#string函数
#string.endswith('4')  判断字符串是不是以4结尾
#len(string)  字符串的长度
# str1='人生苦短，我要学python'
# length=len(str1.encode())  #将其转为utf-8编码 str1.encode('gbk')
# print(length)
# print(str1[1:3])  #截取一段
# #字符串分割
# str2='sdf ads asd'
# print(str2.split())  #默认为空格 返回为列表元素
# str3=str2.split()
# print('@'.join(str3))   #用@作为连接符进行连接
# print(str1.find('python'))  #检索字符串是否存在 可以使用'python' in  str1实现
# #返回-1表示元素不存在
# print(str1.index('python')) #返回指定字符的索引值

# print(str2.startswith("s"))  #判断字符是否以人开头
# print(str2.endswith('d'))  #判断是否已d结尾
#str1.lower()
#str1.upper()
#str1.strip('@.')  将首尾的@ . 字符去掉   lstrip() rstrip()
#str1.format(data1,data2)

#str1.encode('gbk') 将字符转为gbk
#str1.decode('gbk')  将二进制转为字符串

'''
正则表达式
\bmr\w*\b     \b表示单词开始处 \w 任意数量的字母或数字
? 匹配前面的字符0或1次
+ 匹配前面的字符1次或多次
* 匹配前面的字符零次或多次
\d 匹配数字
r'\bmr\w*\b'  使用原生字符串
'''

# import re
# pattern=r'mr_\w+'
# string='MR_SHOP mr_shop'
# match=re.match(pattern,string,re.I)
# print('匹配位置的起始',match.start())
# print('匹配位置的结束',match.end())
# print('匹配位置的元组',match.span())
# print('匹配位置的字符串',match.string)
# print('匹配数据',match.group())
# match1=re.search(pattern,string,re.I)
# print(match1)
# match2=re.findall(pattern,string,re.I)  #re.I 表示不区分大小写
# print(match2) # ['MR_SHOP', 'mr_shop']

#re.sub() 实现字符串的替换
#re.split() 分割字符串
#
#函数
'''
funcname (height=1.83,weight=90)
def funcname(height,person='路人')  指定默认值
funcname.__defaults__ 查看当前函数的默认值
'''
#接收任意参数的函数
# def print_books(*books):
# 	for item in books:
# 		print(item)
# print_books('jsjsj','sfdsdf')
#接收键值对参数
def print_person_message(**person):
	for k,v in person.items():
		print(k,'------',v)
print_person_message(name="tom",age=12,weight=2390)

person={'name':'tom','age':20}
print_person_message(**person)  #接收现有的字典
#python返回值可返回多个数据
return va1,va2



#
#
#日期相关函数
# import datetime
# day=datetime.datetime.now().weekday() #火速当前是星期几
# print(datetime.datetime.now()) #获取当前时间
# print(day)


#异常捕获
# try:
# 	code
# except Exception as e:
# 	print(e)