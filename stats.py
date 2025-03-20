def get_num_words(string_name):
    split_string = string_name.split() #spliting strings by their space
    num_words = len(split_string) #counting the total strings
    print(f"Found {num_words} total words")
    

def get_character_use_count(string_name):
    reduce_character = string_name.lower() # makes the string lowercase
    char = {} # creates an empty dictionary
    for c in reduce_character:
        if c in char:  #this is checking the key c against char,
                        #will not work other way around
            char[c] += 1 #incrimenting by checking
        else:
            char[c] = 1 #initializing the first count
    return char


def sort_on(dict):
    return dict["count"]

def dict_sort(book):
    # Create an empty list to hold our dictionaries
    da_list = []
    # Convert each character and count to a dictionary and add to list
    for x, count in book.items():
        if x.isalpha():
            # What key-value pairs should each dictionary have?
            da_char = {"char": x, "count": count}
            da_list.append(da_char)

    da_list.sort(reverse=True, key=sort_on)
    # Sort the list based on count values
    # How would you sort from greatest to least?
    
    for x in da_list:
        print(f"{x['char']}: {x['count']}")

