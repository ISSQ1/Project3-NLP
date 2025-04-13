import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import os

# ==== Load your fine-tuned model ====
model_path = "./Final_best_model_distilbert"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

# Create pipeline
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

# ==== Load summaries (HTML articles) ====
summary_folder = "html_articles"
category_summaries = {}

for file in os.listdir(summary_folder):
    if file.endswith(".html"):
        category_name = file.replace(".html", "").replace("_", " ")
        with open(os.path.join(summary_folder, file), "r", encoding="utf-8") as f:
            category_summaries[category_name] = f.read()

# ==== Streamlit App UI ====
st.set_page_config(page_title="Product Review Analyzer", layout="wide")
st.title("🛍️ Product Review Analyzer")

# User inputs
review_text = st.text_area("✍️ Write your product review here:")
selected_category = st.selectbox("📦 Select product category:", list(category_summaries.keys()))

if st.button("🔍 Analyze"):
    if not review_text.strip():
        st.warning("Please enter a review before analyzing.")
    else:
        prediction = classifier(review_text)[0]
        sentiment = prediction["label"]

        # Output sentiment
        st.subheader("📊 Sentiment Prediction:")
        st.success(f"**{sentiment}**")

        # Show summary article
        st.subheader("📖 Recommended Article:")
        st.components.v1.html(category_summaries[selected_category], height=600, scrolling=True)
