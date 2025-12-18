Endings = ["st", "nd", "rd", "th", "th"]

print("Type in 5 numbers")
L = []
for i in range(0, 5):
    while True:
        try:
            list.append(L, float(input(f"Type in the {i+1}{Endings[i]} number: ")))
            break
        except:
            print('Invalid input')
list.sort(L)

print(f"These numbers in ascending order are: {L}")
L.reverse()
print(f"And in descending order: {L}")