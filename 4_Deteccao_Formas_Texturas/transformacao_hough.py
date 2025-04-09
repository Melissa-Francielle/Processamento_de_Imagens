from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import os

# Caminho da imagem original
caminho_original = r'Processamento Básico de Imagens\4_Deteccao_Formas_Texturas\Gato_hough_original.png'
img_pil = Image.open(caminho_original).convert("RGB")

# Converter para BGR para uso com OpenCV
img_original = np.array(img_pil)
img_original = cv.cvtColor(img_original, cv.COLOR_RGB2BGR)

# Copiar imagem para desenhar linhas
img_hough = img_original.copy()

# Detectar bordas com Canny
edges = cv.Canny(img_original, 50, 180)

# Aplicar Transformada de Hough
lines = cv.HoughLines(edges, 1, np.pi / 180, 120)

# Se linhas forem detectadas, desenhar
if lines is not None:
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv.line(img_hough, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Mostrar imagem original e com as linhas
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

axs[0].imshow(cv.cvtColor(img_original, cv.COLOR_BGR2RGB))
axs[0].set_title("Imagem Original")
axs[0].axis("off")

axs[1].imshow(cv.cvtColor(img_hough, cv.COLOR_BGR2RGB))
axs[1].set_title("Transformada de Hough")
axs[1].axis("off")

plt.tight_layout()
plt.show()

# Salvar imagem com linhas detectadas
img_hough_pil = Image.fromarray(cv.cvtColor(img_hough, cv.COLOR_BGR2RGB))
img_hough_pil.save(r'Processamento Básico de Imagens\4_Deteccao_Formas_Texturas\Gato_hough.png')
