import json

def handle_dict_json(dict_json):
    """
    dict_json为文件名
    dict_json文件中为dict格式的请求数据
    此方法的目的是，将字典格式转换成json格式，并格式化输出

    """
    with open(file=dict_json,mode='r',encoding='utf-8') as f:
        res = f.readlines()

    for i in res:
        #i为str格式,data为字典格式
        data=eval(i)
        #data为json格式
        data = json.dumps(data,sort_keys=True,ensure_ascii=False,indent=4,separators=(',',':'))
    return data


dict_json='dict_json.txt'
print(handle_dict_json(dict_json))