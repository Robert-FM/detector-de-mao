import cv2
from detectormaos import DetectorMaos

def main():
    captura = cv2.VideoCapture(0)

    detector = DetectorMaos()

    while True:
        _, imagem = captura.read()

        imagem = cv2.flip(imagem,flipCode=1)

        imagem = detector.encontrar_maos(imagem)

        lista_pontos = detector.encontrar_pontos(imagem,ponto_detectado=0)
               
        cv2.imshow('Capitura', imagem)

        cv2.waitKey(1)

if __name__ == '__main__':
    main()