def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k.

    recommended: list of recommended items
    relevant: set or list of ground-truth relevant items
    k: cutoff
    """
    
    top_k = recommended[:k]

    hits = len(set(top_k) & set(relevant))

    precision = hits / k if k > 0 else 0
    recall = hits / len(relevant) if len(relevant) > 0 else 0

    return [precision, recall]