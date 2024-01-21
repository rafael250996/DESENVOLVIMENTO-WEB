# Importando os módulos da biblioteca Flask
from flask import Flask, render_template

# Criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# Rota padrão ou 'URL'
@app.route("/eu")
def eu():
    nome = "Rafael Ribeiro"  # Escreva seu nome
    idade = "16"  # Escreva sua idade
    return render_template('index.html', nome=nome, idade=idade)

# Rota para a página do pai
@app.route("/pai")
def pai():
    nome = "Vilmar Ribeiro"  # Escreva seu nome
    idade = "54"  # Escreva sua idade
    return render_template('pai.html', nome=nome, idade=idade)

# Rota para a página da mãe
@app.route("/mae")
def mae():
    nome = "Adriana Ribeiro"  # Escreva seu nome
    idade = "48"  # Escreva sua idade
    return render_template('mae.html', nome=nome, idade=idade)

# Rota para a página do amigo
@app.route("/amigo")
def amigo():
    nome = "dgl"  # Escreva seu nome
    idade = "17"  # Escreva sua idade
    return render_template('amigo.html', nome=nome, idade=idade)

# Adicione outras rotas, se necessário

# Execute o arquivo
if __name__ == '__main__':
    app.run(debug=True)
