Fruits = ["apples", "oranges", "bananas", "grapes"]

print("What fruits should I eat today?")
print(',' .join(Fruits))

choice = input("Pick a fruit!").lower()

if choice == "apples":
    print("good choice! apples are delicious")
elif choice == "oranges":
    print("oranges are a good source of vitamin C")
elif choice == "bananas":
    print("yummmy bananas")
elif choice == "grapes":
    print("solid prunes?")
else: 
    print ("Cass said to eat a damn fruit.")    