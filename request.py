
#8-9: Function to print out a list.

magician_list = ['benzema', 'junior', 'alaba', 'modric', 'toni']

def show_magicians(magician_list):
    for i in range(0, len(magician_list)):
        print(magician_list[i])

show_magicians(magician_list)

# #8-10: 

def make_great():
    for i in range(0, len(magician_list)):
        j = 0
        temp = magician_list[j]
        magician_list.remove(magician_list[j])
        magician_list.append('the Great ' + temp)
        
make_great()

show_magicians(magician_list)

print(magician_list)

#8-11

magician_list = ['benzema', 'junior', 'alaba', 'modric', 'toni']

great_magician=[]

def make_great():
    for i in range(0, len(magician_list)):
        j = 0
        temp = magician_list[j]
        great_magician.append('the Great ' + temp)

make_great()

show_magicians(great_magician)
show_magicians(magician_list)



