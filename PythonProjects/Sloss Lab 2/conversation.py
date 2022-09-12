"""DESCRIPTION OF THE MODULE GOES HERE

Author: Tyler Sloss
Class: CSI-160-03
Assignment: Week 2 Lab
Due Date:9/12/2022

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""


user_name = input('What is your name? ')  # Ask for user's name and reply to user
print('Nice to meet you ' + user_name + ' I am Deral.')
user_age = int(input('How old are you? '))  # Ask for user's age
favorite_game = input('What is your favorite game to play? ')  # Ask for user's favorite game
print('I have heard a lot about ' + favorite_game + ' before, but I have not played it.')
game_likes = input("What is your favorite aspect of the game? ")  # Ask why user likes the game
print("That is very interesting, I will have to play " + favorite_game + " sometime.")
years_playing = int(input('How many years have you been playing? '))

if years_playing >= 5:   # If user has been playing for 5 years or more reply with excitement
    print('Wow! That is a long time!')

game_lifetime = int(input('How long since the game launched? '))

if game_lifetime == years_playing:
    print('Wow! You were playing since ' + favorite_game + ' came out?!')

age_started_playing = int(input('At what age did you start playing? '))
age_since_start = user_age - age_started_playing   # subtract age from the age the user started playing game
print("Wow, its been " + str(age_since_start) + ' years since you started playing ' + favorite_game)
