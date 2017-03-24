from PyQt5 import QtOpenGL, QtWidgets
import ModernGL, struct


class QGLControllerWidget(QtOpenGL.QGLWidget):
	def __init__(self):
		fmt = QtOpenGL.QGLFormat()
		fmt.setVersion(3, 3)
		fmt.setProfile(QtOpenGL.QGLFormat.CoreProfile)
		fmt.setSampleBuffers(True)
		super(QGLControllerWidget, self).__init__(fmt, None)

	def initializeGL(self):
		self.ctx = ModernGL.create_context()

		prog = self.ctx.Program([
			self.ctx.VertexShader('''
				#version 330

				in vec2 vert;

				void main() {
					gl_Position = vec4(vert, 0.0, 1.0);
				}
			'''),
			self.ctx.FragmentShader('''
				#version 330
			
				out vec4 color;

				void main() {
					color = vec4(0.30, 0.50, 1.00, 1.0);
				}
			'''),
		])

		vbo = self.ctx.Buffer(struct.pack('6f', 0.0, 0.8, -0.6, -0.8, 0.6, -0.8))
		self.vao = self.ctx.SimpleVertexArray(prog, vbo, '2f', ['vert'])

	def paintGL(self):
		print(dir(self))
		self.ctx.viewport = (0, 0, self.width(), self.height())
		self.ctx.clear(240, 240, 240)
		self.vao.render()
		self.ctx.finish()


app = QtWidgets.QApplication([])
window = QGLControllerWidget()
window.show()
app.exec_()

