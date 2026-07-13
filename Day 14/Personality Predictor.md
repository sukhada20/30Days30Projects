# 🧠 Personality Predictor using Machine Learning
Predict whether a person is an **Introvert** or **Extrovert** using behavioral and social interaction data with multiple Machine Learning models.

---

# 📖 Project Overview
The **Personality Predictor** is a Machine Learning project that classifies individuals as **Introverts** or **Extroverts** based on their behavioral characteristics. The system analyzes social habits, communication preferences, stage confidence, and interaction patterns to identify personality traits.
The project compares multiple Machine Learning algorithms along with a Deep Neural Network to determine which model provides the highest prediction accuracy. Data preprocessing, feature scaling, label encoding, model evaluation, and performance comparison are all included in the workflow.

---

# ✨ Key Features
- 🧠 Predicts personality type (Introvert/Extrovert)
- 📊 Performs complete data preprocessing
- 🔄 Handles categorical feature encoding
- 📈 Standardizes numerical features
- 🤖 Trains multiple Machine Learning models
- 🌲 Random Forest Classifier
- 🚀 XGBoost Classifier
- 📉 Logistic Regression
- 🧬 Deep Neural Network (TensorFlow/Keras)
- 📋 Model performance comparison
- 📉 Confusion Matrix generation
- 📑 Classification Report
- 📊 Accuracy, Precision, Recall and F1-Score evaluation

---

# 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| IDE | Jupyter Notebook |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Gradient Boosting | XGBoost |
| Deep Learning | TensorFlow, Keras |
| Data Scaling | StandardScaler |
| Encoding | LabelEncoder |

---

# 📂 Dataset
The dataset contains behavioral and personality-related information collected from individuals.
## Dataset Information

| Attribute | Description |
|-----------|-------------|
| Rows | Personality records |
| Target Variable | Personality |
| Classes | Introvert, Extrovert |

## 📑 Dataset Features

| Feature | Description |
|----------|-------------|
| Time_spent_Alone | Hours spent alone |
| Stage_fear | Fear of speaking on stage |
| Social_event_attendance | Frequency of attending social events |
| Going_outside | Frequency of going outside |
| Drained_after_socializing | Feeling tired after social interactions |
| Friends_circle_size | Number of close friends |
| Post_frequency | Social media posting frequency |
| Personality | Target class (Introvert/Extrovert) |

# ⚙️ Data Preprocessing
- ✅ Loaded dataset using Pandas
- ✅ Encoded categorical values using LabelEncoder
- ✅ Converted target labels into numerical values
- ✅ Standardized features using StandardScaler
- ✅ Split dataset into Training (80%) and Testing (20%)

---

# 🤖 Models Used
## 🌲 Random Forest Classifier
- An ensemble learning algorithm that builds multiple decision trees and combines their outputs to improve prediction accuracy.
## 🚀 XGBoost Classifier
- A powerful gradient boosting algorithm known for high performance and efficient handling of structured data.
## 📉 Logistic Regression
- A statistical classification algorithm used as a baseline model for binary prediction tasks.
## 🧬 Deep Neural Network
- A fully connected neural network implemented using TensorFlow/Keras.
### Architecture
```
Input Layer
      │
      ▼
Dense (64 neurons, ReLU)
      │
      ▼
Dropout (0.3)
      │
      ▼
Dense (32 neurons, ReLU)
      │
      ▼
Dense (1 neuron, Sigmoid)
      │
      ▼
Prediction
```
### Model Configuration

| Parameter | Value |
|-----------|-------|
| Optimizer | Adam |
| Loss Function | Binary Crossentropy |
| Activation | ReLU + Sigmoid |
| Epochs | 30 |
| Batch Size | 32 |
| Validation Split | 10% |

---

# 📊 Model Evaluation Metrics
The models are evaluated using:
- ✅ Accuracy
- ✅ Precision
- ✅ Recall
- ✅ F1 Score
- ✅ Classification Report
- ✅ Confusion Matrix

---

# 📁 Project Structure
```
Personality-Predictor/
│
├── Personality Predictor.ipynb
├── personality_dataset.csv
├── README.md
└── requirements.txt
```

---

# ▶️ How to Run
## 1️⃣ Clone Repository
```bash
git clone https://github.com/yourusername/Personality-Predictor.git
```
## 2️⃣ Move into Project
```bash
cd Personality-Predictor
```
## 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
or
```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost tensorflow
```
## 4️⃣ Add Dataset
Place the dataset file:
```
personality_dataset.csv
```
inside the project directory.
## 5️⃣ Run Notebook
```bash
jupyter notebook
```
Open
```
Personality Predictor.ipynb
```
and execute all cells.

---

# 📈 Workflow
```text
Dataset
   │
   ▼
Data Cleaning
   │
   ▼
Label Encoding
   │
   ▼
Feature Scaling
   │
   ▼
Train-Test Split
   │
   ▼
Model Training
   │
   ├── Random Forest
   ├── XGBoost
   ├── Logistic Regression
   └── Neural Network
   │
   ▼
Prediction
   │
   ▼
Performance Evaluation
```

---

# 🚀 Future Improvements
- 🌐 Deploy using Flask or Streamlit
- 📱 Build a web application
- ☁️ Cloud deployment
- 📊 Hyperparameter tuning
- 🧠 Experiment with additional ensemble methods
- 📈 Real-time personality prediction interface

---

~ sukhada20
