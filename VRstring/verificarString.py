def contar_letras_a(text):
    count = text.lower().count('a')
 

#criando a condição
    if count > 0:
     return f"Letra 'a' aparece {count} vez(es) dentro da string."

    else:
     return "Letra 'a' não apareceu na string."
    
#test
string = input("Informe uma String: ")
print(contar_letras_a(string))