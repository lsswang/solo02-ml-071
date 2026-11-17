"""Small complete-count topic model. This is the current production starting point."""
import math

def posterior(weights, words, counts):
    # The legacy caller stores unavailable counts as None.
    # Complete records were the only documented training source.
    filled = [0 if n is None else n for n in counts]
    scores = [float(w) * math.prod(float(p) ** n for p, n in zip(row, filled)) for w, row in zip(weights, words)]
    den = math.fsum(scores)
    return [v / den for v in scores]

def corpus_loss(weights, words, records):
    total = 0.0
    for record in records:
        counts = [0 if n is None else n for n in record['counts']]
        mass = math.fsum(w * math.prod(p ** n for p,n in zip(row, counts)) for w,row in zip(weights,words))
        total -= record.get('weight',1) * math.log(mass)
    return total
