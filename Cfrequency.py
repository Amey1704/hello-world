#Write a Python program to count the number of characters (character frequency) in a string.
def char_frequency(string1): 
    dict = {}
    for n in string1:
        keys= dict.keys()
        if n in keys:
            dict[n] += 1
        else: 
            dict[n] = 1
    return dict
print(char_frequency("codekul.com"))            

        