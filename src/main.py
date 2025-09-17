import argparse
import os
from region_detection import detect_regions
from output_schema import create_json_output

def main():
    parser = argparse.ArgumentParser(description="Intelligent Document Understanding Pipeline")
    parser.add_argument("image_path", help="Path to the input document image.")
    args = parser.parse_args()

    if not os.path.exists(args.image_path):
        print(f"Error: Image not found at {args.image_path}")
        return

    # Stage 1: Region Detection
    regions = detect_regions(args.image_path)

    # Placeholders for future stages
    ocr_results = {
        0: "This is a title.",
        1: "This is a paragraph of text.",
    }
    descriptions = {
        2: "This is a summary of the table.",
        3: "This is a description of the figure.",
    }

    # Generate JSON output
    json_output = create_json_output(args.image_path, regions, ocr_results, descriptions)

    # Save the output
    output_filename = os.path.splitext(os.path.basename(args.image_path))[0] + ".json"
    output_path = os.path.join("output", output_filename)

    with open(output_path, "w") as f:
        f.write(json_output)

    print(f"Successfully processed {args.image_path} and saved the output to {output_path}")

if __name__ == "__main__":
    main()
