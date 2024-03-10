# def resoudre():
#     # Lecture de n et m
#     nb_plantes, nb_tours = map(int, input().split())
    
#     # Lecture des listes plantes et tours
#     plantes = list(map(int, input().split()))
#     tours = list(map(int, input().split()))
    
#     # Fonction pour vérifier si l'arrosage des plantes est possible avec une certaine capacité d'eau
#     def peut_arroser(capacite):
#         for x in plantes:
#             # Recherche linéaire dans la liste des tours pour trouver l'indice j tel que tours[j] soit le plus petit élément de tours qui est supérieur ou égal à x
#             j = 0
#             while j < nb_tours and tours[j] < x:
#                 j += 1
            
#             # Vérification de la possibilité d'arroser en fonction de la capacité d'eau
#             ok = False
#             if j < nb_tours and tours[j] - x <= capacite:
#                 ok = True
#             if j > 0 and x - tours[j - 1] <= capacite:
#                 ok = True
#             if not ok:
#                 return False
#         return True

#     # Recherche par dichotomie de la plus petite capacité d'eau possible
#     debut, fin = 0, 2e9 + 10
#     while debut < fin:
#         milieu = debut + (fin - debut) // 2
#         if peut_arroser(milieu):
#             fin = milieu
#         else:
#             debut = milieu + 1
#     # Affichage du résultat
#     print(int(fin))

# if __name__ == "__main__":
#     te = 1
#     for _ in range(te):
#         resoudre()
