def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code here
    if len(recommendations) == 0:
        return [0.0]

    hits = 0

    for recs, truth in zip(recommendations, ground_truth):
        top_k = recs[:k]

        if len(set(top_k) & set(truth)) > 0:
            hits += 1

    return hits / len(recommendations)