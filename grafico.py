import matplotlib.pyplot as pyp
import pandas as pd

from simulacion import Simulacion


class Grafico:
	def __init__(self, simulacion: Simulacion):
		self.simulacion = simulacion

	def mostrar_clientes(self):
		print('Clientes:')
		for cliente in self.simulacion.clientes:
			print(f' {cliente.act_tiempo_entre_llegada:>5}', end='')
			print(f' {cliente.reloj_llegada:>5}', end='')
			print(f' {cliente.act_tiempo_de_servicio:>5}', end='')
			print(f' {cliente.reloj_inicio_de_servicio:>5}', end='')
			print(f' {cliente.salida_tiempo_de_espera:>5}', end='')
			print(f' {cliente.reloj_finalizacion_de_servicio:>5}', end='')
			print(f' {cliente.salida_tiempo_total_dentro:>5}', end='')
			print()

	def mostrar_servidores(self):
		for num_servidor, servidor in enumerate(self.simulacion.servidores, 1):
			print('Servidor:', num_servidor)
			for (inicio, fin) in zip(servidor.reloj_inicios_de_servicio, servidor.reloj_finalizaciones_de_servicio):
				print(f'{inicio:>5}', end='')
				print(f'{fin:>5}', end='')
				print()
			print()

	def graficar_tiempos_entre_llegadas(self):
		pd.DataFrame([cliente.act_tiempo_entre_llegada for cliente in self.simulacion.clientes]).plot.hist(bins=1000, title='Tiempos entre llegadas')
		pyp.show()

	def graficar_tiempos_de_servicio(self):
		pd.DataFrame([cliente.act_tiempo_de_servicio for cliente in self.simulacion.clientes]).plot.hist(bins=1000, title='Tiempos de servicio')
		pyp.show()
