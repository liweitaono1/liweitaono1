# print("******单继承使用super().__init__ 发生的状态******")
# class Parent(object):
#     def __init__(self, name):
#         print('parent的init开始被调用')
#         self.name = name
#         print('parent的init结束被调用')
#
# class Son1(Parent):
#     def __init__(self, name, age):
#         print('Son1的init开始被调用')
#         self.age = age
#         super().__init__(name)  # 单继承不能提供全部参数
#         print('Son1的init结束被调用')
#
# class Grandson(Son1):
#     def __init__(self, name, age, gender):
#         print('Grandson的init开始被调用')
#         super().__init__(name, age)  # 单继承不能提供全部参数
#         print('Grandson的init结束被调用')
#
# gs = Grandson('grandson', 12, '男')
# print('姓名：', gs.name)
# print('年龄：', gs.age)
# #print('性别：', gs.gender)
# print("******单继承使用super().__init__ 发生的状态******\n\n")

# class Goods:
#     """python3中默认继承object类
#         以python2、3执行此程序的结果不同，因为只有在python3中才有@xxx.setter  @xxx.deleter
#     """
#     @property
#     def price(self):
#         print('@property')
#
#     @price.setter
#     def price(self, value):
#         print('@price.setter')
#
#     @price.deleter
#     def price(self):
#         print('@price.deleter')
#
# # ############### 调用 ###############
# obj = Goods()
# obj.price          # 自动执行 @property 修饰的 price 方法，并获取方法的返回值
# obj.price = 123    # 自动执行 @price.setter 修饰的 price 方法，并将  123 赋值给方法的参数
# del obj.price      # 自动执行 @price.deleter 修饰的 price 方法




class Goods(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    def get_price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    def set_price(self, value):
        self.original_price = value

    def del_price(self):
        del self.original_price

    PRICE = property(get_price, set_price, del_price, '价格属性描述...')

obj = Goods()
print(obj.PRICE)         # 获取商品价格
obj.PRICE = 200   # 修改商品原价
print(obj.PRICE)         # 获取商品价格
del obj.PRICE     # 删除商品原价
