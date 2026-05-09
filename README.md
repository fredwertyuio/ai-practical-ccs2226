# CCS 2226 Foundations of AI - Practical Project (2026)

## Student Submission

This repository contains practical implementations for the CCS 2226 Artificial Intelligence course. The project covers neural networks, constraint satisfaction problems, logic programming, and search algorithms.

---

## Task 1: MNIST Digit Classification
- Implemented using TensorFlow/Keras
- Neural network trained on MNIST dataset
- Classifies handwritten digits (0–9)
- Uses Dense layers with ReLU and Softmax activation
- Achieved ~97–98% accuracy on test data

---

## Task 2: Constraint Satisfaction Problems (CSP)

### (a) Australia Map Coloring
- Uses 3 colors: Red, Green, Blue
- Ensures no adjacent regions share the same color
- Solved using constraint programming approach

### (b) Nairobi Sub-County Coloring
- Models 17 sub-counties
- Applies graph coloring constraints
- Ensures no neighboring regions share the same color
- Demonstrates real-world CSP application

---

##  Task 3: Prolog Family Tree
- Implemented using SWI-Prolog
- Represents family relationships using logic rules:
  - parent
  - sibling
  - grandparent
  - uncle and aunt
  - cousin
- Demonstrates logical inference and rule-based reasoning

---

##  Task 4: Search Algorithms

### Breadth First Search (BFS)
- Explores nodes level by level
- Guarantees shortest path in unweighted graph

### Depth First Search (DFS)
- Explores deeper paths first
- Uses recursive traversal

Both algorithms return the path from initial node to goal state.

---

##  How to Run the Project

### Python Files
```bash
python task1_mnist.py
python task2_australia.py
python task2_nairobi.py
python task4_search.py