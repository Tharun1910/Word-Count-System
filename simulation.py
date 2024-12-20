import multiprocessing
import os

def run_worker(worker_name, file_path):
    os.system(f"python worker_node.py {worker_name} {file_path}")

if __name__ == "__main__":
    workers = {
        "worker_1": "data1.txt",
        "worker_2": "data2.txt",
        "worker_3": "data3.txt",
        "worker_4": "data4.txt",
    }

    processes = []

    for worker, file_path in workers.items():
        p = multiprocessing.Process(target=run_worker, args=(worker, file_path))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()