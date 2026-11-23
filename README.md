# Prompt Detection Audit

Analyze text-prompt object detection results across images and prompts.

## What this project does

This is an original command-line utility for analyzing or presenting computer vision outputs. It does not include pretrained weights, training code, or copied research implementations.

## Input and output

Input example: `[{"image":"a.jpg","prompt":"person","label":"person","score":0.91}]`

Run: `python main.py predictions.json report.csv`

See `python main.py --help` for positional arguments. Output is written to the requested file, except the neighbor search, which prints ranked results.

## Related tools

Grounding DINO or any detector exporting the documented JSON format. This project is independent of those implementations and consumes their exported results where applicable.

## Requirements

Python 3.10 or newer. No third-party Python packages are required.

## Limitations

Each input record needs image, prompt, label, and score. Model inference is not locally tested. The utility has only been checked for syntax and on small synthetic inputs.


## Why it is useful

A detector can return hundreds of boxes, making it hard to tell which text prompts work consistently. This tool groups detections by prompt and predicted label, counts detections and distinct source images, and reports the arithmetic mean confidence.

## Data contract

Input is a JSON array. Every item contains `image` (string), `prompt` (string), `label` (string), and `score` (number). Extra fields such as bounding boxes are ignored. Output is CSV with one row for each prompt and label pair.

## Reproduce the example

```bash
python main.py examples/predictions.json examples/report.csv
```

The command reads the included sample input. Generated reports in `examples/` can be removed when finished.

## Interpretation

A higher mean score does not establish better detection accuracy. Compare against manually labeled examples before drawing that conclusion.

## License

MIT. See `LICENSE`.

