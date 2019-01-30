# Concepts: strings, lists, indexing, for loops, functions, testing,
# builtin functions

def most_frequent(s):
    """Return the most frequently occuring word in s."""

    s_list = sorted(s.lower().split())
    counts = []
    for word in s_list:
        counts.append(s_list.count(word))
    pos = counts.index(max(counts))
    return s_list[pos]



def test_run():
    """Test most_frequent() with some inputs."""
    print(most_frequent("cat bat mat")==None)
    print(most_frequent("betty bought a bit of butter but the butter was bitter")=='butter')
    print(most_frequent("This is a marklar that I marklar a marklar amount.")=='marklar')

test_run()
