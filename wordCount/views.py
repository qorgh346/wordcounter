from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def result(request):
    data = request.GET['full_text']
    context = {'full_context':data}
    text = data.split(' ')
    word_dict = {}
    for word in text:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    context['text_length'] = len(text)
    context['result'] = word_dict.items()
    return render(request,'result.html',context)