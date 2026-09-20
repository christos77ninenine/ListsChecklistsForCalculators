import gc,sys
gc.collect()
try:
 import ti_system as ts
 H=1
except:H=0;print("No ti_system");sys.exit()
KD=["CKLD","C2LD","C3LD"]
print("CKMIG: Migrate old\ndata to LISTS format")
print("========================")
L=[];a=0
try:
 try:a=int(ts.recall_list("CKCF")[0])
 except:a=0
 st=ts.recall_list("CKLS")
 en=ts.recall_list("CKLD")
 if st and en:
  nm=[];cr=""
  try:
   for v in ts.recall_list("CKNM"):
    if v==0:nm.append(cr);cr=""
    else:cr+=chr(int(v))
   if cr:nm.append(cr)
  except:pass
  sc=[];cs=[]
  for x in st:
   if x==-1:sc.append(cs);cs=[]
   else:cs.append(x)
  sc.append(cs)
  tc=[];ct=[]
  for x in en:
   if x==-1:tc.append(ct);ct=[]
   else:ct.append(x)
  tc.append(ct)
  for i in range(max(len(nm),len(sc),len(tc))):
   nn=nm[i] if i<len(nm) and nm[i] else "L"+str(i+1)
   s0=sc[i] if i<len(sc) else []
   e0=tc[i] if i<len(tc) else []
   tn=[];cr=""
   for v in e0:
    if v==0:tn.append(cr);cr=""
    else:cr+=chr(int(v))
   if cr:tn.append(cr)
   tk=[]
   for j in range(len(tn)):
    v=int(s0[j]) if j<len(s0) else 0
    tk.append([tn[j],v])
   L.append([nn,tk])
except:pass
if not L:
 print("No old data found.")
 sys.exit()
print("Found "+str(len(L))+" lists:")
for i in range(len(L)):
 print(" "+L[i][0][:14]+" ("+str(len(L[i][1]))+")")
gc.collect()
if not(0<=a<len(L)):a=0
s=str(a)
for l in L:
 s+="\n\n"+l[0]
 for t in l[1]:s+="\n"+t[0]+"\t"+str(t[1])
e=[]
for c in s:e.append(ord(c))
for p in range(3):
 c=e[p*999:(p+1)*999]
 try:ts.store_list(KD[p],c if c else[0])
 except:pass
print("========================")
print("Migration complete!\nRun LISTS to verify.")
