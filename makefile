n_iter=4000
n_rows=100000
csv_dir=experiment_output
plots_dir=plots
scripts_path=scripts

all: experiments analysis

experiments:
	@echo 'Starting experiments'
	@python ${scripts_path}/exp1.py --n_iter ${n_iter} --n_rows ${n_rows} --results_dir ${csv_dir}
	@python ${scripts_path}/exp2.py --n_iter ${n_iter} --n_rows ${n_rows} --results_dir ${csv_dir}
	@python ${scripts_path}/exp3.py --n_iter ${n_iter} --n_rows ${n_rows} --results_dir ${csv_dir}
	@python ${scripts_path}/exp4.py --n_iter ${n_iter} --n_rows ${n_rows} --results_dir ${csv_dir}
	@echo 'Finished experiments'

analysis:
	@echo 'Starting analysis'
	@python ${scripts_path}/analyse.py --input_path ${csv_dir} --plots_path ${plots_dir}
	@echo 'Finished analysis'
