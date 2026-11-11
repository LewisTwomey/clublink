import pandas as pd, pickle, collections, itertools, json, re
d=pickle.load(open('h.pkl','rb')); hist=d['hist']
w=pd.read_csv('wikidata-players.csv',dtype=str).fillna('')
wname={}
for q,n,tp,tc in w.itertuples(index=False):
    if not n or n==q: continue
    key=int(tp) if tp.isdigit() else 'wd:'+q
    hist.setdefault(key,set()).add(int(tc)); wname[key]=n
import collections as _c
hist=_c.defaultdict(set,{k:v for k,v in hist.items() if v})
p=pd.read_csv('/mnt/user-data/uploads/players.csv'); mv=dict(zip(p.player_id,p.highest_market_value_in_eur.fillna(0))); pname=dict(zip(p.player_id,p.name))
t=pd.read_csv('/mnt/user-data/uploads/transfers.csv'); tname=dict(zip(t.player_id,t.player_name))
c=pd.read_csv('/mnt/user-data/uploads/clubs.csv'); L=['GB1','ES1','IT1','L1','FR1','NL1','PO1']
pool=c[c.domestic_competition_id.isin(L)].copy()
OV={'Paris FC':'Paris FC','Tottenham Hotspur':'Tottenham','1. Fußballclub Heidenheim 1846':'Heidenheim','1.FC Köln':'FC Köln','1.FC Nuremberg':'Nuremberg','1.FC Union Berlin':'Union Berlin','1.FSV Mainz 05':'Mainz','Associazione Sportiva Roma':'Roma','Società Sportiva Lazio S.p.A.':'Lazio','Bologna Football Club 1909':'Bologna','Parma Calcio 1913':'Parma','Como 1907':'Como','Atlético de Madrid':'Atlético Madrid','Real Betis Balompié':'Real Betis','RCD Espanyol Barcelona':'Espanyol','CF União Madeira (-2021)':'União Madeira','Desportivo Aves (- 2020)':'Desportivo Aves','Bayer 04 Leverkusen':'Bayer Leverkusen','TSG 1899 Hoffenheim':'Hoffenheim','SV Werder Bremen':'Werder Bremen','FC Schalke 04':'Schalke 04','FC Ingolstadt 04':'Ingolstadt','SC Paderborn 07':'Paderborn','SV Darmstadt 98':'Darmstadt','Hannover 96':'Hannover 96','Fortuna Sittardia Combinatie':'Fortuna Sittard','De Graafschap Doetinchem':'De Graafschap','Delfino Pescara 1936':'Pescara','US Livorno 1915':'Livorno','US Salernitana 1919':'Salernitana','Thonon Évian Grand Genève FC':'Évian','Clermont Foot 63':'Clermont','Stade Brestois 29':'Brest','RC Strasbourg Alsace':'Strasbourg','Dijon FCO':'Dijon','ESTAC Troyes':'Troyes','EA Guingamp':'Guingamp','FC Sochaux-Montbéliard':'Sochaux','FC Girondins Bordeaux':'Bordeaux','AS Nancy-Lorraine':'Nancy','Pisa Sporting Club':'Pisa','Ajax Amsterdam':'Ajax','Feyenoord Rotterdam':'Feyenoord','FC Twente Enschede':'FC Twente','Vitesse Arnhem':'Vitesse','Willem II Tilburg':'Willem II','Roda JC Kerkrade':'Roda JC','SC Cambuur Leeuwarden':'Cambuur','Vitória Guimarães SC':'Vitória Guimarães','Vitória Setúbal FC':'Vitória Setúbal','B SAD':'Belenenses SAD','Avs Futebol':'AVS','Real Valladolid CF':'Real Valladolid','Paris Saint-Germain':'PSG','Olympique Lyon':'Lyon','Olympique Marseille':'Marseille','LOSC Lille':'Lille','Stade Rennais FC':'Rennes','OGC Nice':'Nice','Montpellier HSC':'Montpellier','AS Saint-Étienne':'Saint-Étienne','Nîmes Olympique':'Nîmes','Le Havre AC':'Le Havre','SM Caen':'Caen','SC Bastia':'Bastia','Excelsior Rotterdam':'Excelsior','Sparta Rotterdam':'Sparta Rotterdam','Inter Milan':'Inter Milan','AC Milan':'AC Milan','SSC Napoli':'Napoli','ACF Fiorentina':'Fiorentina','Atalanta BC':'Atalanta','Juventus FC':'Juventus','Brighton & Hove Albion':'Brighton','Wolverhampton Wanderers':'Wolves','AFC Bournemouth':'Bournemouth','SL Benfica':'Benfica','SC Braga':'Braga','FC Porto':'Porto','Sporting CP':'Sporting CP','SC Farense':'Farense','SC Olhanense':'Olhanense','SC Beira-Mar':'Beira-Mar','CF Os Belenenses':'Belenenses','CD Santa Clara':'Santa Clara','CD Nacional':'Nacional','CS Marítimo':'Marítimo','Académica Coimbra':'Académica','PSV Eindhoven':'PSV Eindhoven','AZ Alkmaar':'AZ Alkmaar','AS Monaco':'Monaco','AC Ajaccio':'AC Ajaccio','GFC Ajaccio':'GFC Ajaccio','Celta de Vigo':'Celta Vigo','Deportivo de La Coruña':'Deportivo La Coruña','UD Las Palmas':'Las Palmas','UD Almería':'Almería','SD Huesca':'Huesca','SD Eibar':'Eibar','CD Leganés':'Leganés','CA Osasuna':'Osasuna','RCD Mallorca':'Mallorca','Málaga CF':'Málaga','Cádiz CF':'Cádiz','Córdoba CF':'Córdoba','Granada CF':'Granada','Levante UD':'Levante','Sevilla FC':'Sevilla','Valencia CF':'Valencia','Villarreal CF':'Villarreal','Getafe CF':'Getafe','Girona FC':'Girona','Elche CF':'Elche','GD Estoril Praia':'Estoril','GD Chaves':'Chaves','CF Estrela Amadora':'Estrela Amadora','FC Paços de Ferreira':'Paços de Ferreira','Casa Pia AC':'Casa Pia','Rio Ave FC':'Rio Ave','Gil Vicente FC':'Gil Vicente','Moreirense FC':'Moreirense','Boavista FC':'Boavista','Portimonense SC':'Portimonense','US Sassuolo':'Sassuolo','US Lecce':'Lecce','US Cremonese':'Cremonese','Udinese Calcio':'Udinese','Torino FC':'Torino','Genoa CFC':'Genoa','UC Sampdoria':'Sampdoria','Hellas Verona':'Hellas Verona','Chievo Verona':'Chievo','SPAL':'SPAL','Venezia FC':'Venezia','Spezia Calcio':'Spezia','Cagliari Calcio':'Cagliari','Brescia Calcio':'Brescia','Benevento Calcio':'Benevento','Frosinone Calcio':'Frosinone','FC Empoli':'Empoli','FC Crotone':'Crotone','AC Monza':'Monza','AC Carpi':'Carpi','Palermo FC':'Palermo','Catania FC':'Catania','Siena FC':'Siena','Cesena FC':'Cesena'}
def clean(n):
    if n in OV: return OV[n]
    n=re.sub(r'\b(FC|AFC|CF|SC|AC|BC|CFC)\b','',n).strip()
    return re.sub(r'\s+',' ',n)
