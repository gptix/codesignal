def differ_by_one_letter(w1, w2):
#     print(f'w1: {w1}, w2 {w2}')
    diffs = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            diffs += 1
            if diffs == 2:
                return False
    if diffs != 1:
        return False
    return True

def mk_diff_by_1_dict(wrd_list):
    # make set for fast lookup
    words_set = set(wrd_list)

    # make dict to store neighbors for each word
    diff_one_letter = {}

    # make a kv pair for each word
    for word in words_set:
        diff_one_letter[word] = set()

    # for each word, update list of near matches
    for word in words_set:
        for w in words_set:
            # do not match a word to itself (this test avoids running function)
            if not word == w and differ_by_one_letter(word, w):
                diff_one_letter[word].add(w)
                diff_one_letter[w].add(word)

    # remove entries for words with no near matches
    no_diff_by_ones = [word for word, sett in diff_one_letter.items() if sett == set()]
    for n in no_diff_by_ones:
        del diff_one_letter[n]
        
    return diff_one_letter
        
def wordLadder(beginWord, endWord, wordList):
    
    # print(wordList.append(beginWord))
    wordList.append(beginWord)
    word_next_word_dict = mk_diff_by_1_dict(wordList)
    if len(word_next_word_dict) == 0:
        return 0
    # print(wordList)
    # make a queue
    q = []
    
    # initialize queue
    # print(f'1- q is now {q}')
    q.append([beginWord])
    
    # coduct search
    while len(q) > 0:
        # print(f'2- q is now {q}')
        
        word_path = q.pop(0)
        this_word = word_path[-1]
        # print(f'This word: {this_word}')
        # test for success
        
        if this_word == endWord:
            return len(word_path)
            
        # find neighbors
        # do not go backwards
        visited = set(word_path)
        # print(this_word)
        if this_word in word_next_word_dict:
            words_to_use = word_next_word_dict[this_word] - visited
            
            # push neighbors (word paths) onto queue
            for w in words_to_use:
                path_copy = word_path.copy()
                path_copy.append(w)
                q.append(path_copy)
            
    return 0

foo = wordLadder("talk", "tail", ["talk", 
 "tons", 
 "fall", 
 "tail", 
 "gale", 
 "hall", 
 "negs"])
print(foo)