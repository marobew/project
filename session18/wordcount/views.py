from django.shortcuts import render

def count(request):
    return render(request, 'wordcount/count.html')

def result(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split()
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            # count increase
            word_dict[word] += 1

        else:
            # add to the word_dict
            word_dict[word] = 1
    
    return render(request, 'wordcount/result.html', {'fulltext':full_text, 'total': len(word_list), 'dict':word_dict.items()})