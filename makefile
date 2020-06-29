n_iter=100
n_rows=100000
csv_dir="experiment_output"
plots_dir="plots"

all: experiments analysis

experiments:
	@echo 'Starting experiments'
	@python exp1.py --n_iter ${n_iter} --n_rows ${n_rows} --results_dir ${csv_dir}
	@python exp2.py --n_iter ${n_iter} --n_rows ${n_rows} --results_dir ${csv_dir}
	@python exp3.py --n_iter ${n_iter} --n_rows ${n_rows} --results_dir ${csv_dir}
	@echo 'Finished experiments'

analysis:
	@echo 'Starting analysis'
	@python analyse.py --input_path ${csv_dir} --plots_path ${plots_dir}
	@echo 'Finished analysis'
