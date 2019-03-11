import fileinput

width, height = 2000, 2000 #we now have a 1000 x 1000 range matrix. 
matrix = [['.' for x in range(width)] for y in range(height)]
mult_id_count = 0

def read_cordinates():
    global mult_id_count
    input = list(fileinput.input("input.txt"))
    for line in input:
        id, left_co_ord, top_co_ord, inches_wide, inches_tall = strip_line(line)
        fill_locations(id, left_co_ord, top_co_ord, inches_wide, inches_tall)
    return mult_id_count

        
def fill_locations(id, left_co_ord, top_co_ord, inches_wide, inches_tall):
    """Change the matrix at the specified cordinates."""
    global mult_id_count
    for i in range(inches_tall):
        for j in range(inches_wide):
            if check_matrix_square(left_co_ord+j, top_co_ord+i):
                #It has an id already
                if matrix[left_co_ord+j][top_co_ord+i] is not 'X':
                    matrix[left_co_ord+j][top_co_ord+i] = 'X'
                    mult_id_count += 1
            else:
                matrix[left_co_ord+j][top_co_ord+i] = id[1:]
    

def check_matrix_square(left_co_ord, top_co_ord):
    """Checks if it has already been assigned an ID. Returns True if it has."""
    if matrix[left_co_ord][top_co_ord] is '.':
        return False
    else: 
        return True

def strip_line(line):
    line = line.split(" @ ")
    id = (line[0])
    line[1] = line[1].split(",")
    left_co_ord = int(line[1][0])
    line[1] = line[1][1].split(": ")
    top_co_ord = int(line[1][0]) #This is messy, there's a better way.
    line[1] = line[1][1].split("x")
    inches_wide = int(line[1][0])
    inches_tall = int(line[1][1])
    print("id: %s, left: %s, top: %s, wide: %s, tall: %s" % (id, left_co_ord, top_co_ord, inches_wide, inches_tall))
    return (id, left_co_ord, top_co_ord, inches_wide, inches_tall)


print(read_cordinates())
#117948
