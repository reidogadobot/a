medida = float(input('Uma distância em metros: '))
mm = medida *1000
cm = medida * 100
dm = medida *10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('A medida de {}m conresponde a: \n {}mm \n {}cm \n {}dm \n {}dam \n {}hm \n {}km'.format(medida, mm, cm, dm, dam, hm, km))