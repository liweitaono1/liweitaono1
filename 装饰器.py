import time


def set_fon(fon):
    times = 0
    start_time = time.time()
    print(start_time)

    def call_fon():
        nonlocal times
        fon()
        times += 1
        return times
    end_time = time.time()
    print(end_time)
    run_time = end_time - start_time
    print(run_time)
    return call_fon


@set_fon # 装饰器 记录执行时间和执行次数
def test():
    print("测试")


test()
test()
test()
test()
test()
test()
test()
test()
test()
test()
print(test())