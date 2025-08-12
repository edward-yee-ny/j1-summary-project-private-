def extractJson(data):
    """
    Extracts JSON data from a given string.

    Args:
        data (str): The input string containing JSON data.

    Returns:
        dict: The extracted JSON data as a dictionary.
    """
    import json
    try:
        return json.loads(data)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON data: {e}") from e