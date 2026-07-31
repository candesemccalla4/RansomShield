def calculate_score(
    antivirus,
    backup,
    mfa,
    monitoring
):

    score = 0

    if antivirus:
        score += 20

    if backup:
        score += 30

    if mfa:
        score += 20

    if monitoring:
        score += 30

    return score
