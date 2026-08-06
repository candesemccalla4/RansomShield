SECURITY_CATEGORIES = {

    "Prevention": {

        "weight": 30,

        "controls": {

            "endpoint_protection": {

                "weight": 10,

                "options": {
                    "CrowdStrike": 10,
                    "SentinelOne": 10,
                    "Microsoft Defender": 7,
                    "Basic Antivirus": 4,
                    "None": 0
                }
            },


            "identity_security": {

                "weight": 10,

                "options": {
                    "MFA + PAM": 10,
                    "MFA": 7,
                    "Password Policy": 4,
                    "None": 0
                }
            },


            "patch_management": {

                "weight": 10,

                "options": {
                    "Automated Patching": 10,
                    "Regular Updates": 7,
                    "Manual Updates": 4,
                    "None": 0
                }
            }

        }
    },


    "Detection": {

        "weight": 25,

        "controls": {

            "file_monitoring": {

                "weight": 10,

                "options": {
                    "Behavior Monitoring": 10,
                    "Watchdog Monitoring": 7,
                    "Basic Logging": 3,
                    "None": 0
                }
            },


            "network_monitoring": {

                "weight": 15,

                "options": {
                    "IDS": 15,
                    "SIEM Monitoring": 10,
                    "Firewall Logs": 5,
                    "None": 0
                }
            }
        }
    },


    "Recovery": {

        "weight": 20,

        "controls": {

            "backup": {

                "weight": 20,

                "options": {
                    "Immutable Backup": 20,
                    "Cloud Backup": 15,
                    "External Backup": 10,
                    "None": 0
                }
            }
        }
    },


    "Response": {

        "weight": 20,

        "controls": {

            "incident_response": {

                "weight": 10,

                "options": {
                    "Complete IR Plan": 10,
                    "Basic IR Procedures": 5,
                    "None": 0
                }
            },


            "containment": {

                "weight": 10,

                "options": {
                    "Automated Isolation": 10,
                    "Manual Isolation": 5,
                    "None": 0
                }
            }
        }
    },


    "Governance": {

        "weight": 5,

        "controls": {

            "security_training": {

                "weight": 5,

                "options": {
                    "Training + Phishing Simulation": 5,
                    "Security Training": 3,
                    "None": 0
                }
            }
        }
    }

}
