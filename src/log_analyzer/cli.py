import argparse
import json
from parse_file import *
from analyzer import *

def main():
    parser = argparse.ArgumentParser(description="Analyze log files")
    parser.add_argument("input", nargs="+", help="Paths to input log files.")
    parser.add_argument("output", help="Path to output JSON file.")
    parser.add_argument("--mfip", action="store_true", help="Get the most frequent IP address.")
    parser.add_argument("--lfip", action="store_true", help="Get the least frequent IP address.")
    parser.add_argument("--eps", action="store_true", help="Calculate events per second.")
    parser.add_argument("--bytes", action="store_true", help="Calculate total bytes exchanged.")

    args = parser.parse_args()

    # Parse logs files
    logs = []
    for file in args.input:
        logs.extend(parse_logs(file))

    # Perform analyses
    results = {}
    if args.mfip:
        results["most_frequent_ip"] = analyze_most_frequent_ip(logs)
    if args.lfip:
        results["least_frequent_ip"] = analyze_least_frequent_ip(logs)
    if args.eps:
        results["events_per_second"] = calculate_events_per_second(logs)
    if args.bytes:
        results["total_bytes"] = calculate_total_bytes(logs)

    # Write output
    with open(args.output, "w") as f:
        json.dump(results, f, indent=4)

if __name__ == "__main__":
    main()

# python .\cli.py '../../access.log/access.log' '../../access.log/res.json' --mfip --lfip --eps --bytes