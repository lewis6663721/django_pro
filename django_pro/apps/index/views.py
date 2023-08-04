from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.generic import View


class Index(View):
    def get(self, request):

        return render(request, 'Index.html', {})

    def post(self, request):
        res = {
            "status": 0,
            "data": []
        }
        return JsonResponse(res)
