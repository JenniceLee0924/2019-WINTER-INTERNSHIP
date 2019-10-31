CXX = g++
OBJS = main.o multi.o sum.o
TARGET = main
TEST = test

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) -o $@ $(OBJS) -std=c++11

%.o: %.c
	$(CXX) -c -o $@ $<

%.o: %.cpp
	$(CXX) -c -o $@ $<

test:
	$(CXX) -o $(TEST) test.cpp sum.cc multi.cc -isystem /usr/local/include -L/usr/local/build -pthread -lgtest -std=c++11
	./$(TEST)

clean:
	rm -rf $(OBJS) $(TARGET) $(TEST)