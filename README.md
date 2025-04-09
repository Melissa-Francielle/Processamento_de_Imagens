# TRABALHO DA DISCIPLINA DE COMPUTAÇÃO GRÁFICA
Universidade Estadual do Norte do Paraná

Doscente: Welligton Della Mura
Curso: Ciência da Computação

Discente: Melissa Francielle dos Santos - 4º ano.
______________________

# Implementação: processamento básico de imagens 

### Especificação: criar um conjunto de scripts em Python (ou outra linguagem) que contemple as seguintes funcionalidades 

1. Realce e Ajuste de Intensidade (melhorar contraste e brilho)
2. Redução de Ruído e Suavização (remover imperfeições)
3. Detecção de bordas (identificar contornos e formas)
4. Detecção de formas e texturas (identificar padrões na imagem)
5. Transformações geometricas (redimensionamento e distorção)
6. Filtros Morfológicos (processamento de imagens segmentadas)
_______________

# FILTROS
### 1.Realce e Ajuste
* Correção gama (ajusta o brilho de forma não linear).
  
  A correção gama é um método de ajuste de brilho e contraste de imagens para que elas se adequem à percepção humana. É uma técnica não linear que envolve aplicar uma função de potência aos valores de intensidade de uma imagem. Exemplo: Na fotografica, a correção gama é usada para ajustar a imagem reproduzida.

  [Código Python](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/1_Realce_Ajuste/correcao_gama.py)

  [Imagem Original](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/1_Realce_Ajuste/Gato_original.jpg)

  [Resultado](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/1_Realce_Ajuste/Gato_correcao_gama.jpg)

## Comparação do antes e após o processamento
![Gato com Correção Gama](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/Comparações_Processamento/Correcao_gama.png)

### 2.Suavização e Redução de Ruídos
* Gaussiano (Aplica suavização preservando bordas).

    O efeito Gaussiano, ou desforque gaussiano, é um efeito de desfocagem que suaviza imagens e reduz ruídos. Ele é usado em design gráfico e edição de fotos. Usasse uma função matemática chamada função Gaussiana para calcular a intensidade de cada pixel.

    [Código Python](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/2_Suavização_Redução_Ruídos/gaussiano.py)

    [Imagem Original](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/2_Suavização_Redução_Ruídos/Gato_ruido_original.png)
  
    [Resultado](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/2_Suavização_Redução_Ruídos/Gato_gaussiano.png)

## Comparação do antes e após o processamento
![Gato com Filtro Gaussiano](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/Comparações_Processamento/Filtro_Gaussiano.png)

### 3.Detecção de bordas 
* Canny (Combina suavização e gradientes para bordas mais limpas).

    O filtro Canny é um filtro de convolução que usa a primeira derivada. Suavizando o ruído e localizando as bordas, combinando um operador diferencial com um filtro Gaussiano. 

    [Código Python](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/3_Deteccao_Bordas/canny.py)

    [Imagem Original](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/3_Deteccao_Bordas/Gato_canny_original.jpg)
  
    [Resultado](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/3_Deteccao_Bordas/Gato_canny.png)

## Comparação do antes e após o processamento
![Gato com Filtro Canny](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/Comparações_Processamento/Filtro_Canny.png)

### 4.Detecção de formas e texturas
* Transformada em Hough (Detecta linhas e circulos na imagem).

    A Transformada de Hough é uma técnica de extração de características usada em análise de imagens, visão computacional, reconhecimento de padrões e processamento digital de imagens.

    [Código Python](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/4_Deteccao_Formas_Texturas/transformacao_hough.py)

    [Imagem Original](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/4_Deteccao_Formas_Texturas/Gato_hough_original.png)
  
    [Resultado](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/4_Deteccao_Formas_Texturas/Gato_hough.png)

  ![Gato com filtro hough](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/Comparações_Processamento/Filtro_Hough.png)
### 5.Transformações geometricas
* Interpolação Bilinear/Bicúbica (redimensiona imagens).

    A interpolação bilinear é uma técnica de reamostragem que calcula novos valores de pixel a partir dos valores de pixel mais próximos. É utilziada em processamento de imagens e visão computacional. 

    [Código Python](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/5_Transformacao_Geometrica/interpolacao_bilinear.py)

    [Imagem Original](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/5_Transformacao_Geometrica/gato_bilinear_original.jpg)
  
    [Resultado](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/5_Transformacao_Geometrica/gato_bilinear.jpg)
  
   ![Gato com interpolacao](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/Comparações_Processamento/Interpolacao_bilinear.png)
### 6.Filtros Morfológicos
* Abertura (Remove pequenos objetos sem alterar a forma principal).

    É uma operação usada para imagens binárias e também em tons de cinza. Formando duas operações em sequência. Serve para remoção de ruídos pequenos, separação de obejtos conectados por pontes finas, limpar contornos, usados com frequência para OCR.

    [Código Python](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/6_Filtros_Morfologicos/abertura.py)

    [Imagem Original](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/6_Filtros_Morfologicos/gato_abertura_original.jpg)
  
    [Resultado](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/6_Filtros_Morfologicos/gato_abertura.jpg)

     ![Gato com filtro de abertura](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/Comparações_Processamento/Abertura.png)

### Imagens de Referência para o processamento 
**Imagem usada no processamento de Gama:**

> SUM, Michael. *Fotografia de luz solar em floresta*. 2023. Disponível em: https://images.squarespace-cdn.com/content/v1/607f89e638219e13eee71b1e/1684821560422-SD5V37BAG28BURTLIXUQ/michael-sum-LEpfefQf4rU-unsplash.jpg. Acesso em: 9 abr. 2025.

**Imagem usada no processamento Gaussiano:**

> TWITTER. *Imagem de gato publicada em @culturismoftbl*. Disponível em: https://pbs.twimg.com/media/F775U4sXQAA_gDE.jpg:large. Acesso em: 9 abr. 2025.

**Imagem usada no processamento Canny:**

> YOUTUBE. *Miniatura do vídeo "Filtro de detecção de bordas Canny - Python e OpenCV"*. Disponível em: https://i.ytimg.com/vi/czR6DrMptJE/hqdefault.jpg. Acesso em: 9 abr. 2025.

**Imagem utilizada no processamento de Hough:**

> VIRAL HUNTZ. *AA7AF416-7733-457C-938D-F38F00A49627.jpg*. [Imagem]. Disponível em: https://viralhuntz.shop/cdn/shop/files/AA7AF416-7733-457C-938D-F38F00A49627.jpg. Acesso em: 9 abr. 2025.

**Imagem utilizada na interpolação:**

> PINTEREST. *Gato pixelado em 3/4 perfil*. [Imagem]. Disponível em: https://i.pinimg.com/564x/98/2d/4b/982d4b383ed2cd2a6a965f3c00e95f90.jpg. Acesso em: 9 abr. 2025.

**Imagem utilizada no filtro de abertura:**

> WIKIPEDIA. *Longcat is loooooooooong*. [Imagem]. Disponível em: https://upload.wikimedia.org/wikipedia/en/3/3d/Longcat_is_loooooooooong.jpg. Acesso em: 9 abr. 2025.



