# 🔫 Firearm Types Predictor from Features
A Deep Learning-based classification system that predicts firearm types using weapon characteristics and performance features.

---

# 📖 Project Overview
The **Firearm Types Predictor** is a Machine Learning and Deep Learning project that classifies different firearm types based on their numerical characteristics. The model learns patterns from weapon attributes and predicts the correct firearm category using a Neural Network built with TensorFlow/Keras.
The project includes data preprocessing, feature engineering, model training, evaluation, and prediction, making it a complete end-to-end supervised learning pipeline.

---

# ✨ Key Features
- 🔫 Predicts firearm types from weapon features
- 📊 Performs dataset preprocessing
- 🧹 Handles missing values and feature preparation
- 📈 Data visualization and exploratory analysis
- 🤖 Deep Learning classification model
- ⚡ TensorFlow/Keras implementation
- 📉 Model evaluation using multiple metrics
- 📊 Training & validation loss visualization
- 🎯 Multi-class classification
- 📋 Easy-to-use Jupyter Notebook implementation

---

# 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| IDE | Jupyter Notebook |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Deep Learning | TensorFlow, Keras |
| Model Evaluation | Accuracy Score, Confusion Matrix |
| Dataset Source | Kaggle |

---

# 📂 Dataset
The project uses the **Free Fire Weapons Dataset**, containing numerical characteristics of different firearms.
## Dataset Information

| Attribute | Description |
|-----------|-------------|
| Dataset | Free Fire Weapons Dataset |
| Source | Kaggle |
| Target Variable | Firearm Type |
| Task | Multi-Class Classification |

## 📑 Dataset Features

| Feature | Description |
|----------|-------------|
| Weapon Feature 1 | Numerical weapon attribute |
| Weapon Feature 2 | Numerical weapon attribute |
| Weapon Feature 3 | Weapon performance characteristic |
| Weapon Feature 4 | Firearm specification |
| ... | Additional weapon-related features |
| Weapon Type | Target firearm category |

**Note:** Feature names may vary depending on the dataset version used.

# ⚙️ Data Preprocessing
- ✅ Loaded dataset using Pandas
- ✅ Inspected missing values
- ✅ Selected input and target features
- ✅ Converted labels into numerical format
- ✅ Split data into training and testing sets
- ✅ Prepared data for Neural Network training

---

# 🤖 Model Used
## 🧬 Deep Neural Network
A fully connected neural network is used to classify firearm types based on their numerical characteristics.
### Model Architecture
```text
Input Layer
      │
      ▼
Dense (32 neurons, ReLU)
      │
      ▼
Dense (16 neurons, ReLU)
      │
      ▼
Output Layer (Softmax)
      │
      ▼
Predicted Firearm Type
```

## ⚙️ Model Configuration
| Parameter | Value |
|-----------|-------|
| Optimizer | Adam |
| Loss Function | Categorical Crossentropy |
| Output Activation | Softmax |
| Hidden Activation | ReLU |
| Epochs | 50 |
| Batch Size | 32 |
| Early Stopping | Enabled |

---

# 📊 Evaluation Metrics
The model is evaluated using:
- ✅ Accuracy Score
- ✅ Confusion Matrix
- ✅ Mean Absolute Error (MAE)
- ✅ Mean Squared Error (MSE)
- ✅ R² Score
- ✅ Training & Validation Loss

---

# 📁 Project Structure
```text
Firearm-Types-Predictor/
│
├── Firearm_Types_Predictor_from_Features.ipynb
├── weapons_data.csv
├── README.md
└── requirements.txt
```

---

# ▶️ How to Run
## 1️⃣ Clone Repository
```bash
git clone https://github.com/yourusername/Firearm-Types-Predictor.git
```
## 2️⃣ Navigate into the Project
```bash
cd Firearm-Types-Predictor
```
## 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
or
```bash
pip install pandas numpy matplotlib seaborn scikit-learn tensorflow
```
## 4️⃣ Download Dataset
Download the **Free Fire Weapons Dataset** from Kaggle and place:
```text
weapons_data.csv
```
inside the project folder.
## 5️⃣ Launch Jupyter Notebook
```bash
jupyter notebook
```
Open
```text
Firearm_Types_Predictor_from_Features.ipynb
```
Run all cells sequentially.

---

# 📈 Project Workflow
```text
Weapon Dataset
      │
      ▼
Data Loading
      │
      ▼
Preprocessing
      │
      ▼
Feature Selection
      │
      ▼
Train-Test Split
      │
      ▼
Deep Neural Network
      │
      ▼
Prediction
      │
      ▼
Performance Evaluation
```

---

# 🚀 Future Improvements
- 🌐 Deploy as a web application
- 📱 Streamlit dashboard for live predictions
- ☁️ Cloud deployment
- 📊 Hyperparameter optimization
- 🤖 Compare with Random Forest, XGBoost, and SVM
- 📈 Improve accuracy using feature engineering

---

~ sukhada20
