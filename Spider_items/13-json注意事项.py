import json

# 1.包含json类文件对象: 使用open打开的指向json格式文件的对象
nihao = 123
# 2.键和值都必须用双引号
# json_str = "{'name':'lao wang', 'age':10, 'gender':true, 'desc':'老王在炼妖'}"
json_str = "{'name':'lao wang', 'age':10, 'gender':'true', 'desc':'老王在炼妖'}"

# my_str = 'nihao'

# 方法1:使用repalce函数
json_str = json_str.replace("'", '"')
# print(json_str)

# print(eval(json_str))

# 方法2,使用eval,能实现简单的字符串和python类型的转化
# my_str = eval(my_str)
# print(my_str, type(my_str))

# json_str = '{"name":"lao wang", "age":10, "gender":true, "desc":"老王在炼妖"}'

# print(json.loads(json_str))

# 将json数据转化为pthon数据类型
json_dict = json.loads(json_str)

# 3.dump和dumps中的参数:ensure_ascii indent
# ensure_ascii:是否以ascii方式写入,默认为true,中文不显示
# 如果指定为False,则以UTF-8写入,打开文件也必须指定为UTF-8
# indent:格式化输出,用于指定代码块之间几个空格

# 操作文件
# 将Python类型的数据以json格式写入文件
with open("test1.json", "w") as f:
    json.dump(json_dict, f)

# 如果指定为False,则以UTF-8写入,打开文件也必须指定为UTF-8
with open("test2.json", "w", encoding="utf8") as f:
    json.dump(json_dict, f, ensure_ascii=False, indent=4)

# 从文件中读取json数据转化为python类型数据
with open("test2.json", "r") as f:
    print(f.read())

'''
4.往一个文件中写入多个json串，不再是一个json串，不能直接读取
一行写一个json串，按照行来读取 f.readline()
'''