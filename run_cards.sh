#!/bin/bash

for proccard in $(ls pp_*.dat); do
    ../bin/mg5_aMC ${proccard}
done
