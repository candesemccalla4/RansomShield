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
                    "Basic Antivirus": 4
                }
            },

            "identity_security": {
                "weight": 10,
                "options": {
                    "MFA + PAM": 10,
                    "MFA": 7,
                    "Password Policy": 4
                }
            },

            "patch_management": {
                "weight": 10,
                "options": {
                    "Automated Patching": 10,
                    "Regular Updates": 7,
                    "Manual Updates": 4
                }
            }
        }
    },


    "Detection": {

        "weight":25,

        "controls":{

            "file_monitoring":{
                "weight":10,
                "options":{
                    "Behavior Monitoring":10,
                    "Watchdog Monitoring":7,
                    "Basic Logging":3
                }
            },

            "network_monitoring":{
                "weight":10,
                "options":{
                    "IDS":10,
                    "Firewall Monitoring":6,
                    "Basic Logs":3
                }
            }
        }
    },


    "Recovery": {

        "weight":20,

        "controls":{

            "backup":{
                "weight":15,
                "options":{
                    "Immutable Backup":15,
                    "Cloud Backup":10,
                    "Basic Backup":5
                }
            }
        }
    }
}
