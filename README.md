## Implementação do trabalho 1 da disciplina de Processamento Digital de Imagens (PDI) 🖼

### 📚 Organização do repositório 
- Pasta **images** contendo as imagens disponibilizada pelo professor da disciplina para realização dos testes;
- Quatro arquivos com extenção **.txt**: 1. emboss, 2. filtro_media_21x21, 3. prewitt_x e 4. prewitt_y;
- Esses arquivos foram gerados utilizando o código do arquivo *generate_filter* feito pelos alunos, afim de serem utilizados como máscaras nas imagens.
- Arquivo **pdi.ipynb**, contendo todas as questões pedidas no trabalho.
- E uma pasta **.ipynb_checkpoints** contendo os checkpoints do projeto.

### 📄 Descrição das tarefas 
Foi utilizada a linguagem de programação *Python*, para desenvolver um sistema para abrir, exibir, manipular e salvar imagens RGB com 24 bits/pixel (8 bits/componente/pixel). 
O grupo não pode usar bibliotecas ou funções especiais de processamento de imagens, exceto no item 6. 
O sitema deveria possuir as seguinte funcionalidade:

1. Conversão RGB-YIQ-RGB (cuidado com os limites de R, G e B na volta!).
2. Negativo. Duas formas de aplicação devem ser testadas: em RGB (banda a banda) e na banda Y, com posterior conversão para RGB.
3. Correlação m x n sobre R, G e B, com offset, e filtro especificado em um arquivo (txt) a parte. Testado com filtros Média, Prewitt e Emboss e explicar os resultados. Para visualização, utilizou-se o valor absoluto seguido por expansão de histograma para [0, 255].
4. Comparação da aplicação do filtro média 21x21 com a aplicação do filtro média 21x1 seguido pela aplicação do filtro média 1x21, em termos de tempo de processamento e resultado final, para a banda Y do YIQ.
5. Filtro mediana m x n sobre a banda Y do YIQ.
6. Reprodução do exemplo em https://la.mathworks.com/help/images/ref/normxcorr2.html?lang=en, com as imagens woman.png e woman_eye.png, mas aplicando a correlação normalizada banda a banda e tomando como resultado o valor máximo das três correlações, em cada ponto. Para este item pode-se utilizar bibliotecas avançadas. Para visualização, foi utilizado o valor absoluto seguido por expansão de histograma para [0, 255].
7. Reprodução o item 6 utilizando a função correlação desenvolvida no item 3. Para visualização, foi utilizado o valor absoluto seguido por expansão de histograma para [0, 255].

### ⚙ Como rodar o projeto 

1. Faça um clone do repositório
2. Use o Jupyter ou Colab para abrir o projeto
3. No Colab clique em Ambiente de execução -> Executar Tudo, ou use o comando ctrl+F9.
4. No Jupyter basta clicar em *run*
