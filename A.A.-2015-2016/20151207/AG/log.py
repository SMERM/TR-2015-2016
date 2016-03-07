import math  
sfdur= 220    # durata totale del pezzo
phi= 0.6180339
ftime= sfdur*phi # durata del processo di accelerando
w0= 2
w1= 0.03
p0= 0.96 # rapporto tra le due funzioni dur e step
p1= 0.01
t0= 0
t1= ftime
aw= (math.exp(w0)-math.exp(w1))/(t0-t1) # coeff ang funzione
bw= math.exp(w0)-(aw*t0) 
ap= (math.exp(p0)-math.exp(p1))/(t0-t1) 
bp= math.exp(p0)-(ap*t0) 
at= t0
while (at < ftime):
	w= (math.log(aw*at+bw)) # prima funzione lineare (larghezza della finestra) 
	p= (math.log(ap*at+bw)) # seconda f sul rapporto tra dur e step (percentuale tra dur e step) 
	step= w*p
	dur= w-step #n.a: ho dovuto modificare le formule della durata e dello step dato che, per una questione di calcoli, avevo uno step<0 e dunque non avevo uno step (non si sentivano nella traccia gli stacchi).
	print "i1 %8.4f %8.4f %8.4f" % (at, dur, at) # %8.4f argomenti che vengono sost nella stringa
	at= at+w
print "i1 %8.4f %8.4f %8.4f" % (at, sfdur-ftime, at) # %8.4f argomenti che vengono sost nella stringa

