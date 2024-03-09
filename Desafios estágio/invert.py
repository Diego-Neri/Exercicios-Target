string_original = input("Digite uma palavra ou frase: ")


string_invertida = ""

for caractere in reversed(string_original):
    string_invertida += caractere

print("A string invertida é:", string_invertida)
