# Tratamento de erros com Python
# Erros comuns:
# - ZeroDivisionError: divisão por zero 
# - ValueError: Conversão de tipo inválida
# - IndexError: Acesso a índice fora do limite
# - KeyError: Acesso a chave inexistente em dicionário

# Exemplo de tratamento de erros
# print("Exemplo de tratamentos de erros")
try:

    num1 = int(input("Digite o seu primeiro número..."))
    num2 = int(input("Digite o seu segundo número..."))
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado:.2f}")

# except ZeroDivisionError:
#     print("Erro! Não é possivél dividir por 0 (Zero)")

# except ValueError:
#     print("Erro: entrada inválida. Por Favor, digite um número inteiro.")

except NameError:
    print("Erro: Variável não definida.")

except Exception as e:
    print(f"Ocorreu um erro inesperado {e}")

if num1 >100:
    print(") número digitado é maior que 100.")
    for i in range(1, 6):
        print(f"{num1} X {i} = {num1 *i}")
        if num1 * i > 1000:
            print("O resultado da multiplicação é maior que 1000")
            try:
                pass
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")
else:
    print("O número digitado é menor ou igual a 100.")