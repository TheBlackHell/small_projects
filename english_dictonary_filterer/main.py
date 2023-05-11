import codecs

filename = "german_word_list.txt"

with codecs.open(f"english_and_german_words/{filename}", "r", "utf-8") as words: 
    wordlist = words.read().lower().split(sep="\n")

with codecs.open("english_and_german_words/output.txt", "w", "utf-8") as output:
    filtered_words = list(filter(lambda x: x.__contains__("vergewaltigung"), wordlist))         
    for word in filtered_words:
        output.write(f"{word}\n")

#for index, item in enumerate(filtered_words):   
#    with codecs.open(f"german_words/output/output{index}.txt", "w", "utf-8") as f:
#        f.write(f"{item}")
