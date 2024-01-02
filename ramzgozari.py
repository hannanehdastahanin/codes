def m_word(word):
    if word[0] in ['a', 'e', 'i', 'o', 'u']:
        kalame = word[1:] + word[0] + 'v'
    else:
        kalame = word[2:] + word[:2]
    return kalame
def m_sentence(sentence):
    words = sentence[:-1].lower().split() 
    modified_words = [m_word(word) for word in words]
    jomle = ' '.join(modified_words) + '.'
    return jomle
input_sentence = input("Enter a sentence: ")
x = m_sentence(input_sentence)
print(x)
