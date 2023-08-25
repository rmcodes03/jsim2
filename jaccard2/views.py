from django.shortcuts import render

def jaccard_sim(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = len(set1.intersection(set2))
    print(intersection)
    union = len(set1) + len(set2) - intersection
    print(union)
    if union == 0:
        return 0.0
    return intersection / union
'''
def generate_shingle_word(text, k):
    shingles = []
    words = text.split()
    if len(text)<k:
        return shingles
    for i in range(len(words)- k+1):
        shingle = ' '.join(words[i : i+k])
        shingles.append(shingle)
    return shingles
'''
def generate_shingle_character(text, k):
    shingles = []
    if len(text)<k:
        return shingles
    for i in range(len(text)- k+1):
        shingle = ''.join(text[i : i+k])
        shingles.append(shingle)
    return shingles

def homepage(request):
    return render(request, 'home.html')

def count(request):
    wordtext1 = request.GET['wordtext1']
    wordtext2 = request.GET['wordtext2']
    try:
        k = int(request.GET['shingle'])
    except ValueError:
        return render(request, 'error.html')
    
    #shingles1 = generate_shingle_word(wordtext1, k)
    #shingles2 = generate_shingle_word(wordtext2, k)

    shingles1 = generate_shingle_character(wordtext1, k)
    shingles2 = generate_shingle_character(wordtext2, k)
    #print(shingles1)
    #print(shingles2)
    jsim = jaccard_sim(shingles1, shingles2)
    jdis = 1 - jsim
    #print("Jaccard Similarity: ", jsim)
    #print("Jaccard Distance: ", 1-jsim)
    if len(wordtext1)==0 or len(wordtext2)==0:
        return render(request, 'error.html')
    else:
        return render(request, 'output.html', {'text1' : set(shingles1) , 'text2' : set(shingles2) , 'jsim' : jsim, 'jdis': jdis})

def about(request):
    return render(request, 'error.html')