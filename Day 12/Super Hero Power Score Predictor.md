# 🦸‍♂️ Super Hero Power Score Predictor
An end-to-end Machine Learning pipeline and interactive web interface built with Python to predict a superhero's **Power Score** based on their underlying raw characteristics, alignment, and attributes. The project uses a regression model alongside automated data retrieval and interactive serving with Gradio.

---

## 📊 Project Overview
Determining a hero's absolute capability often involves subjective debates. This project provides an empirical approach by leveraging statistical modeling to analyze superhero metrics across various comic book universes. 
### Key Implementations:
* **Programmatic Data Fetching:** Automatically downloads the live dataset using `kagglehub` from Kaggle servers straight into the workspace cache.
* **Feature Engineering & Imputation:** Implements robust preprocessing routines to manage numeric characteristics and factor in zero/null distributions across categorical columns.
* **Statistical Regression:** Trains an explainable **Linear Regression** algorithm using Scikit-Learn to map capability traits to absolute numerical indices.
* **Interactive UI Web App:** Deploys a consumer-facing dashboard interface using **Gradio Blocks**, enabling users to tweak slider features and see predictions update live.

---

## 📂 Dataset Profile
The dataset utilized is the **Superheroes Abilities Dataset** (`hemajitpatel/superheros-abilities-dataset`) hosted on Kaggle. 
### Available Dimensions:
* **Identifiers/Categoricals:** `Name`, `Universe` (e.g., Marvel, DC), `Alignment` (e.g., Hero, Villain, Anti-Hero), `Weapon`
* **Abilities / Core Quantitative Features:**
  * `Strength`
  * `Speed`
  * `Intelligence`
  * `Combat Skill`
* **Target / Performance Metrics:** `Power Score`, `Popularity Score`

---

## ⚙️ Model & Tech Stack
* **Language:** Python 3.8+
* **Data Processing:** `Pandas`, `NumPy`
* **Visualization:** `Seaborn`, `Matplotlib` (forced onto the headless `Agg` backend for container/notebook execution compatibility)
* **ML Architecture:** Scikit-Learn (`LinearRegression`)
* **Evaluation Framework:** $R^2$ Score, Mean Squared Error (MSE), and Feature Permutation Importance (`permutation_importance`)
* **Web UI Server:** `Gradio`

---

## 💻 Installation & Local Deployment
### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/superhero-power-predictor.git](https://github.com/YOUR_USERNAME/superhero-power-predictor.git)
cd superhero-power-predictor
```
### 2. Install Required Dependencies
Ensure you have your environment activated, then install the prerequisite libraries:
```bash
pip install numpy pandas matplotlib seaborn scikit-learn gradio kagglehub
```
### 3. Run the Execution Pipeline
Launch Jupyter Notebook / Lab, or run the notebook script directly inside an IDE or cloud environment (such as Google Colab):
```bash
jupyter notebook Super_Hero_Power_Score_Predictor.ipynb
```
When you reach the final cell block, Gradio spins up an internal server and provisions a temporary secure public tunnel:
```text
* Running on public URL: [https://b873d08b3638189df9.gradio.live](https://b873d08b3638189df9.gradio.live)
This share link expires in 1 week.
```
![image](https://github.com/user-attachments/assets/4b2111f0-4fbf-4823-afc1-ec52366cea68)

---

## 📈 Pipeline Implementation Workflow
1. **Ingestion:** `kagglehub.dataset_download` triggers clean asset staging.
2. **Exploratory Data Analysis (EDA):** Uses Seaborn distribution plots (`sns.histplot`) with kernel density estimation curves to check distribution skews and out-of-bounds metrics.
3. **Training & Splitting:** Divides the structured indices via a standardized train-test split before regression fitting.
4. **Feature Importance:** Computes Permutation Importance scores to evaluate which metrics (e.g., `Strength` vs `Combat Skill`) exert the most mathematical leverage over the target `Power Score`.
5. **Interactive UI App:** Integrates the trained Scikit-Learn weights back into a custom function wrapped by Gradio sliders and input forms for public predictions.

---

~ sukhada2
