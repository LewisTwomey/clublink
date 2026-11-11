import pandas as pd, itertools, collections, json, re
t=pd.read_csv('/mnt/user-data/uploads/transfers.csv'); c=pd.read_csv('/mnt/user-data/uploads/clubs.csv'); p=pd.read_csv('/mnt/user-data/uploads/players.csv')
L=['GB1','ES1','IT1','L1','FR1','NL1','PO1']
pool=c[c.domestic_competition_id.isin(L)]
ids=set(pool.club_id)
hist=collections.defaultdict(set)
for col in ['from_club_id','to_club_id']:
    for pid,cid in zip(t.player_id,t[col]):
        if cid in ids: hist[pid].add(cid)
a=pd.read_csv('/mnt/user-data/uploads/appearances__1_.csv',usecols=['player_id','player_club_id'])
a=a[a.player_club_id.isin(ids)].drop_duplicates()
for pid,cid in zip(a.player_id,a.player_club_id): hist[pid].add(cid)
# current club too
for pid,cid in zip(p.player_id,p.current_club_id):
    if cid in ids: hist[pid].add(cid)
print('players with any pool club',len(hist))
cnt=collections.Counter()
for pid,s in hist.items():
    if len(s)>=3:
        for tr in itertools.combinations(sorted(s),3): cnt[tr]+=1
print('valid trios',len(cnt)); print(collections.Counter(min(v,10) for v in cnt.values()))
pickle={'hist':hist,'cnt':cnt}
import pickle as pk; pk.dump(pickle,open('/home/claude/build/h.pkl','wb'))
