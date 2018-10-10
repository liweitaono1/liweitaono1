class MyFun(object):
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, *args, **kwargs):
        print("success")
        a = 1
        b = 1
        print(a + b)
        # self.fun()
        # pass
    @classmethod
    def a(cls,value):
        print(value)
        # cls.__call__(cls)
        return cls



@MyFun.a("nihao")
def test():
    print("test")


test()


