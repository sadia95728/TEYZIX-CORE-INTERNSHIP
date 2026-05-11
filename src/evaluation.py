import numpy as np
import pandas as pd

def precision_at_k(recommended_items, relevant_items, k=10):
    recommended_k = recommended_items[:k]
    relevant_set = set(relevant_items)

    if len(recommended_k) == 0:
        return 0
    hits = sum([1 for item in recommended_k if item in relevant_set])

    return hits / k

def recall_at_k(recommended_items, relevant_items, k=10):

    recommended_k = recommended_items[:k]
    relevant_set = set(relevant_items)

    if len(relevant_set) == 0:
        return 0

    hits = sum([1 for item in recommended_k if item in relevant_set])

    return hits / len(relevant_set)

def dcg_at_k(recommended_items, relevant_items, k=10):

    recommended_k = recommended_items[:k]
    relevant_set = set(relevant_items)

    dcg = 0.0

    for i, item in enumerate(recommended_k):
        if item in relevant_set:
            dcg += 1 / np.log2(i + 2)

    return dcg

def ndcg_at_k(recommended_items, relevant_items, k=10):

    dcg = dcg_at_k(recommended_items, relevant_items, k)

    # ideal DCG
    ideal_hits = min(len(relevant_items), k)

    idcg = sum([1 / np.log2(i + 2) for i in range(ideal_hits)])

    if idcg == 0:
        return 0

    return dcg / idcg


def evaluate_user(recommended_items, relevant_items, k=10):

    return {
        "precision@k": precision_at_k(recommended_items, relevant_items, k),
        "recall@k": recall_at_k(recommended_items, relevant_items, k),
        "ndcg@k": ndcg_at_k(recommended_items, relevant_items, k)
    }