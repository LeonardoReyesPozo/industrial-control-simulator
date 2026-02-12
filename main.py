import time
from sistema import SistemaIndustrial


def main():
    sistema = SistemaIndustrial()

    try:
        while True:
            sistema.leer_sensores()
            sistema.evaluar_sistema()
            sistema.mostrar_estado()
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nSistema detenido manualmente.")


if __name__ == "__main__":
    main()