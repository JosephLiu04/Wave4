user_input = input("Enter word to be translated:\n")

vowels = ['a','e','i','o','u']
def translate(user_input): 
    first = user_input[0]

    if first in vowels: 
         user_input = user_input.lower()
         index_value = user_input.index
         user_input += user_input[index_value:] +user_input[:index_value] + "ay" 
         return user_input
    else: 
        user_input = user_input.lower()

        for letter in user_input:
            if letter in vowels:
                break

        user_input = user_input.lower()+ "way" 
        return user_input 

print(translate(user_input))