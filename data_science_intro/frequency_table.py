from random import randint

# generate random integers 0-10
integer_min, integers_max, n_integers = 0, 10, 20

random_list = [randint(integer_min, integers_max) \
               for integer in range(n_integers)]

# sort the list
random_list.sort()

# count occurrences
occurrences_list = []
for num in range(integers_max + 1):
  count = random_list.count(num)
  occurrences_list.append(count)

# visualize the distribution
for num, occurrences in enumerate(occurrences_list):
  print(num, "|", "*" * occurrences)
