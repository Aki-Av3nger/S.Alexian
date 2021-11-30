def partitionner(l, debut, fin):
    valeur_piv = l[fin]
    indice_piv = debut

    for i in range(debut, fin):
        if l[i] <= valeur_piv:
            l[i], l[indice_piv] = l[indice_piv], l[i]
            indice_piv += 1

    l[indice_piv], l[fin] = l[fin], l[indice_piv]
    return indice_piv


def tri_rapide(l, debut=0, fin=None):
    if fin == None:
        fin = len(l) -1

    if fin > debut:
        pivot = partitionner(l, debut, fin)

        tri_rapide(l, debut, pivot-1)

        tri_rapide(l,pivot+1 , fin)

l = [15,25,48,68,95,78,47,53,21,45,85]
print(l)
tri_rapide(l)
print(l)