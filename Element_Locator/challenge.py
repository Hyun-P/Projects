
def id_cleaner(id_toclean):
    """

    :param id_toclean: a string data of ID including non-numerical values
    :return: a string data of ID only with numerical values
    """

    # convert the input ID into a list of characters
    id_list = list(id_toclean)

    # Overwrite the list only with numerical values
    id_list = [x for x in id_list if x.isdigit()]

    # convert the list of numerical values back to a string data
    id_cleaned = ''.join(id_list)

    return id_cleaned


def duplicate_remover(ids_toclean):
    """

    :param ids_toclean: a list of IDs in a string format with duplicate elements
    :return: a list of IDs in a string format without duplicate elements
    """

    # convert the list of ids into a set of keys in a dictionary
    ids_dict = dict.fromkeys(ids_toclean)

    # convert the dictionary keys back to a list
    ids_cleaned = list(ids_dict.keys())

    return ids_cleaned


def retriever(list_ids, list_specialties):
    """

    :param list_ids: a list of IDs in a string format
    :param list_specialties: a list of lists with IDs and specialties, where IDs are in an integer format
    :return: a list of specialties selected from the given IDs
    """

    # clean the ID elements in the list of IDs
    ids_cleaned = [int(id_cleaner(x)) for x in list_ids]

    # remove duplicate elements in the list of IDs
    ids_cleaned = duplicate_remover(ids_cleaned)

    # convert the list of specialties into a dictionary
    dict_specialties = {x[0]: x[1] for x in list_specialties}

    # grab the specialties given the ids from the list of cleaned IDs
    list_want = [dict_specialties[x] for x in ids_cleaned]

    return list_want
