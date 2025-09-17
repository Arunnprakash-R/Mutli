def detect_regions(image_path):
    """
    This is a placeholder function for region detection.
    It returns a hardcoded list of detected regions.
    """
    # In a real implementation, this function would use a trained model
    # to detect regions in the input image.

    # The bounding box is in [x, y, width, height] format.
    dummy_regions = [
        {
            "box": [50, 50, 200, 50],
            "label": "Title"
        },
        {
            "box": [50, 120, 400, 200],
            "label": "Text"
        },
        {
            "box": [50, 350, 300, 150],
            "label": "Table"
        },
        {
            "box": [500, 100, 250, 200],
            "label": "Figure"
        }
    ]

    return dummy_regions
