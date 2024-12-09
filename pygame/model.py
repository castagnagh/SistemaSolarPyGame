import numpy as np
import os
import pygame as pg
import glm
import math

class BaseModel:
    def __init__(self, app, vao_name, tex_id, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1),
                 rotation_speed=0.0, orbit_radius=0.0, orbit_speed=0.0):
        self.app = app
        self.pos = glm.vec3(pos)  # Posição inicial
        self.rot = glm.vec3([glm.radians(a) for a in rot])  # Rotação inicial em radianos
        self.scale = scale
        self.rotation_speed = glm.radians(rotation_speed)  # Velocidade de rotação em radianos/frame
        self.orbit_radius = orbit_radius  # Raio da órbita (0 para sem translação)
        self.orbit_speed = glm.radians(orbit_speed)  # Velocidade orbital em radianos/frame
        self.orbit_angle = 0.0  # Ângulo inicial da órbita
        self.m_model = self.get_model_matrix()
        self.tex_id = tex_id
        self.vao = app.mesh.vao.vaos[vao_name]
        self.program = self.vao.program
        self.camera = self.app.camera

    def update(self): 
        # Atualiza a rotação no eixo Y
        self.rot.y += self.rotation_speed

        # Atualiza a posição para a translação orbital, se houver órbita
        if self.orbit_radius > 0:
            self.orbit_angle += self.orbit_speed
            self.pos.x = self.orbit_radius * glm.cos(self.orbit_angle)
            self.pos.z = self.orbit_radius * glm.sin(self.orbit_angle)
        
        # Atualiza a matriz do modelo
        self.m_model = self.get_model_matrix()

    def get_model_matrix(self):
        m_model = glm.mat4()
        # Translate
        m_model = glm.translate(m_model, self.pos)
        # Rotate
        m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))
        m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))
        # Scale
        m_model = glm.scale(m_model, self.scale)

        return m_model
    
    def render(self):
        self.update()
        self.vao.render()


class Esfera(BaseModel):
    def __init__(self, app, vao_name='esfera', tex_id='terra', 
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1), 
                 rotation_speed=0.0, orbit_radius=0.0, orbit_speed=0.0):
        super().__init__(app, vao_name, tex_id, pos, rot, scale, rotation_speed, orbit_radius, orbit_speed)
        self.on_init()

    def update(self):
        super().update()  # Atualiza a rotação e a posição orbital
        self.texture.use()
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)

    def on_init(self):
        # Texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_0'] = 0
        self.texture.use()
        # MVP
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)
        # Light
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)


class Saturno(Esfera):
    def __init__(self, app, vao_name='saturno', tex_id='saturno', 
                 pos=(0, 0, 0), rot=(5, 5, 10), scale=(1, 1, 1), 
                 rotation_speed=0.0, orbit_radius=0.0, orbit_speed=0.0):
        super().__init__(app, vao_name, tex_id, pos, rot, scale, rotation_speed, orbit_radius, orbit_speed)
        self.on_init()

    def update(self):
        super().update()  # Atualiza a rotação e a matriz do modelo
        self.texture.use()
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)

    def on_init(self):
        # Texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_0'] = 0
        self.texture.use()
        # MVP
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)
        # Light
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)





    
