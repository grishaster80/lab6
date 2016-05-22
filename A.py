s=[]
z=int(input('Сколько элементов в массиве'))
for i in range(z):
	s.append(int(input("Введите число")))
for x in range(z):
	if s.count(s[x]) != 1:
		print(s[x])
		break
