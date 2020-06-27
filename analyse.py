import pandas as pd
from exp_helpers import make_double_plot, make_single_plot
from matplotlib import pyplot as plt


for i in [1, 2, 3]:
    exp = pd.read_csv(f'experiment_output/exp{i}.csv')

    make_double_plot(exp)
    plt.savefig(f"plots/double/exp{i}.png")

    make_single_plot(exp)
    plt.savefig(f"plots/single/exp{i}.png")

