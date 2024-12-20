import socket
import threading
import json
from collections import Counter

HOST = "localhost"
PORT = 5000
results = Counter()

# Handle communication with a single worker
def handle_worker(conn, address):
    global results
    try:
        print(f"Connected to worker {address}")

        # Receive results from the worker
        data = conn.recv(4096).decode()
        worker_result = json.loads(data)

        print(f"Received results from {address}: {worker_result}")
        results.update(worker_result)
        print(f"Current aggregated results: {dict(results)}")
    except Exception as e:
        print(f"Worker {address} failed. Error: {e}")
    finally:
        conn.close()

# Master server setup
def master_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print("Master Server is listening...")

    while True:
        conn, address = server.accept()
        thread = threading.Thread(target=handle_worker, args=(conn, address))
        thread.start()

if __name__ == "__main__":
    try:
        master_server()
    except KeyboardInterrupt:
        print("\nFinal Results:", dict(results))