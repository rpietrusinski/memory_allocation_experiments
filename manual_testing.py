import os
import pandas as pd
from exp_helpers import make_double_plot, make_single_plot
from matplotlib import pyplot as plt


exp = pd.read_csv('experiment_output/exp1.csv')
sub_exp = exp
# make_plots(sub_exp)
make_single_plot(sub_exp)






