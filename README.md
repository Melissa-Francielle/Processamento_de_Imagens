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



### 2.Suavização e Redução de Ruídos
* Gaussiano (Aplica suavização preservando bordas).

    O efeito Gaussiano, ou desforque gaussiano, é um efeito de desfocagem que suaviza imagens e reduz ruídos. Ele é usado em design gráfico e edição de fotos. Usasse uma função matemática chamada função Gaussiana para calcular a intensidade de cada pixel.

    [Código Python](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/2_Suavização_Redução_Ruídos/gaussiano.py)

    [Imagem Original](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/2_Suavização_Redução_Ruídos/Gato_ruido_original.png)
  
    [Resultado](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/2_Suavização_Redução_Ruídos/Gato_gaussiano.png)

### 3.Detecção de bordas 
* Canny (Combina suavização e gradientes para bordas mais limpas).

    O filtro Canny é um filtro de convolução que usa a primeira derivada. Suavizando o ruído e localizando as bordas, combinando um operador diferencial com um filtro Gaussiano. 

    [Código Python](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/3_Deteccao_Bordas/canny.py)

    [Imagem Original](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/3_Deteccao_Bordas/Gato_canny_original.jpg)
  
    [Resultado](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/3_Deteccao_Bordas/Gato_canny.png)
### 4.Detecção de formas e texturas
* Transformada em Hough (Detecta linhas e circulos na imagem).

    A Transformada de Hough é uma técnica de extração de características usada em análise de imagens, visão computacional, reconhecimento de padrões e processamento digital de imagens.

    [Código Python](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/4_Deteccao_Formas_Texturas/transformacao_hough.py)

    [Imagem Original](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/4_Deteccao_Formas_Texturas/Gato_hough_original.png)
  
    [Resultado](URL)
### 5.Transformações geometricas
* Interpolação Bilinear/Bicúbica (redimensiona imagens).

    A interpolação bilinear é uma técnica de reamostragem que calcula novos valores de pixel a partir dos valores de pixel mais próximos. É utilziada em processamento de imagens e visão computacional. 

    [Código Python](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/5_Transformacao_Geometrica/interpolacao_bilinear.py)

    [Imagem Original](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/5_Transformacao_Geometrica/gato_bilinear_original.jpg)
  
    [Resultado](URL)
### 6.Filtros Morfológicos
* Abertura (Remove pequenos objetos sem alterar a forma principal).

    É uma operação usada para imagens binárias e também em tons de cinza. Formando duas operações em sequência. Serve para remoção de ruídos pequenos, separação de obejtos conectados por pontes finas, limpar contornos, usados com frequência para OCR.

    [Código Python](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/6_Filtros_Morfologicos/abertura.py)

    [Imagem Original](https://github.com/Melissa-Francielle/Processamento_de_Imagens/blob/main/6_Filtros_Morfologicos/gato_abertura_original.jpg)
  
    [Resultado](URL)
