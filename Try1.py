##This program is useful for simulating the effects of various factors on population growth.
##It's probably very inaccurate, so please don't be negative.
##Problems: Percentage of two children birthing seems wrong to me. But I can't think of any better way.
##Life expectancy is constant but real life is much more random and follow a distribution

life_expectancy = 70
init_year = 2000
year_span = 10
one_child_distr = [0.1 for i in range(10)]
two_child_distr = [0.1 for i in range(10)]
perct_one_child = 0.7
perct_two_child = 0.3
birthing_age_start = 30

age_bar = [i for i in range(life_expectancy)]
population_bar = [200 for i in range(life_expectancy)]
import copy
from matplotlib import pyplot as plt

for year in range(year_span):
    birthing_couples = population_bar[30]
    print(population_bar)
    print("birthing couples " + str(birthing_couples))
    children_born = 0
    for i in range(10):
        couple_birthing_age = birthing_age_start + i
        couple_birthing = population_bar[couple_birthing_age] / 2
        one_child = one_child_distr[i] * perct_one_child * couple_birthing
        two_child = two_child_distr[i] * perct_two_child * couple_birthing * 2
        children_born = children_born + one_child + two_child
        #print(i)
    print("children born " + str(children_born))
    population_bar = [children_born] + population_bar[:len(population_bar)-1]
    print(population_bar)

    

plt.plot(age_bar, population_bar, color = 'green', marker='o', linestyle='solid')

plt.title("Population by Age")
plt.ylabel("Number of People")
plt.show()

