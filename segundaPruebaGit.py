import sys


filename = "./pilar.txt"
num_to_text = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty', 25: 'twenty five', 26: 'twenty six',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }


try:
    f = open(filename, "w")
    print("File " + filename + " opened successfully")
    f.write("holaaaa\n")
except Exception as e:
    print(e)
    sys.exit()

for elem in num_to_text:
    f.write(f'{elem}:{num_to_text[elem]}\n')

f.close()
