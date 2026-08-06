from app.scoring_engine import calculate_score


assessment = {

    "endpoint_protection": "CrowdStrike",

    "identity_security": "MFA + PAM",

    "patch_management": "Automated Patching",

    "file_monitoring": "Behavior Monitoring",

    "network_monitoring": "IDS",

    "backup": "Immutable Backup"

}


result = calculate_score(assessment)


print("==============================")
print("       RansomShield Test")
print("==============================")


print("\nTotal Score:",
      result["total_score"])


print("Risk Level:",
      result["risk"])


print("\nCategory Scores:")


for category, score in result["categories"].items():

    print(category, ":", score)
