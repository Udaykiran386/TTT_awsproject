def summarize_scores(scores):
    """Transforms a list of numerical scores into a summary dictionary."""
    if not scores:
        return {
            "count": 0,
            "total": 0,
            "average": 0.0,
            "min": None,
            "max": None,
        }

    total_score = sum(scores)
    count = len(scores)

    return {
        "count": count,
        "total": total_score,
        "average": total_score / count,
        "min": min(scores),
        "max": max(scores),
    }


# Example usage
scores_list = [85, 92, 78, 90, 88, 95, 60]
summary = summarize_scores(scores_list)

print(summary)