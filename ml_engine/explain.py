def generate_explanation(score):
    if score > 0.7:
        return "High probability of spam due to suspicious patterns."
    elif score > 0.3:
        return "Moderate spam risk detected."
    else:
        return "Likely a normal number."