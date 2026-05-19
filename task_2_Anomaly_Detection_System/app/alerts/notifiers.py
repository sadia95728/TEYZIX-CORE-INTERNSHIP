def send_alert(data):

    if data.get("anomaly"):

        print("\nANOMALY ALERT 🚨")
        print(f"Timestamp: {data['timestamp']}")
        print(f"Value: {data['value']}")
        print(f"Z-score: {data.get('zscore_flag')}")
        print(f"Isolation: {data.get('isolation_flag')}")
        print("-" * 40)