import os
import pygame as pg
import moderngl as mgl

class Texture:
    def __init__(self, ctx):
        self.ctx = ctx
        self.textures = {}
        
        # Usando caminhos absolutos para as texturas
        self.textures['terra'] = self.get_texture(path=self.get_texture_path('terra.jpg'))
        self.textures['jupiter'] = self.get_texture(path=self.get_texture_path('Jupiter3600.jpg'))
        self.textures['marte'] = self.get_texture(path=self.get_texture_path('marssurface.jpg'))
        self.textures['mercurio'] = self.get_texture(path=self.get_texture_path('Mercury.jpg'))
        self.textures['lua'] = self.get_texture(path=self.get_texture_path('Moon.jpg'))
        self.textures['netuno'] = self.get_texture(path=self.get_texture_path('Neptune.jpg'))
        self.textures['plutao'] = self.get_texture(path=self.get_texture_path('Pluto.jpg'))
        self.textures['saturno'] = self.get_texture(path=self.get_texture_path('Saturn_diff.jpg'))
        self.textures['sol'] = self.get_texture(path=self.get_texture_path('Sun.jpg'))
        self.textures['urano'] = self.get_texture(path=self.get_texture_path('2k_uranus.jpg'))
        self.textures['venus'] = self.get_texture(path=self.get_texture_path('venusClouds2.jpg'))
        self.textures['ovni'] = self.get_texture(path=self.get_texture_path('13884_Diffuse.jpg'))
        self.textures['nave'] = self.get_texture(path=self.get_texture_path('2k_uranus.jpg'))


    def get_texture_path(self, texture_name):
        # Obtém o caminho absoluto para a textura dentro da pasta 'textures'
        base_path = os.path.dirname(__file__)
        texture_path = os.path.join(base_path, 'textures', texture_name)
        
        # Verifica o caminho para depuração
        print(f"Texture Path: {texture_path}")
        return texture_path

    def get_texture(self, path):
        # Carregar a textura com o pygame
        texture = pg.image.load(path).convert()
        
        # Ajustar a textura - modo espelho, deixando ela no modo normal (flipping na vertical)
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        
        # Criar a textura do contexto OpenGL com 3 componentes (RGB)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))
        #mipmaps
        texture.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)
        texture.build_mipmaps()
        #AF
        texture.anisotropy = 32.0
        return texture
    
    def destroy(self):
        # Libera as texturas
        [tex.release() for tex in self.textures.values()]
