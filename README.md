# 🛡️ FraudShield AI

### Credit Card Fraud Detection using Machine Learning

FraudShield AI is an end-to-end Machine Learning application that detects potentially fraudulent credit card transactions through an interactive Streamlit web interface.

The application accepts transaction features, applies the required preprocessing, passes the processed data through a trained Machine Learning model, and returns the predicted transaction class along with the estimated probability of fraud.

---

## 📌 Features

- Real-time fraud prediction
- Interactive Streamlit interface
- Transaction amount and time input
- Support for anonymized PCA features (`V1`–`V28`)
- Automated feature scaling for `Time` and `Amount`
- Binary fraud classification
- Fraud probability estimation
- Serialized model loading using Joblib
- Cached model and scaler loading using Streamlit

---

## 🧠 How It Works

The application follows a simple Machine Learning inference pipeline:

**Transaction Input → Preprocessing → ML Model → Prediction → Fraud Probability → Result**

The user provides:

- Transaction Time
- Transaction Amount
- PCA features `V1` through `V28`

The application then:

1. Collects the transaction parameters.
2. Converts the input into a Pandas DataFrame.
3. Scales `Time` and `Amount` using the saved scaler.
4. Passes the processed transaction to the trained model.
5. Predicts whether the transaction is legitimate or fraudulent.
6. Calculates the estimated probability of fraud.
7. Displays the result through the Streamlit interface.

---

## 📊 Dataset

The project is designed around the widely used **Credit Card Fraud Detection dataset**.

The dataset contains anonymized transaction features. The original confidential features have been transformed using Principal Component Analysis (PCA).

### Input Features

| Feature | Description |
|---|---|
| `Time` | Seconds elapsed between the transaction and the first transaction in the dataset |
| `V1` – `V28` | Anonymized PCA-transformed transaction features |
| `Amount` | Transaction amount |

### Target Variable

| Class | Meaning |
|---|---|
| `0` | Legitimate transaction |
| `1` | Fraudulent transaction |

> The `V1`–`V28` variables are anonymized PCA components and do not represent directly interpretable transaction attributes.

---

## 🏗️ Project Architecture

```text
                         FraudShield AI
                               │
                               ▼
                    ┌────────────────────┐
                    │   Streamlit UI     │
                    └─────────┬──────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │   Transaction Inputs    │
                 │                         │
                 │ Time                    │
                 │ Amount                  │
                 │ V1 – V28                │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │     Preprocessing       │
                 │                         │
                 │ Scale Time & Amount     │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │   Trained ML Model      │
                 │                         │
                 │ fraud_model.pkl         │
                 └────────────┬────────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
             ┌─────────────┐    ┌───────────────┐
             │ Prediction  │    │ Fraud         │
             │ Class       │    │ Probability   │
             └──────┬──────┘    └───────┬───────┘
                    │                   │
                    └─────────┬─────────┘
                              ▼
                    ┌────────────────────┐
                    │   Result Display   │
                    │                    │
                    │ Legitimate / Fraud │
                    └────────────────────┘

```
----

## 📁 Project Structure

FraudShield-AI/
│
├── app.py
│
├── models/
│   ├── fraud_model.pkl
│   └── scaler.pkl
│
├── requirements.txt
│
└── README.md

### app.py
Main Streamlit application containing:

- UI configuration
- Transaction input collection
- Model loading
- Scaler loading
- Input preprocessing
- Fraud prediction
- Probability calculation
- Result visualization

### models/fraud_model.pkl

The trained Machine Learning classification model used for fraud detection.

### models/scaler.pkl

The fitted scaler used to transform the Time and Amount features before inference.

### requirements.txt

Contains the Python packages required to run the application.


## 🛠️ Tech Stack
Technology	Purpose
Python	Core programming language
Pandas	Data manipulation
NumPy	Numerical operations
Scikit-learn	Machine Learning and preprocessing
Joblib	Model and scaler serialization
Streamlit	Interactive web application

## ⚙️ Model Inference

