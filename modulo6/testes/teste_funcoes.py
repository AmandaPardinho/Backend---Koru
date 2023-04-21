import pytest
import os
"""Usei o `import os` apenas para verificar o caminho da pasta. depois de verificar, digitei no terminal powershell `cd testes` => enter => pytest teste_funcoes.py"""
"""Fazendo isso o teste rodou"""
caminho = os.path.dirname(__file__)
print(caminho)

from funcoes import soma, subtracao, multiplicacao, divisao, divisao_inteira, resto_divisao

def teste_soma():
    assert soma(2, 3) == 5
    assert soma(0, 0) == 0
    assert soma(-2, 3) == 1

def teste_subtracao():
    assert subtracao(2, 3) == -1
    assert subtracao(0, 0) == 0
    assert subtracao(-2, 3) == -5

def teste_multiplicacao():
    assert multiplicacao(2, 3) == 6
    assert multiplicacao(0, 0) == 0
    assert multiplicacao(-2, 3) == -6

def teste_divisao():
    assert divisao(2, 3) == 0.666
    assert divisao(0, 1) == 0
    assert divisao(6, 2) == 3

def teste_divisao_inteira():
    assert divisao_inteira(2, 3) == 0
    assert divisao_inteira(0, 1) == 0
    assert divisao_inteira(6, 2) == 3

def teste_resto_divisao():
    assert resto_divisao(2, 3) == 2
    assert resto_divisao(1, 1) == 0
    assert resto_divisao(6, 2) == 0