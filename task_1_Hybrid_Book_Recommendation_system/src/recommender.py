import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


book_data = pd.read_csv("data/raw/Book_data.csv")
ratings_data = pd.read_csv("data/raw/book_rating.csv")

book_data['Name'] = book_data['Name'].fillna('')
book_data['Authors'] = book_data['Authors'].fillna('')
book_data['Description'] = book_data['Description'].fillna('')

ratings_data = ratings_data.drop_duplicates()
ratings_data = ratings_data.dropna()

book_data = book_data.copy()

book_data['content'] = (
    book_data['Name'] + " " +
    book_data['Authors'] + " " +
    book_data['Description']
)

train_data, test_data = train_test_split(
    ratings_data,
    test_size=0.2,
    random_state=42
)

user_item_matrix = train_data.pivot_table(
    index='user_id',
    columns='book_id',
    values='rating'
).fillna(0)

train_matrix_filled = user_item_matrix

svd = TruncatedSVD(n_components=50, random_state=42)
latent_matrix = svd.fit_transform(train_matrix_filled)

user_similarity = cosine_similarity(latent_matrix)


def get_collab_scores(user_id):

    if user_id not in user_item_matrix.index:
        return np.zeros(user_item_matrix.shape[1])
    user_index = user_item_matrix.index.get_loc(user_id)
    sim_scores = user_similarity[user_index]
    preds = np.dot(sim_scores, user_item_matrix.values)

    return preds


tfidf = TfidfVectorizer(stop_words='english', max_features=3000)
tfidf_matrix = tfidf.fit_transform(book_data['content'])


def hybrid_recommend(user_id, book_index=0, top_n=10, alpha=0.6):

   
    content_scores = cosine_similarity(
        tfidf_matrix[book_index],
        tfidf_matrix
    ).flatten()
    collab_scores = get_collab_scores(user_id)
    collab_scores = np.array(collab_scores)

    min_len = min(len(content_scores), len(collab_scores))

    content_scores = content_scores[:min_len]
    collab_scores = collab_scores[:min_len]


    hybrid_scores = (alpha * content_scores) + ((1 - alpha) * collab_scores)

    if book_index < len(hybrid_scores):
        hybrid_scores[book_index] = -1

    top_indices = hybrid_scores.argsort()[-top_n:][::-1]

    return book_data.iloc[top_indices][['Name', 'Authors', 'Rating']]



if __name__ == "__main__":
    print(hybrid_recommend("U0058", 0, 10))