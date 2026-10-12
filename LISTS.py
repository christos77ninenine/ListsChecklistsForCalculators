import gc
try:import ti_system as ts;cl=ts.disp_clr
except:cl=int
KD=["C"+c+"LD"for c in"K2345"]
E,D="="*24,"-"*24
def sv(L,a):
 s="%d"%a
 for m,k in L:
  s+="\n\n"+m
  for w,v in k:s+="\n%s\t%d"%(w,v)
 e=list(map(ord,s))
 try:
  for k in KD:ts.store_list(k,e[:999]or[0]);e=e[999:]
 except:0
def ld(f=1):
 s=""
 for k in KD:
  try:
   for v in ts.recall_list(k):
    if v:
     if(31<v<127 or 8<v<11)and v%1==0:s+=chr(int(v))
     elif f:return
     else:s+="?"
  except:0
 p=s.split("\n\n")
 L=[[l[0],[[r[:-2],int(r[-1])]for r in l[1:]]]for l in(b.split("\n")for b in p[1:])]
 a=ix(p[0],len(L)-1)+1
 if a or p[0]in"0"or f<1:return L,a
def P(p):
 try:return input(p).strip()
 except:return"q"
def ix(i,n):return int(i)-1 if i.isdigit()and 0<int(i)<=n else-1
def sh(L,a,p=0):
 t=L[a][1];n=len(t);d=sum(x[1]for x in t);cl();f=n and 16*d//n
 print("%s\n %s\n %d/%d%s\n%s%s"%(E,L[a][0],d,n,n and" ["+"#"*f+"-"*(16-f)+"]"or"",D,"\n  (empty)"*(not t)))
 for i,(w,v)in enumerate(t[p*5:p*5+5],p*5+1):print("%d. [%s] "%(i," X"[v])+"\n       ".join(w[j:j+18]for j in range(0,len(w),18)))
 print(D+"\n#:chk A:add D:del\nE:edt R:rst C:clr\nL:lst +/-:pg Q:quit")
def sl(L,a,*_):
 n=len(L);cl();print(E+"\n     SELECT LIST\n"+D+"\n  (empty)"*(not n))
 for i,(m,k)in enumerate(L):print("%d.%s%s (%d/%d)"%(i+1," *"[i==a],m[:15],sum(x[1]for x in k),len(k)))
 print(D+(n and"\n1-%d:sel +:new R:ren\nD:del B:back"%n or"\n+:new Q:quit"))
def kl(L,a,c):
 n=len(L);i=ix(c,n)
 if c=="b"and n:return a,0
 if c=="+":
  w=P("Name:")
  if w:L+=[[w[:15],[]]];sv(L,n);return n,0
 elif c in"red"and n:
  i=ix(P("#:"),n)
  if~i:
   if c>"d":L[i][0]=P("New:")[:15]or L[i][0]
   elif P("Del? y/n:")in"yY":L.pop(i);a=max(0,min(a,n-2))
   sv(L,a)
 elif~i:sv(L,i);return i,0
 return a,1
def kt(L,a,c,p):
 t=L[a][1];n=len(t);i=ix(c,n)
 if c in"+-":p+=(c=="+")-(c=="-")
 elif c=="a":w=P("New:");t+=[[w,0]]*bool(w);sv(L,a)
 elif c=="c":t[:]=[x for x in t if 0==x[1]];sv(L,a)
 elif c=="r":
  for x in t:x[1]=0
  sv(L,a)
 elif c in"de":
  i=ix(P("#:"),n)
  if~i:
   if c=="d":t.pop(i)
   else:t[i][0]=P("New:")or t[i][0]
   sv(L,a)
 elif~i:t[i][1]^=1;sv(L,a)
 return max(0,min(p,(len(t)-1)//5))
def mn():
 gc.collect()
 r=ld()
 if not r:cl();print(E+"\n CORRUPT DATA\n"+D+"\n y:wipe n:fix");r=P("y/n:")in"yY"and([],0)or ld(0);sv(*r)
 L,a=r;md=1;p=0
 while 1:
  [sh,sl][md or not L](L,a,p)
  c=P("> ").lower()
  if not c:md=not L;continue
  if c in("q","quit","exit"):sv(L,a);return
  if md:a,md=kl(L,a,c);p=0
  else:md=c=="l";p=kt(L,a,c,p)
  gc.collect()
mn()
