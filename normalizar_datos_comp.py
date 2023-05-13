def stark_normalize_data(dict_list:list[dict]) -> list[dict]:
    """
    Casts to float or int type any numeric-only string found as value
    for every dictionary in a given dictionaries list.

    Parameters:
        - dict_list: a list of dictionaries

    Returns:
        A new list of dictionaries where the numeric-only string values
        are converted to float/int as appropiate.
    """
    if not dict_list:
        print("Error: empty list.")
        return None
    else:
        normalized = False
        new_dict_list = []
        for dictionary in dict_list:
            for key, value in dictionary.items():
                if isinstance(value, str) and value.isnumeric():
                    dictionary[key] = int(value)
                    normalized = True
                elif isinstance(value, str) and value.replace(".", "").isnumeric():
                    dictionary[key] = float(value)
                    normalized = True
            new_dict_list.append(dictionary)

        if normalized:
            print("\nData normalized.\n")
        return new_dict_list