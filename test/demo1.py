s= '面试题'
# 生成随机字符串 （指定长度）
# import random
# import string
#
# def generate_random_str(randomlength=16):
#     """
#     string.digits=0123456789
#     string.ascii_letters=abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
#     """
#     str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
#     random_str = ''.join(str_list)
#     return random_str
#
# if __name__ == '__main__':
#     g = generate_random_str()
#     print(g)
# 单列模式：
class Single(object):
    __isinstance =None
    __first_init = False
    def __new__(cls, *args, **kwargs):
        if not cls.__isinstance:
            cls.__isinstance = object.__new__()
        return cls.__isinstance

    def __init__(self,name):
        if not self.__first_init:
            self.name = name
            Single.__first_init = True

list1 = [1, 2, 3, 5]
list2 = [4, 5, 6]
zipped = zip(list1, list2)
print(list(zipped))  # [(1, 4), (2, 5), (3, 6)]