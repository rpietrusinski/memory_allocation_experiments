import pandas as pd
import os
import numpy as np
import psutil
import sys
from datetime import datetime


# Append cols to dict object, concatenate to DF once after loop execution.
print("Starting experiment 2")

memory_snapshots = []
process = psutil.Process(os.getpid())

df = pd.DataFrame({
    'x': np.random.randn(100000),
    'y': np.random.randn(100000)
})

cols_to_add = {}
for i in range(4000):
    colname = f'test_{i}'
    cols_to_add[colname] = df['x'] - df['y']

    current_df_mem = sys.getsizeof(df) / 1024 / 1024
    current_mem = process.memory_info().rss / 1024 / 1024
    current_time = datetime.now()
    current_id = id(df)
    output = (current_time, current_id, current_mem, current_df_mem)
    memory_snapshots.append(output)

    if i%10 == 0:
        print(i)
cols_to_add = pd.DataFrame(cols_to_add)
df = pd.concat((df, cols_to_add), sort=False).shape


memory_snapshots_df = pd.DataFrame(
    memory_snapshots,
    columns=['time', 'id', 'memory', 'df_memory']
)
memory_snapshots_df['duration'] = memory_snapshots_df['time'] - memory_snapshots_df['time'].shift(1)
memory_snapshots_df['duration'] = memory_snapshots_df['duration'].apply(lambda x: x.microseconds + x.seconds * 1e6)
memory_snapshots_df.to_csv("experiment_output/exp2.csv", index=False)
print("Done")
