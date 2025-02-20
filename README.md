# #Projeto de Reconhecimento de Rostos e Objetos em Imagens

Este projeto tem como objetivo demonstrar como utilizar bibliotecas de visão computacional para realizar o reconhecimento de rostos e a detecção de objetos em imagens. A implementação foi feita totalmente em Python utilizando as bibliotecas OpenCV e face_recognition.

Embora o projeto seja baseado no desafio proposto pelo Microsoft Learn - AI Fundamentals, a solução foi construída localmente sem o uso da plataforma Azure. Ele permite a detecção de rostos e objetos em imagens, gerando saídas tanto visuais quanto textuais, com o objetivo de facilitar a análise de imagens em contextos como segurança ou atendimento ao cliente.

# Objetivo
O objetivo deste projeto é identificar rostos e objetos em imagens usando técnicas de visão computacional. A solução detecta os rostos nas imagens e os destaca com caixas delimitadoras, além de gerar informações sobre os objetos encontrados.

# Funcionalidades
Detecção de rostos em imagens utilizando a biblioteca face_recognition.
Detecção de objetos em imagens utilizando o classificador Haar do OpenCV (aqui, "objetos" são representados como rostos, mas o sistema pode ser expandido para outros tipos de objetos).
Manipulação de imagens para desenhar caixas delimitadoras e textos, com a ajuda da biblioteca PIL.
Exibição de uma barra de progresso durante o processamento das imagens com a biblioteca progressbar2.
Bibliotecas Utilizadas
OpenCV: Para o processamento de imagens e detecção de objetos (classificador Haar).
face_recognition: Para o reconhecimento de rostos nas imagens.
Pillow (PIL): Para manipulação de imagens (desenhando caixas ao redor dos rostos e textos informativos sobre os objetos detectados).
progressbar2: Para exibir uma barra de progresso durante o processamento das imagens.
Estrutura do Projeto
inputs/: Contém as imagens que serão processadas. (Estas imagens são apenas exemplos).
output/: Contém as imagens com as caixas de rostos detectados e os arquivos de texto gerados com informações sobre os rostos e objetos detectados.
# Como Usar
Clone o repositório:
git clone https://github.com/Fabianonavarro/ocr-image-analysis.git

# Instale as dependências:
pip install -r requirements.txt

Coloque suas imagens na pasta inputs/.
Execute o script Python:

python processar_imagens.py

# Funcionalidade Interativa

O script permite processar todas as imagens ou escolher uma imagem específica para análise.
Durante o processamento, será exibida uma barra de progresso para acompanhamento.
Exemplos de Imagens e Resultados:
Exemplo de Imagem Original: Antes de processar, as imagens estão na pasta inputs/.
Exemplo de Imagem Processada: Após o processamento, a imagem terá caixas delimitadoras em torno dos rostos detectados e um texto indicando a quantidade de rostos e objetos encontrados.

Resultados Esperados
Imagens processadas com caixas delimitadoras ao redor dos rostos.
Arquivos de texto gerados com detalhes sobre os rostos e objetos detectados.
Licença
Este projeto é de código aberto e distribuído sob a licença MIT.

# Aprendizados e Possíveis Melhorias:

Durante o desenvolvimento deste projeto, aprendi a:

Utilizar a biblioteca face_recognition para detectar rostos em imagens.
Aplicar o OpenCV para detectar objetos (neste caso, rostos) através de um classificador Haar.
Manipular imagens com a biblioteca PIL, sobrepondo texto e caixas de destaque.
Trabalhar com barras de progresso para monitoramento de grandes quantidades de imagens.
Possíveis Melhorias Futuras:
Integrar o reconhecimento de outros objetos além de rostos.
Melhorar a precisão do reconhecimento de rostos em imagens com baixa qualidade.
Utilizar redes neurais mais avançadas para a detecção de objetos.
Permitir a detecção em tempo real, utilizando uma câmera ao invés de apenas imagens estáticas.
Conclusão
Embora este projeto tenha sido desenvolvido com Python, ele se inspira no desafio do Microsoft Learn - AI Fundamentals, adaptando-o para uma solução local sem a necessidade de usar plataformas em nuvem como o Azure. O código resultante oferece uma solução flexível e acessível para detecção de rostos e objetos em imagens, com diversas possibilidades de melhorias e expansões.

