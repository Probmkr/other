PROGNAME := main
LIBDIR := lib
OUTDIR := obj
CC := gcc
LDLIBS := -Wall

main: master.o sub.o
		g++ $(LDLIBS) -o main obj/*.o

master.o: master/master.cpp
		g++ -c master/master.cpp -o obj/master.o

sub.o: sub/sub.cpp
		g++ -c sub/sub.cpp -o obj/sub.o

clean:
	$(RM) main