Genetic
=======

A general purpose parallelized Genetic search library.

Usage
-----

- Any object which provides the following methods can be made
  into an individual in a population
    - `crossover(self, individual2, crossover_rate)`
    - `mutate(self, mutate_rate)`
    - `fitness(self)`
    - `__init__(self, identity)`

- Calling the genetic search function performs the search


Resources
---------

- [Wiki](https://en.wikipedia.org/wiki/Genetic_algorithm)

Todo
----

- [x] multiprocessing support
- [ ] ipyparallel support