The trained model and preprocessing scaler are loaded using Joblib:
```
model = joblib.load('models/fraud_model.pkl')
scaler = joblib.load('models/scaler.pkl')
```
Streamlit resource caching is used to avoid repeatedly loading the model and scaler:
```
@st.cache_resource
def load_artifacts():
    model = joblib.load('models/fraud_model.pkl')
    scaler = joblib.load('models/scaler.pkl')
    return model, scaler
```
## 🔄 Data Preprocessing

Before making a prediction, Time and Amount are transformed using the saved scaler:
```
input_df[['Time', 'Amount']] = scaler.transform(
    input_df[['Time', 'Amount']]
)
```

The same fitted scaler used during model development should be used during inference to maintain consistency between training and prediction.

The PCA features (V1–V28) are passed to the model in their provided form.

## 🔮 Prediction

The application generates the predicted class using:
```
prediction = model.predict(input_df)
```
The estimated probability of each class is obtained using:
```
prediction_proba = model.predict_proba(input_df)
```
The probability associated with class 1 is displayed as the estimated fraud probability:
```
prediction_proba[0][1]
```

## 🖥️ Application Interface

The application provides an interactive sidebar where users can enter transaction parameters.
```
Transaction Parameters
Transaction Time
Transaction Amount
V1
V2
V3
...
V28
```
After entering the values, the transaction summary is displayed in the main panel.

The user can then click:
```
Predict Fraud Status
```
to generate the prediction.

## 🚨 Prediction Results

### Legitimate Transaction

When the model predicts:
```
Class = 0
```
the application displays:
```
✅ Transaction Appears Legitimate.
```
along with the estimated fraud probability.

### Fraudulent Transaction

When the model predicts:
```
Class = 1
```
the application displays:
```
⚠️ Alert! High Fraud Probability Detected!
```
along with the estimated probability associated with the fraud class.

## 💻 Installation

### 1. Clone the Repository
```
git clone https://github.com/<your-username>/FraudShield-AI.git
```
Navigate into the project:
```
cd FraudShield-AI
```
### 2. Create a Virtual Environment

#### Windows
```
python -m venv venv
```
Activate the environment:
```
venv\Scripts\activate
```
#### macOS / Linux
```
python3 -m venv venv
```
Activate the environment:
```
source venv/bin/activate
```
#### 3. Install Dependencies
```
pip install -r requirements.txt
```
▶️ Run the Application

Start the Streamlit application:
```
streamlit run app.py
```
The application will be available at:
```
http://localhost:8501
```

## 📦 Requirements

The project requires:
```
streamlit
pandas
numpy
scikit-learn
joblib
```
A requirements.txt file can contain:
```
streamlit
pandas
numpy
scikit-learn
joblib
```

## 📈 Evaluation Metrics

Fraud detection is generally an imbalanced classification problem. Therefore, evaluating the model using accuracy alone may not provide a complete picture of its performance.

Useful evaluation metrics include:

- Precision
- Recall
- F1-Score
- ROC-AUC
- PR-AUC
- Confusion Matrix

#### Precision

Measures how many transactions predicted as fraudulent are actually fraudulent.

#### Recall

Measures how many actual fraudulent transactions are successfully detected.

#### F1-Score

Provides a balance between precision and recall.

#### ROC-AUC

Measures the model's ability to distinguish between legitimate and fraudulent transactions across different classification thresholds.

#### PR-AUC

Can be particularly useful for evaluating models on highly imbalanced fraud detection datasets.

## ⚠️ Important Note

The probability displayed by the application is obtained directly from the trained classifier through:
```
model.predict_proba(input_df)
```
Therefore, it represents the model's estimated probability and should not automatically be interpreted as a perfectly calibrated real-world probability.

For a production financial fraud detection system, additional validation, probability calibration, threshold optimization, monitoring, and domain-specific testing would be required.

## 🔐 Security & Privacy

The V1–V28 features are anonymized PCA-transformed variables.

This project is intended for educational and demonstration purposes and should not be considered a production-ready financial fraud prevention system.

A production implementation would require additional security measures such as:

