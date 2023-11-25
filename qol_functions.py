def getr(dicts, key):
    """recursively seaches for a value corresponding to key
    :param dicts: nested dicts
    :type dicts: param
    :param key: the key with the value you are looking for
    :type key: the key (usually str, but can be other things)
    """
    # base case: key found
    if key in dicts:
        #prints value corresponding to the key in dicts
        print(dicts[key])
    else:
        # iterates over the values of dicts: does so for every value
        for value in dicts.values():
           # if any value is a dict
            if isinstance(value, dict):
                # if the value is a dicts, recursively search it
                getr(value, key)
