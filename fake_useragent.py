import os,json,random,pathlib,requests,collections
from lxml import html

def load(f):
    with open(f) as p:return json.load(p)

def dump(o,f):
    with open(f,'w') as p:json.dump(o,p,separators=(',',':'))
    return o

def ua2(j,u='https://www.useragents.me',p='/html/body/div[2]/div[2]/div[1]/textarea',l=[]):
    try:return l[0] if l else l[bool(l.append(dump([i['ua'] for i in json.loads(html.fromstring(requests.get(u).content).xpath(p)[0].text)],j) if not os.path.exists(j) else load(j)))]
    except:return l[0] if l else l[bool(l.append(['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0']))]

def header():return{'Accept':'*/*','Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5','Content-Type':'application/json','User-Agent':random.choice(ua2(f'~{pathlib.Path(__file__).stem}.json'))}

def UserAgent(b=('chrome','firefox'),r='random',d={}):
    if not d:
        a=ua2(f'~{pathlib.Path(__file__).stem}.json')
        d[r]=a
        c=list(map(str.casefold,a))
        for i,v in enumerate(b):d[b[i]]=[a[j] for j,w in enumerate(c) if v in w] or a # Edg for edge
    return collections.namedtuple(pathlib.Path(__file__).stem,d.keys())(*map(random.choice,d.values()))

if __name__=='__main__':
    ua=UserAgent()
    print(ua.random,ua.chrome,ua.firefox,sep='\n') # Get a random browser user-agent string or a user-agent string from a specific browser
    print(header()) # Get an HTTP header with a random browser user-agent string
