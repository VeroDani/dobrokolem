"""Score a Verifier run against the golden set.
Usage: python evals/score.py evals/runs/<run>-output.csv
expected_status may list accepted alternatives separated by '|'.
Key-fact detection is judged by a human and recorded in the run analysis."""
import csv, sys
gold = {r["id"]: r for r in csv.DictReader(open("evals/verifier-golden-set.csv", encoding="utf-8"))}
out = {r["id"]: r for r in csv.DictReader(open(sys.argv[1], encoding="utf-8"))}
ok = 0
for i, g in gold.items():
    got = out.get(i, {}).get("status", "-")
    hit = got in g["expected_status"].split("|")
    ok += hit
    print(f'{"OK" if hit else "XX"}  {i}  expected={g["expected_status"]:<28} got={got:<17} {g["name"][:40]}')
print(f"\nStatus score: {ok} / {len(gold)}")
