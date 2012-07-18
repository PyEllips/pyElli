IPE = $(wildcard *.ipe)
PDF_IPE = $(IPE:.ipe=.pdf)

%.pdf: %.ipe
	ipetoipe -pdf $<

%.pdf: %.dia
	dia -t pdf $<

all: ipe UML-crop.pdf

UML-crop.pdf: UML.pdf
	pdfcrop UML.pdf

ipe: $(PDF_IPE)

clean:
	rm -f *.pdf

