from typing import Any, Generator,Type
from elasticsearch import Elasticsearch
from elasticsearch.transport import Transport
import xlrd

class MyES(Elasticsearch):
    def __init__(self, hosts: Any, transport_class: Type[Transport] = Transport, **kwargs: Any) -> None:
        super(MyES,self).__init__(hosts=hosts, transport_class=transport_class, **kwargs)
        self.myid=0

    # get
    # index

    def readDataFromExcel(self, sheetnum: int) -> Generator[dict, None, None]:
        data = xlrd.open_workbook_xls(r"./bilibili.xls")
        table = data.sheets()[sheetnum]
        mydict = dict()
        for r in range(1,table.nrows):
            for c in range(table.ncols):
                key = table.cell_value(0,c)
                value = table.cell_value(r,c)
                mydict[key] = value
            yield mydict

    def inputData(self, index: str = "index", doc_type: str = "_doc") -> None:
        """
        从后缀名为'.xls'的Excel文件中读取数据（document）并添加到ES的索引（index）中
        """
        for dict in self.readDataFromExcel(0):
            body = dict
            self.index(index=index,doc_type=doc_type,body=body)

        '''
        是否要对 ID 设置一个全局变量之类的
        '''

    



