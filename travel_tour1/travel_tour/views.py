from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from travel_tour.models import Tour, Tag, Category

def main(request):
    tours = Tour.objects.all()

    search_query = request.GET.get('search')
    if search_query:
        tours = tours.filter(Q(name__icontains=search_query) | Q(category__name__icontains=search_query) | Q(tags__name__icontains=search_query)).distinct()

    category_id = request.GET.get('category')
    if category_id:
        category = Category.objects.get(id=category_id)
        tours = tours.filter(category=category)


    tag_id = request.GET.get('tag')
    if tag_id: 
        tag = Tag.objects.get(id=tag_id)
        tours = tours.filter(tags=tag)
        

    paginator = Paginator(tours, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    tags = Tag.objects.all()

    return render(request, 'index.html', {'page_obj': page_obj, 'tags': tags})



def detail_tour(request, id):
    tour = Tour.objects.get(id=id)
    return render(request, 'detail_tour.html', {'tour': tour})


