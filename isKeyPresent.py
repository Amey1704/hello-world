#Write a Python script to check if a given key already exists in a dictionary.
d={1:10,2:20,3:30,4:40}
def is_key_present(x):
    if x in d:
        print('key is present in the dictionary')
    else:
        print('key is not present in the dictionary')
is_key_present(2)
is_key_present(7)        
