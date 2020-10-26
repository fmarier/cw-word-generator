FILES = *.py

all:

pyflakes:
	@echo Running pyflakes...
	@pyflakes3 $(FILES)

pydocstyle:
	@echo Running pydocstyle...
	@pydocstyle

pycodestyle:
	@echo Running pycodestyle...
	@pycodestyle $(FILES)

codespell:
	@echo Running codespell...
	@codespell $(FILES)

lint:
	@echo Running pylint...
	@pylint $(FILES)

bandit:
	@echo Running bandit...
	@bandit --quiet -r .

test: pycodestyle pydocstyle pyflakes lint codespell bandit
