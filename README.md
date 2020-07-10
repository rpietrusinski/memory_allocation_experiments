# Memory allocation experiments
Repo provides a bunch of experiments on the CPython memory allocation characteristics, mainly the way memory is allocated in Pandas DataFrames. 
Experiments were created to answer the following questions:
- when is garbage collector triggered?
- can we control when garbage collection is triggered and what's the effect of the gc library triggered manually (generational cycles)?
- how much memory is freed during a single garbage collector's run
- what's the most efficient way of iteratively creating multiple features inside Pandas DF?

## Output
Experiments generate CSV files with metadata describing the experiment flow under the experiment_output/. On the basis of the CSVs there are summary plots generated under the plots/ directory.



## Run
To run experiments run the following command in the root directory:
```
make
```