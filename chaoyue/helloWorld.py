# coding=utf-8
# print两种写法都可以 多个print之间默认是换行的 如果不需要则加上，
print "hello world"
print("hello chaoyue"),
print(" same row")
# if-else 的写法 使用缩进来确定作用域
if True:
    print("this is true")
else:
    print("this is false")

'''
字符串类型使用以下三种定义都可以
可以换行
'''
word = 'this is a word'
word2 = "this is a word2"
word3 = """this is a word3
233333"""
print word + word2 + word3
# 等待用户输入
# raw_input("put enter")
# 同一行显示多条语句
import sys; x='chaoyue'; sys.stdout.write(x + '\n')
