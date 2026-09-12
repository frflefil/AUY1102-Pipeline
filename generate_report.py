"""Módulo para generación de informe de datos procesados."""
import datetime

def generar_informe():
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{fecha_actual}] Procesando datos...")
    print(f"[{fecha_actual}] Informe generado exitosamente.")

if __name__ == "__main__":
    generar_informe()
