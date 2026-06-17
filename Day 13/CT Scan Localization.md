# CT Slice Localization
This project implements a deep learning model for **CT Slice Localization**. The goal of this model is to predict the relative position (reference value) of a CT scan slice within a 3D volume based on its image features.

--- 

## 📌 Project Overview
This project processes medical imaging data to localize CT scan slices. It uses a regression-based approach to map extracted image features to a continuous "reference" value, representing the slice's location.

---

## 🚀 Key Features
* **Automated Data Acquisition**: Programmatically downloads the "CT Slice Localization" dataset from Kaggle via `kagglehub`.
* **Deep Learning Pipeline**: Utilizes a custom TensorFlow/Keras sequential model with Dense layers to perform regression on structured numerical data.
* **Efficient Training**: Employs `EarlyStopping` with a patience of 5 epochs to prevent overfitting and ensure the model retains the best weights.
* **Performance Metric**: Uses Mean Absolute Error (MAE) as the loss function for regression tasks.

---

## 🛠️ Tech Stack
* **Python 3**
* **TensorFlow/Keras**: Used for building and training the neural network.
* **Scikit-Learn**: Utilized for data preprocessing (`train_test_split`) and performance evaluation.
* **Pandas & NumPy**: For efficient data manipulation and numerical operations.
* **Matplotlib**: For visualization of data trends.

---

## 📂 Dataset Details
* **Source**: UCI Machine Learning Repository (hosted on Kaggle).
* **Features**: The model processes 384 input features (`value0` through `value383`) extracted from the CT slices.
* **Target**: The continuous `reference` value.
* **Data Volume**: The processed dataset contains 53,500 samples.

---

## ⚙️ Model Architecture
The model is a simple, feed-forward neural network designed for high-dimensional regression:
* **Input Layer**: Accepts 384 input features.
* **Hidden Layers**:
* Dense layer with 64 units and `ReLU` activation.
* Dense layer with 32 units and `ReLU` activation.
* **Output Layer**: A single neuron with `linear` activation to predict the continuous reference value.
* **Optimizer**: Adam.
* **Loss Function**: Mean Absolute Error (MAE).

---

## 💻 How to Run
1. Ensure you have the required libraries installed:
```bash
pip install tensorflow pandas numpy scikit-learn matplotlib kagglehub
```
2. Run the `CT_Scan_Localization.ipynb` notebook in an environment like Google Colab or Jupyter Lab.
3. The script will automatically authenticate and download the dataset to your local cache before starting the training process.

---

~ sukhada20
