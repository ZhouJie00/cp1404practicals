def count_word_occurrences():
    user_input = input("Enter a string: ")
    words = user_input.split()
    word_list = {}

    # add in the words
    for thing in words:
        if thing in word_list:
            word_list[thing] += 1
        else:
            word_list[thing] = 1


    # Find length of the longest word that is inside the list
    width = max(len(word) for word in word_list.keys())

    # Print the word counts in descending order
    for word, other_thing in sorted(word_list.items()):
        print(f"{thing:{width}} : {other_thing:}")


count_word_occurrences()