def soma(a: int, b: int) -> int: 
    """Recebe dois inteiros e retorna a soma entre eles"""
    return a + b

def subtracao(a: int, b: int) -> int:
    """Recebe dois números inteiros e retorna a subtração entre eles"""
    return a - b

def multiplicacao(a: int, b: int) -> int:
    """Recebe dois inteiros e retorna a multiplicação entre eles"""
    return a * b

def divisao(a: int, b: int) -> float:
    """Recebe dois números inteiros e retorna o resultado da divisão entre eles. Se a divisão não for exata, retorna um float"""
    return a / b

def divisao_inteira(a: int, b: int) -> int:
    """Recebe dois números inteiros e retorna o resultado da divisão inteira entre eles"""
    return a // b

def resto_divisao(a: int, b: int) -> int:
    """Recebe dois numeros inteiros e retorna o resto da divisão entre eles"""
    return a % b