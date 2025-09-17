import json

def create_json_output(image_path, regions, ocr_results, descriptions):
    """
    Creates the JSON output file with the specified schema.
    """
    output = {
        "image_path": image_path,
        "elements": []
    }

    for i, region in enumerate(regions):
        element = {
            "box_2d": region["box"],
            "class_id": region["label"],
            "language": "en",  # Placeholder
            "text": ocr_results.get(i, ""),  # Placeholder
            "description": descriptions.get(i, "")  # Placeholder
        }
        output["elements"].append(element)

    return json.dumps(output, indent=4)
