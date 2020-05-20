from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'wordcount/home.html')

def about(request):
    return render(request, 'wordcount/about.html')

def count(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split() # full_text 띄어쓰기대로 나눠서 [이, 렇, 게, 저장]
    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    # word는 단어 종류
    # word_dictionary[word]는 그 단어의 개수

    return render(request, 'wordcount/count.html', {'fulltext': full_text, 'total':len(word_list), 'dictionary': word_dictionary.items()})
    # fulltext는 wordcount home에서 입력한 글자 저장
    # total은 전체 단어 개수

    
