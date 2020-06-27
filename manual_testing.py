import os
import pandas as pd
from mem_allocation_experiments.exp_helpers import make_double_plot, make_single_plot
from matplotlib import pyplot as plt


exp = pd.read_csv('mem_allocation_experiments/experiment_output/exp1.csv')
sub_exp = exp
# make_plots(sub_exp)
make_single_plot(sub_exp)






