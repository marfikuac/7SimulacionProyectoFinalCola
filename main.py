import random

from grafico import Grafico
from simulacion import Simulacion


def print_stats(simulacion: Simulacion):
	print(f'  Tiempo de espera promedio: {simulacion.calcular_tiempo_de_espera_promedio():.2f}')
	print(f'Tiempo de servicio promedio: {simulacion.calcular_tiempo_de_servicio_promedio():.2f}')
	print(f'    Ocupación de servidores: {simulacion.calcular_tasa_de_ocupacion_de_servidores():.2%}')

tiempo_simulado = 8760 # 1 año
gen_tiempo_entre_llegada = lambda: random.expovariate(1 / 5) # Media 5

num_servidores = 1

gen_tiempo_de_servicio = lambda: random.uniform(0, 8)
simulacion = Simulacion(num_servidores, gen_tiempo_de_servicio, gen_tiempo_entre_llegada, tiempo_simulado)
simulacion.iniciar()
print('[1 cuadrilla de 2 personas]')
print_stats(simulacion)

gen_tiempo_de_servicio = lambda: random.uniform(0, 6)
simulacion = Simulacion(num_servidores, gen_tiempo_de_servicio, gen_tiempo_entre_llegada, tiempo_simulado)
simulacion.iniciar()
print()
print('[1 cuadrilla de 3 personas]')
print_stats(simulacion)

gen_tiempo_de_servicio = lambda: random.uniform(0, 4)
simulacion = Simulacion(num_servidores, gen_tiempo_de_servicio, gen_tiempo_entre_llegada, tiempo_simulado)
simulacion.iniciar()
print()
print('[1 cuadrilla de 4 personas]')
print_stats(simulacion)

num_servidores = 2

gen_tiempo_de_servicio = lambda: random.uniform(0, 8)
simulacion = Simulacion(num_servidores, gen_tiempo_de_servicio, gen_tiempo_entre_llegada, tiempo_simulado)
simulacion.iniciar()
print()
print('[2 cuadrillas de 2 personas c/u]')
print_stats(simulacion)

# Pruebas opcionales:

# grafico = Grafico(simulacion)
# grafico.mostrar_clientes()
# grafico.mostrar_servidores()
# grafico.graficar_tiempos_entre_llegadas()
# grafico.graficar_tiempos_de_servicio()
