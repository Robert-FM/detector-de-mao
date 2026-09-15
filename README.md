# ✋ Detector de Mãos

Aplicação Python para detecção de mãos e extração de landmarks em tempo real a partir da webcam. O projeto combina MediaPipe Hands para o processamento da imagem com OpenCV para captura, transformação e exibição dos frames.

## 🎯 Objetivo

Disponibilizar uma implementação simples e reutilizável para detectar mãos, desenhar seus pontos de referência e conexões e obter as coordenadas dos landmarks identificados.

## ✨ Funcionalidades

- Captura de vídeo pela câmera padrão do computador.
- Espelhamento horizontal dos frames para uma visualização semelhante a um espelho.
- Detecção de até duas mãos por frame.
- Desenho dos landmarks e das conexões das mãos detectadas.
- Extração das coordenadas dos 21 landmarks da mão selecionada.
- Destaque visual de um landmark específico, configurável por identificador.
- Configuração do modo de detecção, número máximo de mãos, níveis de confiança e cores de desenho.

## 🛠️ Tecnologias utilizadas

- Python 3.11.
- OpenCV (`opencv-python`) 4.11.0.86.
- MediaPipe 0.10.21.
- NumPy 1.26.4.
- uv para gerenciamento do ambiente e das dependências.

## 🏗️ Organização do projeto

O fluxo principal é direto: `main.py` captura os frames da webcam, aplica o espelhamento, solicita a detecção à classe `DetectorMaos` e exibe a imagem processada. O módulo `detectormaos.py` encapsula a integração com MediaPipe e a conversão dos landmarks em coordenadas de pixels.

## 📁 Estrutura do projeto

```text
detector-mao/
├── detectormaos.py
├── main.py
├── pyproject.toml
├── uv.lock
├── .python-version
├── .gitignore
└── README.md
```

## 📋 Pré-requisitos

- Python 3.11 ou superior.
- Webcam acessível e permissão para o Python utilizá-la.
- uv, caso seja utilizado o método recomendado.

## 📦 Instalação

### ⚡ Opção 1 — uv

Com o uv instalado, sincronize o ambiente a partir do `pyproject.toml` e do `uv.lock`:

```bash
uv sync
```

### 🐍 Opção 2 — pip

```bash
python -m venv .venv
```

No Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

No Linux/macOS:

```bash
source .venv/bin/activate
```

Instale as dependências declaradas no projeto:

```bash
python -m pip install --upgrade pip
python -m pip install mediapipe==0.10.21 numpy==1.26.4 opencv-python==4.11.0.86
```

## ▶️ Como executar

Com uv:

```bash
uv run python main.py
```

Com o ambiente virtual ativado:

```bash
python main.py
```

O programa acessa a câmera de índice `0`, espelha cada frame e exibe a janela `Capitura` com os landmarks desenhados. O loop atual não define uma tecla de encerramento; interrompa o processo pelo terminal quando necessário.

## 💻 Como utilizar

A classe `DetectorMaos` pode ser utilizada sobre frames BGR do OpenCV:

```python
from detectormaos import DetectorMaos

detector = DetectorMaos()
imagem = detector.encontrar_maos(imagem)
lista_pontos = detector.encontrar_pontos(imagem, ponto_detectado=0)
```

`encontrar_maos` processa o frame e, por padrão, desenha os landmarks e as conexões. `encontrar_pontos` retorna uma lista no formato `[id, x, y]`, com coordenadas em pixels da mão selecionada.

## 📚 Dependências e configuração

As dependências diretas e suas versões estão declaradas em `pyproject.toml` e resolvidas em `uv.lock`. Não há variáveis de ambiente, arquivos `.env`, banco de dados, modelos locais adicionais ou serviços externos configurados.

## ✅ Testes

Não há testes automatizados ou framework de testes configurado no repositório. A validação prevista atualmente é a execução da aplicação com uma webcam disponível.

## 🚀 Possíveis melhorias

Podem ser considerados o tratamento de falhas na abertura ou leitura da câmera, uma tecla para encerrar o loop com segurança e testes unitários para a lógica que não depende de uma webcam física.

## 👨‍💻 Autor

**Robert Melo**

🔗 LinkedIn: [linkedin.com/in/robertdemelo](https://www.linkedin.com/in/robertdemelo/)

🐍 Python | OpenCV | MediaPipe | Visão Computacional | Processamento de Imagens
