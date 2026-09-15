import cv2
import mediapipe as mp


class DetectorMaos():
    def __init__(self,modo=False,max_maos=2,deteccao_confiaca=0.5,
                 rastreio_cofianca=0.5,cor_pontos=(0,0,255),cor_conexoes=(255,255,255)):
        self.modo = modo
        self.max_maos = max_maos
        self.deteccao_confianca = deteccao_confiaca
        self.rastreio_confianca = rastreio_cofianca
        self.cor_pontos = cor_pontos
        self.cor_conexoes = cor_conexoes

        self.maos_mp = mp.solutions.hands
        self.maos = self.maos_mp.Hands(
            self.modo,
            self.max_maos,
            model_complexity = 1,
            min_detection_confidence=self.deteccao_confianca,
            min_tracking_confidence=self.rastreio_confianca
        )

        self.desenho_mp = mp.solutions.drawing_utils

        self.desenho_config_pontos = self.desenho_mp.DrawingSpec(color=self.cor_pontos)

        self.desenho_config_conexoes = self.desenho_mp.DrawingSpec(color=self.cor_conexoes)


    def encontrar_maos(self,imagem,desenho=True):
        imagem_rgb = cv2.cvtColor(imagem,cv2.COLOR_BGR2RGB)

        self.resultado = self.maos.process(imagem_rgb)

        if self.resultado.multi_hand_landmarks:
            for pontos in self.resultado.multi_hand_landmarks:
                if desenho:
                    self.desenho_mp.draw_landmarks(
                        imagem,
                        pontos,
                        self.maos_mp.HAND_CONNECTIONS,
                        self.desenho_config_pontos,
                        self.desenho_config_conexoes
                    )
        return imagem
    
    def encontrar_pontos(self,imagem,mao_num=0,desenho=True,cor=(255,0,255),raio=8,
                         ponto_detectado=0):
        lista_pontos = []

        if self.resultado.multi_hand_landmarks:
            mao = self.resultado.multi_hand_landmarks[mao_num]

            for id,ponto in enumerate(mao.landmark):
                altura, largura, _ = imagem.shape

                centro_x, centro_y = int(ponto.x * largura), int(ponto.y * altura)

                lista_pontos.append([id,centro_x,centro_y])

                if desenho:
                    if id == ponto_detectado:
                        cv2.circle(
                        imagem,
                        center=(centro_x,centro_y),
                        radius=raio,
                        color = cor,
                        thickness=cv2.FILLED

                    )         

        return lista_pontos