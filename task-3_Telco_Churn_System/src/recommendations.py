def generate_recommendation(features, risk_level):
    """
    Generates action plan based on churn drivers
    """

    recommendations = []
    
    if risk_level == "HIGH":

        if "Contract_Two year" not in features:
            recommendations.append("Offer long-term contract discount")

        if "MonthlyCharges" in features:
            recommendations.append("Provide billing discount or flexible payment plan")

        if "TechSupport_No" in features:
            recommendations.append("Assign priority technical support")

        if "tenure" in features:
            recommendations.append("Early retention call from support team")

    elif risk_level == "MEDIUM":

        if "StreamingTV_No" in features:
            recommendations.append("Offer streaming bundle promotion")

        if "OnlineSecurity_No" in features:
            recommendations.append("Suggest security package upgrade")

        recommendations.append("Send personalized retention email campaign")

    else:
        recommendations.append("No immediate action required")
        recommendations.append("Keep customer engaged via newsletters")

    return recommendations