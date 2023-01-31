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

def _show_class(to_show):
    properties = [f"{attr} = {value!r}" for attr, value in vars(to_show).items()]
    joined_properties = ", ".join(properties)
    return "{to_show.__class__.__name__}({joined_properties})"

def _show(to_show):
    is_class = hasattr(to_show, "__dict__")
    return _show_class(to_show) if is_class else repr(to_show)

def _show_list(strings):
    return "\n".join(strings)

def _insert_before_lines(to_insert, text):
    return "\n".join("{}{}".format(to_insert, line) for line in text.split("\n"))

def _indent_lines(num_spaces, text):
    spaces = " " * num_spaces
    return _insert_before_lines(spaces, text)
