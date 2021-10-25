# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import xlwt

class LoginPipeline:
    # 构造方法
    def __init__(self):
        self.fp = None  # 定义一个文件描述符属性
        self.sheet = None
        self.title = None
        self.index = 0

    # 开始爬虫时，执行一次
    def open_spider(self, spider):
        print('爬虫开始')
        self.fp = xlwt.Workbook(encoding="utf-8", style_compression=0)
        self.sheet = self.fp.add_sheet('sheet1', cell_overwrite_ok=True)
        # self.fp = open('./data.csv', 'w')
        self.title = ['Requester','Title','HITs','Reward','Created','Actions', 'Description', 'TimeAllotted', 'Expires']
        for i in range(len(self.title)):
            self.sheet.write(0, i, self.title[i])
        self.index = 1

    def process_item(self, item, spider):
        # 将爬虫程序提交的item进行持久化存储
        for i in range(len(self.title)):
            self.sheet.write(self.index, i, item[self.title[i]])
        self.index += 1
        return item
 
    # 结束爬虫时，执行一次
    def close_spider(self, spider):
        self.fp.save('worker-mturk-data.xls')
        print('爬虫结束')