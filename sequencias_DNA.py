import pyfiglet

def textoInicial():
	from pyfiglet import Figlet

	print(pyfiglet.figlet_format('D N A'))
	input('Por favor, pressione ENTER para continuar')


def textoFinal():
	from pyfiglet import Figlet

	print(pyfiglet.figlet_format('Adeus',font = '3x5'))

def programa_principal():
	"""
	Esta é a função do programa principal
	"""
	try:
	     textoInicial()
	     textoFinal()
	except:
	     print('Ops: algo correu mal!')
