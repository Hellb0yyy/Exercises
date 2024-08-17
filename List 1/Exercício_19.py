def palindromo(palavra):

    palavra = palavra.replace(" ", "").lower()

    return palavra == palavra[::-1]

palavra = input("Digite uma palavra: ")

if palindromo(palavra):
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
