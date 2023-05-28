# i have created this website 
from django.http import HttpResponse 
from django.shortcuts import render

# def index(request):
#     return HttpResponse("Hello")

# def about(request):
#     return HttpResponse("about")

# def lol(request):
#     return HttpResponse("<h1>Ram Ram </h1>")


# def index(request):
#     params = {'name': 'anushk' , 'place' : 'Mars'}
#     return render(request , 'index.html' , params)


def index(request):
    return render(request , "index.html")


def analyze(request):
    # get the data
    # djtext = request.GET.get('text' , 'default')
    # removepunc = request.GET.get('removepunc' , 'off')
    # fullcaps = request.GET.get('fullcaps' , 'off')
    # lower = request.GET.get('lower' , 'off')
    # removespace = request.GET.get('spaceremove' , 'off')
    # counter = request.GET.get('counter' , 'off')
    # newlineremover = request.GET.get('newlineremover' , 'off')
    djtext = request.POST.get('text' , 'default')
    removepunc = request.POST.get('removepunc' , 'off')
    fullcaps = request.POST.get('fullcaps' , 'off')
    lower = request.POST.get('lower' , 'off')
    removespace = request.POST.get('spaceremove' , 'off')
    counter = request.POST.get('counter' , 'off')
    newlineremover = request.POST.get('newlineremover' , 'off')
    # print(removepunc)

    
    # analyze the text

    # FOR REMOVING PUNCTUATION
    if(removepunc == 'on'):
        punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char


        # params = { 'purpose' : ' Remove Punctuation' , 'analyzed_text' : analyzed}
        djtext = analyzed
        
        # return render(request , 'analyze.html' , params)
    
    # FOR CAPITALIZING TEXT
    if(fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        # params = { 'purpose' : 'Capitalize' , 'analyzed_text' : analyzed}
        djtext = analyzed

        # return render(request , 'analyze.html' , params)

    # FOR LOWERCASE
    if(lower == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()

        # params = { 'purpose' : 'lower case' , 'analyzed_text' : analyzed}
        djtext = analyzed

        # return render(request , 'analyze.html' , params)
        
    # REMOVING THE SPACE
    if(removespace == 'on'):
        analyzed = ""
        for index , char in enumerate(djtext):
            if(djtext[index] == " " and djtext[index + 1] == " "):
                pass
            else:
                analyzed = analyzed + char

        # params = { 'purpose' : 'removing spaces' , 'analyzed_text' : analyzed}
        djtext = analyzed

        # return render(request , 'analyze.html' , params)

    # COUNTING THE CHARACTER
    if(counter == 'on'):
        count = 0
        for char in djtext:
            count = count + 1

        # params = { 'purpose' : 'counting character' , 'analyzed_text' : count}
        djtext = djtext + " " + str(count) 

        # return render(request , 'analyze.html' , params)

    # NEW LINE REMOVER
    if(newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if(char != '\n' and char != '\r'):
                analyzed = analyzed + char

        # params = { 'purpose' : 'removing new lines' , 'analyzed_text' : analyzed}
        djtext = analyzed

        # return render(request , 'analyze.html' , params)

    # else:
    #     return HttpResponse('Error')
    if(removepunc != 'on' and fullcaps != 'on' and lower != 'on' and removespace != 'on' and counter != 'on' and newlineremover != 'on'):
        return HttpResponse("ERROR - NO INPUT RECORDED")
    else:
        params = {'purpose' : 'all' , 'analyzed_text' : djtext}
        return render(request , 'analyze.html' , params)

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("Removes new line")

# def spaceremove(request):
#     return HttpResponse("Removes Spaces")

# def charcount(request):
#     return HttpResponse("count the character")