# Distributed Word Count System

A scalable and fault-tolerant distributed word count system implemented in Python. This project demonstrates the principles of distributed systems, including task distribution, parallel processing, and result aggregation, through a master-worker architecture.

---

## **Features**
- **Scalability:** Efficiently handles large datasets by leveraging multiple worker nodes.
- **Fault Tolerance:** Detects and recovers from node failures using heartbeat monitoring and task reassignment.
- **Parallel Processing:** Distributes data processing tasks across multiple nodes for faster execution.
- **Accuracy:** Ensures consistent and reliable word count results.

---

## **System Architecture**
The system employs a **master-worker architecture**:
1. **Master Node:**
   - Allocates tasks to worker nodes.
   - Monitors worker status and redistributes tasks if a node fails.
   - Aggregates results from worker nodes.
2. **Worker Nodes:**
   - Process assigned data chunks independently.
   - Send partial results back to the master node.

---

## **Workflow**
1. **Data Partitioning:** The input dataset is divided into smaller chunks using the `data_splitter` module.
2. **Task Assignment:** The master node distributes tasks to worker nodes dynamically.
3. **Data Processing:** Worker nodes perform word counts on their assigned data chunks.
4. **Result Aggregation:** The master node combines partial results to compute the final word frequencies.

---

## **Technologies Used**
- **Programming Language:** Python
- **Communication Protocol:** Sockets
- **Python Libraries:**
  - `socket` for inter-node communication.
  - `multiprocessing` for local node simulation.
  - `matplotlib` for results visualization.

---

## **Installation**

### Prerequisites
1. Python 3.x installed.
2. Basic understanding of distributed systems.
3. Docker (optional) for containerized simulations.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Tharun1910/distributed-word-count.git
   cd distributed-word-count
