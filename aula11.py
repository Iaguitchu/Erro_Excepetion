lista = [1, 10]
b = 0
arquivo = open('teste.txt', 'r')
try:
    divisao = 10 / 1
    numero = lista[1]
    x = b
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0')

except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritmética')

except IndexError:
    print('Erro ao acessar um indice inválido da lista')

except Exception as ex:
    print(f'erro desconhecido. Erro: {ex}')

else:
    print('executa quando nao houver nenhuma exceção')
finally:
    print('Sempre executa')
    arquivo.close()