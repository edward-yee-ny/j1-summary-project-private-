def packJson(data):
    """
    Packs a Python dictionary into a JSON string.
    
    Args:
        data (dict): The dictionary to be packed into JSON.
        
    Returns:
        str: A JSON string representation of the input dictionary.
    """
    import json
    return json.dumps(data, ensure_ascii=False)