from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'wordcount/home.html')

def about(request):
    return render(request, 'about/about.html')

def count(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split()
    word_dictionary={}
    total = len(full_text)
    for word in word_list:
        if word in word_dictionary:
            # Increase
            word_dictionary[word] += 1
        else:
            # add to the dictionary
            word_dictionary[word] = 1
    return render(request, 'count/count.html', {'fulltext':full_text, 'wordlist':word_list, 'dictionary':word_dictionary.items(), 'total':total})