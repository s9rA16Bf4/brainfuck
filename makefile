CC := g++
LIB := lib
SRC := src
BIN := bf
RM := rm

compile:
	$(CC) $(SRC)/*.cpp -I$(LIB) -o $(BIN)


clean:
	-$(RM) $(BIN)