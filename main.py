# Importation de la bibliothèque random
import random


# Initialisation des constantes et variables globales
life = 6
answer = ""
answer_hidden = ["_"] * len(answer)
clue = False


# Ceci est la fonction d'execution principale
def main(file = "mots_pendu.txt"):
    global answer, answer_hidden, clue
    replay_check = "O"

    # Tant que le vérificateur de replay est à oui, on boucle
    while replay_check == "O":
        used_letter_list = []
        answer = delete_accent(word_selection(file))
        print(answer) # Affiche la réponse pour tester le programme
        answer_hidden = ["_"] * (len(answer))
        game_initialisation(list_to_string(answer_hidden))

        # On boucle tant que les tentatives sont supérieurs à 0 ET que la fonction check_word retourne faux
        while life > 0 and check_for_underscore() == False:
            # On vérifie si l'utilisateur rempli les conditions pour recevoir un indice
            if life == 1 and clue == False and answer_hidden.count("_") > 1:
                give_clue()
            guess_letter(used_letter_list)

        # On vérifie si l'utilisateur gagne ou s'il perd
        if check_for_underscore() is True:
            print_win()
        else:
            print_lose()

        # On demande à l'utilisateur s'il veut rejouer
        replay_check = replay()
    return


# Cette fonction transforme une liste de lettre en str
def list_to_string(word):
    word_str = ""
    for letters in word:
        word_str += letters
    return word_str


# Cette fonction sélectionne un mot aléatoire selon le fichier choisi par l'utilisateur
def word_selection(file):
    with open(file, "r", encoding='utf-8') as word_list:
        lines = word_list.readlines()
    num = random.randrange(len(lines))
    return lines[num].strip()


# Cette fonction remplace les lettres avec des accents par des lettres simples.
def delete_accent(word_accent):
    word = list(word_accent)
    for i in range(len(word)):
        if word[i] in ("à","â","ä"):
            word[i] = "a"
        elif word[i] in ("é","è","ê","ë"):
            word[i] = "e"
        elif word[i] in ("î","ï"):
            word[i] = "i"
        elif word[i] in ("ô", "ö"):
            word[i] = "o"
        elif word[i] in ("ù","û"):
            word[i] = "u"
    return list_to_string(word)


# Cette fonction initialise le jeu
def game_initialisation(word):
    print(f"\n\nBienvenue au jeu du pendu. Un mot aléatoire a été sélectionner et votre but est de le trouver.\n"
          f"Dites moi une lettre et je vous dirais si elle est présente dans le mot recherché.\n"
          f"Le mot contient {len(word)} lettres et vous possédez {life} tentatives.\n"
          f"{list_to_string(answer_hidden)}\n")
    return


# Cette fonction enlève une tentatives à l'utilisateur.
def lose_life():
    global life
    life -= 1
    return


# Cette fonction vérifie si l'entrée est une lettre minuscule et si elle est dans le mot.
def guess_letter(letter_list):
    check = False
    letter = "A"
    letter_list_check = True

    # Boucle qui vérifie que l'entrée est valide
    while (letter.isascii() is False or letter.islower() is False or len(letter) > 1) or letter_list_check is True:
        letter_list_check = False
        letter = str(input(f"\nVoici la liste des lettres déjà jouer : {letter_list}\n"
                           f"Choisissez une lettre que le mot pourrait contenir : "))
        if len (letter) > 1:
            print(f"\n L'entrée {letter} est plus qu'un caractère. Veuillez entrée une seule lettre minuscule")
        elif letter.isnumeric() is True:
            print(f"\nL'entrée {letter} est un chiffre. L'entrée doit être une lettre !")
        elif letter.isupper() is True:
            print(f"\nL'entrée doit être une minuscule !")
        elif letter.isalnum() is False:
            print(f"\nL'entrée {letter} est un caractère spécial. Veuillez entrée une lettre minuscule du format ASCII !")
        elif letter in letter_list:
            print(f"\nLa lettre {letter} a déjà été nommée. Veuillez en choisir une autre")
            letter_list_check = True
        else:
            letter_list.append(letter)

    # Boucle qui vérifie si la lettre entrée est dans la réponse et mets à jour la
    for i in range(len(answer)):
        if answer[i] == letter:
            answer_hidden[i] = letter
            check = True

    # Si le check passe, la console affiche un message qui confirme que la lettre est dans le mot, puis on retourne au main
    if check is True:
        print(f"\nBien joué ! La lettre {letter} est présente dans le mot recherché: {list_to_string(answer_hidden)}"
              f"\nIl vous reste {life} tentatives).\n")

    # Sinon, la console affiche un message qui infirme que la lettre est dans le mot, puis on retourne au main
    else:
        lose_life()
        print(f"\nDommage ... La lettre {letter} n'est pas présente dans le mot recherché: {list_to_string(answer_hidden)}"
              f"\nIl vous reste {life} tentatives).\n")
    return answer_hidden


# Cette fonction vérifie si la réponse contient un souligné (_).
def check_for_underscore():
    for letters in answer_hidden:
        if letters == "_":
            return False
    return True


# Cette fonction imprime dans la console un message de victoire.
def print_win():
    print(f"""Vous avez gagné ! Le mot recherché était {answer}
    ======================================================================================
      \\\\    //   =========   ||      ||      \\\\                //  ==========  ||\\\\     ||
       \\\\  //   ||       ||  ||      ||       \\\\              //       ||      ||  \\\\   ||
        \\\\//    ||       ||  ||      ||        \\\\    //\\\\    //        ||      ||   \\\\  ||
         ||     ||       ||  ||      ||         \\\\  //  \\\\  //         ||      ||    \\\\ ||
         ||      =========    ========           \\\\//    \\\\//      =========   ||     \\\\||
    ======================================================================================  """)
    return


# Cette fonction imprime dans la console un message de défaite.
def print_lose():
    print(f"""\nVous avez perdu ... Le mot était recherché {answer}
    =====================================================================================
      \\\\    //  =========   ||      ||       ||         =========    ========   ========
       \\\\  //  ||       ||  ||      ||       ||        ||       ||  ||          ||      
        \\\\//   ||       ||  ||      ||       ||        ||       ||   ========   ||======
         ||    ||       ||  ||      ||       ||        ||       ||          ||  ||      
         ||     =========    ========         =======   ========     ========   ========
    ======================================================================================""")
    return


# Cette fonction donne un indicé à l'utilisateur
def give_clue():
    user_input = ""
    global answer, clue
    while user_input not in ("O", "N"):
        user_input = input("Voulez-vous un indice ? (O/N): ")
        if user_input not in ("O", "N"):
            print("Veuillez répondre par O pour oui ou N pour Non\n")
    if user_input == "O":
        index = answer_hidden.index("_")
        answer_hidden[index] = answer[index]
        print(f"Le mot contient la lettre {answer[index]} ! "
              f"Le mot ressemble à ceci : {list_to_string(answer_hidden)} !")
        clue = True
        return


# Cette fonction demande à l'utilisateur s'il veut rejouer
def replay():
    user_input = ""
    global clue, life
    life = 6
    clue = False
    while user_input not in ("O", "N"):
        user_input = input("Voulez-vous rejouer ? (O/N): ")
        if user_input not in ("O", "N"):
            print("Veuillez répondre par O pour oui ou N pour Non\n")
    return user_input


# Cette ligne appelle la fonction main, qui lance le code
main()
