from django.shortcuts import render
from .models import List
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse

from django.urls import reverse
# Create your views here.
def index(request):
    obj_list = List.objects.all()
    if request.method == "POST":
        print("delete")
    for i in obj_list:
        print(i)
    print("리스트 작동")
    context = {"obj_list" : obj_list}
    return render(request, "list/list.html", context)

def create_list(request):
    print("만들기")
    if request.method == "POST":
        data = request.POST
        title = request.POST.get("title")
        category = request.POST.get("category")
        print(title)
        print(bool(title))
        print(category)
        List.objects.create(
            category = category,
            title = title,
            success = 0
        )
        return redirect('/list/')
    return render(request, "list/create_list.html")


def delete_list(request, list_id):
    print(list_id)
    cut_list = List.objects.get(id=list_id)
    print("delete")
    print(cut_list)
    cut_list.delete()
    obj_list = List.objects.all()
    context = {"obj_list": obj_list}
    return redirect('/list/')


def list_config(request, list_id):
    print(f"Received list_id: {list_id}")  # list_id를 출력합니다

    if request.method == "POST":
        success_value = request.POST.get('success')
        print(f"Received success value: {success_value}")  # 입력된 success 값을 출력합니다
        try:
            success_value = int(success_value)  # 문자열을 숫자로 변환
        except ValueError:
            return HttpResponse("Invalid success value", status=400)


        list_item = get_object_or_404(List, id=list_id)
        list_item.success = success_value
        list_item.save()
        return redirect('/list/')  # 원하는 URL로 변경합니다

    return HttpResponse(status=405)  # POST 요청이 아닌 경우 405 에러를 반환합니다