- Authentication and authorization
- Encryption
- Secure API communication
- Data privacy controls
- Audit logging
- Model monitoring
- Access control

## Fraud investigation workflows

### 🚀 Future Improvements

The current application can be extended into a more comprehensive fraud detection platform.

#### Machine Learning
- Hyperparameter optimization
- Cross-validation
- Class imbalance handling
- Threshold optimization
- Probability calibration
- Ensemble models
- Anomaly detection
- Cost-sensitive classification

#### Explainable AI

Integrate SHAP or similar explainability techniques to understand why a transaction was flagged as potentially fraudulent.

For example:
```
Transaction Risk Explanation

V14        ███████████████
V10        ███████████
Amount     ███████
V4         █████
```
This could help fraud analysts understand the factors contributing to a prediction.

#### Application

- CSV batch prediction
- Transaction history
- Fraud analytics dashboard
- Risk scoring
- Confusion matrix visualization
- Model performance dashboard
- Adjustable classification threshold
- Transaction monitoring

#### Production Architecture

A future production-oriented version could use:
```
Transaction
     │
     ▼
API / Transaction Gateway
     │
     ▼
Fraud Detection Service
     │
     ▼
ML Model
     │
     ▼
Risk Score
     │
     ├──────────────► Approve
     │
     ├──────────────► Review
     │
     └──────────────► Block
```

Additional infrastructure could include FastAPI, Docker, PostgreSQL, Redis, Kafka, MLflow, cloud deployment, and model monitoring.

🧪 Example

A transaction can be entered through the interface using:
```
Time:   1200
Amount: 50

V1:  0.0
V2:  0.0
V3:  0.0
...
V28: 0.0
```
After clicking Predict Fraud Status, the application processes the input and returns the prediction generated by the trained model.

Example output:
```
✅ Transaction Appears Legitimate.

Fraud Probability: XX.XX%
```
or:
```
⚠️ Alert! High Fraud Probability Detected!

Confidence: XX.XX%
```
The values shown above are illustrative. Actual predictions depend on the trained model and input features.

## 📚 Key Learning Outcomes

This project demonstrates the complete transition from a trained Machine Learning model to an interactive application.
```
Dataset
   ↓
Data Preprocessing
   ↓
Feature Engineering / Transformation
   ↓
Model Training
   ↓
Model Serialization
   ↓
Model Loading
   ↓
Real-Time Inference
   ↓
Interactive Web Application
```
Through this project, the following practical concepts are demonstrated:

- Machine Learning classification
- Feature preprocessing
- Feature scaling
- Model serialization
- Model inference
- Probability prediction
- Streamlit application development
- Basic ML deployment workflow

## ⚠️ Limitations

The current version has several limitations:

- PCA features must be entered manually.
- The application performs single-transaction prediction.
- There is no persistent transaction database.
- There is no real-time transaction stream.
- There is no model monitoring system.
- There is no automated model retraining.
- There is no explainability module.
- The application is not designed for direct use in real financial systems.

## 📜 Disclaimer

FraudShield AI is an educational Machine Learning project created to demonstrate credit card fraud detection and ML model deployment.

It is not a production-grade financial fraud prevention system and should not be used to make real-world financial decisions without appropriate validation, security controls, regulatory compliance, monitoring, and domain-specific testing.

## 👩‍💻 Author
Kruti Peepre

B.Tech — Computer Science & Engineering (AI/ML)

Interested in:

Machine Learning
Artificial Intelligence
Deep Learning
Research
Intelligent Systems
⭐ Project Highlights
🛡️ Credit Card Fraud Detection
🤖 Machine Learning Classification
📊 PCA-Based Anonymized Features
⚙️ Feature Scaling
🔮 Probability-Based Prediction
🖥️ Interactive Streamlit Interface
📦 Serialized ML Model
🚀 End-to-End ML Inference Pipeline
⭐ Support

If you found this project useful, consider giving the repository a star.

Built with Python • Machine Learning • Streamlit

### License

This project is intended for educational and research purposes.

### Live DEMO:
https://krutipeepre-credit-card-fraud-detector-app-ztjkjk.streamlit.app/
