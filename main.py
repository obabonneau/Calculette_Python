# Définition de la fonction de bienvenue
def print_welcome_message():
    print("Bienvenue sur la mini-calculatrice !")

# Définition de la fonction du choix de l'opération
def print_menu_and_get_choice():
    print("=== MENU ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")

    user_choice = input("Entrez votre choix (1-4) : ")
    while user_choice not in ["1", "2", "3", "4"]:
        user_choice = input("Choix invalide. Entrez votre choix (1-4) : ")

    return user_choice

# Définition de la fonction de calcul
def run_calculation(user_choice):
    num1, num2 = input_two_number()
    match user_choice:
        case '1':
            result = sum(num1, num2)
        case '2':
            result = substraction(num1, num2)
        case '3':
            result = multiplication(num1, num2)
        case '4':
            result = division(num1, num2)
    return result

# Définition de la fonction de saisie des nombres
def input_two_number():
    user_chaine1 = input("Entrez le premier nombre : ")
    while not conv_test_decimal(user_chaine1):
        user_chaine1 = input("Nombre invalide, entrez le premier nombre : ")
    user_chaine1 = conv_test_decimal(user_chaine1)[1]

    user_chaine2 = input("Entrez le deuxième nombre : ")
    while not conv_test_decimal(user_chaine2):
        chaine2 = input("Nombre invalide, entrez le deuxième nombre : ")
    user_chaine2 = conv_test_decimal(user_chaine2)[1]

    return user_chaine1, user_chaine2

# Définition de la fonction de test des nombres saisies 
def conv_test_decimal(chaine):
    try:
        chaine = chaine.replace(',', '.') # Pour passer du format français au format anglais (1,5 = 1.5)
        chaine = float(chaine)
        return True, chaine
    except ValueError:
        return False

# Définition de la fonction addition
def sum(a, b):
    return a + b

# Définition de la fonction soustraction
def substraction(a, b):
    return a - b

# Définition de la fonction multiplication
def multiplication(a, b):
    return a * b

# Définition de la fonction division
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur : division par zéro"

# Programme autolancé
if __name__ == '__main__':
    print_welcome_message()
    user_choice = print_menu_and_get_choice()
    result = run_calculation(user_choice)
    print(result)