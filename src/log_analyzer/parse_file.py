# from analyzer import *

def parse_logs(file_path):
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(" ", 9)
                if len(parts) < 10:
                    continue
                try:
                    logs.append({
                        "timestamp": float(parts[0]),
                        "response_header_size": parts[1],
                        "client_ip": parts[2],
                        "http_response_code": parts[3],
                        "response_size": parts[4],
                        "http_method": parts[5],
                        "url": parts[6],
                        "username": parts[7],
                        "destination": parts[8],
                        "response_type": parts[9],
                    })
                except ValueError as e:
                    print(f"Skipping line due to error: {e}")
                    continue
                except FileNotFoundError:
                    print(f"File not found: {file_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return logs

# results = {}
# logs = parse_logs(file_path="../../access.log/access.log")
# results["most_frequent_ip"] = analyze_most_frequent_ip(logs)
# results["least_frequent_ip"] = analyze_least_frequent_ip(logs)
# results["events_per_second"] = calculate_events_per_second(logs)
# results["total_bytes"] = calculate_total_bytes(logs)
# print("~~~~~~~~~~~~~~~~~~",results)