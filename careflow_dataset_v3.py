"""CareFlow V3: reproducible synthetic patient event log.

Run: python careflow_dataset_v3.py
Requires: Python 3.9+ (standard library only).
Reads the V2 CSV for patient IDs; keeps the original five-column schema.
All journeys are simulated, not real patient records.
"""
import csv
import random
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path

SEED = 20261022
RNG = random.Random(SEED)
INPUT = Path(__file__).with_name('careflow_100_patients_final.csv')
OUTPUT = Path(__file__).with_name('careflow_100_patients_v3.csv')
START = datetime(2026, 10, 1)

DEPT = {
    'Registration':'Reception', 'Vitals':'Nursing', 'Triage':'Emergency',
    'Doctor':'Consultation', 'Billing Counter':'Billing', 'Pathology':'Laboratory',
    'Pathology report':'Laboratory', 'X-Ray':'Radiology',
    'X-Ray report':'Radiology', 'Pharmacy':'Pharmacy',
    'Discharge':'Discharge', 'Left Early':'Exit'
}
R='Registration'; V='Vitals'; T='Triage'; D='Doctor'; B='Billing Counter'
P='Pathology'; PR='Pathology report'; X='X-Ray'; XR='X-Ray report'
F='Pharmacy'; Z='Discharge'; L='Left Early'

# Exactly 18 clinically plausible variants. Diagnostic reports follow their tests.
# Templates 14 and 15 are expedited emergency flows; 16 and 17 end early.
PATHS = [
 [R,V,T,D,F,Z],
 [R,V,T,D,B,F,Z],
 [R,V,T,D,B,P,PR,D,F,Z],
 [R,V,T,D,B,X,XR,D,F,Z],
 [R,V,T,D,B,P,PR,D,Z],
 [R,V,T,D,B,X,XR,D,Z],
 [R,V,T,D,B,P,PR,X,XR,D,F,Z],
 [R,V,T,D,B,X,XR,P,PR,D,F,Z],
 [R,V,T,D,B,P,PR,D,X,XR,D,F,Z],
 [R,V,T,D,B,X,XR,D,P,PR,D,F,Z],
 [R,V,T,D,B,P,PR,T,D,F,Z],
 [R,V,T,D,B,X,XR,T,D,F,Z],
 [R,V,T,D,B,P,PR,D,T,D,F,Z],
 [R,V,T,D,B,X,XR,P,PR,T,D,F,Z],
 [R,D,V,T,P,PR,D,F,Z],
 [R,D,V,X,XR,D,Z],
 [R,V,T,L],
 [R,V,T,D,L],
]
# Balanced path allocation: 100 cases; no single pathway dominates.
PATH_COUNTS = [10,9,8,8,7,7,7,6,6,5,5,5,4,4,3,3,2,1]
assert len(PATHS)==18 and sum(PATH_COUNTS)==100


def choose_daily_loads():
    """100 arrivals across 30 days, with quiet (1-2) and busy (5-7) days."""
    while True:
        loads = [RNG.randint(1, 7) for _ in range(30)]
        if sum(loads) != 100:
            # Adjust one patient at a time, preserving 1..7.
            while sum(loads) != 100:
                direction = 1 if sum(loads)<100 else -1
                candidates=[i for i,x in enumerate(loads) if 1<=x+direction<=7]
                loads[RNG.choice(candidates)] += direction
        if min(loads)<=2 and max(loads)>=6 and len(set(loads))>=5:
            return loads


def minute_gap(activity, next_activity, long_wait=False, emergency=False):
    if next_activity in (PR,XR):
        return RNG.randint(60,120) if long_wait else RNG.randint(25,65)
    if next_activity == D and activity in (T,PR,XR):
        return RNG.randint(5,16) if emergency else RNG.randint(8,38)
    if next_activity in (L,Z): return RNG.randint(4,15)
    if next_activity in (P,X): return RNG.randint(8,25)
    return RNG.randint(4,19)


