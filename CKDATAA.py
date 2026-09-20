import gc,sys
gc.collect()
try:
 import ti_system as ts
 H=True
except:
 H=False
def sv(L,a):
 if not H:return
 try:
  ts.store_list("C3CF",[a])
  ne=[]
  se=[]
  te=[]
  for i in range(len(L)):
   if i>0:
    ne.append(0)
    se.append(-1)
    te.append(-1)
   for c in L[i][0]:ne.append(ord(c))
   for j in range(len(L[i][1])):
    if j>0:te.append(0)
    se.append(L[i][1][j][1])
    for c in L[i][1][j][0]:te.append(ord(c))
  ts.store_list("C3NM",ne)
  ts.store_list("C3LS",se)
  ts.store_list("C3LD",te)
 except:pass
def ld():
 if not H:return None,0
 try:
  try:a=int(ts.recall_list("C3CF")[0])
  except:a=0
  st=ts.recall_list("C3LS");en=ts.recall_list("C3LD")
  if not st and not en:return None,0
  try:
   nm=[];cr=""
   for v in ts.recall_list("C3NM"):
    if v==0:nm.append(cr);cr=""
    else:cr+=chr(int(v))
   if cr:nm.append(cr)
  except:nm=[]
  sc=[];tc=[];cs=[];ct=[]
  for x in(st if st else []):
   if x==-1:sc.append(cs);cs=[]
   else:cs.append(x)
  sc.append(cs)
  for x in(en if en else []):
   if x==-1:tc.append(ct);ct=[]
   else:ct.append(x)
  tc.append(ct)
  n=max(len(nm),len(sc),len(tc))
  if n==0:return None,0
  L=[]
  for i in range(n):
   nn=nm[i] if i<len(nm) and nm[i] else "L"+str(i+1)
   s=sc[i] if i<len(sc) else [];e=tc[i] if i<len(tc) else []
   tn=[];cr=""
   for v in e:
    if v==0:tn.append(cr);cr=""
    else:cr+=chr(int(v))
   if cr:tn.append(cr)
   tk=[]
   for j in range(len(tn)):
    v=int(s[j]) if j<len(s) else 0;tk.append([tn[j],v])
   L.append([nn,tk])
  if not(0<=a<len(L)):a=0
  return L,a
 except:return None,0
