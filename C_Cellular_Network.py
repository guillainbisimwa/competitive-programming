def resoudre():
    nb_plantes, nb_tours = map(int, input().split())
    
    plantes = list(map(int, input().split()))
    tours = list(map(int, input().split()))
    
    def peut_arroser(capacite):
        for x in plantes:
            j = 0
            while j < nb_tours and tours[j] < x:
                j += 1
            
            ok = False
            if j < nb_tours and tours[j] - x <= capacite:
                ok = True
            if j > 0 and x - tours[j - 1] <= capacite:
                ok = True
            if not ok:
                return False
        return True

    debut, fin = 0, 2e9 + 10
    while debut < fin:
        milieu = debut + (fin - debut) // 2
        if peut_arroser(milieu):
            fin = milieu
        else:
            debut = milieu + 1
    # Affichage du résultat
    print(int(fin))

if __name__ == "__main__":
    te = 1
    for _ in range(te):
        resoudre()
