# Exception handling

try:
    f = open('simple.txt', 'w')
    f.write("Test write to simple file")
except IOError:
    print("ERROR: could not file file or write to file")
finally:
    print("I always work!")
    f.close()