def main():
    with INPUT.open(newline='', encoding='utf-8-sig') as fh:
        source = list(csv.DictReader(fh))
    ids = sorted({row['Case_ID'] for row in source})
    if len(ids)!=100:
        raise ValueError(f'Expected 100 unique patients in {INPUT.name}; found {len(ids)}')
    allocations=[index for index,count in enumerate(PATH_COUNTS) for _ in range(count)]
    RNG.shuffle(allocations)
    loads=choose_daily_loads()
    day_numbers=[day for day,count in enumerate(loads) for _ in range(count)]
    RNG.shuffle(day_numbers)
    # Guarantee long report waits in a subset of patients with diagnostics.
    eligible=[i for i,p in enumerate(allocations) if PR in PATHS[p] or XR in PATHS[p]]
    long_wait_patients=set(RNG.sample(eligible, min(35,len(eligible))))
    output=[]
    for i, patient_id in enumerate(ids):
        path=PATHS[allocations[i]]
        date=START+timedelta(days=day_numbers[i])
        start_minutes=RNG.randint(8*60,11*60+30)
        moment=date+timedelta(minutes=start_minutes)
        report_wait_used=False
        for j,activity in enumerate(path):
            if j:
                prev=path[j-1]
                long_wait=(i in long_wait_patients and activity in (PR,XR) and not report_wait_used)
                moment+=timedelta(minutes=minute_gap(prev,activity,long_wait,allocations[i] in (14,15)))
                if long_wait: report_wait_used=True
            output.append({'Case_ID':patient_id, 'Activity_Name':activity,
                           'Date':moment.strftime('%Y-%m-%d'), 'Time':moment.strftime('%H:%M'),
                           'Department':DEPT[activity]})
        if moment.date()!=date.date():
            raise AssertionError(f'{patient_id} crossed midnight')
    # Validate all five columns, all patients, unique path count, chronological order.
    grouped={pid:[] for pid in ids}
    for row in output: grouped[row['Case_ID']].append(row)
    paths=Counter(tuple(r['Activity_Name'] for r in rows) for rows in grouped.values())
    assert len(paths)==18 and max(paths.values())<=10
    for pid,rows in grouped.items():
        dates={r['Date'] for r in rows}
        times=[datetime.strptime(r['Date']+' '+r['Time'],'%Y-%m-%d %H:%M') for r in rows]
        assert len(dates)==1 and all(a<b for a,b in zip(times,times[1:])),pid
        names=[r['Activity_Name'] for r in rows]
        for test,report in [(P,PR),(X,XR)]:
            if report in names: assert test in names and names.index(test)<names.index(report)
        assert names[-1] in (Z,L)
    with OUTPUT.open('w',newline='',encoding='utf-8') as fh:
        writer=csv.DictWriter(fh,fieldnames=['Case_ID','Activity_Name','Date','Time','Department'])
        writer.writeheader();writer.writerows(output)
    daily=Counter(rows[0]['Date'] for rows in grouped.values())
    emergency=sum(allocations[i] in (14,15) for i in range(100))
    early=sum(allocations[i] in (16,17) for i in range(100))
    triage_loop=sum([T in path and path.count(T)>1 for path in (PATHS[a] for a in allocations)])
    doctor_revisits=sum(PATHS[a].count(D)>1 for a in allocations)
    print('Saved:', OUTPUT)
    print('Patients:',len(grouped),'Events:',len(output),'Unique pathways:',len(paths))
    print('Largest pathway:',max(paths.values()),'Emergency:',emergency,'Left early:',early)
    print('Triage loop-back patients:',triage_loop,'Repeat Doctor patients:',doctor_revisits)
    print('Patients with 60-120 min report waits:',len(long_wait_patients))
    print('Days:',len(daily),'Daily patients min/max:',min(daily.values()),max(daily.values()))
    print('Validation: PASS (one date per case; increasing times; tests precede reports)')

if __name__=='__main__': main()


