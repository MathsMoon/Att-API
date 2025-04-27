const apiUrlUsuarios = 'https://api.com/usuarios';

async function carregarUsuarios() {
    const response = await fetch(apiUrlUsuarios);
    const usuarios = await response.json();
    
    const usuariosList = document.getElementById('usuarios-list');
    usuariosList.innerHTML = ''; // Limpar lista existente
    
    usuarios.forEach(usuario => {
        const usuarioElement = document.createElement('div');
        usuarioElement.innerHTML = `
            <p><strong>${usuario.nome}</strong> - ${usuario.email}</p>
            <hr>
        `;
        usuariosList.appendChild(usuarioElement);
    });
}

async function adicionarUsuario(event) {
    event.preventDefault();
    
    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
    const senha = document.getElementById('senha').value;
    
    const novoUsuario = {
        nome,
        email,
        senha
    };
    
    const response = await fetch(apiUrlUsuarios, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(novoUsuario)
    });
    
    if (response.ok) {
        alert('Usuário adicionado com sucesso!');
        carregarUsuarios(); // Recarregar a lista de usuários
    } else {
        alert('Erro ao adicionar usuário');
    }
}

document.addEventListener('DOMContentLoaded', carregarUsuarios);
document.getElementById('add-usuario-form').addEventListener('submit', adicionarUsuario);