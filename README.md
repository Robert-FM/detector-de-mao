# ✋ Detector de Mãos

Aplicação Python para detecção de mãos e pontos de referência (landmarks) em tempo real a partir da câmera do computador. O projeto utiliza MediaPipe para processar as mãos e OpenCV para captura, manipulação e exibição dos frames.

## 🎯 Objetivo

Demonstrar uma base reutilizável para identificar mãos em imagens capturadas pela webcam, desenhar suas conexões e destacar pontos específicos. A classe `DetectorMaos` concentra a integração com o MediaPipe.

## 🚀 Funcionalidades

- 📹 Captura de vídeo pela câmera padrão.
- ✋ Detecção de até duas mãos por frame.
- 🔗 Desenho dos landmarks e conexões.
- 📍 Obtenção das coordenadas dos pontos detectados.
- 🎨 Destaque visual de um ponto específico.
- ⚙️ Configuração de confiança, rastreamento e cores dos desenhos.

## 🛠️ Tecnologias utilizadas

- Python 3.11 ou superior
- OpenCV (`opencv-python`) 4.11.0.86
- MediaPipe 0.10.21
- NumPy 1.26.4
- `uv` para gerenciamento do ambiente e dependências

## 📁 Organização do projeto

```text
.
├── detectormaos.py   # Classe de detecção e extração dos pontos das mãos
├── main.py           # Ponto de entrada e demonstração com a webcam
├── pyproject.toml    # Metadados e dependências
├── uv.lock           # Versões resolvidas pelo uv
├── .python-version   # Versão indicada: 3.11
└── .gitignore        # Arquivos ignorados pelo Git
```

O diretório `.venv`, quando presente, é um ambiente virtual local e não é necessário para publicar o projeto.

## ✅ Pré-requisitos

- Python 3.11 ou superior.
- Uma câmera acessível pelo computador.
- Permissão para o Python acessar a câmera.
- `uv` instalado, caso seja utilizado o método recomendado.

## 📦 Instalação com `uv`

O projeto possui `pyproject.toml` e `uv.lock`:

```bash
uv sync
uv run python main.py
```

Não há dependências de desenvolvimento declaradas.

## 🐍 Instalação tradicional com `pip`

Crie e ative um ambiente virtual:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

No Linux/macOS, use `source .venv/bin/activate`. Depois instale as dependências:

```bash
python -m pip install --upgrade pip
python -m pip install mediapipe==0.10.21 numpy==1.26.4 opencv-python==4.11.0.86
```

## ▶️ Como executar

```bash
python main.py
```

O programa acessa a câmera de índice `0`, espelha a imagem horizontalmente e abre uma janela chamada `Capitura` com os landmarks detectados. Para encerrar, interrompa o processo no terminal ou feche a janela.

## 💻 Como utilizar a classe

O fluxo utilizado em `main.py` é:

```python
detector = DetectorMaos()
imagem = detector.encontrar_maos(imagem)
lista_pontos = detector.encontrar_pontos(imagem, ponto_detectado=0)
```

`encontrar_maos` processa um frame BGR e desenha as mãos por padrão. `encontrar_pontos` retorna uma lista no formato `[id, x, y]` para os landmarks da mão selecionada.

## 🔧 Dependências e configuração

As dependências diretas e suas versões estão em `pyproject.toml` e travadas em `uv.lock`. O projeto não possui arquivos `.env`, variáveis de ambiente, banco de dados ou serviços externos configurados.

## 🧪 Testes

Não foram encontrados testes automatizados. A validação disponível é a execução da aplicação com uma câmera compatível.

## 💡 Possíveis melhorias

Podem ser considerados o tratamento de falhas na câmera, uma forma explícita de encerrar o loop e testes para componentes que não dependam de uma câmera física.

## 👤 Autor

**Robert Melo**

🔗 LinkedIn: [linkedin.com/in/robertdemelo](https://www.linkedin.com/in/robertdemelo/)

🐍 Python | OpenCV | MediaPipe | Visão Computacional | Processamento de Imagens
