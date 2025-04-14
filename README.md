# 📊 NLP Project – Automated Customer Reviews Analyzer

This project aims to build an end-to-end NLP solution that automates the process of understanding and summarizing customer reviews from Amazon products using classification, clustering, and generative models.

---

## 🔍 Project Overview

**Goal:**  
To automate the analysis of customer reviews to extract insights, classify sentiments, group products, and generate recommendation-style summaries.

---

## 📁 Dataset

- Source: [Kaggle - Datafiniti Amazon Product Reviews](https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products/data)
- Two datasets were used:
  - May19 Dataset: ~28,000 reviews  
  - 2018 Dataset: ~5,000 reviews
- Each review includes: `reviews.text`, `reviews.rating`, `categories`, `imageURLs`, etc.

---

## 🧠 Tasks & Models

### 1. Sentiment Classification
- **Goal:** Classify reviews into Positive, Neutral, or Negative.
- **Model Used:** Fine-tuned `DistilBERT` with weighted loss to address class imbalance.
- **Evaluation Metrics:**
  - Accuracy: 97%
  - Macro F1 Score: 88%
  - Per-class precision and recall reported
- **Used in the deployed app to predict review sentiment.**

---

### 2. Product Category Clustering
- **Goal:** Group similar products into broader categories.
- **Method:**
  - Used Sentence Embeddings (`all-mpnet-base-v2`)
  - Applied `KMeans` with evaluation via Silhouette Score
- **Final Clusters:**
  - E-Readers
  - Office & Laptop Accessories
  - Smart Home & Audio Devices
  - Home & Pet Supplies
  - Tablets & Kids Tech

---

### 3. Review Summarization (Recommendation Articles)
- **Goal:** Generate blog-style summaries per product category.
- **Model Used:** `GPT-3.5` via OpenAI API
- **Output:** Markdown-formatted articles highlighting:
  - Top 3 recommended products
  - Key differences
  - Worst product to avoid
  - Conclusion for buyers
- Articles are converted to styled HTML and shown in the web app.

---

## 🌐 Deployment

- **Framework:** `Streamlit`
- **App Features:**
  - User inputs a review
  - Selects product category
  - Model predicts sentiment
  - Corresponding summary article is shown
- **Hosted App:** [🔗 Click here to try the app](https://project3-nlp-92a9mns33smfqsthvaszd2.streamlit.app/)
- **QR Code also provided in presentation for easy access**

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Project3-NLP.git
cd Project3-NLP
```

### 2. Create a Virtual Environment & Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App

```bash
streamlit run app.py
```

---

## 📦 Project Structure

```
Project3-NLP/
│
├── html_articles/                 # Contains generated HTML summaries  
├── Final_best_model_distilbert/  # Fine-tuned classification model  
├── notebooks/                     # All model development notebooks  
│   ├── Project3_Task_0_1_Classification_.ipynb  
│   └── Project3_Task_2_3_Clustering_Summarization.ipynb  
├── presentation/                  # Final presentation slides and demo video  
│   ├── final_presentation.pdf  
│   └── demo_video.mp4  
├── app.py                         # Streamlit app script  
├── requirements.txt               # List of required packages  
└── README.md                      # Project documentation  
```

---

## 🖥️ Presentation

A short 15-minute presentation summarizing:

- The problem and solution
- Models used
- Final deployed demo

🔗 Includes a QR code to the app and visuals to showcase the system.

---

## 🙌 Acknowledgments

- Dataset provided by Datafiniti on Kaggle.
- Pretrained models from HuggingFace Transformers.
- Summarization powered by OpenAI GPT-3.5 API.


