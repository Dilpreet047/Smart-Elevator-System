
import numpy as np


from scipy.stats import truncnorm


def truncated_normal_val(mean=0, sd=1, low=0, upp=10, type=int):
    return truncnorm((low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)


def truncated_normal_floats(mean=0, sd=1, low=0, upp=10, num=100):
    res = truncated_normal_val(mean=mean, sd=sd, low=low, upp=upp)
    return res.rvs(num)


def truncated_normal_ints(mean=0, sd=1, low=0, upp=10, num=100):
    res = truncated_normal_val(mean=mean, sd=sd, low=low, upp=upp)
    return res.rvs(num).astype(np.uint8)


number_of_items_per_class = [450, 500]
elevators = {}


# Healthy Elevator
number_of_items = number_of_items_per_class[0]
temperature = truncated_normal_floats(
    mean=57.5, sd=10, low=25, upp=80, num=number_of_items)
speed = truncated_normal_ints(mean=1, sd=1, low=0, upp=3, num=number_of_items)
voltage = truncated_normal_ints(
    mean=230, sd=15, low=100, upp=260, num=number_of_items)
# emergency = np.ones(number_of_items)
data = np.column_stack((temperature, speed, voltage))
elevators["Healthy"] = data

# Unhealthy Elevator
number_of_items = number_of_items_per_class[1]
temperature = truncated_normal_floats(
    mean=88, sd=13, low=82, upp=90, num=number_of_items)
speed = truncated_normal_ints(mean=1, sd=1, low=0, upp=3, num=number_of_items)
voltage = truncated_normal_ints(
    mean=130, sd=15, low=100, upp=260, num=number_of_items)
# emergency = np.zeros(number_of_items)
data = np.column_stack((temperature, speed, voltage))
elevators["Unhealthy"] = data
data = np.concatenate((elevators["Healthy"], elevators["Unhealthy"]), axis=0)


# Assign the labels
target = np.zeros(sum(number_of_items_per_class))
previous_end = 0
for i in range(1, 2):
    num = number_of_items_per_class[i - 1]
    beg = previous_end
    target[beg:beg+num] += i
    previous_end = beg+num
conc_data = np.concatenate((data, target.reshape(target.shape[0], 1)), axis=1)
np.savetxt("./elevator_data.txt", conc_data, fmt="%2.2f")



print(list(elevators.keys()))
