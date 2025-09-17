import json

def create_json_output(image_path, regions, ocr_results, descriptions, language="en"):
    """
    Creates the JSON output file with the specified schema.
    """
    output = {
        "image_path": image_path,
        "elements": []
    }

    for i, region in enumerate(regions):
        element = {
            "bounding_box": region["box"],
            "region_type": region["label"],
            "language": language,
            "text": ocr_results.get(i, ""),
            "description": descriptions.get(i, "")
        }
        output["elements"].append(element)

    return json.dumps(output, indent=4)
