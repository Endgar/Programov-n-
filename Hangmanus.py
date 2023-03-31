import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    pokus = 6
    print("Hrajeme ŠIBENICI!")
    print(display_hangman(pokus))
    print(word_completion)match
    print("\n")
    while not guessed and pokus > 0:
        guess = input("Hádej slovo nebo písmenko: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Už si hádal tohle písmenko!", guess)
            elif guess not in word:
                print(guess, "není ve slově :(.")
                pokus -= 1
                guessed_letters.append(guess)
            else:
                print("Dobrá práce,", guess, "je ve slově!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Už si hádal tohle slovo", guess)
            elif guess != word:
                print(guess, "není to slovo.")
                pokus -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(pokus))
        print(word_completion)
        print("\n")
    if guessed:
        print("Gratuluji, výhrál si!")
    else:
        print("HMM... Slovo bylo " + word + ". Možná příště vyhraješ!")


def display_hangman(pokus):
    stages = [  
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # hlavu, trup, obě paže a jednu nohu
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # hlavu, trup a obě paže
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # hlava, trup a jedna paže
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # hlavu a trup
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # hlava
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # nic
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[pokus]


def main():
    word = get_word()
    play(word)
    while input("Chceš hrát znova? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()