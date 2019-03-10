import fileinput


def get_lines():
    with open("input.txt") as lines:
        lines1 = lines.readlines()
        for line in lines1:
            for line2 in lines1:
                total_count = 0
                for key,val in zip(line, line2):
                    print(line,line2)
                    if key != val:
                        total_count += 1
                    if total_count > 1:
                        break
                if total_count is 1:
                    print ("in here")
                    return (line, line2)


def compare_line(line_tuple):
    position_track = 0 
    entry, entry2 = line_tuple
    for ent, ent2 in zip(entry, entry2):
        
        #compare to see if they're the same.
        if ent == ent2:
            position_track +=1
        else:
            print (position_track)
            return (entry[:position_track] + entry[(position_track+1):])


line = get_lines()
print(compare_line(line))

