# Conversor de Imagens para Tons de Cinza e Preto & Branco

Este projeto implementa a conversão manual de uma imagem colorida (RGB) para tons de cinza e binarizada (preto e branco) sem o uso de funções prontas de bibliotecas.

# Tecnologias Utilizadas

Python

NumPy

Matplotlib

ImageIO

Como Funciona

# O código possui duas funções principais:

rgb_to_grayscale(image): Converte uma imagem colorida para tons de cinza utilizando a fórmula de luminância.

grayscale_to_binary(image, threshold=128): Transforma uma imagem em tons de cinza para preto e branco, comparando os pixels com um limite (threshold).

# Como Executar

Instale as dependências, se necessário:

pip install numpy matplotlib imageio

Coloque a imagem desejada no mesmo diretório do código e renomeie-a para image.jpg (ou ajuste no código).

Execute o script Python.

As imagens convertidas serão exibidas na tela e salvas como grayscale_image.jpg e binary_image.jpg.

# Exemplo de Uso

Após rodar o código, três imagens serão exibidas:

Imagem Original

Imagem em Tons de Cinza

Imagem Binarizada (Preto e Branco)

Este projeto foi desenvolvido como um exercício de manipulação de imagens em Python sem utilizar funções prontas de conversão.
