from django.http import HttpResponse
from django.shortcuts import render

def test_view(request):
    return HttpResponse("Test")

def test_view_hello(request):
    return HttpResponse("Hello", status=500)


def test_view_bye(request):
    return HttpResponse("Goodbye")

# def test_view(request):
#     my_list = [1, 2, "3", 4]
#     return HttpResponse("Test")

# def test_view(request):
#     html = """<!DOCTYPE html> 
# <html lang="ru"> 
#    <head> 
#       <meta charset="UTF-8"> 
#       <title>HTML Document</title> 
#    </head> 
#    <body> 
#       <p> 
#          <b> 
#             Этот текст будет полужирным, <i>а этот — ещё и курсивным lfkb</i>. 
#          </b> 
#       </p>     
#    </body> 
# </html>"""
#     return HttpResponse(html)

# def test_view(request):
#     my_list = [1, 2, "3", 4]
#     headers = {"Name": "Aza"}
#     return HttpResponse(my_list, headers=headers, status=404)

def catch_number_view(request, number):
    return HttpResponse(f"Your number: {number}")


def catch_string_view(request, string):
    return HttpResponse(f"Your string: {string}")