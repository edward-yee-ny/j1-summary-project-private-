def extractJson(filename):
    """
    Extracts JSON data from a filename.

    Args:
        data (str): The filename.

    Returns:
        dict: The extracted JSON data as a dictionary.
    """
    import json
    
    with open(filename, 'r') as f:
        data = json.load(f)
    
    return data