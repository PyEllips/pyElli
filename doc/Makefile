filename=documentation

all: tex bib
	pdflatex $(filename)
	pdflatex $(filename)
tex:
	cd fig && make
	pdflatex $(filename)
bib:
	bibtex $(filename)

clean:
	rm -f *.log *.aux *.bbl *.blg *.out


