#--------Operating System Project--------
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
import qrcode
import plyer
Window.size=405,720

class Function(ScreenManager):
	def generate_qr_code(self,root):
		if self.ids.link_text.text != '' and self.ids.image_name.text != '':
			name=str(self.ids.image_name.text)
			code=qrcode.QRCode(version=1.0, box_size=15, border=4)
			code.add_data(self.ids.link_text.text)
			code.make(fit=True)
			img=code.make_image(fill = 'Black',back_color='White')
			img.save(f"{name}.png")
			#img.save(f"{path}/{name}.png")
			plyer.notification.notify(
				title = 'QR Code Generator',message="QR Code Generated"
			) 
			self.ids.img_.source=f"{name}.png"
			root.current="image"
		else:
			plyer.notification.notify(
				title = 'QR Code Generator',message="Input Field is Empty"
			)
	
	def make_another(self,root):
		self.ids.link_text.text = ''
		self.ids.image_name.text = ''
		root.current="first"
		

class Main(MDApp):
	Builder.load_file('files/layout.kv')
	def build(self):
		self.title = 'QR Code Generator/Scanner'
		return Function()

Main().run()


#---MADE BY :  Coding PLEX ---
#---Instagram : @codingplex_ and @codingmemes404
#---Youtube : Coding PLEX
#---https://coding-plex.blogspot.com---
