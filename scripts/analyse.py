import os
import re
import pandas as pd
import click
from exp_helpers import make_double_plot, make_single_plot
from matplotlib import pyplot as plt



@click.command()
@click.option('--input_path', type=str,  help='Directory with csv files - output from experiments')
@click.option('--plots_path', type=str,  help='Where to save plots.')
def main(input_path, plots_path):

    pattern = r"^exp\d{1,2}\.csv"
    csv_files = [x for x in os.listdir(input_path) if re.search(pattern, x)]


    for file in csv_files:
        exp = pd.read_csv(f'{input_path}/{file}')
        name = file.split(".")[0]

        make_double_plot(exp)
        plt.savefig(f"{plots_path}/double/{name}.png")

        make_single_plot(exp)
        plt.savefig(f"{plots_path}/single/{name}.png")


if __name__ == '__main__':
    main()
