

'''
	Este codigo utiliza el microfono de la rasp y convierte el Speech to text
'''

import speech_recognition as sr

#Calse speech to text
class STT():

	#Inicializo el paquete
	def __init__(self):
		self.Chismoso = sr.Recognizer()

	#Utilzo el paquete para escuchar y convertir el audio en texto
	def Lisen(self):

		print("Escuchando ...")
		with sr.Microphone() as source:

			audio = self.Chismoso.listen(source, phrase_time_limit=5)
			texto = "Lo siento carnal no entendi nada"

			try:
				text = self.Chismoso.recognize_google(audio,language="es-MX")
				texto = text.lower()

				print("Esto entendio: ",text)
			except:
				print(texto)

		return texto

STT1 = STT()
Text = STT1.Lisen()  

print(Text)