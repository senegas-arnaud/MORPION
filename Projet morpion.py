
# MORPION




# Défini les variables pour le joueur1 et le joueur2
J1 = "X"
J2 = "O"
J0 = " "  
tableau = [J0 for _ in range(9)] 




# Fonction pour dessiner le tableau grace a une liste de 0 à 8 
def morpion_tableau():      
    print(f"{tableau[0]} | {tableau[1]} | {tableau[2]}")
    print("--|---|--")
    print(f"{tableau[3]} | {tableau[4]} | {tableau[5]}")
    print("--|---|--")
    print(f"{tableau[6]} | {tableau[7]} | {tableau[8]}")




# Défini les conditions de victoires(Lignes, colonnes, diagonales) 
def win_cond(joueur):
    # Lignes
    if (tableau[0] == tableau[1] == tableau[2] == joueur) or\
       (tableau[3] == tableau[4] == tableau[5] == joueur) or\
       (tableau[6] == tableau[7] == tableau[8] == joueur):
        return True

    # Colonnes
    if (tableau[0] == tableau[3] == tableau[6] == joueur) or\
       (tableau[1] == tableau[4] == tableau[7] == joueur) or\
       (tableau[2] == tableau[5] == tableau[8] == joueur):
        return True

    # Diagonales
    if (tableau[0] == tableau[4] == tableau[8] == joueur) or\
       (tableau[2] == tableau[4] == tableau[6] == joueur):
        return True
    return False




# Si le tableau est rempli d'espace vide (J0), le match se termine sur une égalité
def match_nul():
    return J0 not in tableau




# Fonction pour jouer
def jouer():
    # Défini le premier joueur
    joueur_actuel = J1 
    # et le tour en cours
    tour = 0  

    while True:
        morpion_tableau()
        print(f"Tour du joueur {joueur_actuel} :")
        # le joueur choisi une case dans le terminal
        choix = int(input("Choisissez une case (0-8) : "))
        
        # Si la case n'est pas égal a un espace vide  
        if tableau[choix] != J0:                            
            print("Case deja occupée")                     
            continue

        # Permet de remplacer l'espace vide choisi par le joueur (X ou O)
        tableau[choix] = joueur_actuel

        # Si une condition de victoires est respecté alors le jeu s'arrete
        if win_cond(joueur_actuel):
            morpion_tableau()
            print(f"Le joueur {joueur_actuel} a gagné!")
            break

        # Si la condition pour une égalité est respecté alors le jeu s'arrete
        if match_nul():  
            morpion_tableau()
            print("Match nul!")
            
            
        else:
            print("Valeur invalide")




        # Permet d'alterner chaque tours entre joueur1 et joueur2
        joueur_actuel = J2 if joueur_actuel == J1 else J1  
        tour += 1


jouer()