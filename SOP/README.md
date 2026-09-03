# 💻 Lógica de Programação: Configuração de Ambientes (Windows, Linux e iOS)

## 📝 1. Conteúdo Programático das Aulas
*   **Abstração de Sistema Operacional**: Como o código interage com o hardware através do S.O.
*   **Interface de Linha de Comando (CLI)**: Navegação básica por terminais em diferentes plataformas.
*   **Ambientes de Execução**: Configuração de interpretadores, compiladores e variáveis de ambiente.
*   **IDEs e Editores de Texto**: Instalação e uso de ferramentas multiplataforma (Ex: VS Code).
*   **Desenvolvimento Mobile e Cloud**: Alternativas para programar lógica diretamente em dispositivos móveis.

---

## 🪟 2. Desenvolvimento no Windows

### Configuração do Ambiente
*   **Instalação**: Download do instalador oficial (.exe) com marcação da opção "Add to PATH" (Variáveis de Ambiente).
*   **Terminal Padrão**: Uso do *PowerShell* ou *Prompt de Comando (CMD)* para executar scripts.
*   **Gerenciador de Pacotes**: Uso do `winget` para instalar ferramentas via terminal.

### Comandos Básicos de Terminal (CMD/PowerShell)
*   `dir`: Lista arquivos e pastas do diretório atual.
*   `cd nome_da_pasta`: Entra em uma pasta específica.
*   `cls`: Limpa a tela do terminal.

### Execução de Código (Exemplo: Python)
```cmd
:: Verificando a instalação no CMD
python --version

:: Executando um script de lógica
python meu_programa.py
```

---

## 🐧 3. Desenvolvimento no Linux

### Configuração do Ambiente
*   **Nativo**: A maioria das distribuições Linux (Ubuntu, Debian, Fedora) já vem com Python ou compiladores C instalados.
*   **Gerenciador de Pacotes**: Instalação rápida e centralizada via terminal (Ex: `apt`, `dnf`).
*   **Permissões**: Uso do comando `chmod` para tornar scripts executáveis no sistema.

### Comandos Básicos de Terminal (Bash)
*   `ls`: Lista arquivos e pastas do diretório atual.
*   `cd nome_da_pasta`: Entra em uma pasta específica.
*   `clear`: Limpa a tela do terminal.

### Execução de Código (Exemplo: Terminal Linux)
```bash
# Instalando o interpretador (se necessário no Ubuntu/Debian)
sudo apt update && sudo apt install python3

# Executando o script de lógica
python3 meu_programa.py
```

---

## 📱 4. Desenvolvimento e Lógica no iOS (iPhone / iPad)

### Limitações e Alternativas
*   **Ambiente Fechado**: O iOS não possui um terminal nativo acessível para compilar código do sistema como o Windows ou Linux.
*   **Aplicativos de Execução Local (Sandbox)**: Uso de apps específicos que trazem interpretadores embutidos.
    *   *Pyto* ou *Pythonista*: Ambientes completos para rodar scripts Python localmente.
    *   *iPharo* ou *Carnets*: Ambientes baseados em Jupyter Notebooks para estudantes.
*   **IDEs na Nuvem (Cloud)**: Uso de plataformas web pelo navegador Safari (Ex: *Replit*, *GitHub Codespaces*, *Google Colab*).

### Aprendizado de Lógica Nativo (Apple Swift Playgrounds)
*   **Gamificação**: Uso do aplicativo gratuito *Swift Playgrounds* da Apple para ensinar conceitos fundamentais (loops, condicionais, funções) de forma visual e interativa.

### Exemplo de Fluxo em Nuvem (Safari/Chrome no iOS)
1. O aluno acessa o site do [Replit](https://replit.com) ou [Google Colab](https://google.com).
2. Cria um arquivo de código diretamente pelo navegador do tablet ou celular.
3. Executa o algoritmo nos servidores da nuvem, contornando as restrições de hardware do iOS.
