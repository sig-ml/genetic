import random
from collections import deque
import multiprocessing as mp

# --------------
def p_starmap(fn, data, n_jobs=None):
    "Parallel starmap function"
    if n_jobs is None:
        n_jobs = mp.cpu_count()
    with mp.Pool(n_jobs) as pool:
        results = pool.starmap(fn, data)
    return results

def p_map(fn, data, n_jobs=None):
    "Parallel map function"
    if n_jobs is None:
        n_jobs = mp.cpu_count()
    with mp.Pool(n_jobs) as pool:
        results = pool.map(fn, data)
    return results

def make_population(individual_class, size):
    "Make a new random population. Individual class __init__ must take no arguments other than self"
    pop = p_map(individual_class.__call__, range(size))
    #pop = [individual_class() for _ in range(size)]
    return pop

def select(population, fitnesses):
    "Given fitness and pop, select individual"
    total = sum(fitnesses)
    mark =  random.random() * total
    count, chosen_one = 0, None
    for member, fitness in zip(population, fitnesses):
        count += fitness
        if count >= mark:
            chosen_one = member
            break
    return chosen_one

def get_two_children(population, fitnesses, mutate_rate, crossover_rate):
    "Get two children from the said population"
    i1, i2 = select(population, fitnesses), select(population, fitnesses)
    n1, n2 = i1.crossover(i2, crossover_rate), i2.crossover(i1, crossover_rate)
    n1.mutate(mutate_rate)
    n2.mutate(mutate_rate)
    return n1, n2
            

def mate_population(population, mutate_rate, crossover_rate, new_size):
    "Mate a population and produce a new one"

    assert len(set(type(i) for i in population)) == 1
    ind_type = type(population[0])
    fitnesses = p_map(ind_type.fitness, population)

    new_pop = p_starmap(get_two_children,
            ((population, fitnesses, mutate_rate, crossover_rate)
                for _ in range(int(new_size / 2))))
    #new_pop = deque()
    #for _ in range(int(new_size / 2)):  # we append 2 children per pass
        #i1, i2 = select(population, fitnesses), select(population, fitnesses)
        #n1, n2 = i1.crossover(i2, crossover_rate), i2.crossover(i1, crossover_rate)
        #n1.mutate(mutate_rate)
        #n2.mutate(mutate_rate)
        #new_pop.append(n1)
        #new_pop.append(n2)
    return list(new_pop)

def get_only_new_pop(population, new_population):
    "Return new population"
    return new_population

def genetic_search(individual_class, mutate_rate, crossover_rate, population_size, get_survivors, epochs):
    """
    Perform genetic search

    individual_class            : class of an individual in the population
    mutate_rate                 : mutation rate
    crossover_rate              : crossover rate
    population_size             : size of the initial population
    get_survivors               : given a population and child population, get a survivor population
    epochs                      : how many cycles of evolution happen
    """
    population = make_population(individual_class, population_size)
    for epoch in range(epochs):
        new_population = mate_population(population, mutate_rate, crossover_rate, population_size)
        population = get_survivors(population, new_population)
    return population
