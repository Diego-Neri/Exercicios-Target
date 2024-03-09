# Sequência  1, 3, 5, 7, ___
def proximo_elemento_a():
    # sequência aumenta de 2 em 2
    return 7 + 2

# Sequência 2, 4, 8, 16, 32, 64, ___
def proximo_elemento_b():
    # cada elemento é o dobro do anterior
    return 64 * 2

# Sequência 0, 1, 4, 9, 16, 25, 36, ___
def proximo_elemento_c():
    # cada elemento é o quadrado 
    return 7 ** 2

# Sequência 4, 16, 36, 64, ___
def proximo_elemento_d():
    # Como cada elemento é o quadrado do índice ímpar
    return 5 ** 2

# Sequência 1, 1, 2, 3, 5, 8, ___
def proximo_elemento_e():
    # próximo elemento será a soma dos dois anteriores
    ultimo = 8
    penultimo = 5
    return ultimo + penultimo

# Sequência 2, 10, 12, 16, 17, 18, 19, ___
def proximo_elemento_f():
    # Não entendi está lógica, valor usado como referência 1
    return 19 + 1

print("a) Próximo elemento:", proximo_elemento_a())
print("b) Próximo elemento:", proximo_elemento_b())
print("c) Próximo elemento:", proximo_elemento_c())
print("d) Próximo elemento:", proximo_elemento_d())
print("e) Próximo elemento:", proximo_elemento_e())
print("f) Próximo elemento:", proximo_elemento_f())
