from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Caminho da imagem original
caminho_original = r'C:\Users\melfr\OneDrive\Documentos\Faculdade\Materias\Computação Gráfica\Processamento Básico de Imagens\1_Realce_Ajuste\Gato_original.jpg'

# Abrir imagem original
img_original = Image.open(caminho_original).convert("RGB")

# Clonar a imagem para aplicar a correção gama
img_gamma = img_original.copy()
matrix = img_gamma.load()

# Aplicar correção gama
gamma = 0.7
for i in range(img_gamma.size[0]):
    for j in range(img_gamma.size[1]):
        r = int((matrix[i, j][0] / 255) ** gamma * 255)
        g = int((matrix[i, j][1] / 255) ** gamma * 255)
        b = int((matrix[i, j][2] / 255) ** gamma * 255)
        matrix[i, j] = (r, g, b)

# Mostrar as duas imagens lado a lado
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Converter para array para exibir com matplotlib
axs[0].imshow(np.array(img_original))
axs[0].set_title("Imagem Original")
axs[0].axis("off")

axs[1].imshow(np.array(img_gamma))
axs[1].set_title(f"Correção Gama (γ = {gamma})")
axs[1].axis("off")

plt.tight_layout()
plt.show()

# Salvar a imagem corrigida
img_gamma.save(r'C:\Users\melfr\OneDrive\Documentos\Faculdade\Materias\Computação Gráfica\Processamento Básico de Imagens\1_Realce_Ajuste\Gato_correcao_gama.jpg')
