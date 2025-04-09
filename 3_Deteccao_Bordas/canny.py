import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image
import os 

# Caminho da imagem original
caminho_original = r'Processamento Básico de Imagens\3_Deteccao_Bordas\Gato_canny_original.jpg'

# Abrir imagem com PIL (resolve problema com acentos no caminho)
img_pil = Image.open(caminho_original).convert("RGB")

# Converter para array numpy e para BGR (formato do OpenCV)
img_original = np.array(img_pil)
img_original = cv2.cvtColor(img_original, cv2.COLOR_RGB2BGR)

# Converter para escala de cinza
gray = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)

# Aplicar filtro Canny
threshold1 = 50
threshold2 = 150
edge = cv2.Canny(gray, threshold1, threshold2)

# Mostrar a imagem com as bordas detectadas (opcional)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Mostrar as duas imagens lado a lado com matplotlib
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Converter a imagem original para RGB para o matplotlib
img_original_rgb = cv2.cvtColor(img_original, cv2.COLOR_BGR2RGB)

axs[0].imshow(img_original_rgb)
axs[0].set_title("Imagem Original")
axs[0].axis("off")

axs[1].imshow(edge, cmap='gray')
axs[1].set_title(f"Filtro Canny (threshold1 = {threshold1}, threshold2 = {threshold2})")
axs[1].axis("off")

plt.tight_layout()
plt.show()

# Salvar a imagem. Converter a imagem Canny (numpy array) para PIL e salvar
img_canny = Image.fromarray(edge)
img_canny.save(r'Processamento Básico de Imagens\3_Deteccao_Bordas\Gato_canny.png')
