import gc,sys
gc.collect()
try:
 import ti_system as ts
 H=1
except:H=0
KD=["CKLD","C2LD","C3LD","C4LD","C5LD"]
def sv(L,a):
 if not H:return
 s=str(a)
 for l in L:
  s+="\n\n"+l[0]
  for t in l[1]:s+="\n"+t[0]+"\t"+str(t[1])
 e=[]
 for c in s:e.append(ord(c))
 for p in range(5):
  c=e[p*999:(p+1)*999]
  try:ts.store_list(KD[p],c if c else[0])
  except:pass
def ld():
 if not H:return[],0
 try:
  e=[]
  for p in range(5):
   try:
    r=ts.recall_list(KD[p])
    if r and(len(r)>1 or int(r[0])!=0):e+=list(r)
   except:pass
  if not e:return[],0
  s="".join([chr(int(v))for v in e])
  p=s.split("\n\n")
  L=[]
  try:a=int(p[0])
  except:a=0
  for i in range(1,len(p)):
   ln=p[i].split("\n");tk=[]
   for j in range(1,len(ln)):
    r=ln[j].split("\t")
    try:tk.append([r[0],int(r[1])])
    except:tk.append([r[0],0])
   L.append([ln[0],tk])
  if a>=len(L):a=0
  return(L,a)if L else([],0)
 except:return[],0
def sh(L,a):
 t=L[a][1]
 print("\n========================\n "+L[a][0][:10]+" ("+str(a+1)+"/"+str(len(L))+")")
 n=len(t);d=sum([x[1] for x in t])
 if n>0:
  f=int(16*d/n)
  print(" "+str(d)+"/"+str(n)+" ["+"#"*f+"-"*(16-f)+"]")
 else:print(" 0/0")
 print("------------------------")
 if not t:print("  (empty)")
 for i in range(n):
  print(str(i+1)+". ["+("X" if t[i][1] else " ")+"] "+t[i][0][:16])
 print("------------------------\n1-9:chk +:add D:del\nE:edt R:rst C:clr\nL:lst       Q:quit")
def P(p):
 try:return input(p).strip()
 except:return"q"
def mn():
 gc.collect()
 L,a=ld()
 if not L:L=[["School",[["Math",0],["Physics",0]]],["Personal",[["Gym",0]]]];a=0
 md=0
 while 1:
  t=L[a][1]
  if md:
   print("\n========================\n     SELECT LIST\n------------------------")
   for i in range(len(L)):
    print(str(i+1)+"."+("*" if i==a else " ")+L[i][0][:10]+" ("+str(sum([x[1] for x in L[i][1]]))+"/"+str(len(L[i][1]))+")")
   print("------------------------\n1-"+str(len(L))+":sel +:new R:ren\nD:del B:back")
  else:sh(L,a)
  c=P("> ").lower()
  if not c:
   if md:md=0
   continue
  if c in("q","quit","exit"):sv(L,a);sys.exit()
  if md:
   if c=="b":md=0
   elif c=="+":
    w=P("Name:")
    if w:L.append([w[:16],[]]);a=len(L)-1;sv(L,a);md=0
   elif c in("r","e"):
    i=P("#:")
    if i.isdigit() and 0<=int(i)-1<len(L):
     w=P("New:")
     if w:L[int(i)-1][0]=w[:16];sv(L,a)
   elif c=="d":
    i=P("#:")
    if len(L)>1 and i.isdigit() and 0<=int(i)-1<len(L):
     L.pop(int(i)-1)
     if a>=len(L):a=len(L)-1
     sv(L,a)
   elif c.isdigit() and 0<=int(c)-1<len(L):a=int(c)-1;sv(L,a);md=0
  else:
   if c=="l":md=1
   elif c=="+":
    w=P("New:")
    if w:t.append([w,0]);sv(L,a)
   elif c=="c":
    L[a][1]=[x for x in t if not x[1]]
    sv(L,a)
   elif c=="r":
    for x in t:x[1]=0
    sv(L,a)
   elif c in("d","e"):
    i=P("#:")
    if i.isdigit() and 0<=int(i)-1<len(t):
     if c=="d":t.pop(int(i)-1)
     else:
      w=P("New:")
      if w:t[int(i)-1][0]=w
     sv(L,a)
   elif c.isdigit() and 0<=int(c)-1<len(t):
    t[int(c)-1][1]=1-t[int(c)-1][1]
    sv(L,a)
try:mn()
except SystemExit:pass
