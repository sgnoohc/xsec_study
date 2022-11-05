#!/bin/env python

import os
import sys

particles = ["w+", "w-", "z", "t", "tx", "h"]

final_states = []
nice_names = []
models = []

def determine_model(fs):
    if "w+" in fs and "w-" in fs:
        return "loop_sm"
    else:
        return "loop_sm-no_b_mass"

nparticles = len(particles)

for np in range(nparticles):
    final_state = particles[np]
    nice_name = particles[np]
    final_states.append(final_state)
    nice_names.append(nice_name)
    models.append(determine_model(final_state))

for np_1 in range(nparticles):
    for np_2 in range(np_1, nparticles):
        final_state = "{} {}".format(particles[np_1], particles[np_2])
        nice_name = particles[np_1] + particles[np_2]
        final_states.append(final_state)
        nice_names.append(nice_name)
        models.append(determine_model(final_state))

for np_1 in range(nparticles):
    for np_2 in range(np_1, nparticles):
        for np_3 in range(np_2, nparticles):
            final_state = "{} {} {}".format(particles[np_1], particles[np_2], particles[np_3])
            nice_name = particles[np_1] + particles[np_2] + particles[np_3]
            final_states.append(final_state)
            nice_names.append(nice_name)
            models.append(determine_model(final_state))

for np_1 in range(nparticles):
    for np_2 in range(np_1, nparticles):
        for np_3 in range(np_2, nparticles):
            for np_4 in range(np_3, nparticles):
                final_state = "{} {} {} {}".format(particles[np_1], particles[np_2], particles[np_3], particles[np_4])
                nice_name = particles[np_1] + particles[np_2] + particles[np_3] + particles[np_4]
                final_states.append(final_state)
                nice_names.append(nice_name)
                models.append(determine_model(final_state))

# print(nice_names)
# print(final_states)
# print(models)

for n, f, m in zip(nice_names, final_states, models):
    command = "sed 's/NAME/{}/;s/MODEL/{}/;s/PROC/{}/' template.dat > cards/pp_{}.dat".format(n, m, f, n)
    print(command)
