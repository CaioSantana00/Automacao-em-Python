# Automação em Python

Projeto de **automação em Python** projetado para realizar o **login e cadastros automáticos de produtos em um sistema web**, utilizando dados através de um arquivo **CSV**.

O script simula interações humanas (mouse e teclado) por meio da biblioteca **PyAutoGUI**, evitando tarefas manuais repetitivas e reduzindo significamente o tempo de trabalho.

---

## 🚀 Visão Geral

Este projeto executa as seguintes etapas:

- 📄 Lê os dados dos produtos a partir do arquivo `produtos.csv`
- 🌐 Acessa um sistema web previamente aberto
- 🔐 Realiza o login automaticamente
- 🧾 Preenche formulários de cadastro de produtos
- 🔁 Repete o processo para todos os registros do **CSV**

Ideal para cenários onde o sistema não possui API ou importação em massa.

---

## 🧠 Tecnologias Utilizadas

- **Python 3**
- **PyAutoGUI** – Automação de mouse e teclado
- **Pandas** – Leitura e manipulação de arquivos CSV
- **Time** – Controle de pausas durante a automação

---

## 📁 Estrutura do Projeto

```text
Automacao-em-Python/
┣ Auxiliar.py         -→ Funções auxiliares da automação
┣ Codigo.py           -→ Script principal
┣ Produtos.csv        -→ Base de dados dos produtos
┗ Requirements.txt    -→ Dependências do projeto

```
---

## ⚙️ Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- Python 3.x
- Git
- Um editor de código (VS Code, PyCharm, etc.)

---

## 📦 Instruções de Instalação e Execução 

**Clone o repositório:** 
```bash
https://github.com/CaioSantana00/Automacao-em-Python.git
cd Automacao-em-Python
```

**(Opcional, mas recomendado) Crie um ambiente virtual:** 
```bash
python -m venv venv
```

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

**Instale as dependências**
```bash
pip install -r requirements.txt
```

**Execute o script principal:**
```bash
python codigo.py
```
---

## ⚠️ Observações Importantes

- O PyAutoGUI depende da posição da tela e resolução
- Não utilize mouse ou teclado durante a execução
- Ajustes de tempo **(time.sleep)** podem ser necessários
- Projeto indicado para fins educacionais e automações controladas

---

## 📌 Conclusão

Este projeto demonstra a aplicação prática de Python para automação de processos, organização de código e resolução de problemas reais encontrados no dia a dia corporativo.

Caso a automação falhe, ajuste os tempos **(time.sleep)** ou coordenadas no código **(auxiliar.py)**

---

**Obrigado por visitar este repositório!**

Se este projeto te ajudou ou inspirou, considere deixar uma ⭐ ou um feedback, será muito bem-vindo 🙂

