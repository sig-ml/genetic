import genetic as ge

def x_raised_to_x(x):
    "Calculation function"
    return x**x

def x_raised_to_y(x, y):
    return x ** y

def test_p_map_runs():
    "Test and see if p_map runs faster than normal inbuilt map"

    data = list(range(1000))
    results = ge.p_map(x_raised_to_x, data)

    assert len(results) == 1000
    assert results[:6] == [1, 1, 4, 27, 256, 3125]

def test_make_population():
    "See if a population is made"
    pop = ge.make_population(str, 10)
    assert len(pop) == 10
    assert all(isinstance(i, str) for i in pop)

def test_p_starmap():
    data = [ (i, i*2) for i in range(1000)]
    results = ge.p_starmap(x_raised_to_y, data)

    assert len(results) == 1000

def test_select():
    elements = [1, 6]
    fitness = [3, 1]
    selections = [ge.select(elements, fitness) for _ in range(1000)]

    assert selections.count(1) >= selections.count(6)
    assert ((selections.count(1) / selections.count(6))
            - 3.) < 0.1
