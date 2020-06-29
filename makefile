all: experiments analysis

experiments:
	@echo 'Starting experiments'
	@python exp1.py
	@python exp2.py
	@python exp3.py
	@echo 'Finished experiments'

analysis:
	@echo 'Starting analysis'
	@python analyse.py
	@echo 'Finished analysis'
