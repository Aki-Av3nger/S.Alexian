def min(liste, début):
	index_min = début
	for i in range (début + 1, len(liste)):
		if liste[index_min]>liste[i]:
			index_min = i
	return index_min

liste = [17, 28, 7, 28, 30, 25, 112]

for i in range (0, len(liste)-1):
	index_min = min(liste, i)

	liste[i], liste[index_min] = liste[index_min], liste[i]

print(liste)