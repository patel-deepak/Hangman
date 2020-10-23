

from IMAGES import images



print("  ----- ------------ * * Welcome to Hangman Game man !! * *--------------\n")
print("Please try to save Life of man form hanging ?   By guessing right word \n")
# Print("In this game you have to guess the word by guessing it's word one by one :\n")
print("Total Lives you will get 8  If you will loose those your game will be over \n")
print()
# print(word)
print()

def play_again():
    
    user=input("Ops You Loose the Game :-   Do you want to play again ----   Y/N ").lower()
    if user=="y":
        play_game()
    else:
        return ("  Hope you enjoyed a lot:-  \n               Thanks.Dear!\n                              made by DEEPAK PATEL  ")

# def play_game():
#     from word1 import word
#     l=len(word)
#     print("Your word contains   ",l," ","__ "*l,"Letters")
#     guessed=False
#     tries=7
#     letters_guessed=[]
#     abc="abcdefghijklmnopqrstuvwxyz"
#     while guessed==False and tries>=0:
#         print("You are left with  "+str(tries)+"  Lives")
#         guess=input("\tGuess a letter or a word:-  ")
#         if len(guess)==1:
#             #If you guess a letter!
#             if guess not in abc:
#                 print("You have not guessed the Letters Yet! ")
#             elif guess in letters_guessed:
#                 print("Sorry! You have already guessed this letter before!")
            
#             elif guess in word:
#                 print("************************************************")
#                 print("* * Well Done! You have Guessed the right letter !* *")
#                 print("_________________________________________________")
#                 letters_guessed.append(guess)
#             elif guess not in word:
#                 images(tries)
#                 print("Letter Entered by you does not Exists in the word:-")
#                 print()
#                 tries-=1
#             else:
#                 print("Server Error! Plz Try Again!")
#       #If user guess word:----------------------------
#         elif len(guess)==len(word):
#             if guess==word:
#                 print("<<<<<<<<<-=->>>>>>>>>-=-<<<<<<<<<-=->>>>>>>>>")
#                 print("Well Done! You have Guessed the right Word !")
#                 print("_________________________________________________")
#                 guessed=True
#             else:
#                 print("The lenght of the word is not the word we're looking for")
#         status=""
#         if guessed==False:
#             for letter in  word:
#                 if letter in letters_guessed:
#                     status+=letter
#                 else:
#                     status+="__"
#             print()
#             print("\t",status)
#             print()
#             if len(word)==len(status):
#                 guessed=True
#                 print("<<<<<<<<<-=->>>>>>>>>-=-<<<<<<<<<-=->>>>>>>>>")
#                 print("Well Done! You have Guessed the right Word !")
#                 print("_________________________________________________")

    
#             elif tries==0:
#                 guessed=True
#                 images(tries)
#                 print("You are left with no more tries :" )
#                 print("you wasn't able to save the man   !!!",word)
#                 play_again()
                


# play_game()


