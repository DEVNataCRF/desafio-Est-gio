def fibonacci(n):
    fib_sequence = [0, 1]

    while fib_sequence[-1] < n:
    #calculando os número da seq
     next_num = fib_sequence[-1] + fib_sequence[-2]
     fib_sequence.append(next_num)

    #vamos verificar se está na sequencia
    if n in fib_sequence:
        return f"O número {n} pertence à sequência de Fibonacci."    
    else:
        return f"O número {n} NÃO pertence à sequência de Fibonacci."

#resultado do meu mano fibonacci
num = int(input("Informe um número: "))    
print (fibonacci(num))