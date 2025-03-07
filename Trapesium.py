#input
AB = 37
DC = 24
AD = 16
AE = 5

#Phytagoras
h = AD**2 - AE**2
h = h**(1/2)
print(f"h= {h:.2f}")

#Mencari CB
CB = h**2 + (AB - DC - AE)**2
CB = CB**(1/2)
print(f"CB= {CB:.2f}")

#Mencari Luas
L = ((AB + DC) /2)*h
print(f"L= {L:.2f}")

#Mencari Keliling
K = AB + CB + DC + AD
print(f"K= {K:.2f}")

#Output
print(f"Jadi Luas dan Keliling Trapesium Sembarangan dengan Berturut-turut adalah {L:.2f} dan {K:.2f}")