pool['disp']=pool.name.map(clean)
assert pool.disp.is_unique, pool[pool.disp.duplicated(keep=False)][['name','disp']]
pool=pool.sort_values('disp'); cid2i={cid:i for i,cid in enumerate(pool.club_id)}
clubs=[[r.disp,r.domestic_competition_id] for r in pool.itertuples()]
# players sorted by fame desc
realmv=dict(mv)
for k,v in hist.items():
    if not mv.get(k): mv[k]=min(2e6*len(v),8e6)
pids=sorted(hist,key=lambda x:-mv.get(x,0))
pi={pid:i for i,pid in enumerate(pids)}
players=[[pname.get(pid) if isinstance(pname.get(pid),str) else tname.get(pid) if isinstance(tname.get(pid),str) else wname.get(pid,'?'), sorted(cid2i[c] for c in hist[pid])] for pid in pids]
links=collections.defaultdict(list)
for pid in pids:
    s=sorted(cid2i[c] for c in hist[pid])
    if len(s)>=3:
        for tr in itertools.combinations(s,3): links[tr].append(pi[pid])
cf=collections.Counter()
for pid,s in hist.items():
    for c in s: cf[cid2i[c]]+=realmv.get(pid,0)
top=set(c for c,_ in cf.most_common(45))
trios=[]
for tr,ls in links.items():
    b=mv.get(pids[ls[0]],0)
    n=len(ls)
    tier=0 if (set(tr)<=top and (b>=2e7 or n>=5)) else 1 if (b>=1e7 or n>=3) else 2
    trios.append([*tr,tier,ls[:5],len(ls)])
print(len(clubs),len(players),len(trios),collections.Counter(x[3] for x in trios))
json.dump({'clubs':clubs,'players':players,'trios':trios},open('site/data.json','w'),ensure_ascii=False,separators=(',',':'))
