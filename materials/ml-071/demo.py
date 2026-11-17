import json
from pathlib import Path
from topic_model import posterior, corpus_loss
from testlet_assembly import assemble
case=json.loads(Path(__file__).with_name('example.json').read_text())
weights,words=case['weights'],case['words']
posteriors={p:posterior(weights,words,case['passages'][v]) for p,v in [('a','before'),('b','b'),('c','c')]}
print(json.dumps({'complete_posterior':posteriors['a'],'partial_posterior':posterior(weights,words,[1,None,None]),'loss':corpus_loss(weights,words,case['records']),'assembly':assemble(posteriors,case['testlets'],case['budget'],case['needed'])},sort_keys=True))
