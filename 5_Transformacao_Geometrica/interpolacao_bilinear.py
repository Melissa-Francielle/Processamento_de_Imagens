# A interpolação bilinear é uma técnica usada para redimensionar imagens (ampliar ou reduzir),
# preservando a suavidade entre os pixels. Diferente da interpolação mais simples (vizinho mais próximo),
# ela calcula a média ponderada de 4 pixels vizinhos para estimar a cor de um novo pixel.
#
# Nesse exemplo, a imagem original é reduzida com um fator de escala (10% do tamanho original).
# Para cada novo pixel da imagem redimensionada, localizamos sua posição correspondente na imagem original
# e usamos os quatro vizinhos ao redor para calcular o novo valor de cor.
# Esse cálculo leva em conta a distância proporcional de cada vizinho (dx, dy), gerando uma transição mais suave.
#
# Ao final, exibimos a imagem original e a redimensionada lado a lado para comparação.

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Abrir imagem e converter para RGB
img = Image.open(r'Processamento Básico de Imagens\5_Transformacao_Geometrica\gato_bilinear_original.jpg').convert("RGB")
arr = np.array(img)
orig_h, orig_w, channels = arr.shape

# Fator de escala
escala = 0.1
new_h = int(orig_h * escala)
new_w = int(orig_w * escala)

# Nova imagem vazia
nova_img = np.zeros((new_h, new_w, channels), dtype=np.uint8)

# Para cada pixel na nova imagem
for i in range(new_h):
    for j in range(new_w):
        # Coordenadas na imagem original
        y = i / escala
        x = j / escala

        y1 = int(y)
        x1 = int(x)
        y2 = min(y1 + 1, orig_h - 1)
        x2 = min(x1 + 1, orig_w - 1)

        dy = y - y1
        dx = x - x1

        for c in range(channels):
            p11 = arr[y1, x1, c]
            p21 = arr[y1, x2, c]
            p12 = arr[y2, x1, c]
            p22 = arr[y2, x2, c]

            valor = (p11 * (1 - dx) * (1 - dy) +
                     p21 * dx * (1 - dy) +
                     p12 * (1 - dx) * dy +
                     p22 * dx * dy)

            nova_img[i, j, c] = int(valor)

# Mostrar resultado
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(arr)
plt.title("Imagem Original")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(nova_img)
plt.title(f"Imagem Redimensionada (x{escala})")
plt.axis("off")
plt.tight_layout()
plt.show()

# Salvar imagem resultante
Image.fromarray(nova_img).save(r'Processamento Básico de Imagens\5_Transformacao_Geometrica\gato_bilinear.jpg')
