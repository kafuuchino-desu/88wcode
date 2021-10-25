HELP:
	echo "#######################################################################"
	echo "WARNING: this repo contains mega brain damage"
	echo "available make options are listed below:"
	echo "gensrc: generates the braindamaged megalegendary c code for compiiling"
	echo "build: does the same thing as the option name itself, builds the c code"
	echo "run: the only option u will need"
	echo "clean: wipe my ass for me plz"
	echo "#######################################################################"
gensrc:
	python gen.py
build: gensrc
	gcc -Wall src.c -o braindamage
run: build
	./braindamage
clean:
	rm ./src.c
	rm ./braindamage

ifndef VERBOSE
.SILENT:
endif
