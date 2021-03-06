import pandas as pd
import os
import numpy as np
import psutil
import sys
from datetime import datetime
import click

# Append generators to dict object, evaluate & concatenate to DF once after loop execution.
print("Starting experiment 4")


@click.command()
@click.option('--n_iter', type=int, help='Number of iterations')
@click.option('--n_rows', type=int, help='Number of rows in a DF')
@click.option('--results_dir', type=str, help='Output dir')
@click.option('--exp_name', type=str, default="exp4", help='Experiment name')
def main(n_iter,
         n_rows,
         results_dir,
         exp_name):
    memory_snapshots = []
    process = psutil.Process(os.getpid())

    df = pd.DataFrame({
        'x': np.random.randn(n_rows),
        'y': np.random.randn(n_rows)
    })

    cols_to_add = {}
    for i in range(n_iter):
        colname = f'test_{i}'
        cols_to_add[colname] = (x[0] - x[1] for x in zip(df['x'], df['y']))

        current_df_mem = sys.getsizeof(df) / 2 ** 20
        current_mem = process.memory_info().rss / 2 ** 20
        current_time = datetime.now()
        current_id = id(df)
        output = (current_time, current_id, current_mem, current_df_mem)
        memory_snapshots.append(output)

        if i % 10 == 0:
            print(i)
    cols_to_add = pd.DataFrame(cols_to_add)
    df = pd.concat((df, cols_to_add), sort=False)

    memory_snapshots_df = pd.DataFrame(
        memory_snapshots,
        columns=['time', 'id', 'memory', 'df_memory']
    )
    memory_snapshots_df['duration'] = memory_snapshots_df['time'] - memory_snapshots_df['time'].shift(1)
    memory_snapshots_df['duration'] = memory_snapshots_df['duration'].apply(lambda x: x.microseconds + x.seconds * 1e6)
    results_path = os.path.join(os.getcwd(), results_dir, f"{exp_name}.csv")
    memory_snapshots_df.to_csv(results_path, index=False)
    print("Done")


if __name__ == '__main__':
    main()
