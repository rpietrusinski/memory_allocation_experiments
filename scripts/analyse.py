import os
import re
import pandas as pd
import click
from exp_helpers import make_double_plot, make_single_plot
from matplotlib import pyplot as plt


@click.command()
@click.option('--input_path', type=str, help='Directory with csv files - output from experiments')
@click.option('--plots_path', type=str, help='Where to save plots.')
def main(input_path, plots_path):
    pattern = r"^exp\d{1,2}\.csv"
    csv_files = [x for x in os.listdir(input_path) if re.search(pattern, x)]

    for file in csv_files:
        csv_path = os.path.join(os.getcwd(), input_path, file)
        exp = pd.read_csv(csv_path)
        name = file.split(".")[0]

        double_plot_path = os.path.join(os.getcwd(), plots_path, "double", f"{name}.png")
        make_double_plot(exp)
        plt.savefig(double_plot_path)

        single_plot_path = os.path.join(os.getcwd(), plots_path, "single", f"{name}.png")
        make_single_plot(exp)
        plt.savefig(single_plot_path)


if __name__ == '__main__':
    main()
