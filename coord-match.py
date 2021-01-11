def main():
    v = open('newOutput-LACounty.csv','r')
    c = v.read()
    v.close()
    w = open('join_blocks_coordinates.csv','r')
    d = w.read()
    w.close()
    c_list = d.split('\n') # list of coords for census bgs
    #print(c_list[-2])
    mod_list = c.split('\n') #job flow
    #print(mod_list[3])
    retStr =''
    inputx1='0'
    inputy1='0'
    inputx2='0'
    inputy2='0'
    #establish points to look at
    SET_BLOCKS = set()
    for a in c_list[1:-1]:
        ln_lst = a.split(',')
        SET_BLOCKS.add(ln_lst[4].strip('"')[:]) # add census block group
        
    for line in mod_list[1:-1]: #goes through each line in job flow and assigns coordintes
        # print(line)
        line_list = line.strip('\n').split(',')
        #print('t')
        if int(line_list[2]) < 1:
            continue
        elif line_list[0] not in SET_BLOCKS or line_list[1] not in SET_BLOCKS:
            continue
        if int(line_list[2]) > 0:
                #print('test')
            for a in c_list[1:-1]:
                    #print(a)
                ln_lst = a.split(',')
                    #print(ln_lst[4].strip('"')[1:])
                if int(ln_lst[4].strip('"')[:]) == int(line_list[0]):
                    print('match pt 1')
                    inputx1 = ln_lst[0]
                    inputy1 = ln_lst[1]
                elif int(ln_lst[4].strip('"')[:]) == int(line_list[1]):
                    print('match pt 2')
                    inputx2 = ln_lst[0]
                    inputy2 = ln_lst[1]
                #xy coordinate
                #print(line_list)
            lineString = '"LINESTRING('+inputx1+" "+inputy1+", "+inputx2+" "+inputy2+')"'
            line_list.append(lineString)
                #print('p')
            print(','.join(line_list) + '\n')
            retStr += ','.join(line_list) + '\n'
    print(retStr)
    return retStr
    
    
retStr = main()
print('t')
b = open('coord_output.csv','w')
b.write(retStr)
b.close()
