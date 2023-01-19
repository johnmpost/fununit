def _structurally_equal_seq(a, b):
    return len(a) == len(b) and \
        all(_structurally_equal(x, y) for x, y in zip(a, b))

def _structurally_equal_dict(a, b):
    return set(a.keys()) == set(b.keys()) and \
        all(_structurally_equal(v, b[k]) for k, v in a.items())

def _structurally_equal_class(a, b):
    return _structurally_equal(vars(a), vars(b))

def _structurally_equal(a, b):
    if type(a) != type(b):
        return False
    elif isinstance(a, (list, tuple)):
        return _structurally_equal_seq(a, b)
    elif isinstance(a, dict):
        return _structurally_equal_dict(a, b)
    elif hasattr(a, "__dict__"):
        return _structurally_equal_class(a, b)
    else:
        return a == b

def _show_list(strings):
    return "\n".join(strings)

