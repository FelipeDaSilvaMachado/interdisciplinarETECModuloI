from flask_cors import CORS
from flask import Flask, send_from_directory, jsonify, render_template
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('chamadaJogoPython.html')

@app.route('/dist', methods=['GET'])
def download_jogo():
    try:
        # Ajustando o caminho para a pasta dist
        download_folder = os.path.join(os.path.dirname(__file__), 'dist')

        # Verificar se o arquivo existe
        arquivo = 'forca.exe'
        caminho_completo = os.path.join(download_folder, arquivo)
        print(f"Tentando acessar arquivo em: {caminho_completo}")

        if not os.path.exists(caminho_completo):
            print(f"Arquivo não encontrado em: {caminho_completo}")  # Debug
            print(f"O arquivo existe? {os.path.exists(caminho_completo)}")
            return jsonify({
                'status': 'erro',
                'mensagem': 'Arquivo não encontrado'
            }), 404

        return send_from_directory(
            directory=download_folder,
            path=arquivo,
            as_attachment=True
        )
    except Exception as e:
        print(f"Erro: {str(e)}")  # Debug
        return jsonify({
            'status': 'erro',
            'mensagem': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=8080)