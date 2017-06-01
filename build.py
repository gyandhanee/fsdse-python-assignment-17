import operator


def solution_asc(dic):
    list_key_value = [ (k,v) for k, v in dic.items() ]
    list_key_value.sort(key=operator.itemgetter(0))
    return list_key_value


def solution_desc(dic):
    list_key_value = [ (k,v) for k, v in dic.items() ]
    list_key_value.sort(key=operator.itemgetter(0), reverse=True)
    return list_key_value
