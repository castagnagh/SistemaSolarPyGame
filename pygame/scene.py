from model import *

#classe criada para centralizar todos os objetos e componentes criados
#necessitando apenas chamar essa classe no init da class Main
class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object
        
        ##########################################################################################################################
        #--------------------------- SISTEMA SOLAR SEM ROTAÇÃO E SEM TRANSLAÇÃO / ESCALA E DISTANCIA REAL (obs: ALTERAR A VELOCIDADE NA camera.py)-----------------------#
        add(Esfera(app, tex_id='sol', pos=(-50, 0, 0), scale=(5, 5, 5)))
        add(Esfera(app, tex_id='mercurio', pos=(57.9, 0, 0), scale=(0.02, 0.02, 0.02)))
        add(Esfera(app, tex_id='venus', pos=(108.2, 0, 0), scale=(0.04, 0.04, 0.04)))
        add(Esfera(app, tex_id='terra', pos=(149.6, 0, 0), scale=(0.05, 0.05, 0.05)))
        add(Esfera(app, tex_id='lua', pos=(154.9, 0, 0), scale=(0.01, 0.01, 0.01)))
        add(Esfera(app, tex_id='marte', pos=(227.9, 0, 0), scale=(0.02, 0.02, 0.02)))
        add(Esfera(app, tex_id='jupiter', pos=(778.5, 0, 0), scale=(0.5, 0.5, 0.5)))
        add(Esfera(app, tex_id='saturno', pos=(1433.5, 0, 0), scale=(0.4, 0.4, 0.4)))
        add(Esfera(app, tex_id='urano', pos=(2872.5, 0, 0), scale=(0.2, 0.2, 0.2)))
        add(Esfera(app, tex_id='netuno', pos=(4495.1, 0, 0), scale=(0.2, 0.2, 0.2)))
        add(Esfera(app, tex_id='plutao', pos=(5906.4, 0, 0), scale=(0.01, 0.01, 0.01)))

        ##########################################################################################################################
        #--------------------------- SISTEMA SOLAR COM ROTAÇAO E ESCALA REAL / DISTANCIA FICTICIA ----------------------------------------------------#
        # add(Esfera(app, tex_id='sol', pos=(-50, 0, 0), scale=(5, 5, 5), rotation_speed=0.01))  # Rotação lenta do Sol
        # add(Esfera(app, tex_id='mercurio', pos=(50, 0, 0), scale=(0.02, 0.02, 0.02), rotation_speed=0.0012))  # 58,6 dias
        # add(Esfera(app, tex_id='venus', pos=(100, 0, 0), scale=(0.04, 0.04, 0.04), rotation_speed=0.0002))  # 243 dias
        # add(Esfera(app, tex_id='terra', pos=(150, 0, 0), scale=(0.05, 0.05, 0.05), rotation_speed=0.1))  # 1 dia
        # add(Esfera(app, tex_id='lua', pos=(155, 0, 0), scale=(0.01, 0.01, 0.01), rotation_speed=0.004))  # Rotação aproximada da Lua
        # add(Esfera(app, tex_id='marte', pos=(200, 0, 0), scale=(0.02, 0.02, 0.02), rotation_speed=0.098))  # 1,03 dias
        # add(Esfera(app, tex_id='jupiter', pos=(250, 0, 0), scale=(0.5, 0.5, 0.5), rotation_speed=2.44))  # 0,41 dias

        # add(Saturno(app, tex_id='saturno', pos=(300, 0, 0), rot=(5, 10, 250), scale=(0.02, 0.02, 0.02), rotation_speed=2.08))  # 0,45 dias

        # add(Esfera(app, tex_id='urano', pos=(350, 0, 0), scale=(0.2, 0.2, 0.2), rotation_speed=0.87))  # 0,72 dias
        # add(Esfera(app, tex_id='netuno', pos=(400, 0, 0), scale=(0.2, 0.2, 0.2), rotation_speed=0.94))  # 0,67 dias
        # add(Esfera(app, tex_id='plutao', pos=(450, 0, 0), scale=(0.01, 0.01, 0.01), rotation_speed=0.003))  # Rotação lenta estimada
        ##########################################################################################################################

        ##########################################################################################################################
        #--------------------------- SISTEMA SOLAR COM ROTAÇAO E TRANSLAÇÃO ESCALA REAL / DISTANCIA FICTICIA ----------------------------------------------------#
        # # Sol fixo
        # add(Esfera(app, tex_id='sol', pos=(0, 0, 0), scale=(5, 5, 5), rotation_speed=0.01))

        # # Planetas com translação orbital
        # add(Esfera(app, tex_id='mercurio', orbit_radius=50, orbit_speed=4.74, scale=(0.02, 0.02, 0.02), rotation_speed=0.0012))
        # add(Esfera(app, tex_id='venus', orbit_radius=100, orbit_speed=3.5, scale=(0.04, 0.04, 0.04), rotation_speed=0.0002))
        # add(Esfera(app, tex_id='terra', orbit_radius=150, orbit_speed=2.98, scale=(0.05, 0.05, 0.05), rotation_speed=0.1))
        # add(Esfera(app, tex_id='marte', orbit_radius=200, orbit_speed=2.41, scale=(0.02, 0.02, 0.02), rotation_speed=0.098))
        # add(Esfera(app, tex_id='jupiter', orbit_radius=250, orbit_speed=1.31, scale=(0.5, 0.5, 0.5), rotation_speed=2.44))
        # add(Esfera(app, tex_id='saturno', orbit_radius=300, orbit_speed=0.97, scale=(0.4, 0.4, 0.4), rotation_speed=2.08))
        # add(Esfera(app, tex_id='urano', orbit_radius=350, orbit_speed=0.68, scale=(0.2, 0.2, 0.2), rotation_speed=0.87))
        # add(Esfera(app, tex_id='netuno', orbit_radius=400, orbit_speed=0.54, scale=(0.2, 0.2, 0.2), rotation_speed=0.94))
        ##########################################################################################################################

    def render (self):
        for obj in self.objects:
            obj.render()