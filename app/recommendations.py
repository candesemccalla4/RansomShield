"""
RansomShield Recommendation Engine

Provides security improvement suggestions
based on missing ransomware protection controls.
"""


def generate_recommendations(
        antivirus,
        backup,
        mfa,
        monitoring
):

    recommendations = []


    # Check antivirus protection
    if not antivirus:

        recommendations.append(
            "Enable antivirus or endpoint protection "
            "to prevent malicious software execution."
        )


    # Check backup protection
    if not backup:

        recommendations.append(
            "Implement secure backups to improve "
            "ransomware recovery capability."
        )


    # Check MFA protection
    if not mfa:

        recommendations.append(
            "Enable multi-factor authentication "
            "to reduce unauthorized account access."
        )


    # Check monitoring capability
    if not monitoring:

        recommendations.append(
            "Enable file monitoring to detect "
            "suspicious ransomware behavior."
        )


    # If all controls exist
    if len(recommendations) == 0:

        return (
            "Strong ransomware protection configuration.\n"
            "Continue monitoring and maintaining security controls."
        )


    return "\n\n".join(recommendations)
