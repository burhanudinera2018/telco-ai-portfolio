# Telco Customer Churn Prediction - AI/ML Portfolio

## 📌 Project Overview

End-to-end machine learning solution untuk prediksi customer churn di industri telekomunikasi, dengan integrasi **Network KQI (Key Quality Indicators)**. Project ini dirancang untuk memenuhi standar **Senior Data Science/AI/ML** di Indosat.

**Durasi Pengerjaan:** 2 Hari  
**Platform:** Google Cloud Platform (GCP)  
**Model:** XGBoost  
**Best AUC:** 87.65%

---

## 🎯 Business Problem

Mempertahankan pelanggan (customer retention) adalah tantangan utama di industri telekomunikasi. Project ini bertujuan untuk:

1. Memprediksi pelanggan yang berisiko churn
2. Mengidentifikasi faktor-faktor utama penyebab churn
3. Memberikan rekomendasi bisnis yang actionable
4. Mengintegrasikan metrik kualitas jaringan (Network KQI) sebagai fitur prediktif

---

## 🏗️ Architecture & Tech Stack

```
┌─────────────────────────────────────────────────────────────────┐
│ GCP Stack                                                       │
├─────────────────────────────────────────────────────────────────┤
│ Data Layer                                                      │
│ ├── BigQuery (Data Warehouse)                                   │
│ └── Cloud Storage (Model Artifact Storage)                      │
├─────────────────────────────────────────────────────────────────┤
│ ML Layer                                                        │
│ ├── Vertex AI Model Registry                                    │
│ ├── Vertex AI Endpoint (deployment attempt)                     │
│ └── XGBoost (Model Training)                                    │
├─────────────────────────────────────────────────────────────────┤
│ Visualization                                                   │
│ └── Looker Studio Dashboard                                     │
└─────────────────────────────────────────────────────────────────┘

```


**Tools & Libraries:**
- Python 3.11
- Pandas, NumPy, Scikit-learn
- XGBoost
- Google Cloud SDK (BigQuery, Storage, Vertex AI)
- Matplotlib, Seaborn, Plotly
- Looker Studio

---

## 📁 Project Structure
```
telco-ai-portfolio/
├── notebooks/
│ ├── 01_setup_and_data_loading.ipynb
│ ├── 02_feature_engineering_network_kqi.ipynb
│ ├── 03_eda_visualization.ipynb
│ ├── 04_model_training_xgboost.ipynb
│ ├── 05_deploy_vertex_endpoint.ipynb
│ └── 06_looker_studio_dashboard.ipynb
├── models/
│ └── model.pkl
├── data/
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

**Source:** IBM Telco Customer Churn dataset (7,043 records, 21 features)

**Feature Engineering yang dilakukan:**
- Encoding categorical variables
- Handling missing values
- **Network KQI Simulation:**
  - `avg_throughput_mbps` - Rata-rata throughput jaringan
  - `latency_ms` - Latency jaringan
  - `drop_call_rate` - Tingkat drop call
  - `network_quality_score` - Skor kualitas jaringan komposit

---

## 📈 Model Performance

| **Metric** | **Score** |
|------------|-----------|
| **AUC** | **87.65%** |
| Precision | 57.58% |
| Recall | 77.14% |
| F1-Score | 65.94% |

### Feature Importance Top 5

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | Contract | 35.80% |
| 2 | OnlineSecurity | 14.61% |
| 3 | TechSupport | 6.87% |
| 4 | InternetService | 6.40% |
| 5 | tenure | 3.12% |

---

## 💡 Business Insights

### Key Findings

1. **Kontrak Month-to-month memiliki churn rate 9x lebih tinggi** dibandingkan kontrak 2 tahun
2. **Pelanggan tanpa layanan keamanan online** berisiko churn lebih tinggi
3. **Network quality score** adalah prediktor churn yang signifikan
4. **12 bulan pertama** adalah periode kritis untuk retensi pelanggan

### Recommendations

| **Rekomendasi** | **Implementasi** |
|----------------|------------------|
| **Retention Program** | Berikan insentif khusus untuk pelanggan kontrak month-to-month dengan kualitas jaringan rendah |
| **Network Investment** | Prioritaskan peningkatan kualitas jaringan di area dengan skor < 40 |
| **Customer Success** | Fokuskan upaya retensi pada 12 bulan pertama tenure |
| **Early Warning System** | Gunakan network quality score sebagai indikator peringatan dini churn |

---

## 🎯 Model Deployment Status

| **Komponen** | **Status** | **Link/ID** |
|--------------|------------|-------------|
| BigQuery Dataset | ✅ Loaded | `telco_dataset.features_network_kqi` |
| Cloud Storage Artifact | ✅ Stored | `gs://telco-portfolio-bucket-20260602/models/model.pkl` |
| Vertex AI Model Registry | ✅ Registered | Model ID: `3867959310969470976` |
| Vertex AI Endpoint | ✅ Created | Endpoint ID: `525347205507186688` |
| Looker Studio Dashboard | ✅ Published | [Link Dashboard](https://datastudio.google.com/reporting/02a263d8-71a8-4523-99bf-72670cb088d5) |

**Deployment Note:**  
Endpoint deployment encountered a timeout issue (>20 minutes in `Deploying` state). This is a known GCP issue related to the container startup timeout. The model artifact is fully prepared and can be deployed using standard Vertex AI workflow.

---

## 📊 Looker Studio Dashboard

Dashboard interaktif yang menampilkan:
- **Churn rate by contract type** (Month-to-month: 27%, Two year: 3%)
- **Churn rate by network quality tier**
- **Customer segmentation analysis**

[Link to Dashboard](https://datastudio.google.com/reporting/02a263d8-71a8-4523-99bf-72670cb088d5)

---

## 🚀 How to Run This Project

### Prerequisites

```bash
# Python 3.11+
# GCP Account with billing enabled
# Vertex AI, BigQuery, Cloud Storage APIs enabled

Installation
```bash
# Clone repository
git clone https://github.com/yourusername/telco-ai-portfolio.git
cd telco-ai-portfolio

# Create virtual environment
python3.11 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Authenticate to GCP
gcloud auth application-default login
gcloud config set project telco-portfolio

```

Run Notebooks
Run notebooks in order:

01_setup_and_data_loading.ipynb

02_feature_engineering_network_kqi.ipynb

03_eda_visualization.ipynb

04_model_training_xgboost.ipynb

06_looker_studio_dashboard.ipynb

📸 Screenshots
Model Training Result
https://screenshots/model_performance.png

Looker Studio Dashboard
https://screenshots/dashboard.png

Vertex AI Model Registry
https://screenshots/model_registry.png

🎓 Key Learnings
Data Leakage Prevention - Mengidentifikasi dan menghilangkan fitur yang mengandung informasi target

Telco Domain Expertise - Mengintegrasikan Network KQI sebagai fitur prediktif

GCP MLOps - BigQuery, Cloud Storage, Vertex AI Model Registry

Business Communication - Menyajikan insight yang actionable untuk stakeholder

## 📝 About the Author
Burhanudin Badiuzaman

Target Position: Senior Data Science / AI/ML - Indosat

Expertise: Machine Learning, MLOps, GCP, Telco Analytics

- Email: studyburhanudin@gmail.com

- LinkedIn: [linkedin.com/in/yourprofile](https://www.linkedin.com/in/burhanudin-badiuzaman4a9204161/)

- GitHub: github.com/yourusername

## 📄 License
This project is for portfolio purposes for the Senior Data Science/AI/ML position at Indosat.

