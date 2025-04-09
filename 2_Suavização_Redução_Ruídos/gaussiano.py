from PIL import Image
from PIL import ImageFilter
import matplotlib.pyplot as plt
import numpy as np

# Caminho da imagem original
caminho_original = r'Processamento Básico de Imagens\2_Suavização_Redução_Ruídos\Gato_ruido_original.png'

# Abrir imagem original
img_original = Image.open(caminho_original).convert("RGB")

# Clonar a imagem para aplicar a correção gama
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

# Salvar a imagem corrigida
img_gaussiana.save(r'Processamento Básico de Imagens\2_Suavização_Redução_Ruídos\Gato_gaussiano.png')
