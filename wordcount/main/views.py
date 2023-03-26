from django.shortcuts import render
import re
import string
# Create your views here.


def main(request):
    return render(request, 'main.html')


def about(request):
    return render(request, 'about.html')


def result(request):
    import re
    import string
    text = request.GET['text']
    text_list = text.split()
    print(text_list)

    regex = re.compile('[%s]' % re.escape(string.punctuation))

    original_length = len(text)
    length_without_spaces = len(text.replace(' ',''))

    text_dict = {}
    for word in text_list:
        if word in text_dict:
            text_dict[word] += 1
        else:
            text_dict[word] = 1
    words = sorted(text_dict.items(), key=lambda x: x[1], reverse=True)

    print(text_dict)
    return render(request, 'result.html', {"words": words, "original_length": original_length, "length_without_spaces": length_without_spaces})

