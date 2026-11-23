import argparse, csv, json
from collections import defaultdict

def summarize(records):
    groups = defaultdict(lambda: [0, 0.0, set()])
    for row in records:
        key = (row["prompt"], row["label"])
        item = groups[key]
        item[0] += 1
        item[1] += float(row["score"])
        item[2].add(row["image"])
    return [{"prompt": p, "label": l, "detections": v[0],
             "mean_score": round(v[1] / v[0], 4), "images": len(v[2])}
            for (p, l), v in sorted(groups.items())]

def main():
    ap = argparse.ArgumentParser(description="Audit prompt-based detections")
    ap.add_argument("input"); ap.add_argument("output")
    args = ap.parse_args()
    records = json.load(open(args.input, encoding="utf-8"))
    result = summarize(records)
    with open(args.output, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["prompt","label","detections","mean_score","images"])
        writer.writeheader(); writer.writerows(result)
if __name__ == "__main__": main()

