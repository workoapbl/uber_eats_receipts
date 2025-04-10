from collections import defaultdict

from_pdfs = {'total': 164.72,
             'Gwyneth': 48.29765929370859,
             'Gabriel': 44.19578663453256,
             'Washieu': 28.47179775280899,
             'Angeline': 21.977621840525067, 
             'Joey': 14.817134478424803, 
             'Kristen': 6.96}

dumplings = {'total': 33.16,
             'Gwyneth': 33.16/5,
             'Jace': 33.16/5,
             'Sam': 33.16/5,
             'Kristen': 33.16/5,
             'Tamara': 33.16/5}

boston_halal = {'total': 21.98,
                'Gwyneth': 21.98/2,
                'Jace': 21.98/2}

auntie_annes = {'total': 41.92,
                'Gwyneth': 41.92/2,
                'Washieu': 41.92/2}

combined = defaultdict(float)

for d in [from_pdfs, dumplings, boston_halal, auntie_annes]:
    for key, value in d.items():
        combined[key] += value

# Print results well formatted
for key, value in combined.items():
    print(f"{key}: {value:.2f}")
