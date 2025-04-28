import pytesseract
import cv2
import os

#primeira vez usando isso entao provavelmente a documentacao vai me ajudar muito mais doq tudo

if os.name == 'nt':
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # ajuste se necessário

def extrair_texto_documento(path_arquivo):
    """Recebe o caminho da imagem do documento, retorna o texto extraído."""
    imagem = cv2.imread(path_arquivo)

    if imagem is None:
        raise ValueError("Não foi possível ler a imagem.")

    # Conversão para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Pré-processamento: suavização para reduzir ruídos
    imagem_tratada = cv2.GaussianBlur(imagem_cinza, (5,5), 0)

    # Binarização (thresholding)
    _, imagem_binaria = cv2.threshold(imagem_tratada, 127, 255, cv2.THRESH_BINARY)

    # OCR
    texto = pytesseract.image_to_string(imagem_binaria, lang='por')

    return texto
