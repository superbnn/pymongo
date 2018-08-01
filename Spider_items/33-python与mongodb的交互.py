from pymongo import MongoClient
'''
使用python向集合t6中插入1000条文档, 文档包含_id和name
id的值为0, 1, 2, 3,...999
name的值为py0, py2, ....

查询显示出_id为100整数的倍数的文档, 如100, 200, 300...

'''


class MongoTest(object):
    '''MongoDB和Python的交互'''

    def __init__(self):
        # 创建客户端对象，链接到MongoDB服务器
        # self.client = MongoClient(host, port)
        self.client = MongoClient() # 本机可省略
        # 获取要操作的集合
        self.collection = self.client['zwb']['t6']

    def insert_data(self):
        '''插入数据'''
        # 生成数据列表
        data_list = [{'_id': i, 'name': 'py{}'.format(i)} for i in range(1000)]
        # 向集合中插入多条数据
        self.collection.insert_many(data_list)

    def find_data(self):
        '''查询数据'''
        # 1.查询一条数据
        # self.collection.insert_one({'_id':1001, 'name':'py888'})
        s1 = self.collection.find_one({'name':'py100'})
        print(s1)

        # 2.查找全部数据：返回一个游标Cursor可迭代对象,但是只能够进行一次读取
        cursor = self.collection.find({'name':'py888'})
        for i in cursor:
            print(i)
        for i in cursor:
            print(i)

    def updata_data(self):
        '''更新数据'''
        # 1.更新一条数据
        self.collection.update_one({'name':'py555'}, {'$set':{'name':'new_py555'}})
        # self.collection.update_one({"name": "py666"}, {"$set": {"name": "new_py666"}})

        # 2.更新多条数据
        self.collection.update_many({'name':'py666'}, {"$set":{'name':'new_py666'}})

    def delete_data(self):
        '''删除数据'''
        # 1.删除一条数据
        self.collection.delete_one({'name':'py0'})

        # 2.删除多条数据
        self.collection.delete_many({'_id':1})

if __name__ == '__main__':
    test = MongoTest()
    # test.insert_data()
    test.find_data()
    test.updata_data()
    test.delete_data()