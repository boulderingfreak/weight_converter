print("Hi in my weight converter")

choice = int(input("Type 1 to convert kgs into lbs. \nType 2 to convert lbs into kgs. \nYour choice: "))

if choice == 1:
    kgs1 = float(input("Kgs: "))
    result1 = kgs1*2.2
    print(f"{kgs1} kilograms is {round(result1, 3)} lbs.")
elif choice == 2:
    lbs = float(input("Lbs: "))
    result2 = lbs/2.2
    print(f"{lbs} lbs is {round(result2, 3)} kgs.")