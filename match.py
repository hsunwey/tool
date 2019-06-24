import sys
# filename = sys.argv[1]
filename = 'copy.html'
new_file_path = 'class.txt'
mylist = []

f = open(filename, 'r')
for line in f:
    if len(line) > 0:
        if 'class=\"' in line:
            pos = line.find('class=\"')+7
            pos2 = line.find('\"', pos+1)
            # print(line[pos:pos2])
            # with open(new_file_path, 'a') as my_file:
            #     my_file.write(line[pos:pos2]+'\n')
            newline = line[pos:pos2].replace(' ', '\n')
            # print(newline)
            mylist.append(newline)
    
f.close()

myset = set(mylist)
print('============')
for items in myset:
    print(items)

# new_file_path = 'class.txt'
# f = open(new_file_path, 'r')
# for line in f:
#     new = line.replace(' ', '\n')
#     print(new)
# f.close


# new_file_path = 'class.txt'
# f = open(new_file_path, 'r')
# for line in f:
#     if len(line) > 0:
#         list.append(line.replace('\n',''))
# f.close
# myset = set(list)
# for values in myset:
#     with open('final.txt', 'a') as my_file:
#         my_file.write(values+'\n')