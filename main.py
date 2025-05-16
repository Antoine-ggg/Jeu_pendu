# Initialisation des constantes

NBR_VIE = 6
answer = ""
answer_list = ["_"] * len(answer)

life = NBR_VIE

def main():
    replay = "O"
    while replay == "O":
        global
        answer = 1
        answer_list = ["_"] * len(answer)
        initialisation_jeu(list_to_string(answer_list))
        while life > 0 and check_word() == False:
            guess_letter()

        if check_word() == True:
            print_win()
        else:
            print_lose()
        replay = rejouer()

    return


def lose_life():
    global life
    life -= 1
    return


def initialisation_jeu(word):
    print(f"""\tLe mot contient {len(word)} lettres. Vous avez {NBR_VIE} chances.
    \t{list_to_string(answer_list)}\n""")
    return


def guess_letter():
    check = False
    letter = str(input("\tChoississez une lettre que le mot pourrait contenir : "))

    for i in range(len(answer)):
        if answer[i] == letter:
            answer_list[i] = letter
            check = True
        if life == 1:
            clue()

    if check is True:
        print(f"""\tLa lettre {letter} est présente dans le mot recherché: {list_to_string(answer_list)}
    Il vous reste {life} vies\n""")
    else:
        lose_life()
        print(f"""\tLa lettre {letter} n'est pas présente dans le mot recherché: {list_to_string(answer_list)}
    Il vous reste {life} vies\n""")
    return answer_list


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

def check_word():
    for letters in answer_list:
        if letters == "_":
            return False
    return True

def print_win():
    print("""Vous avez gagné !\n
    ======================================================================================
      \\\\    //   =========   ||      ||      \\\\                //  ==========  ||\\\\     ||
       \\\\  //   ||       ||  ||      ||       \\\\              //       ||      ||  \\\\   ||
        \\\\//    ||       ||  ||      ||        \\\\    //\\\\    //        ||      ||   \\\\  ||
         ||     ||       ||  ||      ||         \\\\  //  \\\\  //         ||      ||    \\\\ ||
         ||      =========    ========           \\\\//    \\\\//      =========   ||     \\\\||
    ======================================================================================  """)
    return

def print_lose():
    print("""Vous avez perdu ...\n
    ======================================================================================
      \\\\    //  =========   ||      ||       ||         =========    ========   ========
       \\\\  //  ||       ||  ||      ||       ||        ||       ||  ||          ||      
        \\\\//   ||       ||  ||      ||       ||        ||       ||   ========   ||======
         ||    ||       ||  ||      ||       ||        ||       ||          ||  ||      
         ||     =========    ========         =======   ========     ========   ========
    ======================================================================================  """)
    return

def clue():
    user_input = ""
    while user_input not in ("O", "N"):
        user_input = input("Voulez-vous un indice ? (O/N)")
        if user_input not in ("O", "N"):
            print("Veuillez répondre par O pour oui ou N pour Non")
    if user_input = "O":

        return

def rejouer():
    user_input = ""
    while user_input not in ("O", "N"):
        user_input = input("Voulez-vous rejouer ? (O/N)")
        if user_input not in ("O", "N"):
            print("Veuillez répondre par O pour oui ou N pour Non")
    return user_input

main()
