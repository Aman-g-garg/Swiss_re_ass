from collections import Counter

def analyze_most_frequent_ip(logs):
    ips = [log["client_ip"] for log in logs]
    return Counter(ips).most_common(1)[0][0] if ips else None

def analyze_least_frequent_ip(logs):
    ips = [log["client_ip"] for log in logs]
    return Counter(ips).most_common()[-1][0] if ips else None

def calculate_events_per_second(logs):
    timestamps = [log["timestamp"] for log in logs]
    return len(logs) / (max(timestamps) - min(timestamps))

def calculate_total_bytes(logs):
    return sum(len(log["response_size"]) for log in logs)
