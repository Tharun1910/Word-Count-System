import socket
import json
from collections import Counter

HOST = "localhost"
PORT = 5000

# Word count function
def word_count(text):
    words = text.lower().split()
    return dict(Counter(words))

# Worker node setup
def worker_node(worker_name, file_path):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    try:
        print(f"{worker_name} connected to master server...")

        # Read data from file
        with open(file_path, 'r') as f:
            data_to_process = f.read()

        # Process the data
        partial_result = word_count(data_to_process)

        print(f"{worker_name} sending results: {partial_result}")
        client.send(json.dumps(partial_result).encode())
    except Exception as e:
        print(f"Error in {worker_name}: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python worker_node.py <worker_name> <file_path>")
        sys.exit(1)

    worker_name = sys.argv[1]
    file_path = sys.argv[2]
    worker_node(worker_name, file_path)