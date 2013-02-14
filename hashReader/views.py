from django.shortcuts import render_to_response

def root_page(request):
    return render_to_response('hashreader.html', {})
