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

def make_data_type(desired_data_type, data=None, length=None):
    """This is just a qol function to randomly generate me a complex datalist type
    :param desired_data_type: Here is a list of available options [list, set, dict, list_of_tuples, list_of_sets, list_of_dicts, nested_list, nested_dict]
    :type desired_data_type: str
    :param data: The default for data is an int: Here is a list of available options [str, list, set, dict]
    :type data: str
    :param length: how long you want your list, set, dict, or how many tuples in an iterable, or how many nested elements in an iterable
    :type length: int
    """
    from random import randint
    
    if length is None:
        length = 5
    
    if desired_data_type == 'list':
        my_list = []
        for i in range(length):
            if data is None:
                my_list.append(randint(1, 9))
            elif data == 'string':
                my_list.append(str(randint(1, 9)))
            elif data == 'list' or data == 'nested_list':
                for i in range(length): 
                    my_listz = []
                    for i in range(3):
                        my_listz.append(randint(1, 9))
                    my_list.append(my_listz)
                    break
            elif data == 'set':
                return 'Same thing as list'
            elif data == 'dict':
                for i in range(length): 
                    my_dictz = {}
                    my_listt = []
                    for i in range(3):
                        my_listt.append(randint(1,9))
                        for i, num in enumerate(my_listt):
                            my_dictz[str(i)] = num
                    my_list.append(my_dictz)
                    break
            else:
                print(f"{data} is not available")
        return my_list
        
    elif desired_data_type == 'set':
        my_set = set()
        for i in range(length):
            if data is None:
                my_set.add(randint(1, 9))
            elif data == 'string':
                my_set.add(str(randint(1, 9)))
            elif data == 'list':
                for i in range(length):
                    my_listz = []
                    for i in range(3):
                        my_listz.append(randint(1, 9))
                    my_set.add(tuple(my_listz))
                    break
        return my_set
    
    elif desired_data_type == 'dict':
        my_dict = {}
        my_list = []
        my_sets = make_data_type('list', 'set', length)
        my_lists = make_data_type('list','list', length)
        my_dicts = make_data_type('list', 'dict', length)
        for i in range(length):
            my_list.append(randint(1, 9))
            
        if data is None:
            for i, num in enumerate(my_list):
                my_dict[str(i)] = num
        elif data == 'string':
            print('Looks weird, you dont need dictionaries with strings as values')
        elif data == 'list':
            for i, num in enumerate(my_lists):
                my_dict[str(i)] = num
        elif data == 'set':
            for i, num in enumerate(my_sets):
                my_dict[str(i)] = num
        elif data == 'dict':
            for i, num in enumerate(my_dicts):
                my_dict[str(i)] = num
        return my_dict
            

    elif desired_data_type == 'list_of_tuples':
        my_list1 = []
        for i in range(length):
            my_list2 = []
            for i in range(3):
                my_list2.append(randint(1, 9))
            my_list1.append(tuple(my_list2))
        return my_list1
    else:
        print(f"{desired_data_type} not available for generation.")



        
