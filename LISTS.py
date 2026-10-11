import gc
try:import ti_system as ts
except:pass
KD=["C"+c+"LD"for c in"K2345"]
E="="*24
D="-"*24
def sv(L,a):
 s=str(a)
 for l in L:
  s+="\n\n"+l[0]
  for t in l[1]:s+="\n%s\t%d"%tuple(t)
 e=[ord(c)for c in s]
 try:
  for k in KD:ts.store_list(k,e[:999]or[0]);e=e[999:]
 except:pass
def ld(f=1):
 s=""
 for k in KD:
  try:e=ts.recall_list(k)
  except:e=[]
  for v in e:
   if v:
    try:s+=chr(int(v)//((31<v<127 or 8<v<11)-v%1==1))
    except:
     if f:return
     s+="?"
 p=s.split("\n\n")
 L=[[b.split("\n")[0],[[r[:-2],+(r[-1:]=="1")]for r in b.split("\n")[1:]]]for b in p[1:]]
 a=ix(p[0],len(L)-1)+1
 if a or p[0]in"0"or f<1:return L,a
def cl():
 try:ts.disp_clr()
 except:pass
def P(p):
 try:return input(p).strip()
 except:return"q"
def ix(i,n):return(int(i)if i.isdigit()and 0<int(i)<=n else 0)-1
def sh(L,a):
 t=L[a][1];n=len(t);d=sum(x[1]for x in t);cl();f=n and 16*d//n
 print(E+"\n "+L[a][0]+"\n %d/%d"%(d,n)+(" ["+"#"*f+"-"*(16-f)+"]"if n else"")+"\n"+D)
 if not t:print("  (empty)")
 for i in range(n):w=t[i][0];print(str(i+1)+". ["+" X"[t[i][1]]+"] "+"\n       ".join(w[j:j+18]for j in range(0,len(w),18)))
 print(D+"\n1-9:chk A:add D:del\nE:edt R:rst C:clr\nL:lst   Q:quit")
def sl(L,a):
 n=len(L);cl();print(E+"\n     SELECT LIST\n"+D)
 for i in range(n):k=L[i][1];print("%d.%s%s (%d/%d)"%(i+1," *"[i==a],L[i][0][:15],sum(x[1]for x in k),len(k)))
 print(D+"\n1-%d:sel +:new R:ren\nD:del B:back"%n)
def kl(L,a,c):
 n=len(L);i=ix(c,n)
 if c=="b":return a,0
 if c=="+":
  w=P("Name:")
  if w:L+=[[w[:15],[]]];sv(L,n);return n,0
 elif c in"red":
  i=ix(P("#:"),n)
  if c>"d"and~i:L[i][0]=P("New:")[:15]or L[i][0];sv(L,a)
  elif i>=0<n-1 and P("Del? y/n:")[:1].lower()=="y":L.pop(i);a=min(a,n-2);sv(L,a)
 elif~i:sv(L,i);return i,0
 return a,1
def kt(L,a,c):
 t=L[a][1];n=len(t);i=ix(c,n)
 if c=="a":
  w=P("New:")
  if w:t+=[[w,0]]
 elif c=="c":t[:]=[x for x in t if not x[1]]
 elif c=="r":
  for x in t:x[1]=0
 elif c in"de":
  i=ix(P("#:"),n)
  if i<0:return
  if c=="d":t.pop(i)
  else:t[i][0]=P("New:")or t[i][0]
 elif~i:t[i][1]^=1
 else:return
 sv(L,a)
def mn():
 gc.collect()
 r=ld()
 if not r:
  cl();print(E+"\n DATA CORRUPTION!\n"+D+"\n y:format lists\n n:fix bad values")
  r=P("y/n:").lower()=="y"and([],0)or ld(0);sv(*r)
 L,a=r
 if not L:L=[["School",[["Math",0],["Physics",0]]],["Personal",[["Gym",0]]]]
 md=1
 while 1:
  [sh,sl][md](L,a)
  c=P("> ").lower()
  if not c:md=0;continue
  if c in("q","quit","exit"):sv(L,a);return
  if md:a,md=kl(L,a,c)
  else:md=c=="l";kt(L,a,c)
  gc.collect()
mn()
