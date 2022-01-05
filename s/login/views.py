from typing import no_type_check_decorator
from django.http import response
from django.shortcuts import render, HttpResponse
from django.http.response import JsonResponse
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
# from elasticsearch import Elasticsearch

# es = Elasticsearch()

from .myes import MyES
es=MyES(["localhost:9200"])

def filter_msg(search_msg):
    body = {
        "query":{
            "match":{
                "标题":search_msg,
            }
        }
    }
    res = es.search(index="index",doc_type="_doc",body=body)
    # print(res)
    return res

def index(request):
    if request.method == 'POST':
        search_msg = request.POST.get("search_msg")
        res = filter_msg(search_msg)
        return JsonResponse(res)
    else:
        return render(request, 'index.html')


def es2(request):
    w2=es.search(index="index",
                doc_type="_doc",
                body={
                    "query":{
                        "match":{
                            "标题":"荒野求生"
                        }
                    }
                })
    print(w2)
    # es.indices.create(index='s18')
    return HttpResponse('OK')
