word_dict = {}
text = input("Enter your text: ")
list = text.strip(",").split()
for word in list:
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1
sort_keys = sorted(word_dict, key=word_dict.__getitem__, reverse=True)
for key in sort_keys:
    print("{:9s} -> {:2d}".format(key, word_dict[key]))