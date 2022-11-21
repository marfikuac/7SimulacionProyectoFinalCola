class Cliente:
	def __init__(self, tiempo_entre_llegada):
		self.reloj_llegada = 0
		self.reloj_inicio_de_servicio = 0
		self.reloj_finalizacion_de_servicio = 0
		self.act_tiempo_entre_llegada = tiempo_entre_llegada
		self.act_tiempo_de_servicio = 0
		self.salida_tiempo_de_espera = 0
		self.salida_tiempo_total_dentro = 0


class Servidor:
	def __init__(self):
		self.reloj_inicios_de_servicio = []
		self.reloj_finalizaciones_de_servicio = []
		self.ocupado = False

	def calcular_tasa_ocupacion(self):
		fin_simulacion_respecto_servidor = self.reloj_finalizaciones_de_servicio[-1]
		tiempo_ocupado = sum([fin - inicio for inicio, fin in zip(self.reloj_inicios_de_servicio, self.reloj_finalizaciones_de_servicio)])
		tasa_ocupacion = tiempo_ocupado / fin_simulacion_respecto_servidor
		return tasa_ocupacion
