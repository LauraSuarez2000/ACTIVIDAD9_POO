from typing import Tuple

class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        temperaturas = []
        humedades = []
        presiones = []
        velocidades_viento = []
        direcciones_viento = []

        # Diccionario de direcciones de viento y sus equivalentes en grados
        direcciones_grados = {
            "N": 0,
            "NNE": 22.5,
            "NE": 45,
            "ENE": 67.5,
            "E": 90,
            "ESE": 112.5,
            "SE": 135,
            "SSE": 157.5,
            "S": 180,
            "SSW": 202.5,
            "SW": 225,
            "WSW": 247.5,
            "W": 270,
            "WNW": 292.5,
            "NW": 315,
            "NNW": 337.5,
        }

        with open(self.nombre_archivo, 'r') as archivo:
            for linea in archivo:
                if linea.startswith("Temperatura:"):
                    temperaturas.append(float(linea.split(":")[1].strip()))
                elif linea.startswith("Humedad:"):
                    humedades.append(float(linea.split(":")[1].strip()))
                elif linea.startswith("Presion:"):  
                    presiones.append(float(linea.split(":")[1].strip()))
                elif linea.startswith("Viento:"):
                    viento_info = linea.split(":")[1].strip().split(',')
                    velocidad = float(viento_info[0])
                    direccion = viento_info[1]
                    velocidades_viento.append(velocidad)
                    direcciones_viento.append(direccion)

        temperatura_promedio = sum(temperaturas) / len(temperaturas)
        humedad_promedio = sum(humedades) / len(humedades)
        presion_promedio = sum(presiones) / len(presiones)
        velocidad_promedio = sum(velocidades_viento) / len(velocidades_viento)

        # Calcular la dirección predominante del viento
        grados_promedio = sum(direcciones_grados[d] for d in direcciones_viento) / len(direcciones_viento)
        for direccion, grados in direcciones_grados.items():
            if abs(grados - grados_promedio) < 11.25:
                direccion_predominante = direccion
                break

        return temperatura_promedio, humedad_promedio, presion_promedio, velocidad_promedio, direccion_predominante

if __name__ == "__main__":
    nombre_archivo = r'C:\Users\ASUS\Desktop\POO_9\datos.txt'  # Ruta completa al archivo
    datos = DatosMeteorologicos(nombre_archivo)
    temperatura_promedio, humedad_promedio, presion_promedio, velocidad_promedio, direccion_predominante = datos.procesar_datos()

    print(f"Temperatura promedio: {temperatura_promedio}°C")
    print(f"Humedad promedio: {humedad_promedio}%")
    print(f"Presión promedio: {presion_promedio} hPa")
    print(f"Velocidad promedio del viento: {velocidad_promedio} m/s")
    print(f"Dirección predominante del viento: {direccion_predominante}")
