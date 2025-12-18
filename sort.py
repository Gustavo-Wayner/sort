def intParse(prompt):
    while True:
        try: return int(input(prompt))
        except: print("Invalid input")

amount = intParse("How many integers do you want to sort? ")

if amount <= 1:
    print("Ok... I'll give you one more chance")
    amount = intParse("How many integers do you want to sort? ")

    if amount <= 1:
        print("Alright. Piss off")
        quit()

if amount > 50:
    print("Bro...")
elif amount > 30:
    print(f"Oof. {amount}? Hey you do you bro")
elif amount > 20:
    print(f"{amount}? That's a lot ain't it?")


endings = []

for i in range(1, amount+1):
    strI = str(i)
    if (len(strI) > 1 and int(strI[len(strI) - 2]) != 1) or (len(strI) == 1):
        match strI[len(strI)-1]:
            case '1':
                list.append(endings, "st")
            case '2':
                list.append(endings, "nd")
            case '3':
                list.append(endings, "rd")
            case _: list.append(endings, "th")
    else: list.append(endings, "th")

print(f"Type in {amount} integers")
L = []

for i in range(0, amount):
    list.append(L, intParse(f"Type in the {i+1}{endings[i]} number: "))
list.sort(L)

print(f"These numbers in ascending order are:   {L}")
L.reverse()
print(f"And in descending order:                {L}")