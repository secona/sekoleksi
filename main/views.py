from django.shortcuts import render

def show_main(request):
    return render(request, "main.html", {
        "name": "Muhammad Vito Secona",
        "npm": "2306152411",
        "class": "F",
    })
