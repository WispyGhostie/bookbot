def get_num_words(string_name):
    split_string = string_name.split() #spliting strings by their space
    num_words = len(split_string) #counting the total strings
    print(f"{num_words} words found in the document")
    

def get_character_use_count(string_name):
    reduce_character = string_name.lower() # makes the string lowercase
    char = {} # creates an empty dictionary
    for c in reduce_character:
        if c in char:  #this is checking the key c against char,
                        #will not work other way around
            char[c] += 1 #incrimenting by checking
        else:
            char[c] = 1 #initializing the first count
            
    dict_sort(char)

def dict_sort(book):
    lowest_val = float("-inf")
    if 
