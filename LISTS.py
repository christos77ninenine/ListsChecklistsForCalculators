import gc,sys
gc.collect()
try:import ti_system as ts
except:pass
KD=["CKLD","C2LD","C3LD","C4LD","C5LD"]
E="="*24
D="-"*24
def sv(L,a):
 s=str(a)
 for l in L:
  s+="\n\n"+l[0]
  for t in l[1]:s+="\n"+t[0]+"\t"+str(t[1])
 e=[ord(c)for c in s]
 try:
  for p in range(5):ts.store_list(KD[p],e[p*999:p*999+999]or[0])
 except:pass
def ld():
 e=[]
 for k in KD:
  try:e+=ts.recall_list(k)
  except:pass
 try:
  p="".join([chr(int(v))for v in e if v]).split("\n\n")
  L=[[b.split("\n")[0],[[r[:-2],int(r[-1:]=="1")]for r in b.split("\n")[1:]]]for b in p[1:]]
  a=int(p[0])
  return L,a if a<len(L) else 0
 except:return[],0
def cl():
 try:ts.disp_clr()
 except:pass
def P(p):
 try:return input(p).strip()
 except:return"q"
def ix(i,n):
 return int(i)-1 if i.isdigit() and 0<int(i)<=n else -1
def sh(L,a):
 t=L[a][1];n=len(t);d=sum([x[1]for x in t]);cl()
 print(E+"\n "+L[a][0])
 f=int(16*d/n)if n else 0
 print(" "+str(d)+"/"+str(n)+(" ["+"#"*f+"-"*(16-f)+"]"if n else""))
 print(D)
 if not t:print("  (empty)")
 for i in range(n):print(str(i+1)+". ["+("X"if t[i][1]else" ")+"] "+t[i][0][:16])
 print(D+"\n1-9:chk A:add D:del\nE:edt R:rst C:clr\nL:lst       Q:quit")
def sl(L,a):
 cl();print(E+"\n     SELECT LIST\n"+D)
 for i in range(len(L)):
  k=L[i][1]
  print(str(i+1)+"."+("*"if i==a else" ")+L[i][0][:10]+" ("+str(sum([x[1]for x in k]))+"/"+str(len(k))+")")
 print(D+"\n1-"+str(len(L))+":sel +:new R:ren\nD:del B:back")
def kl(L,a,c):
 n=len(L);i=ix(c,n)
 if c=="b":return a,0
 if c=="+":
  w=P("Name:")
  if w:L.append([w[:16],[]]);sv(L,n);return n,0
 elif c in"re":
  i=ix(P("#:"),n)
  w=i>=0 and P("New:")
  if w:L[i][0]=w[:16];sv(L,a)
 elif c=="d":
  i=ix(P("#:"),n)
  if n>1 and i>=0:L.pop(i);a=min(a,n-2);sv(L,a)
 elif i>=0:sv(L,i);return i,0
 return a,1
def kt(L,a,c):
 t=L[a][1];n=len(t);i=ix(c,n)
 if c=="l":return 1
 if c=="a":
  w=P("New:")
  if not w:return 0
  t.append([w,0])
 elif c=="c":L[a][1]=[x for x in t if not x[1]]
 elif c=="r":
  for x in t:x[1]=0
 elif c in"de":
  i=ix(P("#:"),n)
  if i<0:return 0
  if c=="d":t.pop(i)
  else:
   w=P("New:")
   if w:t[i][0]=w
 elif i>=0:t[i][1]^=1
 else:return 0
 sv(L,a)
 return 0
def mn():
 gc.collect()
 L,a=ld()
 if not L:L=[["School",[["Math",0],["Physics",0]]],["Personal",[["Gym",0]]]];a=0
 md=1
 while 1:
  if md:sl(L,a)
  else:sh(L,a)
  c=P("> ").lower()
  if not c:md=0;continue
  if c in("q","quit","exit"):sv(L,a);sys.exit()
  if md:a,md=kl(L,a,c)
  else:md=kt(L,a,c)
  gc.collect()
try:mn()
except SystemExit:pass
