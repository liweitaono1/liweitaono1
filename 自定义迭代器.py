class MyList(object):

    def __init__(self,list):
        self.my_list = list

    def __iter__(self):
        # 可迭代对象的本质：遍历可迭代对象的时候其实获取的是可迭代对象的迭代器， 然后通过迭代器获取对象中的数据
        my_iterator = MyIterator(self.my_list)
        return my_iterator



class MyIterator(object):

    def __init__(self, my_list):
        self.my_list = my_list

        # 记录当前获取数据的下标
        self.current_index = 0


    def __iter__(self):
        return self

    # 获取迭代器中下一个值
    def __next__(self):
        if self.current_index < len(self.my_list):
            self.current_index += 1
            return self.current_index, self.my_list[self.current_index - 1]
        else:
            # 数据取完了，需要抛出一个停止迭代的异常
            raise StopIteration

a = [1,2,34,5,6,78,70,9]
mylist = MyList(a)
my_iter = iter(mylist)
while True:
    try:
        value = next(my_iter)
        print(value)
    except StopIteration as e:
        break


