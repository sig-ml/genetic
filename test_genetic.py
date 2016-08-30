import genetic as ge

def x_raised_to_x(x):
    "Calculation function"
    return x**x

def test_p_map_runs():
    "Test and see if p_map runs faster than normal inbuilt map"

    data = list(range(1000))
    results = ge.p_map(x_raised_to_x, data)

    assert len(results) == 1000
    assert results[:6] == [1, 1, 4, 27, 256, 3125]

def test_make_population():
    "See if a population is made"
    pop = ge.make_population(list, 10)
    assert len(pop) == 10
    assert all(isinstance(i, list) for i in pop)
