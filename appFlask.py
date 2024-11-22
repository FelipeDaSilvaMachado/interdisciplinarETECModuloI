from flask import Flask, request, jsonify
import forca

# Esta linha importa as classes e funções necessárias do módulo Flask:
# Flask: Usado para criar a aplicação web.
# request: Usado para acessar dados da solicitação HTTP.
# jsonify: Usado para converter o retorno da função em JSON.

app = Flask(__name__)
jogo = forca()
# Cria uma instância da aplicação Flask.
# __name__ é um argumento especial que define o nome do módulo atual.

@app.route('/')
def index(): 
    return render_template('chamadaJogoPython.html')

@app.route('/jogar', methods=['POST'])
def jogar():
    dados = request.json
    # Função que executa a lógica do seu jogo
    resultadoJogo = executarJogo(dados)
    return jsonify(resultadoJogo)

# @app.route('/jogar', methods=['POST']):
# Define uma rota /jogar para a aplicação.
# Especifica que essa rota aceita apenas solicitações HTTP do tipo POST.
# def jogar():
# Define a função que será executada quando a rota /jogar for acessada.
# dados = request.json:
# Captura os dados JSON enviados na solicitação POST.
# resultado_jogo = executar_jogo(dados):
# Chama a função executar_jogo passando os dados recebidos.
# (Você deve implementar a lógica do jogo nesta função.)
# return jsonify(resultado_jogo):
# Converte o resultado da função executar_jogo em JSON e retorna como resposta.


def executarJogo(dados):
    # Lógica do seu jogo aqui
    return {"mensagem": "Jogo executado com sucesso!", "dados": dados}

# def executar_jogo(dados)::
# Define a função que contém a lógica do seu jogo.
# Lógica do seu jogo aqui:
# Comentário indicando onde a lógica do jogo deve ser implementada.
# return {"mensagem": "Jogo executado com sucesso!", "dados": dados}:
# Retorna um dicionário com uma mensagem de sucesso e os dados recebidos.


if __name__ == '__main__':
    app.run(debug=True)
# if __name__ == '__main__'::
# Garante que a aplicação Flask só será executada se o script for executado
# diretamente, e não importado como um módulo.
# app.run(debug=True):
# Inicia o servidor Flask com o modo de depuração ativado, permitindo mensagens
# de erro detalhadas e reinicialização automática do servidor ao fazer
# alterações no código.