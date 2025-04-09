import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image
import os

# Caminho da imagem original
caminho_original = r'Processamento Básico de Imagens\6_Filtros_Morfologicos\gato_abertura_original.jpg'

# Abrir imagem com PIL
img_pil = Image.open(caminho_original).convert("RGB")

# Converter para array numpy e para BGR (formato do OpenCV)
img_original = np.array(img_pil)
img_original = cv2.cvtColor(img_original, cv2.COLOR_RGB2BGR)

# Corrigir a conversão para escala de cinza
gray = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)

# Criar kernel e aplicar abertura (erosão + dilatação)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
abertura = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)

# Mostrar as imagens
fig, axs = plt.subplots(1, 2, figsize=(12, 6))
img_original_rgb = cv2.cvtColor(img_original, cv2.COLOR_BGR2RGB)

axs[0].imshow(img_original_rgb)
axs[0].set_title("Imagem Original")
axs[0].axis("off")

axs[1].imshow(abertura, cmap='gray')
axs[1].set_title("Filtro Abertura")
axs[1].axis("off")

plt.tight_layout()
plt.show()

# Converter para PIL e salvar
Image.fromarray(abertura).save(r'Processamento Básico de Imagens\6_Filtros_Morfologicos\gato_abertura.jpg')
