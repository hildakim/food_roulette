from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request, "menu.html")

def menu_roulette(request, menu_id):
    menu = ['fastfood', 'westernfood', 'koreanfood', 'chinesefood', 'japanesefood']
    urls = menu[menu_id] + ".html"
    return render(request, urls)

