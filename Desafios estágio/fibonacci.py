def verifica_fibonacci(number):
    a, b = 0, 1
    while b < number:
        a, b = b, a + b
    if b == number:
        return True
    return False

number = int(input("Informe um número: "))
result = verifica_fibonacci(number)
if result:
    print(f"O número {number} pertence à sequência de Fibonacci.")
else:
    print(f"O número {number} não pertence à sequência de Fibonacci.")

