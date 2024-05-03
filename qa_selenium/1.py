# a = 5
# b = 10
# a = 20
# c = [1, 2, 3]
# print(a + b, c)
# a, b, c, d = 1, 2, 3, 4
# print(a, b, c, d) # комментарии
# a = "20"
# print(type(int(a)))
# print(int(a)+5)
# # my_str = input('Input 1 number: ')
# # print(my_str)
# my_str = 'Saint-Peterburg'
# print(my_str[-6:-1])  # erbur
# print(my_str[::-1]) # grubreteP-tniaS
# print(my_str[1:15]) #aint-Peterburg
# print(my_str[:]) #Saint-Peterburg
# print(my_str[-0]) #S
# print(my_str[0]) #S
# print(issubclass(str, my_str))

words_to_try_1 = ['listen', 'silent']
words_to_try_2 = ['насос', 'сосна', 'сосна']

def anagram(list_to_try):
    for i in range(len(list_to_try)):
        first = set(list_to_try[i])
        j = i + 1
        for j in range(len(list_to_try)):
            next = set(list_to_try[j])
            if first == next: # недоделала цикл
               

      next = set(list_to_try[j])
      if first == next:

                  

        return True
      
    else:
        return False

print(anagram(words_to_try_1))
print(anagram(words_to_try_2))