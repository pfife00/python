# Find matching words in given string
text = "Python is a great programming language. I love coding in Python!"
word_list = ["Python", "Java", "coding", "Ruby", "programming"]
res_list = []

def find_matching_words(text, word_list):
    text_set = set(text.split())
    res_list.append([word for word in word_list if word in text_set])
    return res_list
    

print(find_matching_words(text, word_list))