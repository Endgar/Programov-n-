import random
from words import list_slov


def get_word():
    slovo = random.choice(list_slov)
    return slovo.upper()


def play(slovo):
    word_completion = "_" * len(slovo)
    guessed = False
    guessed_letters = []
    guessed_words = []
    pokus = 6
    print("Hrajeme ŠIBENICI!")
    print(display_hangman(pokus))
    print(word_completion)
    print("\n")
    while not guessed and pokus > 0:
        guess = input("Hádej slovo nebo písmenko: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Už si hádal tohle písmenko!", guess)
            elif guess not in slovo:
                print(guess, "není ve slově :(.")
                pokus -= 1
                guessed_letters.append(guess)
            else:
                print("Dobrá práce,", guess, "je ve slově!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(slovo) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(slovo) and guess.isalpha():
            if guess in guessed_words:
                print("Už si hádal tohle slovo", guess)
            elif guess != slovo:
                print(guess, "není to slovo.")
                pokus -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = slovo
        else:
            print("Not a valid guess.")
        print(display_hangman(pokus))
        print(word_completion)
        print("\n")
    if guessed:
        print("Gratuluji, výhrál si!")
    else:
        print("HMM... Slovo bylo " + slovo + ". Možná příště vyhraješ!")


def display_hangman(pokus):
    obraz = [  
                """
                   +=======
                   |      |
                   |      0
                   |     \\|/
                   |      |
                   |     / \\
                =========
                """,
                # hlavu, trup, obě paže a jednu nohu
                """
                   +=======
                   |      |
                   |      0
                   |     \\|/
                   |      |
                   |     / 
                =========
                """,
                # hlavu, trup a obě paže
                """
                   +=======
                   |      |
                   |      0
                   |     \\|/
                   |      |
                   |      
                =========
                """,
                # hlava, trup a jedna paže
                """
                   +=======
                   |      |
                   |      0
                   |     \\|
                   |      |
                   |     
                =========
                """,
                # hlavu a trup
                """
                   +=======
                   |      |
                   |      0
                   |      |
                   |      |
                   |     
                =========
                """,
                # hlava
                """
                   +=======
                   |      |
                   |      0
                   |    
                   |      
                   |     
                =========
                """,
                # nic
                """
                   +=======
                   |      |
                   |      
                   |    
                   |      
                   |     
                =========
                """
    ]
    return obraz[pokus]


def main():
    slovo = get_word()
    play(slovo)
    while input("Chceš hrát znova? (Y/N) ").upper() == "Y":
        slovo = get_word()
        play(slovo)


if __name__ == "__main__":
    main()