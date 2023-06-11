# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import MindMap


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def main(request):
    # mindmaps = MindMap.objects.order_by('big_label', 'created_at')
    # mindmap_with_index =  [(index, mindmap) for index, mindmap in enumerate(mindmaps)]
    
    mindmaps_raw = MindMap.objects.order_by('big_label', 'small_label', 'contents', 'created_at')
    
    big_label_dict = {}
    for mindmap in mindmaps_raw:
        if mindmap.big_label not in big_label_dict:
            big_label_dict[mindmap.big_label] = {}
        if mindmap.small_label not in big_label_dict[mindmap.big_label]:
            big_label_dict[mindmap.big_label][mindmap.small_label] = []
        big_label_dict[mindmap.big_label][mindmap.small_label].append(mindmap.contents)

    mindmap_with_index =  [(index, big_label, small_label_dict.items()) for index, (big_label, small_label_dict) in enumerate(big_label_dict.items())]
    
    context = {
        'mindmap': mindmap_with_index,
    }

    return render(request, 'pang/pang.html', context)
