import pandas as pd
from scripts.exp_helpers import make_single_plot

exp = pd.read_csv('experiment_output/exp3.csv')
sub_exp = exp.iloc[0:1000]
# make_plots(sub_exp)
make_single_plot(sub_exp)






