A = input("학생A카드: ").split(" ")
B = input("학생B카드: ").split(" ")

card = set(A)&set(B)
print(card)