from vbo import VBO
from shader_program import ShaderProgram

class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        #dicionario de Vertex Array Objects para cada objeto
        #esfera vao
        self.vaos['esfera'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['esfera'])
        
        self.vaos['saturno'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['saturno'])
        
        self.vaos['nave'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['nave'])
        
        self.vaos['ovni'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['ovni'])
        
    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)])
        return vao
    
    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()