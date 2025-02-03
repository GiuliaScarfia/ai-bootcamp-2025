while True:
    user_input = input(">>>").strip()
    if user_input.lower() == "quit":
        print("bye!")
        break

    try:
        num1, op, num2 = user_input.split()
        num1, num2 = float(num1), float(num2)

        if op == "+":
            print(num1 + num2)
        elif op == "-":
            print(num1 - num2)
        elif op == "*":
            print(num1 * num2)
        elif op == "/":
            if num2 != 0:
                print(num1 / num2)
            else:
                print("Divisione per zero non consentita.")
        else:
            print("Operatore non valido. Sono ammesse solo addizioni e sottrazioni, moltiplicazioni e divisioni.")
    except ValueError:
        print("Input non valido. Assicurati di inserire due numeri interi con un operatore valido (+, -, *, /).")
