import subprocess
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite requisições de diferentes origens


@app.route('/testeForca', methods=['GET'])
def jogar():
    # Executa o arquivo Python do jogo com Tkinter usando subprocess
    executarJogo = subprocess.Popen(
    ['python', 'testeForca.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = executarJogo.communicate()  # Chamando o jogo em python

    # Podemos retornar uma resposta imediata dizendo que o jogo foi iniciado
    if executarJogo.returncode == 0:
        return jsonify({'status': 'sucesso', 'mensagem': 'Jogo iniciado no Tkinter!', 'saida': stdout.decode()})
    else:
        return jsonify({'status': 'erro', 'mensagem': stderr.decode()}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)

# from flask import Flask, jsonify, send_file
# # Importa as bibliotecas necessárias
# import subprocess  # Para executar processos externos
# import sys  # Para informações do sistema Python
# import os  # Para manipulação de caminhos de arquivos

# # Configura o aplicativo Flask
# # static_folder='.' permite servir arquivos estáticos da raiz do projeto
# # static_url_path='/' permite acessar arquivos diretamente pela raiz

# app = Flask(__name__,
#             static_folder='.',
#             static_url_path='/')

# # Configura o recarregamento automático de templates (útil durante desenvolvimento)
# # app.config['TEMPLATES_AUTO_RELOAD'] = True

# # Rota principal que serve o arquivo HTML


# @app.route('/')
# def index():
#     # Envia o arquivo HTML principal
#     return send_file('chamadaJogoPython.html')

# # Rota específica para iniciar o jogo


# @app.route('/testeForca', methods=['GET'])
# def executar_jogo():
#     try:
#         # Obtém o caminho absoluto para o script do jogo
#         script_path = os.path.abspath('testeForca.py')

#         # Usa subprocess para executar o script Python em um novo processo
#         # sys.executable garante que usa o mesmo interpretador Python atual
#         subprocess.Popen([sys.executable, script_path])

#         # Retorna um JSON de sucesso com status 200 (OK)
#         return jsonify({'status': 'Jogo iniciado com sucesso'}), 200
#     except Exception as e:
#         # Em caso de erro, retorna mensagem de erro com status 500 (Erro Interno do Servidor)
#         return jsonify({'error': str(e)}), 500


# # Verifica se o script está sendo executado diretamente (não importado)
# if __name__ == '__main__':
#     # Inicia o servidor Flask
#     # debug=True ativa o modo de depuração
#     # port=5000 define a porta do servidor
#     app.run(debug=True, port=5000)
