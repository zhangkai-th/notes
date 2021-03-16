#coding:utf-8
height=float(input("请输入身高"))

if height > 170:
	print("\033[41;1m 中等 %s\033[0m"% height)
elif height <= 170:
	print("\033[42;1m 较低 %s\033[0m"% height)

s=("如果一个字符串不能再一行完全显示，可以使用（）将其分行显示"
	"第二行内容")
"""
使用单个下划线_的模块变量或者函数，是受保护的，不能通过from  xxx import xxx 引入

"""