from entidades import Cliente, Servidor


class Evento:
	def __init__(self, reloj, tipo, cliente: Cliente, servidor: Servidor = None):
		self.reloj = reloj
		self.tipo = tipo
		self.cliente = cliente
		self.servidor = servidor


class TipoDeEvento:
	LLEGADA_CLIENTE = 1
	SALIDA_CLIENTE = 2


class Simulacion:
	def __init__(self, num_servidores: int, gen_tiempo_de_servicio, gen_tiempo_entre_llegada, tiempo_simulado: int):
		self.num_servidores = num_servidores
		self.gen_tiempo_de_servicio = gen_tiempo_de_servicio
		self.gen_tiempo_entre_llegada = gen_tiempo_entre_llegada
		self.tiempo_simulado = tiempo_simulado

		# Estado del sistema:
		self.reloj = 0
		self.servidores = [Servidor() for _ in range(num_servidores)]
		self.clientes = []
		self.num_clientes_en_espera = 0

	def iniciar(self):
		# Programar el primer evento para que se puedan desencadenar los demás.
		tiempo_entre_llegada = self.gen_tiempo_entre_llegada()
		noticias_de_eventos = [Evento(tiempo_entre_llegada, TipoDeEvento.LLEGADA_CLIENTE, Cliente(tiempo_entre_llegada))]

		while(len(noticias_de_eventos) > 0):
			# Avanzar al siguiente evento más próximo.
			noticias_de_eventos.sort(key=lambda evento: evento.reloj)
			evento = noticias_de_eventos.pop(0)

			if evento.tipo == TipoDeEvento.LLEGADA_CLIENTE:
				self._on_llegada_cliente(evento, noticias_de_eventos)
			elif evento.tipo == TipoDeEvento.SALIDA_CLIENTE:
				self._on_salida_cliente(evento, noticias_de_eventos)

	def _on_llegada_cliente(self, evento: Evento, noticias_de_eventos):
		self.reloj = evento.reloj
		cliente = evento.cliente

		cliente.reloj_llegada = self.reloj
		cliente.act_tiempo_de_servicio = self.gen_tiempo_de_servicio()

		self.clientes.append(cliente)
		self.num_clientes_en_espera += 1

		for servidor in self.servidores:
			if not servidor.ocupado:
				noticias_de_eventos.append(Evento(self.reloj + cliente.act_tiempo_de_servicio, TipoDeEvento.SALIDA_CLIENTE, cliente, servidor))
				servidor.ocupado = True
				self.num_clientes_en_espera -= 1
				break

		tiempo_entre_llegada = self.gen_tiempo_entre_llegada()
		if self.reloj + tiempo_entre_llegada < self.tiempo_simulado:
			noticias_de_eventos.append(Evento(self.reloj + tiempo_entre_llegada, TipoDeEvento.LLEGADA_CLIENTE, Cliente(tiempo_entre_llegada)))

	def _on_salida_cliente(self, evento: Evento, noticias_de_eventos):
		self.reloj = evento.reloj
		cliente = evento.cliente
		servidor = evento.servidor

		cliente.reloj_inicio_de_servicio = self.reloj - cliente.act_tiempo_de_servicio
		cliente.reloj_finalizacion_de_servicio = self.reloj
		cliente.salida_tiempo_de_espera = cliente.reloj_inicio_de_servicio - cliente.reloj_llegada
		cliente.salida_tiempo_total_dentro = self.reloj - cliente.reloj_llegada

		servidor.reloj_inicios_de_servicio.append(cliente.reloj_inicio_de_servicio)
		servidor.reloj_finalizaciones_de_servicio.append(cliente.reloj_finalizacion_de_servicio)
		servidor.ocupado = False

		if self.num_clientes_en_espera > 0:
			cliente_siguiente = self.clientes[-self.num_clientes_en_espera]
			noticias_de_eventos.append(Evento(self.reloj + cliente_siguiente.act_tiempo_de_servicio, TipoDeEvento.SALIDA_CLIENTE, cliente_siguiente, servidor))
			servidor.ocupado = True
			self.num_clientes_en_espera -= 1

	def calcular_tiempo_de_espera_promedio(self):
		tiempo_de_espera_promedio = sum([cliente.salida_tiempo_de_espera for cliente in self.clientes]) / len(self.clientes)
		return tiempo_de_espera_promedio

	def calcular_tiempo_de_servicio_promedio(self):
		tiempo_de_servicio_promedio = sum([cliente.act_tiempo_de_servicio for cliente in self.clientes]) / len(self.clientes)
		return tiempo_de_servicio_promedio

	def calcular_tasa_de_ocupacion_de_servidores(self):
		tasa_ocupacion_promedio = sum([servidor.calcular_tasa_ocupacion() for servidor in self.servidores]) / len(self.servidores)
		return tasa_ocupacion_promedio
