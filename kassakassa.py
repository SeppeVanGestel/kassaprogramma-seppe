import pcinput
pcinput.getInteger

#deel code hieronder wordt vervangen door de import van pcinput
"""
def aantal(vraag):    
    while True:
        try:
            totaal = int(input(vraag))
            break
        except ValueError:
            print("Oops!  That was not a valid number.  Try again..")       
    return totaal

"""

# geef aantal friet in
aantal_friet = pcinput.getInteger("het aantal mosselfriet ")


# geef aantal koniginnenhapjes in
aantal_koniginnenhapjes= pcinput.getInteger("het aantal koniginnenhapjes ")


# geef aantal ijsjes in
aantal_ijs= pcinput.getInteger("het aantal ijsjes ")


# geef aantal drank in
aantal_drank= pcinput.getInteger("het aantal dranken ")


totaal_friet = aantal_friet * 20
totaal_koniginnenhapjes = aantal_koniginnenhapjes * 10
totaal_ijsjes = aantal_ijs * 3
totaal_drank = aantal_drank * 2




rekening = totaal_friet + totaal_koniginnenhapjes + totaal_ijsjes + totaal_drank

if rekening >= 50:
    korting = 5
    nieuw_bedrag = rekening- korting
else:
    pass    

   


 #Totaal te betalen: xx euro
print("_" *72)
print("{:^65}".format("Rekening:"))
print("_" *72)
print("| {:30} | {:8}{:8} | {:10}  {} |".format("Aantal mosselen friet ",aantal_friet,"st.", totaal_friet, "euro."))
print("| {:30} | {:8}{:8} | {:10}  {} |".format("Aantal koniginnenhapjes ",aantal_koniginnenhapjes,"st.", totaal_koniginnenhapjes, "euro."))
print("| {:30} | {:8}{:8} | {:10}  {} |".format("Aantal ijs ",aantal_ijs,"st.", totaal_ijsjes, "euro."))
print("| {:30} | {:8}{:8} | {:10}  {} |".format("Aantal drank ",aantal_drank,"st.", totaal_drank, "euro."))
print("_" *72)


print("| {:30} | {:29}  {} |".format("Totaal:",rekening,"euro."))
print("| {:30} | {:29}  {} |".format("Uw korting:",korting,"euro."))
print("| {:30} | {:29}  {} |".format("Totaal te betalen:",nieuw_bedrag,"euro."))
print("_" *72)


betaling= pcinput.getInteger("Geef het bedrag in: ")
teruggave = betaling - rekening


aantal1 = teruggave//100
rest = teruggave % 100

aantal2 = rest//50
rest = rest % 50

aantal3 = rest//20
rest = rest % 20

aantal4 = rest//10
rest = rest % 10

aantal5 = rest//5
rest = rest % 5

aantal6 = rest//2
rest = rest % 2

aantal7 = rest//1
rest = rest % 1




    
print("_" *30)
print("{:^30}".format("Teruggave:"))
print("_" *30)

if aantal1 > 0:
    print("| {:5} | {:20}|".format(aantal1,"briefjes van 100"))   
else:
    pass 

if aantal2 > 0:
    print("| {:5} | {:20}|".format(aantal2,"briefjes van 50"))   
else:
    pass 

if aantal3 > 0:
    print("| {:5} | {:20}|".format(aantal3,"briefjes van 20"))   
else:
    pass 

if aantal4 > 0:
    print("| {:5} | {:20}|".format(aantal4,"briefjes van 10"))   
else:
    pass 

if aantal5 > 0:
    print("| {:5} | {:20}|".format(aantal5,"briefjes van 5"))   
else:
    pass 

if aantal6 > 0:
    print("| {:5} | {:20}|".format(aantal6,"briefjes van 1"))   
else:
    pass 

print("_" *30)
print("Totaal terug te geven:", teruggave, "euro.")

print("_" *30)




