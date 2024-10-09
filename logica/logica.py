# a) Sequência: 1, 3, 5, 7, ___
def proximo_a(seq):
    return seq[-1] + 2

# b) Sequência: 2, 4, 8, 16, 32, 64, ____
def proximo_b(seq):
    return seq[-1] * 2

# c) Sequência: 0, 1, 4, 9, 16, 25, 36, ____
def proximo_c(seq):
    n = len(seq)  # posição do próximo número
    return n * n  # quadrado perfeito

# d) Sequência: 4, 16, 36, 64, ____
def proximo_d(seq):
    n = len(seq) * 2  # posição do próximo número é sempre um par
    return n * n  # quadrado perfeito de um número par

# e) Sequência de Fibonacci: 1, 1, 2, 3, 5, 8, ____
def proximo_e(seq):
    return seq[-1] + seq[-2]

# f) Sequência: 2, 10, 12, 16, 17, 18, 19, ____
def proximo_f(seq):
    if seq[-1] == 19:
        return seq[-1] + 8  # após 19, adiciona 8
    else:
        return seq[-1] + 1  # no padrão dos outros números, adiciona 1

# Função para testar cada sequência
def testar_sequencias():
    # Teste a)
    a = [1, 3, 5, 7]
    print(f"Próximo número da sequência a): {proximo_a(a)}")

    # Teste b)
    b = [2, 4, 8, 16, 32, 64]
    print(f"Próximo número da sequência b): {proximo_b(b)}")

    # Teste c)
    c = [0, 1, 4, 9, 16, 25, 36]
    print(f"Próximo número da sequência c): {proximo_c(c)}")

    # Teste d)
    d = [4, 16, 36, 64]
    print(f"Próximo número da sequência d): {proximo_d(d)}")

    # Teste e) (Fibonacci)
    e = [1, 1, 2, 3, 5, 8]
    print(f"Próximo número da sequência e): {proximo_e(e)}")

    # Teste f)
    f = [2, 10, 12, 16, 17, 18, 19]
    print(f"Próximo número da sequência f): {proximo_f(f)}")

testar_sequencias()
