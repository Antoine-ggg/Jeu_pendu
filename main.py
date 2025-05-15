# Initialisation des constantes
CHANCE_INITIALE = 6
word = "cobalt"
hidden_word = "_" * len(word)

def main():
    life = CHANCE_INITIALE
    return

def perdre_vie(life):
    life -= 1
    return life

def is_letter(word, letter):
    for letters in word:
        print(str(letters))
        if letter == str(letters):
            hidden_word.replace("_", letter)
    return hidden_word

def initialisation_jeu(word):
    print(f"\t\t\t\t\t\t ______")
    print(f"\t\t\t\t\t\t|      |")
    print(f"\t\t\t\t\t\t|      ô")
    print(f"\t\t\t\t\t\t|      |")
    print(f"{hidden_word}\t\t\t\t  __|__")
    return

initialisation_jeu(word)

print(is_letter(word, "a"))