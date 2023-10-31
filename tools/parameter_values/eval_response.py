def Evaluate_Response(response, desired_answer):
    # For simplicity, reward shorter answers that contain desired info
    score = 0
    if desired_answer in response:
        score += 10
    score -= len(response) * 0.1  # Penalize longer responses
    return score
