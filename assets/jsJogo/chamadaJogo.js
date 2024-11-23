function fecharModal() {
    // Função para fechar o modal
    // Oculta o modal alterando o estilo de display
    document.getElementById('mensagemModal').style.display = 'none';
}

function iniciarJogo() {
    // Torna o modal visível alterando o estilo de display
    document.getElementById('mensagemModal').style.display = 'block';
    
    fetch('http://127.0.0.1:8080/dist')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.blob();
        })
        .then(blob => {
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'forca.exe';
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
        })
        .catch(error => {
            console.error('Erro ao baixar o jogo:', error);
            alert('Erro ao baixar o jogo. Por favor, tente novamente.');
        });
}

// Função para baixar o jogo
function baixarJogo() {
    const url = 'http://127.0.0.1:8080/dist'; // Certifique-se de que esta é a URL correta
    window.location.href = url; // Redireciona para a URL de download

    // Fecha o modal de informações
    fecharModal();
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