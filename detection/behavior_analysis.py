def analyze_behavior(
    modified_files,
    deleted_files,
    renamed_files
):

    risk = 0

    if modified_files > 50:
        risk += 40

    if deleted_files > 10:
        risk += 30

    if renamed_files > 20:
        risk += 30


    if risk >= 70:
        return "HIGH RISK: Possible ransomware activity"

    elif risk >= 40:
        return "MEDIUM RISK: Suspicious activity"

    else:
        return "LOW RISK: Normal activity"
