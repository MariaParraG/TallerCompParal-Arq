import multiprocessing  # Importamos la librería para manejar procesos en paralelo

# Memoria compartida usando Value de multiprocessing
memoria_compartida = multiprocessing.Value('i', 0)  # Se define un entero compartido entre procesos

# Candado (Lock) para proteger el acceso concurrente a la memoria compartida
lock = multiprocessing.Lock()

# Función que será ejecutada por cada proceso
def procesador(id_procesador, incremento, memoria_compartida, lock):
    """
    Función que representa un procesador que accede a la memoria compartida.

    - id_procesador: Identificador del procesador.
    - incremento: Valor que se sumará a la memoria compartida.
    - memoria_compartida: Variable compartida entre procesos.
    - lock: Candado para evitar condiciones de carrera.
    """
    print(f"Procesador {id_procesador} intentando acceder a la memoria compartida...")
    
    # Se usa el candado (lock) para evitar accesos simultáneos a la memoria compartida
    with lock:
        print(f"Procesador {id_procesador} accedió a la memoria compartida.")
        
        # Leer el valor actual en la memoria compartida
        valor_actual = memoria_compartida.value
        print(f"Procesador {id_procesador} lee: {valor_actual}")

        # Sumar el incremento al valor actual
        nuevo_valor = valor_actual + incremento
        memoria_compartida.value = nuevo_valor
        print(f"Procesador {id_procesador} escribió: {nuevo_valor}")
    
    print(f"Procesador {id_procesador} terminó su trabajo.")

# Lista para almacenar los procesos
procesos = []

# Crear 4 procesos con diferentes valores para incrementar
for i in range(4):
    incremento = i + 1  # Cada proceso suma un número diferente (1, 2, 3, 4)
    
    # Se crea un nuevo proceso que ejecuta la función 'procesador'
    proceso = multiprocessing.Process(target=procesador, args=(i+1, incremento, memoria_compartida, lock))
    
    procesos.append(proceso)  # Se agrega el proceso a la lista

# Iniciar todos los procesos
for proceso in procesos:
    proceso.start()

# Esperar a que todos los procesos terminen su ejecución
for proceso in procesos:
    proceso.join()

# Mostrar el valor final de la memoria compartida después de que todos los procesos han terminado
print(f"Valor final en la memoria compartida: {memoria_compartida.value}")
