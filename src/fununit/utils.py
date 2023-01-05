def structurally_equal(a, b):
    if a.__class__ != b.__class__:
        return False

    for key, value in a.__dict__.items():
        if isinstance(value, (list, dict, set)):
            if value != b.__dict__[key]:
                return False
        elif isinstance(value, object):
            if not structurally_equal(value, b.__dict__[key]):
                return False
        else:
            if value != b.__dict__[key]:
                return False
    return True
