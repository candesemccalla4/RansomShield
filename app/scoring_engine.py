from app.assessment_config import SECURITY_CATEGORIES


def calculate_score(user_selection):

    total_score = 0

    category_scores = {}


    for category, data in SECURITY_CATEGORIES.items():

        category_score = 0

        for control, details in data["controls"].items():

            selected = user_selection.get(control)

            if selected:

                points = details["options"].get(selected, 0)

                category_score += points


        category_scores[category] = category_score

        total_score += category_score


    if total_score >= 90:
        risk = "Excellent Protection"

    elif total_score >= 70:
        risk = "Moderate Protection"

    elif total_score >= 50:
        risk = "High Risk"

    else:
        risk = "Critical Risk"


    return {
        "total_score": total_score,
        "risk": risk,
        "categories": category_scores
    }
