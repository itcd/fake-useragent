import os,json,time,random,pathlib,requests,collections

def load(f):
    with open(f) as p:return json.load(p)

def dump(o,f):
    with open(f,'w') as p:json.dump(o,p,separators=(',',':'))
    return o

def useragents(u='https://www.useragents.me/api',t=999999,l=[]):return l[0] if l else l[bool(l.append((lambda f:dump([i.get('ua') for i in requests.get(u).json().get('data')],f) if not os.path.exists(f) or time.time()-os.path.getmtime(f)>t else load(f))(f'~{pathlib.Path(__file__).stem}.json')))]
def header():return{'Accept':'*/*','Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5','Content-Type':'application/json','User-Agent':random.choice(useragents())}

def UserAgent(b=['chrome','edge','firefox','safari'],r='random',d={}):
    if not d:
        a=useragents()
        d[r]=a
        c=list(map(str.casefold,a))
        for i,v in enumerate(k[:-1] for k in b):d[b[i]]=[a[j] for j,w in enumerate(c) if v in w] or a # Edg for edge
    return collections.namedtuple(pathlib.Path(__file__).stem,d.keys())(*map(random.choice,d.values()))

if __name__=='__main__':
    print(header(),UserAgent(),UserAgent(),sep='\n')
