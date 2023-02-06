
import string
import random

def gen_str(str_length):
    """
    生成指定长度的字符
    """
    #生成所有字母数字
    num=string.digits+string.ascii_letters
    #定义一个空列表
    str_list=[]
    #从num中取n个样本数，返回的是一个字符串组成的列表
    for i in range(str_length):
        str_list.append(random.choice(num)) #  str_list为取的指定长度的字符串的列表
    #将列表转换成字符串
    str=''.join(str_list)
    return str

print(gen_str(250))