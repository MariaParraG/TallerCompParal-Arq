from multiprocessing import Process, Queue

# Función que envía datos desde el primer procesador
def send_data(q):
    data = "Mensaje desde el Procesador 1"
    print("Procesador 1: Enviando datos...")
    q.put(data)  # Coloca el mensaje en la cola

# Función que recibe datos en el segundo procesador
def receive_data(q):
    data = q.get()  # Obtiene el mensaje de la cola
    print("Procesador 2: Recibió el mensaje:", data)

if __name__ == "__main__":
    q = Queue()  # Crear la cola de comunicación

    # Crear procesos independientes
    p1 = Process(target=send_data, args=(q,))
    p2 = Process(target=receive_data, args=(q,))

    # Iniciar procesos
    p1.start()
    p2.start()

    # Esperar a que los procesos terminen
    p1.join()
    p2.join()
