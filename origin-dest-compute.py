GROUP_DICT = {} #future census blocks
counter = 0
def test(line):
    global counter
    counter = counter + 1
    if counter%1000000 == 0:
        print(counter, 'lines parsed')
def add_to_main(line):
    global counter
    counter = counter + 1
    if counter%1000000 == 0:
        print(counter, 'lines parsed')
    COUNTY_CODE = '06037' # code for CA
    attrib = line.split(',')
    try:
        CENSUS_BLOCK_G = attrib[0]
        CENSUS_BLOCK_G_H = attrib[1]
        if CENSUS_BLOCK_G[:5] == COUNTY_CODE: # in specified county
            FLOW = int(attrib[3])
            CENSUS_BLOCK_G = CENSUS_BLOCK_G[5:12] # converts blocks to block groups
            CENSUS_BLOCK_G_H = CENSUS_BLOCK_G_H[5:12]
            try:
                GROUP_DICT[CENSUS_BLOCK_G][CENSUS_BLOCK_G_H] += FLOW
            except:
                try:
                    GROUP_DICT[CENSUS_BLOCK_G][CENSUS_BLOCK_G_H] = FLOW
                except:
                    GROUP_DICT[CENSUS_BLOCK_G] = {}
                    GROUP_DICT[CENSUS_BLOCK_G][CENSUS_BLOCK_G_H] = FLOW
    except:
        print(attrib)

with open('ca_od_main_JT00_2017.csv') as infile:
    for line in infile:
        add_to_main(line)

retStr = ''
blockStr = ''
print('done w analysis')
countC = 0
for block_group in GROUP_DICT:
    if counter%10000 == 0:
        print(counter, 'lines written')
    countC = 0
    for val in GROUP_DICT[block_group]: #this gets us all CENSUS_BLOCK_G_H
        retStr += block_group+','+val+','+str(GROUP_DICT[block_group][val])+'\n'
        countC +=GROUP_DICT[block_group][val]
    blockStr += block_group + ','+str(countC)+'\n'
    
v = open('newOutput-LACounty.csv','w')
v.write(retStr)
v.close()
v = open('jobCount-LACounty.csv','w')
v.write(blockStr)
v.close()




