import pandas as pd
import os
import numpy as np
import psutil
import sys
from datetime import datetime
import gc
import click

# Iteratively add cols to DF with square brackets notion, Trigger gc after each loop iteration
print("Starting experiment 3")


@click.command()
@click.option('--n_iter', type=int, help='Number of iterations')
@click.option('--n_rows', type=int, help='Number of rows in a DF')
@click.option('--results_dir', type=str, help='Output dir')
@click.option('--exp_name', type=str, default="exp3", help='Experiment name')
def main(n_iter,
         n_rows,
         results_dir,
         exp_name):
    gc.disable()
    memory_snapshots = []
    process = psutil.Process(os.getpid())

    df = pd.DataFrame({
        'x': np.random.randn(n_rows),
        'y': np.random.randn(n_rows)
    })

    for i in range(n_iter):
        colname = f'test_{i}'
        df[colname] = df['x'] - df['y']

        current_df_mem = sys.getsizeof(df) / 2 ** 20
        current_mem = process.memory_info().rss / 2 ** 20
        current_time = datetime.now()
        current_id = id(df)
        output = (current_time, current_id, current_mem, current_df_mem)
        memory_snapshots.append(output)
        gc.collect()

        if i % 10 == 0:
            print(i)

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
