import fileinput

lines = list(fileinput.input("input.txt"))

def get_resulting_frequency():
    start = 0
    resulting_freq_list = {start}
    while True:
        for line in lines:
            start += int(line)
            if start in resulting_freq_list:
                return start
            resulting_freq_list.add(start)  

print (get_resulting_frequency())





