filename=documentation

pdf:
	pdflatex $(filename)
	bibtex $(filename)
	pdflatex $(filename)
	pdflatex $(filename)
tex:
	pdflatex $(filename)

bib:
	bibtex $(filename)

clean:
	rm -f *.log *.aux *.bbl *.blg *.out


