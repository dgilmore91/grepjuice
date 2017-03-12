def generate_bigrams_list(sentence):
    words_list = sentence.split(" ")
    bigrams_list = []
    for index, word in enumerate(words_list):
        if index <= len(words_list) - 2:
            bigram = [word, words_list[index + 1]]
            bigrams_list.append(bigram)
    return bigrams_list
