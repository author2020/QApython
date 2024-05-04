
# my_str = input('Input the phrase "Привет человек, меня зовут Кот": ')
# print(len(my_str),  my_str[::], my_str.replace('Кот', 'кот'))

# Напишите функцию которая будет принимать две строки и возвращать True если они будут является анаграммами друг друга и False в противном случае

def anagram(str_1, str_2):
    word_1 = set (str_1)
    word_2 = set (str_2)
    if word_1 == word_2 and len(str_1) == len(str_2):
        return True
    else:
        return False

print(anagram('listen', 'silent'))
print(anagram('сосна', 'насос'))
print(anagram('listen', 'ssilent'))
