from time import sleep

first_name = input("What is your name? - ")
sleep(2)
age = int(input("How old are you? - "))

print(f"Hello {first_name}")
sleep(2)
print(f"You are so old: {age}")
sleep(2)

if first_name == 'Donald Tusk':
    print('Ty ruska onuco!')
    sleep(2)
elif age >= 18:
    print("Miło mi cię jest poznać! ^^")
    sleep(2)


if age >= 18:
    print("Zapraszamy!")
    sleep(2)
elif first_name == 'Donald Tusk':
    print("Won!")
    sleep(2)
else:
    print("A spierdalaj. Jesteś niepełnoletni!")
    sleep(2)
