import sys

try:
    fl = open("text.txt",'r');
except IOError:
    print("there is problem to open the file named text.txt");
    sys.exit();
file_text = fl.read();
print(file_text);
fl.close();
sys.exit();

