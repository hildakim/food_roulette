from django.shortcuts import render

# Create your views here.
def map(request):
    #food : 룰렛에서 받아온 메뉴명
    # food = request.GET.get('food') 
    food = '찌개'
    return render(request, 'map.html', {'food': food})