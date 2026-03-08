# Triangle Counting in Complex Networks

This project implements and evaluates various algorithms for triangle counting within graphs, focusing on both exact and approximate methodologies. It explores the trade-offs between accuracy, efficiency, and suitability for different graph sizes and densities.

---

## Features

### Core Functionality
* **Exact Counting**: Implements three exact algorithms:
    * **All Triplets**: A brute-force method that checks every possible triplet of nodes.
    * **Node Iterator**: Iterates over each node and examines pairs of its neighbors to identify triangles.
    * **Compact Forward**: An optimized exact method that exploits node ordering and common neighbor searches to reduce computational overhead.
* **Approximate Counting (DOULION)**: Uses graph sparsification by randomly removing edges with a probability $p$ to estimate total triangles in large-scale graphs.
* **Streaming Estimation (TRIEST)**: Designed for dynamic graphs using reservoir sampling to maintain a fixed-size edge sample and estimate triangle counts during edge insertions.

### Technical Features
* **Deduplication**: Ensures unique triangle identification by sorting node triplets.
* **Scalability**: Evaluated across small-scale (GR-QC), medium-scale (New Sites), and large-scale (Artist) datasets.
* **Performance Tracking**: Includes built-in execution timers and triangle counters for benchmarking.

---

## Architecture

The project is structured into modular components:
* **Main.py**: The entry point for the application, handling execution and result presentation.
* **Algorithms/**: Contains dedicated classes for each counting logic (e.g., `AllTriplets.py`, `NodeIterator.py`, `CompactForward.py`, `Doulion.py`, `Triest.py`).
* **Graphs/**: A directory for storing dataset CSV files (e.g., `ca-GrQc.csv`, `tvshow_edges.csv`).

---

## Technology Stack

* **Language**: Python 3.x
* **Data Processing**: `pandas` for CSV manipulation and data loading.
* **Graph Theory**: `networkx` for graph construction and neighbor analysis.
* **Utilities**: `numpy` (for random choice in Doulion) and `time` (for benchmarking).

---

## Results & Performance

Below are the benchmark results as recorded in the source code implementation:

### 1. Exact Algorithms Benchmarks
| Dataset | Algorithm | Triangles Found | Execution Time (s) |
| :--- | :--- | :--- | :--- |
| **ca-GrQc.csv** | All Triplets | 48,260 | 2.059 |
| | Node Iterator | 48,260 | 1.610 |
| | Compact Forward | 48,260 | 1.288 |
| **new_sites_edges.csv** | All Triplets | 387,444 | 68.657 |
| | Node Iterator | 387,444 | 18.451 |
| | Compact Forward | 387,444 | 29.882 |
| **artist_edges.csv** | All Triplets | 2,273,700 | 846.824 |
| | Node Iterator | 2,273,700 | 151.738 |
| | Compact Forward | 2,273,700 | 328.705 |

### 2. Approximate Estimation
The **Doulion** algorithm estimates the original count by using the formula:
$$\text{Estimation} = \frac{\text{Triangles in Sparsified Graph}}{p^3}$$
(where $p$ is the keep-probability).

---

## Getting Started

### Prerequisites
Ensure you have Python installed along with the following libraries:
* pandas
* networkx
* numpy

### Installation
1. Clone this repository to your local machine.
2. Ensure your datasets are placed in a folder named `Graphs` relative to the script.
3. Install dependencies:
   ```bash
   pip install pandas networkx numpy