import multiprocessing
import os
import shutil


def copy(path, new_path, file_name):
    try:
        file_path = path + "/" + file_name
        with open(file_path, "rb") as f:
            while True:
                content = f.read()
                with open(new_path + "/" + file_name, "ab") as n_f:
                    if content:
                        n_f.write(content)
                    else:
                        break
    except Exception as e:
        print(e)


def main():
    count = os.cpu_count()
    print(os.cpu_count())
    pool = multiprocessing.Pool(count)
    path = input("请输入要复制文件夹的路径:")
    new_path = input("请输入要复制到的路径:")
    if os.path.exists(new_path):
        shutil.rmtree(new_path)
    print(new_path)
    os.mkdir(new_path)
    for x in os.listdir(path):
        print(x)
        pool.apply_async(copy(path, new_path, x))
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
