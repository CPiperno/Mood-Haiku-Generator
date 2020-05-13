"""
Literature in the Age of AI Final Project
Clelia Piperno & Giselle Valdez

Mood Haiku Poem Generator


Coded By : Clelia
"""

import random


def read_syllables(filename):
        
    file = open(filename, 'r') 
    
    #creates a dictionary to store syllables
    syllables = dict()

    for line in file:
        line = line.strip().lower()
        
        words = line.split(",")
        
        key = words[0]
        
        if key not in syllables:
            syllables[key] = words[1:]
        else:
            syllables[key].append(words[1:])
     
        
    return syllables


    
def read_moods(filename):
    
    file = open(filename, 'r') 
    
    #creates a dictionary to store moods
    moods = dict()

    for line in file:
        line = line.strip()
        
        words = line.split(",")
        
        key = words[0]
        
        if key not in moods:
            moods[key] = words[1:]
        else:
            moods[key].append(words[1:])
     
    return moods
    

    
def user_mood_selection(m):
    
    print("select a ~mood~")
    
    #stores moods which can later be indexed according to user input
    moods = []
    index = 1
    
    for item in moods_dict.keys():
        moods.append(item)
        print(index, ":", item)
        index += 1
    
    #user input -- adjusts for 0 index
    user = input ("choice : ")
    index = int(user) - 1
    
    #accounts for out of bounds errors in user input
    while (index == -1) or (index > len(moods)) :
        print("\nsorry, the mood you have selected is not valid.")
        print("please select a number between 1 and", len(moods), ".")
        user = input ("\nchoice : ")
        index = int(user) - 1
    
    return (moods[index])
    

def mood_theme_generator(s, m, mood):
    
    syllables = set()
    moods = set()
    
    theme = dict()
    it = 1
    
    #creates set storing mood chosen
    for item in m[mood]:
        moods.add(item)

    #correctly classifies syllables of mood choosen
    #takes intersection of the sets (moods and syllables) and stores as new dictionary (theme)
    for syllable in s.values():
        for word in syllable:
            syllables.add(word)
        
        intersection = moods.intersection(syllables)
        theme[it] = list(intersection)
        
        syllables.clear()
        it += 1
        
    return theme
    
    
def haiku(m):
    
    #syllables in respective haiku lines
    haiku_form = {1:5, 2:7, 3:5}


    word_index = set()
    
    
    haiku = dict()
    haiku_line = []
    line_count = 1
    
    
    #generates each line in haiku sequentially and individually
    for line_syl in haiku_form.values():
        while line_syl > 0:
            if line_syl >= 3:
                dict_index = random.randint(1,3)
            else:
                dict_index = random.randint(1, line_syl)
                
            elem_index = random.randint(0, len(m[dict_index])-1)
            
            #ensures words do not get selected twice and are thus unique
            ID = str(dict_index) + str(elem_index)
            if ID not in word_index:
                word_index.add(ID)      
            else:
                while ID in word_index:
                    if line_syl >= 3:
                        dict_index = random.randint(1,3)
                    else:
                        dict_index = random.randint(1, line_syl)
                    
                    elem_index = random.randint(0, len(m[dict_index])-1)
                
                    ID = str(dict_index) + str(elem_index)
                    
                word_index.add(ID)
                
            #adds word selection to haiku and adjusts syllable counter
            haiku_line.append(m[dict_index][elem_index])
            line_syl -= dict_index


        #saves generated line as respective line in haiku
        #clears set storing line so it can be reused -- word_index not cleared to ensure words are unique
        haiku[line_count] = haiku_line
        haiku_line = []

        line_count += 1

    return haiku


def print_haiku(h, mood):
    
    print ("\nyour ~{0}~ haiku".format(mood))

    for line in h.values():
        count = 0
        
        while count < len(line):
            if count == len(line) - 1:
                print (line[count])
            else:
                print (line[count], "/ ", end="", flush=True)
                
            count += 1

    


if __name__ == "__main__":
    
    filename_syllables = "Syllables.csv"
    filename_moods = "Moods.csv"
    
    #reads in data
    syllables_dict = read_syllables(filename_syllables)
    moods_dict = read_moods(filename_moods)
    
    #mood selection
    mood = user_mood_selection(moods_dict)
    mood_themes = mood_theme_generator(syllables_dict, moods_dict, mood)
    
    #generates and prints haiku
    haiku = haiku(mood_themes)
    print_haiku(haiku, mood)
    
    
    
    
    
