# O filtro de abertura é uma operação morfológica utilizada principalmente para remover ruídos pequenos em imagens.
# Ele consiste na aplicação de duas etapas sequenciais:
#   1. Erosão: Remove pixels das bordas dos objetos, diminuindo áreas pequenas e desconectadas.
#   2. Dilatação: Restaura o tamanho dos objetos após a erosão, mas sem os ruídos removidos.
#
# Essa operação é muito útil em pré-processamento de imagens binárias ou em imagens com pequenas imperfeições.
# Neste código, utilizamos um kernel retangular 5x5 para aplicar a abertura usando a função `cv2.morphologyEx`.
# Ao final, a imagem original e a filtrada são exibidas lado a lado para comparação.


import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image
import os

# Caminho da imagem original
caminho_original = r'Processamento Básico de Imagens\6_Filtros_Morfologicos\gato_abertura_original.jpg'

# Abrir imagem com PIL
img_pil = Image.open(caminho_original).convert("RGB")

# Converter para array numpy e para BGR
img_original = np.array(img_pil)
img_original = cv2.cvtColor(img_original, cv2.COLOR_RGB2BGR)

# Corrigir a conversão para escala de cinza
colors = cv2.cvtColor(img_original, cv2.COLOR_RGB2BGR)

# Criar kernel e aplicar abertura (erosão + dilatação)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
abertura = cv2.morphologyEx(colors, cv2.MORPH_OPEN, kernel)

# Mostrar as imagens
fig, axs = plt.subplots(1, 2, figsize=(12, 6))
img_original_rgb = cv2.cvtColor(img_original, cv2.COLOR_BGR2RGB)

axs[0].imshow(img_original_rgb)
axs[0].set_title("Imagem Original")
axs[0].axis("off")

axs[1].imshow(abertura)
axs[1].set_title("Filtro Abertura")
axs[1].axis("off")

plt.tight_layout()
plt.show()

# Converter para PIL e salvar
Image.fromarray(abertura).save(r'Processamento Básico de Imagens\6_Filtros_Morfologicos\gato_abertura.jpg')
