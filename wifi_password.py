import random

def generate_password(sentence, min_length = 3):
    words = sentence.split()
    special_chars = '%$&()'
    password = ''
    if len(words) < min_length:
        raise AttributeError('zu wenige woerter')
    for word in words:
        special_char_index = random.randint(0,len(special_chars)-1)
 #       if word[0] == 'x':
 #           continue
        password += word[0] #+ \
                    #str(random.randint(0,9)) + \
                    #special_chars[special_char_index]
    return password