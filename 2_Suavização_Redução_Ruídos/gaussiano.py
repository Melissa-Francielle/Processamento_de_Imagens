
# O filtro gaussiano é uma técnica de suavização usada para reduzir ruídos e
# variações bruscas em imagens, mantendo suas bordas suaves.
# Ele funciona aplicando uma convolução com uma máscara baseada na função gaussiana,
# o que resulta em uma média ponderada dos pixels vizinhos.
# Neste código, a imagem original é carregada e processada com o filtro gaussiano
# usando a função GaussianBlur() da biblioteca PIL.
# O parâmetro 'radius' define o grau de suavização: quanto maior o valor, mais borrada
# a imagem fica.
# O resultado é exibido ao lado da imagem original e salvo em disco para comparação.

from PIL import Image
from PIL import ImageFilter
import matplotlib.pyplot as plt
import numpy as np

# Caminho da imagem original
caminho_original = r'Processamento Básico de Imagens\2_Suavização_Redução_Ruídos\Gato_ruido_original.png'

# Abrir imagem original
img_original = Image.open(caminho_original).convert("RGB")

# Clonar a imagem para aplicar o filtro gaussiano
img_gaussiana = img_original.copy()
matrix = img_gaussiana.load()

# Aplicar filtro gaussiano
r = 7
img_gaussiana = img_gaussiana.filter(ImageFilter.GaussianBlur(radius=r))

# Mostrar as duas imagens lado a lado
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Converter para array para exibir com matplotlib
axs[0].imshow(np.array(img_original))
axs[0].set_title("Imagem Original")
axs[0].axis("off")

axs[1].imshow(np.array(img_gaussiana))
axs[1].set_title(f"Filtro Gaussiano (radius= {r})")
axs[1].axis("off")

plt.tight_layout()
plt.show()

# Salvar a imagem filtrada
img_gaussiana.save(r'Processamento Básico de Imagens\2_Suavização_Redução_Ruídos\Gato_gaussiano.png')
