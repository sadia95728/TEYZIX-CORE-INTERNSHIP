# 📚 Hybrid Book Recommendation System

## 📌 Project Overview

This project is a Hybrid Recommendation System that recommends books to users using two approaches: Collaborative Filtering (based on user interaction behavior) and Content-Based Filtering (based on book metadata such as title, author, and description). Both methods are combined to form a hybrid model that improves recommendation accuracy and helps solve the cold-start problem for new users.

---

## 🚀 Features

- Collaborative Filtering using Matrix Factorization (SVD)
- Content-Based Filtering using TF-IDF and Cosine Similarity
- Hybrid Recommendation Model using weighted scoring
- Cold-start handling using content-based filtering
- REST API built with FastAPI
- Offline evaluation using standard recommender system metrics

---

## 🧠 Recommendation Approach

The system uses three main components:

1. Collaborative Filtering: Learns hidden patterns from user-book interactions using Singular Value Decomposition (SVD) to predict user preferences.

2. Content-Based Filtering: Uses TF-IDF vectorization on book metadata (title, author, description) and computes cosine similarity to find similar books.

3. Hybrid Model: Combines both approaches using a weighted formula:

   final_score = α * content_score + (1 - α) * collaborative_score

This ensures better accuracy and balanced recommendations.

---

## 📊 Evaluation Metrics

The model is evaluated using:

- Precision@K
- Recall@K
- NDCG@K

These metrics measure recommendation accuracy, coverage of relevant items, and ranking quality of recommendations.

---

## ⚙️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- FastAPI
- Uvicorn

---

## 📁 Project Structure

TEYZIX-CORE-INTERNSHIP/
│
├── api/
│   └── main.py
│
├── src/
│   ├── recommender.py
│   └── evaluation.py
│
├── data/
│   └── raw/
│       ├── Book_data.csv
│       └── book_rating.csv
│
├── notebooks/
│   └── task_1.ipynb
│
└── README.md

---

## 🚀 How to Run the Project

1. Create virtual environment:
   python -m venv .venv

2. Activate environment:
   .venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Run FastAPI server:
   uvicorn api.main:app --reload

5. Open API documentation:
   http://127.0.0.1:8000/docs

---

## 📡 API Endpoint

GET /recommend/{user_id}

Example:
GET /recommend/U0058

Response:
{
  "user_id": "U0058",
  "recommendations": [
    {
      "Name": "Book Title",
      "Authors": "Author Name",
      "Rating": 4.2
    }
  ]
}

---

## ❄️ Cold Start Handling

For new users with no interaction history, the system uses only content-based filtering to generate recommendations based on similarity of book metadata.

---

## 👨‍💻 Author

Internship Project – Recommendation System  
Designed for academic submission and evaluation purposes.

---

## 📌 Note

This project is modul# 📚 Hybrid Book Recommendation System

## 📌 Project Overview

This project is a Hybrid Recommendation System that recommends books to users using two approaches: Collaborative Filtering (based on user interaction behavior) and Content-Based Filtering (based on book metadata such as title, author, and description). Both methods are combined to form a hybrid model that improves recommendation accuracy and helps solve the cold-start problem for new users.

---

## 🚀 Features

- Collaborative Filtering using Matrix Factorization (SVD)
- Content-Based Filtering using TF-IDF and Cosine Similarity
- Hybrid Recommendation Model using weighted scoring
- Cold-start handling using content-based filtering
- REST API built with FastAPI
- Offline evaluation using standard recommender system metrics

---

## 🧠 Recommendation Approach

The system uses three main components:

1. Collaborative Filtering: Learns hidden patterns from user-book interactions using Singular Value Decomposition (SVD) to predict user preferences.

2. Content-Based Filtering: Uses TF-IDF vectorization on book metadata (title, author, description) and computes cosine similarity to find similar books.

3. Hybrid Model: Combines both approaches using a weighted formula:

   final_score = α * content_score + (1 - α) * collaborative_score

This ensures better accuracy and balanced recommendations.

---

## 📊 Evaluation Metrics

The model is evaluated using:

- Precision@K
- Recall@K
- NDCG@K

These metrics measure recommendation accuracy, coverage of relevant items, and ranking quality of recommendations.

---

## ⚙️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- FastAPI
- Uvicorn

---

## 📁 Project Structure

TEYZIX-CORE-INTERNSHIP/
│
├── api/
│   └── main.py
│
├── src/
│   ├── recommender.py
│   └── evaluation.py
│
├── data/
│   └── raw/
│       ├── Book_data.csv
│       └── book_rating.csv
│
├── notebooks/
│   └── task_1.ipynb
│
└── README.md

---

## 🚀 How to Run the Project

1. Create virtual environment:
   python -m venv .venv

2. Activate environment:
   .venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Run FastAPI server:
   uvicorn api.main:app --reload

5. Open API documentation:
   http://127.0.0.1:8000/docs

---

## 📡 API Endpoint

GET /recommend/{user_id}

Example:
GET /recommend/U0058

Response:
{
  "user_id": "U0058",
  "recommendations": [
    {
      "Name": "Book Title",
      "Authors": "Author Name",
      "Rating": 4.2
    }
  ]
}

---

## ❄️ Cold Start Handling

For new users with no interaction history, the system uses only content-based filtering to generate recommendations based on similarity of book metadata.

---

## 👨‍💻 Author

Internship Project – Recommendation System  
Designed for academic submission and evaluation purposes.

---

## 📌 Note

This project is modular, reproducible, and designed for scalability. It can be extended to neural collaborative filtering, real-time recommendation systems, and A/B testing frameworks.ar, reproducible, and designed for scalability. It can be extended to neural collaborative filtering, real-time recommendation systems, and A/B testing frameworks.