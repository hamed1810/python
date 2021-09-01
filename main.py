## soal 1
vorodi = int(input("enter number: "))
q = 0
for i in range(1, vorodi + 1):
    vorodi -= 1
    q += 1
    print(vorodi * "  ", q * "* ")


## soal 2
vorodi = int(input("enter number: "))
for i in range(1, vorodi + 1):
    print("* " * i)
for i in range(vorodi - 1, 0, -1):
    print("* " * i)


## soal 3
vorodi = int(input("enter number: "))
b = vorodi - 1
q = 0
for i in range(vorodi):
    vorodi -= 1
    q += 1
    print(vorodi * " ", q * "* ")
q = 0
for i in range(b, -1, -1):
    q += 1
    print(q * " ", b * "* ")
    b -= 1
