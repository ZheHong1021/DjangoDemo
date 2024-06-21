# 【用於欲顯示資料的數量及欄位】
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
class CustomPagination(PageNumberPagination):
    page_size = 30  # 默認每頁顯示的項目數
    page_size_query_param = 'page_size'  # 允許客戶端通過該參數自定義每頁大小
    max_page_size = 100  # 可以限制客戶端設置的最大每頁項目數


    def paginate_queryset(self, queryset, request, view=None):
        # 找尋 request.query_params中有無帶入 page_size
        page_size = request.query_params.get(self.page_size_query_param, self.page_size)
    
        if page_size == "-1": # 如果有帶且又是給 "-1" => 代表一頁帶入全部數據
            self.page_size = len(queryset)
        elif request.query_params.get("no_page", None): # 如果參數中包含 no_page: 代表不想要分頁效果
            return None
        else:
            self.page_size = int(page_size)
        return super().paginate_queryset(queryset, request, view)
    
    def get_paginated_response(self, data):
        return Response({
            'next': self.page.next_page_number() if self.page.has_next() else None,
            'previous': self.page.previous_page_number() if self.page.has_previous() else None,
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages, # 總頁數
            'data': data,  # 修改分页结果的键名为'data'
            'page': self.page.number,  # 当前页码
        })