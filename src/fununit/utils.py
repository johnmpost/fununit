def _structurally_equal_seq(a, b):
    return len(a) == len(b) and \
        all(structurally_equal(x, y) for x, y in zip(a, b))

def _structurally_equal_dict(a, b):
    return set(a.keys()) == set(b.keys()) and \
        all(structurally_equal(v, b[k]) for k, v in a.items())

def _structurally_equal_class(a, b):
    return structurally_equal(vars(a), vars(b))

def structurally_equal(a, b):
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

# Test simple cases
assert structurally_equal(1, 1)
assert structurally_equal('a', 'a')
assert structurally_equal(True, True)
assert not structurally_equal(1, 2)
assert not structurally_equal('a', 'b')
assert not structurally_equal(True, False)

# Test lists
assert structurally_equal([1, 2, 3], [1, 2, 3])
assert not structurally_equal([1, 2, 3], [3, 2, 1])
assert not structurally_equal([1, 2, 3], [1, 2, 3, 4])
assert structurally_equal([[1, 2], [3, 4]], [[1, 2], [3, 4]])
assert not structurally_equal([[1, 2], [3, 4]], [[1, 2], [4, 3]])
assert not structurally_equal([[1, 2], [3, 4]], [[1, 2], [3, 4, 5]])

# Test tuples
assert structurally_equal((1, 2, 3), (1, 2, 3))
assert not structurally_equal((1, 2, 3), (3, 2, 1))
assert not structurally_equal((1, 2, 3), (1, 2, 3, 4))
assert structurally_equal(((1, 2), (3, 4)), ((1, 2), (3, 4)))
assert not structurally_equal(((1, 2), (3, 4)), ((1, 2), (4, 3)))
assert not structurally_equal(((1, 2), (3, 4)), ((1, 2), (3, 4, 5)))

# Test dictionaries
assert structurally_equal({'a': 1, 'b': 2}, {'a': 1, 'b': 2})
assert structurally_equal({'a': 1, 'b': 2}, {'b': 2, 'a': 1})
assert not structurally_equal({'a': 1, 'b': 2}, {'a': 1, 'b': 2, 'c': 3})
assert structurally_equal({'a': {'x': 1, 'y': 2}, 'b': {'x': 3, 'y': 4}}, {'a': {'x': 1, 'y': 2}, 'b': {'x': 3, 'y': 4}})
assert not structurally_equal({'a': {'x': 1, 'y': 2}, 'b': {'x': 3, 'y': 4}}, {'a': {'x': 1, 'y': 2}, 'b': {'x': 4, 'y': 3}})
assert not structurally_equal({'a': {'x': 1, 'y': 2}, 'b': {'x': 3, 'y': 4}}, {'a': {'x': 1, 'y': 2}, 'b': {'x': 3, 'y': 4, 'z': 5}})

# Test objects
class TestObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

assert structurally_equal(TestObject(1, 2), TestObject(1, 2))
assert not structurally_equal(TestObject(1, 2), TestObject(2, 1))
assert structurally_equal(TestObject(TestObject(1, 2), TestObject(3, 4)), TestObject(TestObject(1, 2), TestObject(3, 4)))
assert not structurally_equal(TestObject(TestObject(1, 2), TestObject(3, 4)), TestObject(TestObject(1, 2), TestObject(4, 3)))
assert not structurally_equal(TestObject(TestObject(1, 2), TestObject(3, 4)), TestObject(TestObject(1, 2), TestObject(4, 5)))

assert structurally_equal(
    {
        'a': [TestObject(1, 2), TestObject(3, 4)],
        'b': TestObject(TestObject(5, 6), TestObject(7, 8)),
    },
    {
        'a': [TestObject(1, 2), TestObject(3, 4)],
        'b': TestObject(TestObject(5, 6), TestObject(7, 8)),
    },
)
assert not structurally_equal(
    {
        'a': [TestObject(1, 2), TestObject(3, 4)],
        'b': TestObject(TestObject(5, 6), TestObject(7, 8)),
    },
    {
        'a': [TestObject(1, 2), TestObject(4, 3)],
        'b': TestObject(TestObject(5, 6), TestObject(7, 8)),
    },
)
assert not structurally_equal(
    {
        'a': [TestObject(1, 2), TestObject(3, 4)],
        'b': TestObject(TestObject(5, 6), TestObject(7, 8)),
    },
    {
        'a': [TestObject(1, 2), TestObject(3, 4)],
        'b': TestObject(TestObject(5, 6), TestObject(8, 7)),
    },
)
assert not structurally_equal(
    {
        'a': [TestObject(1, 2), TestObject(3, 4)],
        'b': TestObject(TestObject(5, 6), TestObject(7, 8)),
    },
    {
        'a': [TestObject(1, 2), TestObject(3, 4)],
        'b': TestObject(TestObject(6, 5), TestObject(7, 8)),
    },
)
assert not structurally_equal(
    {
        'a': [TestObject(1, 2), TestObject(3, 4)],
        'b': TestObject(TestObject(5, 6), TestObject(7, 8)),
    },
    {
        'a': [TestObject(1, 2), TestObject(3, 4)],
        'b': TestObject(TestObject(5, 6), TestObject(8, 7)),
    },
)
assert not structurally_equal(
    {
        'a': [TestObject(1, 2), TestObject(3, 4)],
        'b': TestObject(TestObject(5, 6), TestObject(7, 8)),
    },
    {
        'a': [TestObject(1, 2), TestObject(3, 4)],
        'b': TestObject(TestObject(5, 6), TestObject(7, 8)),
        'c': TestObject(9, 10),
    },
)
