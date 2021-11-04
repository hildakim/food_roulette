from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request, "roulette.html")

def menu_roulette(request, menu_id):
    menu = ['korean','chinese','japanese','western','fastfood']
    urls = menu[menu_id] + "_roulette.html"
    return render(request, urls)

def map(request, food):
    #food : 룰렛에서 받아온 메뉴명
    return render(request, 'map.html', {'menu': food})

