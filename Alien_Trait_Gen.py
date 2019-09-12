import random as r
fh_ridges= ['None','Klingon','Cardassian','Romulan','Lukari','Firangi','Talaxian']

n_ridges=['None','Bajoran']

ears=['Ocampan','Human','Vulcan','Cardassian','Danoblian','Vorta','Holes','Firangi']

skin_color=['Light Blue','Dark Blue','Light Red','Dark Red','Light Green','Dark Green','Light Purple','Dark Purple','Grey']+['Brown','Black']*9+['Peach']*18

skin_pattern=['Trill','Talaxian','Gradiant','None','Stripes']

nose=['None','Holes','Firangi','Human']

c_shape=['Human','Firangi']

n_ridges=['None','Cardassian','Vadwarr']

hsf=str(r.randrange(1,12))
hsi=str(r.randrange(0,12))
hef=str(r.randrange(1,12))
hei=str(r.randrange(0,12))
while hef<=hsf:
	hef=str(r.randrange(1,12))

print('This was made by one person so if you')
print('have any bugs, or sugs, contact me on either Amino, or email')
print('3068799@gmail.com')
print('yes I Know its wierd')
print('with the subject: alien get sug, or alien gen bug rep')
print('')
print('')
sc_c=r.choice(skin_color)
print('skin color: %s' % (sc_c))
print('min height: %s ft, %s in' % (hsf, hsi))
print('max height: %s ft, %s in' % (hef, hei))
fh_c= r.choice(fh_ridges)
print('forehead ridges: %s' % (fh_c))
nc=r.choice(n_ridges)
print('nose ridges: %s' % (nc))
ec=r.choice(ears)
print('ears: %s' % (ec))
spc=r.choice(skin_pattern)
spcc= r.choice(skin_color)
if spc.lower() == 'none':
	spcc='None'
print('skin pattern: %s , %s' % (spc, spcc))
nsc=r.choice(nose)
print('nose shape: %s' % (nsc))
csc=r.choice(c_shape)
print('cranium shape: %s' % (csc))
