def contarvocales():
    voc=0
    for i in len(cad):
        if caDa[i]=='a' or cada[i]=='e'or cada[i]=='i' or cada[i]=='o' or cada[i]=='u' or cad[i]=='A'or cad[i]=='E' or cad[i]=='I' or cad[i]=='O'or cad[i]=='U':
            voc=voc+1
            return voc


caDa = int(input("digite una palabra "))
print contarvocales(caDa)
