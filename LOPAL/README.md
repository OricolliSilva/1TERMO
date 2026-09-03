# 💻 Lógica de Programação com Python e GitHub

## 📝 1. Conteúdo Programático das Aulas
*   **Pensamento Computacional**: Decomposição, reconhecimento de padrões e algoritmos.
*   **Fundamentos da Linguagem**: Sintaxe Python, variáveis e tipos de dados.
*   **Estruturas de Controle**: Condicionais (if/else) e laços de repetição (while/for).
*   **Estruturas de Dados**: Listas, tuplas, dicionários e manipulação de coleções.
*   **Modularização**: Criação de funções, passagem de parâmetros e escopo.
*   **Controle de Versão**: Fundamentos do Git e hospedagem de código no GitHub.

---

## 🐍 2. Fundamentos de Python

### Variáveis e Tipos de Dados
*   **Tipagem Dinâmica**: O tipo da variável é definido automaticamente pelo interpretador.
*   **Tipos Primitivos**: `int` (inteiro), `float` (decimal), `str` (texto) e `bool` (booleano).

### Estruturas Condicionais e de Repetição
*   **Indentação Obrigatória**: Define os blocos de código através do espaçamento vertical.

```python
# Exemplo de Condicional (if/else)
idade = 18
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

# Exemplo de Repetição (for)
for i in range(1, 6):
    print(f"Contagem: {i}")
```

### Funções e Listas
```python
# Criando uma lista e manipulando dados com uma função
def calcular_media(notas):
    total = sum(notas)
    return total / len(notas)

lista_notas = [7.5, 8.0, 9.5]
media_final = calcular_media(lista_notas)
print(f"Média do aluno: {media_final:.2f}")
```

---

## 🐙 3. Git e GitHub para Estudantes

### O que é o Git?
*   **Sistema de Controle de Versão**: Rastreia o histórico de alterações nos arquivos de código.
*   **Trabalho Local**: Funciona diretamente no computador do desenvolvedor (offline).

### O que é o GitHub?
*   **Plataforma de Hospedagem**: Armazena repositórios Git na nuvem para colaboração.
*   **Portfólio**: Vitrine digital para estudantes demonstrarem seus projetos de código.

### Fluxo de Trabalho Essencial (Terminal/Prompt)

1. **Inicializar o repositório local:**
   ```bash
   git init
   ```
2. **Adicionar os arquivos modificados para a área de preparação:**
   ```bash
   git add nome_do_arquivo.py
   ```
3. **Gravar as alterações localmente com uma mensagem descritiva:**
   ```bash
   git commit -m "Adiciona exercício de média de notas"
   ```
4. **Vincular o repositório local ao repositório criado no GitHub:**
   ```bash
   git remote add origin github.com
   ```
5. **Enviar o código local para a nuvem do GitHub:**
   ```bash
   git push -u origin main
   ```

### 🤝 Boas Práticas no GitHub
*   **Arquivo README.md**: Página inicial do projeto explicando o que o código faz e como executá-lo.
*   **Mensagens de Commit Claras**: Mensagens curtas no imperativo (Ex: `Adiciona`, `Corrige`, `Remove`).
*   **Arquivo .gitignore**: Arquivo para listar pastas e arquivos locais que não devem ir para o GitHub (Ex: pastas de configuração da IDE).
