
import json

def handle_data_format(text):
    """
    处理通过F12抓包的数据，get请求
    格式为
    menuId: de43e55ef041192a505f723eee2320f6
    处理为json字符串
    {"menuId": "de43e55ef041192a505f723eee2320f6"}
    :param text:文件名
    :return:
    """
    with open(file=text,mode='r',encoding='gbk') as f:
        #读取所有的内容，['DEPARTURE_AIRPORT: PVG\n',..]包含有\n
        res = f.readlines()
        #res为列表
        #print(res,type(res))

    #定义一个空字典
    dic = {}
    for i in res:
        # 以冒号分割，['DEPARTURE_AIRPORT', ' PVG\n']
        i=i.split(':')
        # 取出列表中第一元素的值
        key=i[0]
        # 取出列表中第二个元素的值
        value=i[1]
        # 组合成字典格式,{'DEPARTURE_AIRPORT': ' PVG\n'
        dic[key]=value

    #处理字典格式中的空格和\n,{'DEPARTURE_AIRPORT': 'PVG', 'page': '1',
    data = eval(str(dic).replace('\\n','').replace(' ',''))
    # 将字典转成json字符串
    data=json.dumps(data)

    return data

if __name__ == '__main__':

    #text在同一级目录下，可以直接写文件名，如果不在同一级目录下，可以写上路径
    # text='../conf/text.txt'
    text='text.txt'
    print(handle_data_format(text))