with open("E:\py practice\wordle\word_list.txt") as word_list:
    word_list = [word.rstrip() for word in word_list]

def frequency_dict():
    freq = {}
    for alphabet in list('abcdefghijklmnopqrstuvwxyz'):
        freq[alphabet] = 0
    for one in word_list:
        letters = list(one)
        for i in letters:
            freq[i] += 1
    freq_list = sorted(((value, key) for key, value in freq.items()), reverse=True)
    freq = dict((k,v) for v,k in freq_list)
    return freq

overall_freq = frequency_dict()

def suggest_best_words(list_of_words, overall_freq):
    word_fame = {}
    print('input', len(list_of_words))
    for word in list_of_words:
        word_weight = 0
        letters = list(word)
        # letters = list(set(letters))
        for i in letters:
            word_weight += overall_freq[i]
        word_fame[word] = word_weight
    print('output', len(word_fame))
    
    fame_tuple = sorted(((value, key) for key, value in word_fame.items()), reverse=True)
    word_fame = dict((k,v) for v,k in fame_tuple)
    return word_fame

# best_words = suggest_best_words(word_list, overall_freq)
# best_words = dict(list(best_words.items())[0:10])
# print(best_words)

def filtration(word, hint, look_into):
    filtered_words = []
    word = list(str(word))
    hint = list(str(hint))
    bad_letters, useful_letters = [], {}
    position = -1
    for letter, weight in zip(word, hint):
        position += 1
        if weight == '0':
            bad_letters.append(letter)
        elif weight == '2':
            useful_letters[str(position)] = letter
    for cur_word in look_into:
        unwanted_word = False
        list_of_letters = list(cur_word)
        if len(set(bad_letters).intersection(list_of_letters)) == 0:
            position = -1
            for letter, weight in zip(word, hint):
                position += 1
                for loc, cur_word_letter in enumerate(list_of_letters):
                    if (cur_word_letter == letter) and (loc == position):
                        unwanted_word = True
                        break
                if weight == '2':
                    if letter == list_of_letters[position]:
                        filtered_words.append(cur_word)
                elif weight == '1':
                    if letter in list_of_letters:
                        if letter == list_of_letters[position] and cur_word in filtered_words:
                            filtered_words.remove(cur_word)
                        elif letter != list_of_letters[position] and unwanted_word == False:
                            filtered_words.append(cur_word)
                    else:
                        if cur_word in filtered_words:
                            filtered_words.remove(cur_word)
                if len(useful_letters) > 0:
                    for k,v in useful_letters.items():
                        if  list_of_letters[int(k)] != v and cur_word in filtered_words:
                            # print('CHECKING=>', useful_letters[k], list_of_letters[int(k)])
                            # print(cur_word)
                            filtered_words.remove(cur_word)

    print('Total Useful Words:', len(filtered_words))
    famous_words = suggest_best_words(filtered_words, overall_freq)
    return famous_words

useful1 = filtration('arose', '20100', word_list)
useful2 = filtration('auloi', '20220', useful1)
# useful3 = filtration('altho', '22001', useful2)
# useful4 = filtration('allod', '22220', useful3)
# useful5 = filtration('alloy', '22220', useful4)
print(list(useful2.items())[:20])

best = ['soare', 'arose']
w = 'allow'