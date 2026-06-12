# Star and Galaxy Image Classifier
A deep learning project implemented in PyTorch that performs binary image classification to distinguish between **Stars** and **Galaxies**. The project leverages transfer learning via a pre-trained **MobileNetV2** backbone to achieve high accuracy with minimal training time.

---

## 📌 Project Overview
Astronomical data classification is a fundamental step in processing large-scale sky surveys. This project automates the sorting of star and galaxy image cutouts. It handles everything from programmatic dataset downloading and automated preprocessing to neural network training and comprehensive model evaluation.

---

## 🚀 Key Features
* **Automated Data Retrieval:** Dynamically downloads the required dataset directly from Kaggle using `kagglehub`.
* **Transfer Learning Pipeline:** Utilizes a pre-trained MobileNetV2 architecture, optimized for lightweight and fast training environments.
* **Robust Evaluation:** Includes performance evaluation metrics such as classification reports (precision, recall, F1-score) and confusion matrix visualization.
* **State Preservation:** Tracks and loads the best model weights based on validation accuracy during the training loop.

---

## 🛠️ Tech Stack & Requirements
The project requires Python 3 and the following primary libraries:
* **PyTorch** & **Torchvision** (Deep Learning framework and pre-trained backbones)
* **Kagglehub** (Dataset programmatic download)
* **Scikit-Learn** (Classification report and confusion matrix generation)
* **Matplotlib** & **NumPy** (Data visualization and numerical arrays)
To install the required packages, run:
```bash
pip install torch torchvision kagglehub scikit-learn matplotlib numpy
```

---

## 📂 Dataset Details
The model trains on the **Dummy Astronomy Data** (`divyansh22/dummy-astronomy-data`) available on Kaggle.
* **Target Classes:** `galaxy` and `star`
* **Data Splits:** 80% of the dataset is allocated for training, and 20% is held out for validation.
* **Image Preprocessing:** All cutout images are resized to `224x224` pixels and normalized using ImageNet channel means (`[0.485, 0.456, 0.406]`) and standard deviations (`[0.229, 0.224, 0.225]`).

---

## ⚙️ Model Architecture & Training Setup
* **Base Model:** Pre-trained `mobilenet_v2` backbone.
* **Classifier Layer:** The final classifier layer is replaced with a custom `nn.Linear` block mapping to the `2` target classes.
* **Loss Function:** `CrossEntropyLoss`.
* **Optimizer:** `Adam` optimizer with a learning rate of `1e-4`.
* **Batch Size:** 32.

---

## 📊 Performance & Evaluation Results
The performance breakdown recorded from the validation pass highlights strong predictive power:
### Training Logs (1 Epoch Demonstration)
```text
Epoch 1/1
------------------------------
Train Loss: 0.1944 | Acc: 0.9147
Val Loss: 0.3241 | Acc: 0.8596
```
### Classification Report
The model achieves an overall classification accuracy of **86%**:
```text
              precision    recall  f1-score   support

      galaxy       0.74      0.72      0.73       208
        star       0.90      0.91      0.91       590

    accuracy                           0.86       798
   macro avg       0.82      0.81      0.82       798
weighted avg       0.86      0.86      0.86       798
```
* **Stars:** Captured with higher precision (90%) and recall (91%) due to a larger representative support size in the sample data.
* **Galaxies:** Achieved a balanced 73% F1-score.

---

## 💻 How to Use
1. **Open the Notebook:** Run the Jupyter Notebook `Star_and_Galaxy_Classifier.ipynb` in your preferred environment (e.g., Google Colab, Jupyter Lab).
2. **Execute Steps:**
* Download the dataset through the initial `kagglehub` code block.
* Set up your target device (`cuda` will automatically be prioritized if a GPU is available).
* Run the training module to compute metrics and plot the final `Confusion Matrix`.

---

~ sukhada20
