def risk_level(prob):
    if prob >= 0.7:
        return "HIGH"
    elif prob >= 0.4:
        return "MEDIUM"
    else:
        return "LOW"