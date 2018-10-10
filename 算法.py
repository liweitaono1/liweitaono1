# def binary_search(list, item):
#     low = 0
#     high = len(list) - 1
#     while low <= high:
#         mid = (low + high)//2
#         guess = list[mid]
#         if guess == item:
#             return mid
#         if guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#
#     return None
# my_list = [1,3,5,7,9]
# print(binary_search(my_list, 3))
# print(binary_search(my_list, -1))

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i #存储最小的值
            #存储最小元素的索引
    return smallest_index



def selectionSort(arr): # 对数组进行排序
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr
print (selectionSort([5, 3, 6, 2, 10]))


"""
写一段代码, 从一个整数数组,得出其中所有正数的两倍的数组
写一个验证电话号码正则表达式,010-85413698,0341-8715666 区号3/4位 号码7/8位
实现一个装饰器函数, 能够在被包装函数调用时前后输出一些内容, 例如如下代码中的print_debug函数
@print_debug
def login():
print(“xxxxxx”)

login()
# => ‘enter login’
# => ‘xxxxxx’
# => ‘exit login
"""


# def set_foun(founc):
#     def call_foun(*args, **kwargs):
#         print(1)
#         a = founc(*args, **kwargs)
#         print(2)
#         return a
#     return call_foun
#
# @set_foun
# def test():
#     print("test")
#
# test()

# import re
# data = input("请输入号码")
# msg = re.match(r"\d{3,4}-\d{7,8}", data).group()
# if msg:
#     print(msg)
# else:
#     print("输入错误")

# list = [1,2,3,-1,-6,-7,24,-5,0]
# new_list = []
# for x in list:
#     if x > 0:
#         new_list.append(x*2)
#
# print(new_list)