from myes import MyES


es=MyES(["localhost:9200"])
# a=es.get(index="test1",doc_type="_doc",id=4,filter_path=["_source"])
# print(a)
es.inputData()