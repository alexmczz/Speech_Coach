from os import system
import os
import sys
import string
import animated_intro as animate
import time

#common filler words
commonFiller = [
    "um", "uh", "like", "you know", "well uhm", "so", "basically",
    "literally", "kind of", "sort of", "pretty", "really", "just", "I mean",
    "okay", "alright", "fine", "sure", "right", "hmm", "ah", "oh", "yeah",
    "uh-huh", "mmm", "hm", "wow", "oh my god", "oh dear", "oops", "uh-oh"
]

#takes external file entered after counter.py as parameter
usr_dock = sys.argv[1:]
user_dock = ','.join(usr_dock)
system('clear')
count = 0
totalCount = 0

translator = str.maketrans("", "", string.punctuation)

with open(f'{user_dock}', 'r') as f:
    current_filler_words =[]
    for line in f:
        words = line.split()  # Split the line into words
        for word in words:
            totalCount +=1
            
            word_without_punctuation = word.translate(translator)
            for filler in commonFiller:
                if word_without_punctuation.strip().lower() == filler.lower():
                    count += 1
                    current_filler_words.append(filler)

#gers percentafe of filler words throughout transcript
def percentage(): 
    if count == 0:
        return 0
    else:
        return round((count/totalCount)*100, 2)
        


def happy():
    print(f'count: {count}                                  {animate.clock()}')
    print('-----------------------------------------------------------------')  
    print('                  YAY!       /////////////////////////')
    print('      YAY!                   || Filler Word Counter ||')
    print('                             ||        great!       ||')
    print(f'        HECK      \O/        ||  {percentage}% || {count}/{totalCount}!    ||')
    print('            YEA!   |         ////////////////////////x')
    print('                  / \        |||||||||||||||||||||||x')
    print('-----------------------------------------------------------------')
    
    print("""
        This range is ideal for formal writing, academic papers, 
        professional documents, and speeches. It indicates a high level 
        of precision and clarity.
            """)


def couldBeBetter():
    print(f'count: {count}                                  {animate.clock()}')
    print('-----------------------------------------------------------------')
    print('                             /////////////////////////')
    print('      MEH                    || Filler Word Counter ||')
    print('                             ||        not bad      ||')
    print(f'                  O          ||  {percentage}% || {count}/{totalCount}!    ||')
    print('                  <|>        ////////////////////////x')
    print('                  / \        |||||||||||||||||||||||x')
    print('-----------------------------------------------------------------')
    
    print(f"""
        In less formal contexts, such as blog posts or opinion pieces, 
        a slightly higher percentage may be acceptable to maintain a 
        conversational tone. However, it's still important to use filler 
        words judiciously.
            
        Filler words used: {current_filler_words}
        """)
    

   


def doBetter():
    print(f'count: {count}                                  {animate.clock()}')
    print('-----------------------------------------------------------------')
    print('                             /////////////////////////')
    print('                             || Filler Word Counter ||')
    print('                             ||       uh oh!        ||')
    print(f'                   O         ||  {percentage}% || {count}/{totalCount}!    ||')
    print('                  /|\        ////////////////////////x')
    print('                  / \        |||||||||||||||||||||||x')
    print('-----------------------------------------------------------------') 

    time.sleep(5)
    animate.walk_away(percentage, count, totalCount)
    os.system('clear')
    print(f'count: {count}                                  {animate.clock()}')
    print('-----------------------------------------------------------------')
    print('      Tommato*               /////////////////////////')
    print('                             || Filler Word Counter ||')
    print(f'                 Tommato*    ||      uh oh!         ||')
    print(f' O/       BOO!               ||   {percentage}% ||   {count}/{totalCount}!  ')
    print('/|                           ////////////////////////x')
    print('/ \    Tommato*              |||||||||||||||||||||||x')
    print('-----------------------------------------------------------------')
    
    print(f"""
        A higher percentage of filler words may be acceptable in very 
        informal or personal writing, but it's crucial to strike a balance. 
        Too many fillers can make the writing seem less polished and can 
        detract from the message.
        
        Filler words used: {current_filler_words}
            """)

percentage = float(percentage())
animate.walking(percentage, count, totalCount)
print(f'count: {count}')
if percentage >= 0 and percentage <= 2:
    os.system('clear')
    happy()

elif percentage >= 3 and percentage <=5:
    os.system('clear')
    couldBeBetter()
    
else:
    os.system('clear')
    doBetter()
    
