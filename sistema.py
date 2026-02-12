import random
import os
import json
from datetime import datetime

class SistemaIndustrial:

    def __init__(self):
        self.temperatura = 0
        self.presion = 0
        self.alarma = False
        self.bomba = False

    def leer_sensores(self):
        self.temperatura = random.randint(40, 100)
        self.presion = random.randint(10, 70)

    def evaluar_sistema(self):
        self.alarma = False
        self.bomba = False

        if self.temperatura > 80 or self.presion > 50:
            self.alarma = True
            self.registrar_evento()

        if self.temperatura > 60 and self.presion > 30:
            self.bomba = True

    def registrar_evento(self):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        evento = {
            "fecha": fecha,
            "temperatura": self.temperatura,
            "presion": self.presion,
            "alarma": True
        }

        ruta_script = os.path.dirname(os.path.abspath(__file__))
        carpeta_registro = os.path.join(ruta_script, "registro")

        os.makedirs(carpeta_registro, exist_ok=True)

        ruta_archivo = os.path.join(carpeta_registro, "registro_eventos.json")

        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        else:
            datos = []

        datos.append(evento)

        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4)

    def mostrar_estado(self):
        print(f"Temperatura: {self.temperatura} °C")
        print(f"Presión: {self.presion} bar")
        print(f"Alarma: {'ACTIVA' if self.alarma else 'INACTIVA'}")
        print(f"Bomba: {'ENCENDIDA' if self.bomba else 'APAGADA'}")
        print("-" * 30)