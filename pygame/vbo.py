import numpy as np
import moderngl as mgl
import pywavefront

class VBO:
    def __init__(self, ctx):
        self.vbos = {}
        self.vbos['esfera'] = EsferaVBO(ctx)
        self.vbos['saturno'] = SaturnoVBO(ctx)
        self.vbos['nave'] = NaveVBO(ctx)
        self.vbos['ovni'] = OVNIVBO(ctx)
    
    def destroy(self):
        [vbo.destroy() for vbo in self.vbos.values()]

class BaseVBO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = self.get_vbo()
        self.format: str = None
        self.attrib: list = None
    
    def get_vertex_data(self): ...

    def get_vbo(self):
        vertex_data = self.get_vertex_data()
        #aqui um obj buffer é criado passando os vértices para a memória da GPU
        vbo = self.ctx.buffer(vertex_data)
        return vbo

    def destroy(self):
        self.vbo.release()
    
class EsferaVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront(r'C:\Users\Gabriel Castagna\Documents\Projetos GitHub\SistemaSolarPyGame\pygame\objects\esfera\earth3OBJ.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
    
class SaturnoVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront(r'C:\Users\Gabriel Castagna\Documents\Projetos GitHub\SistemaSolarPyGame\pygame\objects\Saturno\13906_Saturn_v1_l3.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
    
class NaveVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        # objs = pywavefront.Wavefront(r'objects/ovni/13884_UFO_Saucer_v1_l2.obj', cache=True, parse=True)
        objs = pywavefront.Wavefront(r'C:\Users\Gabriel Castagna\Documents\Projetos GitHub\SistemaSolarPyGame\pygame\objects\nave\Uncommon Rocket Without Texture.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
    
class OVNIVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront(r'C:\Users\Gabriel Castagna\Documents\Projetos GitHub\SistemaSolarPyGame\pygame\objects\ovni\13884_UFO_Saucer_v1_l2.obj', cache=True, parse=True)

        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data