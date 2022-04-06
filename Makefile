superclean: clean
	rm -f thermo.pdf

clean:
	rm -f thermo.aux thermo.bbl thermo.bcf thermo.blg thermo.log thermo.run.xml thermo.tex.backup thermo.to thermo.toc missfont.log

compil:
	pdflatex thermo.tex; pdflatex thermo.tex

install:
	cp thermo.pdf /cnrm/phynh/data1/riette/Public/thermo

all: clean compil install clean
