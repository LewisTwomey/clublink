# ClubLink (Three Clubs)

Pub football game: three clubs come up, name a player who played for all three.
3 points for all three, 2 for two, 1 for one. 30 seconds per guess, no repeats in a round.

- `index.html` – the whole game (static, no build step)
- `data.json` – clubs, player club histories and pre-computed valid trios
- `scripts/` – Python used to build `data.json` from the Transfermarkt Kaggle dataset
  (players, clubs, transfers, appearances) plus a Wikidata export of club memberships

Every generated trio has at least one player who played for all three clubs.
Deploy: import this repo into Vercel as a static site (no settings needed).
