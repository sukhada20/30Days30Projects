# Cotton Crop Disease Detection using DenseNet121
This repository contains an end-to-end deep learning pipeline built with PyTorch to detect and classify diseases in cotton crops using transfer learning. By leveraging a pre-trained **DenseNet121** model, the system achieves high classification accuracy, providing a reliable tool for early disease identification and smart agriculture applications.

--- 

## 🚀 Project Overview
Crop diseases are a major threat to global food security and agricultural economies. This project automates the identification of cotton crop abnormalities by analyzing leaf images. Key elements of the implementation include:
* **Automated Data Fetching**: Utilizes `kagglehub` to download the latest version of the target dataset directly into the workspace.
* **Transfer Learning**: Employs a pre-trained DenseNet121 architecture as a frozen feature extractor to minimize training time while retaining deep visual representations.
* **Robust Evaluation**: Monitored across multiple epochs using cross-entropy loss, precision-recall indicators, and confusion matrices to guarantee robustness.

---

## 📊 Dataset Detail
The model is trained on the **Cotton Crop Disease Detection** dataset hosted on Kaggle. 
* **Source**: `paridhijain02122001/cotton-crop-disease-detection`
* **Structure**: Divided into explicit `train` and `test` directories matching standard PyTorch `ImageFolder` layouts.
* **Preprocessing**: 
  * All images are dynamically resized to `224 × 224` pixels.
  * Training data undergoes data augmentation via random horizontal flips to combat overfitting.
  * Pixels are normalized using standard ImageNet mean values `[0.485, 0.456, 0.406]` and standard deviations `[0.229, 0.224, 0.225]`.

---

## 🧠 Model Architecture
The core architecture treats the backbone of **DenseNet121** as a fixed feature extractor, updating only a newly appended custom classification head tailored to the dataset's unique classes:
```
       [ Input Image: 224x224x3 ]
                    │
                    ▼
┌──────────────────────────────────────┐
│  DenseNet121 Base (Frozen Features)  │
└──────────────────────────────────────┘
                    │
                    ▼
┌──────────────────────────────────────┐
│     Custom Classifier Sequence       │
│  ├─ Linear (1024 -> 512)             │
│  ├─ ReLU Activation                  │
│  ├─ Dropout Layer (p=0.3)            │
│  └─ Linear (512 -> Number of Classes)│
└──────────────────────────────────────┘
                    │
                    ▼
          [ Class Predictions ]
```
### Hyperparameters
* **Loss Function**: Cross-Entropy Loss (`nn.CrossEntropyLoss`)
* **Optimizer**: Adam Optimizer (`optim.Adam`)
* **Learning Rate**: `0.001`
* **Batch Size**: `32`
* **Epochs**: `5`

--- 

## 📈 Training Performance
The model converged rapidly within 5 epochs, capturing optimal weights on validation benchmarks early in the process:

| Epoch | Train Loss | Train Accuracy | Val Loss | Val Accuracy | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | 0.6062 | 78.91% | 0.2082 | 92.79% | Saved Best Model |
| **2** | 0.3211 | 88.75% | 0.1867 | 93.76% | Saved Best Model |
| **3** | 0.2536 | 91.49% | 0.2292 | 91.82% | - |
| **4** | 0.2217 | 92.30% | 0.1252 | **96.39%** | **Saved Best Model (Peak)** |
| **5** | 0.2123 | 92.44% | 0.1296 | 95.42% | - |

*The final evaluation restores the top-performing state-dictionary evaluated during Epoch 4.*

---

## 🛠️ Installation & Setup
1. **Clone the Repository**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/cotton-disease-detection.git](https://github.com/YOUR_USERNAME/cotton-disease-detection.git)
   cd cotton-disease-detection
   ```
2. **Install Required Libraries**
Ensure you have Python 3.8+ and install the dependencies:
```bash
pip install torch torchvision matplotlib scikit-learn tqdm kagglehub
```
3. **Run the Notebook**
Launch Jupyter Notebook or open the file in Google Colab/Kaggle Notebooks and run all cells:
```bash
jupyter notebook Cotton_Disease_Detection_using_DenseNet121.ipynb
```

---

## 📂 Project Workflow & File Directory
* **Dataset Download**: Automatically managed by `kagglehub` on initial execution.
* **Transforms & Dataloaders**: Built dynamically with PyTorch utility functions.
* **Training & Validation Loop**: Saves the model to `best_model.pth` when validation accuracy hits a new ceiling.
* **Performance Visualizations**: Outputs training vs. validation loss/accuracy curves alongside Scikit-Learn evaluation matrices.

---

~ sukhada20
