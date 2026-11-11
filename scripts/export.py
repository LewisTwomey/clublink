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
clubs=[[r.disp,r.domestic_competition_id,int(r.club_id)] for r in pool.itertuples()]
disp_by_id=dict(zip(pool.club_id,pool.disp))
# players sorted by fame desc
realmv=dict(mv)
for k,v in hist.items():
    if not mv.get(k): mv[k]=min(2e6*len(v),8e6)
pids=sorted(hist,key=lambda x:-mv.get(x,0))
pi={pid:i for i,pid in enumerate(pids)}
pr=p.set_index('player_id')
def shortclub(cid,name):
    if cid in disp_by_id: return disp_by_id[cid]
    if not isinstance(name,str): return ''
    n=re.sub(r'^(Club Atlético|Club Atletico|Clube de Regatas do|Club de Regatas|Sport Club|Associação Atlética|Asociación Atlética|Club Sportivo|Club Social y Deportivo|Club Deportivo|Club|Clube)\s+','',name)
    n=re.sub(r'\b(FC|SC|CF|AC|Futebol Clube|Football Club|Fútbol Club|Soccer Club)\b','',n)
    return re.sub(r'\s+',' ',n).strip()
POS={'Attack':'Forward','Midfield':'Midfielder','Defender':'Defender','Goalkeeper':'Goalkeeper'}
def info(pid):
    if pid not in pr.index: return ['','','']
    r=pr.loc[pid]
    club=shortclub(r.current_club_id,r.current_club_name)
    yr=str(r.date_of_birth)[:4] if isinstance(r.date_of_birth,str) else ''
    if r.last_season>=2025 and club: st=club
    elif club: st=f"Last club: {club} ({int(r.last_season)})"
    else: st=''
    if yr: st+=f" · b.{yr}"
    nat=r.country_of_citizenship if isinstance(r.country_of_citizenship,str) else ''
    pos=POS.get(r.position,'') if isinstance(r.position,str) else ''
    return [st,nat,pos]
def nm(pid):
    for d in (pname,tname,wname):
        v=d.get(pid)
        if isinstance(v,str): return v
    return '?'
players=[[nm(pid), sorted(cid2i[c] for c in hist[pid]), *info(pid)] for pid in pids]
links=collections.defaultdict(list)
for pid in pids:
    s=sorted(cid2i[c] for c in hist[pid])
    if len(s)>=3:
        for tr in itertools.combinations(s,3): links[tr].append(pi[pid])
cf=collections.Counter()
for pid,s in hist.items():
    for c in s: cf[cid2i[c]]+=realmv.get(pid,0)
BIG=['Arsenal','Chelsea','Liverpool','Manchester City','Manchester United','Tottenham',
'Real Madrid','Barcelona','Atlético Madrid','Sevilla','Valencia','Villarreal',
'Juventus','Inter Milan','AC Milan','Napoli','Roma','Lazio',
'Bayern Munich','Borussia Dortmund','Bayer Leverkusen','RB Leipzig','Schalke 04','Eintracht Frankfurt',
'PSG','Marseille','Lyon','Monaco','Lille','Rennes',
'Ajax','PSV Eindhoven','Feyenoord','AZ Alkmaar','FC Twente','Utrecht',
'Benfica','Porto','Sporting CP','Braga','Vitória Guimarães','Boavista']
ci={c[0]:i for i,c in enumerate(clubs)}
top=set(ci[n] for n in BIG)
print('top six per league:',sorted(clubs[i][0] for i in top))
trios=[]
for tr,ls in links.items():
    b=mv.get(pids[ls[0]],0)
    n=len(ls)
    big=set(tr)<=top
    tier=(0 if (b>=2e7 or n>=3) else 1) if big else 2
    trios.append([*tr,tier,ls[:5],len(ls)])
print(len(clubs),len(players),len(trios),collections.Counter(x[3] for x in trios))
json.dump({'clubs':clubs,'players':players,'trios':trios},open('site/data.json','w'),ensure_ascii=False,separators=(',',':'))
