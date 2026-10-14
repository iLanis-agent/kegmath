import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)
def round0(x): return jsnum(math.floor(x + 0.5))

OZ_PER_GAL = 128
KEGS_PER_LB = 1.5
MIN_PER_DEG = 0.75

def pour_plan(gal, pourOz):
    if not (gal > 0) or not (pourOz > 0):
        return {"error": "the keg and the pour must be positive"}
    servings = round0(gal * OZ_PER_GAL / pourOz)
    if servings <= 50: verdict = "a small gathering"
    elif servings <= 100: verdict = "a proper party"
    else: verdict = "a serious crowd"
    return {"servings": servings, "verdict": verdict}

def gas_plan(lb):
    if not (lb > 0):
        return {"error": "the tank must be positive"}
    kegs = round1(lb * KEGS_PER_LB)
    if kegs < 3: verdict = "a season of weekends"
    elif kegs <= 8: verdict = "a year of parties"
    else: verdict = "a cellar's worth"
    return {"kegs": kegs, "verdict": verdict}

def chill_plan(startF, targetF):
    if not (targetF < startF):
        return {"error": "the keg is already at or below the target"}
    hours = round1((startF - targetF) * MIN_PER_DEG)
    if hours <= 6: verdict = "chill this morning"
    elif hours <= 24: verdict = "chill the day before"
    else: verdict = "a two-day promise"
    return {"hours": hours, "verdict": verdict}

def render_pour(r, gal, pourOz):
    return "A " + fmt(gal) + " gal keg pours " + fmt(r["servings"]) + " servings at " + fmt(pourOz) + " oz - " + r["verdict"] + "."

def render_gas(r, lb):
    return "A " + fmt(lb) + " lb CO2 tank pushes about " + fmt(r["kegs"]) + " half-barrels - " + r["verdict"] + "."

def render_chill(r, startF, targetF):
    return "Cooling " + fmt(startF) + " F to " + fmt(targetF) + " F needs " + fmt(r["hours"]) + " h in the fridge - " + r["verdict"] + "."

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[15.5,16],[5.16,16],[7.75,16],[15.5,12],[5,16],[2.5,12],[10,16],[20,16],[0,16],[5,0]]:
    add("pourPlan", pour_plan, render_pour, a)
for a in [[5],[2.5],[10],[1],[20],[3],[7],[4],[0],[0.5]]:
    add("gasPlan", gas_plan, render_gas, a)
for a in [[70,38],[60,38],[80,38],[50,38],[45,40],[65,40],[72,38],[55,38],[38,70],[70,70]]:
    add("chillPlan", chill_plan, render_chill, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
