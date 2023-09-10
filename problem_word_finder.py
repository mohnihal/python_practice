test_input = ["Z<E","W<I","N<D","S<W","E<R","T<Z","L<A","A<N","I<T","R<L"]
# test_input = ["I<N","S<P","A<I","P<A"]

def wordFinder(input_list):
    word_length = len(test_input)+1
    word_list = ["?"]*word_length
    print (word_list)
    word_unique_set = set()
    starting_words = set()
    ending_words = set()
    word_dict = dict()
    for w in test_input:
        word_dict[w[0]]=w[2]
        starting_words.add(w[0])
        ending_words.add(w[2])
    word_list[0] = (starting_words-ending_words).pop()

    for i in range(word_length-1):
        word_list[i+1]=word_dict[word_list[i]]
    
    return "".join(word_list)


print (wordFinder(test_input))
