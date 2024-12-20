# Projeto Pygame 3D com ModernGL

Este projeto utiliza **Pygame**, **ModernGL**, **PyGLM** (biblioteca de matemática otimizada para gráficos 3D) e **pywavefront** (utilizada especialmente para gerenciar arquivos OBJ) para carregar e renderizar objetos 3D, como um sistema solar, utilizando OpenGL moderno.

<img src="imagemMd\image.png">

# Video de demonstração


[Demonstração do projeto](https://www.youtube.com/watch?v=XVFlGe-Op7A)

## Instalação

Siga os passos abaixo para configurar e rodar o projeto.

### 1. Clonar o repositório

Primeiro, clone este repositório para sua máquina local:

```
git clone https://github.com/castagnagh/SistemaSolarPyGame.git
cd pygame
```

### 2. Instalar as dependências

Instale as seguintes bibliotecas Python necessárias para rodar o projeto. Utilize os comandos abaixo:


```
pip install pygame moderngl numpy

pip install PyGLM

pip install pywavefront 
```


### 3. Executar o projeto

Após a instalação das dependências, você pode rodar o projeto com o seguinte comando:

```
python main.py
```
Certifique-se de que todos os arquivos OBJ (objetos 3D) estejam no caminho correto dentro da pasta objects do projeto.


## Referência
Este projeto foi desenvolvido com base no tutorial do canal Coder Space:


[Let's code 3D Engine in Python. OpenGL Pygame Tutorial](https://www.youtube.com/watch?v=eJDIsFJN4OQ&t=1s&ab_channel=CoderSpace)

Assista ao tutorial para aprender mais sobre o ModernGL e como ele é aplicado no Pygame.
