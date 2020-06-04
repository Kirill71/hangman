import random


class Hangmen:
    title = "H A N G M A N"

    def __init__(self, words):
        self.words = words

    @staticmethod
    def __find_letter_indices(word, letter):
        indicies = []
        for i in range(len(word)):
            if word[i] == letter:
                indicies.append(i)
        return tuple(indicies)

    def play(self):
        MAX = 8
        word = random.choice(self.words)
        hidden = ["-"] * len(word)
        print(game.title)
        founded_letters = set()
        while True:
            print()
            print("".join(hidden))
            letter = input("Input a letter: ")
            if letter in founded_letters:
                print("No improvements")
                MAX -= 1
                continue

            indices = self.__find_letter_indices(word, letter)
            for idx in indices:
                hidden[idx] = letter
                founded_letters.add(letter)

            if len(indices) == 0:
                print("No such letter in the word")
                MAX -= 1

            if MAX == 0:
                print("You are hanged!")
                break

            if "-" not in hidden:
                print()
                print(word)
                print("You guessed the word!")
                print("You survived!")
                break


game = Hangmen(['python', 'java', 'kotlin', 'javascript'])
game.play()
