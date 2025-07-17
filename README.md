# Material Discovery with Graph Neural Networks (GNNs)

> Proyecto de Ciencia de Datos que utiliza redes neuronales con grafos (GNNs) para predecir propiedades de materiales a partir de su estructura atómica. Implementado con PyTorch Geometric.

---

## 🌍 English Version

### 🎓 Project Overview
This project explores **material property prediction** using **Graph Neural Networks (GNNs)**, leveraging atomic structure data from the `matbench_mp_e_form` dataset (via Matminer). Each material is represented as a graph, where nodes are atoms and edges are bonds or distances.

### 🚀 Goals
- Predict the **formation energy per atom** of materials.
- Convert crystalline structures into graphs.
- Build a GNN model from scratch with **PyTorch Geometric**.
- Evaluate performance and visualize results.

### 📂 Dataset
- Source: [Matbench - matminer](https://hackingmaterials.lbl.gov/matminer/)
- Dataset: `matbench_mp_e_form`
- Format: CIF files transformed into graphs.

### 💪 Tech Stack
- Python
- PyTorch + PyTorch Geometric
- Pandas, Matplotlib, Scikit-learn
- ASE (Atomic Simulation Environment), Matminer

### 💡 Highlights
- Hands-on conversion of materials to graph format.
- Training a custom GNN for regression.
- Error analysis, visualizations, and model saving.

---

## 🌐 Versión en Español

### 🎓 Descripción del Proyecto
Este proyecto aplica **Redes Neuronales con Grafos (GNNs)** para predecir **la energía de formación** de materiales a partir de su estructura atómica. Cada material se modela como un grafo, donde los nodos representan átomos y las aristas representan enlaces o distancias.

### 🚀 Objetivos
- Predecir la energía de formación por átomo.
- Convertir estructuras cristalinas en grafos.
- Implementar una GNN desde cero usando **PyTorch Geometric**.
- Evaluar el modelo y visualizar resultados.

### 📂 Conjunto de Datos
- Fuente: [Matbench - matminer](https://hackingmaterials.lbl.gov/matminer/)
- Dataset: `matbench_mp_e_form`
- Formato: Archivos CIF convertidos a grafos.

### 💪 Tecnologías Utilizadas
- Python
- PyTorch + PyTorch Geometric
- Pandas, Matplotlib, Scikit-learn
- ASE, Matminer

### 💡 Lo Destacado
- Procesamiento directo de estructuras a grafos.
- Entrenamiento de una red neuronal para regresión.
- Análisis de errores y visualización de resultados.

---

## 📊 Resultado
El modelo fue capaz de aprender patrones en los datos atómicos y predecir energía de formación con buen desempeño, visualizando la relación entre predicciones y valores reales.

---

## 👀 Screenshots
Encuentra las gráficas generadas en la carpeta `/images/`.

---

## 🌍 Author / Autor
**Nabila Isabel Padilla Resendiz (mecatronabi)**
- Aspiring Data Scientist
- Background: Mechatronics & Technology Management
- [GitHub Profile](https://github.com/mecatronabi)
