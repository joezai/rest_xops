from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10  # 定义每页多少条
    page_size_query_param = 'pagesize'  # 定义url 每页条数的参数名
    page_query_param = 'page'  # 定义 url 第几页的参数名
    max_page_size = 100

