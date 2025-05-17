# Initialisation des constantes
import random

NBR_VIE = 6
life = NBR_VIE

answer = ""
answer_list = ["_"] * len(answer)
replay = "O"
clue = False


def main():
    replay = "O"

    while replay == "O":
        global answer, answer_list, clue
        answer = delete_accent(word_selection())
        #print(answer)
        answer_list = ["_"] * (len(answer) - 1)
        initialisation_jeu(list_to_string(answer_list))

        while life > 0 and check_word() == False:
            if life == 1 and clue == False:
                give_clue()
            guess_letter()

        if check_word() == True:
            print_win()
        else:
            print_lose()

        replay = rejouer()
    return


def list_to_string(word):
    word_str = ""
    for letters in word:
        word_str += letters
    return word_str


def string_to_list(word):
    word_list = []
    for letters in word:
        word_list.append(letters)
    return word_list


def word_selection():
    file = "mots_pendu.txt"
    word_list = open(file, "r", encoding='utf-8')
    num = random.randrange(126)
    answer = word_list.readlines()[num]
    return answer


def delete_accent(word_accent):
    word = string_to_list(word_accent)
    for i in range(len(word)):
        if word[i] in ("à, â, ä"):
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


def initialisation_jeu(word):
    print(f"""\n\nBienvenue au jeu du pendu. Un mot aléatoire a été sélectionner et votre but est de le trouver.
Dite moi une lettre et je vous dirais si elle est présente dans le mot recherché.
Le mot contient {len(word)} lettres et vous possédez {NBR_VIE} vies.
{list_to_string(answer_list)}\n""")
    return


def lose_life():
    global life
    life -= 1
    return


def guess_letter():
    check = False
    letter = str(input("\tChoississez une lettre que le mot pourrait contenir : "))

    for i in range(len(answer)):
        if answer[i] == letter:
            answer_list[i] = letter
            check = True

    if check is True:
        print(f"""\tBien joué ! La lettre {letter} est présente dans le mot recherché: {list_to_string(answer_list)}
    Il vous reste {life} vies\n""")

    else:
        lose_life()
        print(f"""\tDommage ... La lettre {letter} n'est pas présente dans le mot recherché: {list_to_string(answer_list)}
    Il vous reste {life} vies\n""")
    return answer_list


def check_word():
    for letters in answer_list:
        if letters == "_":
            return False
    return True


def print_win():
    print(f"""Vous avez gagné ! Le mot rechercé était {answer}    ======================================================================================
      \\\\    //   =========   ||      ||      \\\\                //  ==========  ||\\\\     ||
       \\\\  //   ||       ||  ||      ||       \\\\              //       ||      ||  \\\\   ||
        \\\\//    ||       ||  ||      ||        \\\\    //\\\\    //        ||      ||   \\\\  ||
         ||     ||       ||  ||      ||         \\\\  //  \\\\  //         ||      ||    \\\\ ||
         ||      =========    ========           \\\\//    \\\\//      =========   ||     \\\\||
    ======================================================================================  """)
    return


def print_lose():
    print(f"""Vous avez perdu ... Le mot était rechercé {answer}    ======================================================================================
      \\\\    //  =========   ||      ||       ||         =========    ========   ========
       \\\\  //  ||       ||  ||      ||       ||        ||       ||  ||          ||      
        \\\\//   ||       ||  ||      ||       ||        ||       ||   ========   ||======
         ||    ||       ||  ||      ||       ||        ||       ||          ||  ||      
         ||     =========    ========         =======   ========     ========   ========
    ======================================================================================""")
    return


def give_clue():
    user_input = ""
    global answer, clue
    while user_input not in ("O", "N"):
        user_input = input("Voulez-vous un indice ? (O/N): ")
        if user_input not in ("O", "N"):
            print("Veuillez répondre par O pour oui ou N pour Non\n")
    if user_input == "O":
        index = answer_list.index("_", random.randrange(len(answer_list)))
        answer_list[index] = answer[index]
        print(f"Le mot contient la lettre {answer[index]} ! "
              f"Le mot ressemble à ceci : {list_to_string(answer_list)} !")
        clue = True
        return


def rejouer():
    user_input = ""
    global clue, life
    life = 6
    clue = False
    while user_input not in ("O", "N"):
        user_input = input("Voulez-vous rejouer ? (O/N): ")
        if user_input not in ("O", "N"):
            print("Veuillez répondre par O pour oui ou N pour Non\n")
    return user_input


main()
