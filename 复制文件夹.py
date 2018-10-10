import os
import multiprocessing
import shutil
def copy(dest_name, src_name, file_name):
    with open(src_name, "wb") as src_file:
        while  True:
            content = src_file.read(1024)
            if content:
                with open(dest_name + file_name, "ab") as dest_file:
                    dest_file.write(content)
            else:
                break


def main():
    src_name = input("请输入文件夹名称:")
    index = src_name.rfind("/")
    print(index)
    dest_name = src_name[index:]
    print(dest_name)
    if os.path.exists(dest_name):
        shutil.rmtree(dest_name)
    os.mkdir(dest_name)
    file = os.listdir(src_name)
    pool = multiprocessing.Pool(3)
    for file_name in file:
        pool.apply_async(copy,(src_name, dest_name, file_name))

    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
