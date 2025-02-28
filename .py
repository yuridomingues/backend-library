# CIFRA DE CESAR

text = input("- Insira o texto para ser codificado: \n")
key = int(input("- Insira a chave para a criptografia: \n"))

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

PASSWORD = ""

for letter in text:
    for i in range(len(alphabet)):
        if letter.upper() == alphabet[i]:
            PASSWORD += alphabet[(i + key)]

print (f"Seu texto encriptado ficou como: {PASSWORD}")