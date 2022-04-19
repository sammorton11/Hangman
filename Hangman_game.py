import random

hangmanpics = ['''
 +---+

   |   |

       |

       |

       |

       |

 =========''', '''



   +---+

   |   |

   O   |

       |

       |

       |

 =========''', '''



   +---+

   |   |

   O   |

   |   |

       |

       |

 =========''', '''



   +---+

   |   |

   O   |

  /|   |

       |

       |
 =========''', '''

   +---+

   |   |

   O   |

  /|\  |
       |
       |

 =========''', '''



   +---+

   |   |

   O   |

   /|\  |

   /    |

        |

  =========''', '''



   +---+

   |   |

   O   |

  /|\  |

  / \  |

       |

=========''']


print('Welcome to Hangman')

counter = 7

word_list = ['dab', 'hello', 'weed', 'maty']
random_word = random.choice(word_list)
word_length = len(random_word)

display = []

for letter in random_word:
    display += '_'
print(display)

end_of_game = False

while not end_of_game:
    
    user_guess = input("guess a letter: ").lower()
    for position in range(word_length):
        letter = random_word[position]
        if letter == user_guess:
            display[position] = letter
            print("Lives:", counter)
            print(display)
         

    if user_guess not in display and user_guess != random_word:
        counter -= 1
        #print("Lives:", counter)
        #print(display)
    #print(display)

    if counter == 6:
        print(hangmanpics[0])
        print("Lives:", counter)
        print(display)
    if counter == 5:
        print(hangmanpics[1])
        print("Lives:", counter)
        print(display)
    if counter == 4:
        print(hangmanpics[2])
        print("Lives:", counter)
        print(display)
    if counter == 3:
        print(hangmanpics[3])
        print("Lives:", counter)
        print(display)
    if counter == 2:
        print(hangmanpics[4])
        print("Lives:", counter)
        print(display)
    if counter == 1:
        print(hangmanpics[5])
        print("Lives:", counter)
        print(display)
    

    if '_' not in display or user_guess == random_word:
        display = []
        display += random_word
        print(display)
        print(f"You Win! Word: {random_word} Lives: {counter}")
        end_of_game = True
        break

    if counter == 0:
        display = []
        display += random_word
        print(display)
        print(f"You Died! Word: {random_word} Lives: {counter}")
        end_of_game = True
        break
    
