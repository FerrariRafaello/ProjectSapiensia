# ProjectSapiensia
# ProjectSapiensia

Bem-vindo ao **ProjectSapiensia**! 

Este é um projeto que visa a extração e exibição de dados de forma adaptativa e responsiva. Se você está aqui, é porque provavelmente está interessado em como isso funciona. Então, vamos direto ao ponto!

## O que é isso?

ProjectSapiensia é uma aplicação web simples que extrai dados e exibe de maneira estilosa e responsiva. A aplicação tem uma tela de carregamento bacana e dois modos de extração de dados: automática (últimas 12 horas) e manual.

## Como funciona?

Quando você acessa a aplicação, ela mostra uma tela de carregamento por 2 segundos dizendo "Extraindo dados...". Depois disso, os dados extraídos das últimas 12 horas são exibidos em um retângulo estiloso no centro da tela.

Se você clicar no botão "Extrair Manualmente", outra tela de carregamento aparece dizendo "Extraindo dados manualmente..." e, em seguida, a página de extração manual é exibida.

## Estrutura do Projeto

- `templates/`
  - **index.html**: Página principal que exibe os dados extraídos automaticamente.
  - **manual_extraction.html**: Página de extração manual dos dados.

- `static/`
  - **style.css**: Arquivo de estilo que deixa a aplicação bonita e responsiva.

## Como rodar?

1. Clone este repositório:
   ```sh
   git clone https://github.com/FerrariRafaello/ProjectSapiensia.git
   cd ProjectSapiensia
   
## Observações:
Certifique-se de que você tem o Python e o Flask instalados. Se não, instale:

sh
sudo apt-get install python3
pip install flask
Rode a aplicação:

sh
python3 app.py
Abra o navegador e acesse http://127.0.0.1:5000.

## Contribuições
Curtiu o projeto e quer contribuir? Sinta-se à vontade para abrir um PR. Qualquer melhoria é bem-vinda!

## Licença
Este projeto está sob a licença MIT. Faça bom uso!
