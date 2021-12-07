archive_stash_type = open(r'C:\Users\sonvi\Documents\6 - InvManag\Tab\Tab_List.txt')
stash_type = [line.split() for line in archive_stash_type.readlines()]
path = r'C:\Users\sonvi\Documents\6 - InvManag\Tab\{}.txt'
stash_dict = {
}
for i in range(0, len(stash_type)):
    aux = open(path.format(stash_type[i]),'r')
    aux2 = ''
    aux2 = aux2.join(stash_type[i])
    aux3 = ''
    aux3 = aux3.join(aux.readlines())
    stash_dict[aux2] = aux3
    print(aux2, stash_dict[aux2]) 
