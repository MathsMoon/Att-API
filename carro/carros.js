const apiUrl = 'https://api.com/carros';

// Função para carregar e exibir a lista de carros
async function carregarCarros() {
    const response = await fetch(apiUrl);
    const carros = await response.json();
    
    const carrosList = document.getElementById('carros-list');
    carrosList.innerHTML = ''; // Limpar lista existente
    
    carros.forEach(carro => {
        const carroElement = document.createElement('div');
        carroElement.innerHTML = `
            <p><strong>${carro.nome}</strong> - ${carro.modelo} (${carro.ano})</p>
            <p>Preço: R$ ${carro.preco.toFixed(2)}</p>
            <hr>
        `;
        carrosList.appendChild(carroElement);
    });
}

// Função para adicionar um novo carro
async function adicionarCarro(event) {
    event.preventDefault();
    
    const nome = document.getElementById('nome').value;
    const modelo = document.getElementById('modelo').value;
    const ano = document.getElementById('ano').value;
    const preco = document.getElementById('preco').value;
    
    const novoCarro = {
        nome,
        modelo,
        ano,
        preco
    };
    
    const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(novoCarro)
    });
    
    if (response.ok) {
        alert('Carro adicionado com sucesso!');
        carregarCarros(); // Recarregar a lista de carros
    } else {
        alert('Erro ao adicionar carro');
    }
}

// Carregar os carros ao carregar a página
document.addEventListener('DOMContentLoaded', carregarCarros);

// Adicionar o carro quando o formulário for enviado
document.getElementById('add-carro-form').addEventListener('submit', adicionarCarro);