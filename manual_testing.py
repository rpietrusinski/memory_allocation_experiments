import os
import pandas as pd
from exp_helpers import make_double_plot, make_single_plot
from matplotlib import pyplot as plt


exp = pd.read_csv('experiment_output/exp3.csv')
sub_exp = exp.iloc[0:1000]
# make_plots(sub_exp)
make_single_plot(sub_exp)






