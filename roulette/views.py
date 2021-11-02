from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request, "menu.html")

def menu_roulette(request, menu_id):
    menu = ['fastfood', 'westernfood', 'koreanfood', 'chinesefood', 'japanesefood']
    urls = menu[menu_id] + ".html"
    return render(request, urls)

def map(request, food):
    #food : 룰렛에서 받아온 메뉴명
    menu = food
    #food = '찌개'
    return render(request, 'map.html', {'menu': menu})

