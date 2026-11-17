"""Legacy assembly scores each question separately using marginal probabilities."""
from itertools import combinations, product
import math

def independent_coverage(posteriors, testlets, selected, needed):
    question_probabilities = [posteriors[testlets[i]['passage']] for i in selected for _ in range(testlets[i]['questions'])]
    result=0.0
    for topics in product(range(len(needed)), repeat=len(question_probabilities)):
        if all(topics.count(k) >= need for k,need in enumerate(needed)):
            result += math.prod(p[t] for p,t in zip(question_probabilities,topics))
    return result

def assemble(posteriors, testlets, budget, needed):
    feasible=[]
    for n in range(len(testlets)+1):
        for selected in combinations(range(len(testlets)),n):
            if sum(testlets[i]['minutes'] for i in selected)<=budget:
                feasible.append((independent_coverage(posteriors,testlets,selected,needed),selected))
    value=max(v for v,_ in feasible)
    selected=min(s for v,s in feasible if abs(v-value)<=1e-12)
    return {'selected':list(selected),'estimated_coverage':value}
