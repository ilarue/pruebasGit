import sys
import csv
# we can change something in order to view the differences and so
#filename = "./data.txt"
#filename = "C:/Users/pruete/Desktop/ComputerScience/Labs/Python_2/Python\data.txt"
filename = "C:/Users/pruete/Desktop/ComputerScience/Labs/Python_2/Python\data.csv"
num_to_text = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty', 25: 'twenty five', 26: 'twenty six',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }


try:
    f = open(filename, "r")
    print("File " + filename + " opened successfully")
except Exception as e:
    print(e)
    sys.exit()
# Using bach instead of git gui
#No we try with git gui
file_content = csv.reader(f, delimiter=',')
for row in file_content:
    temp = float(row[0])
    #print(temp)
    integer_part = int(temp)
    decimal_part = round(temp%1*10)*1
    print("The temperature is", num_to_text[integer_part], ' dot ', num_to_text[decimal_part], " degrees Celsius")

f.close()
