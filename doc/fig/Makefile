IPE = $(wildcard *.ipe)
PDF_IPE = $(IPE:.ipe=.pdf)

%.pdf: %.ipe
	ipetoipe -pdf $<

all: $(PDF_IPE)

clean:
	rm -f *.pdf

