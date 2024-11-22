// Função para abrir o modal de informações do jogo
function iniciarJogo() {
    // Torna o modal visível alterando o estilo de display
    document.getElementById('mensagemModal').style.display = 'block';
}

// Função para fechar o modal
function fecharModal() {
    // Oculta o modal alterando o estilo de display
    document.getElementById('mensagemModal').style.display = 'none';
}

// Função principal para executar o jogo
function executarJogo() {
    document.getElementById('jogar').style.display = 'block';

    // Fecha o modal de informações
    fecharModal();

    // Faz uma requisição para o endpoint do jogo (ajustando a URL para um endpoint Flask correto)
    fetch('/testeForca', {  // '/JogoDaForca' o endpoint correto
        method: 'GET' // Usa o método GET para solicitar iniciar o jogo
    })
        .then(response => response.json()) // Converte a resposta para JSON
        .then(data => {
            console.log('Jogo iniciado:', data.mensagem); // Loga a mensagem de status no console
        })
        .catch(error => console.error('Erro ao iniciar jogo:', error)); // Captura e exibe possíveis erros
    document.getElementById('loading').classList.add('active');
    fetch('/JogoDaForca')
        .then(response => response.json())
        .then(data => {
            console.log(data.mensagem);
            document.getElementById('loading').classList.remove('active');
        })
        .catch(error => {
            console.error(error);
            document.getElementById('loading').classList.remove('active');
        });
}

// Evento para fechar o modal se clicar fora dele
window.onclick = function (event) {
    // Obtém o elemento do modal
    let modal = document.getElementById('mensagemModal');

    // Verifica se o clique foi fora do conteúdo do modal
    if (event.target == modal) {
        // Fecha o modal
        modal.style.display = 'none';
    }
}