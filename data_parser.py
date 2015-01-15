import numpy as np
# import mammo_network #required to create a list and the network should call these functions to get this list



def parse_data(data_file_name):
    inputfile = open(data_file_name)
    output_data = listmammo[ mammo() for i in inputfile]
    i=0
    
    for line in inputfile:
        strings = line.split()
        listmammo[i].BI-RADS=strings[0]
        listmammo[i].age=strings[1]
        listmammo[i].shape=strings[2]
        listmammo[i].margin=strings[3]
        listmammo[i].density=strings[4]
        listmammo[i].severity=strings[5]
        i += 1
        check_missing_arg(listmammo[i])

    return listmammo
    
def check_missing_arg(mammo):
    if(mammo.BI-RADS == "?"):
        mammo.BI-RADS = -1
    else:
        mammo.BI-RADS = int(mammo.BI-RADS)

    if(mammo.age == "?"):
        mammo.age = -1
    else:
        mammo.age = int(mammo.age)

    if(mammo.shape == "?"):
        mammo.shape = -1
    else:
        mammo.shape = int(mammo.shape)

    if(mammo.margin == "?"):
        mammo.margin = -1
    else:
        mammo.margin = int(mammo.margin)

    if(mammo.density == "?"):
        mammo.density = -1
    else:
        mammo.density = int(mammo.density)

    if(mammo.severity == "?"):
        mammo.severity = "NONSENSEGETOUTOFMYLAWN"
    else:
        mammo.severity = int(mammo.severity)



                                                
