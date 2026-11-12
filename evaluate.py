"""Preliminary document-level retrieval benchmark (not a final gold-page evaluation)."""
import argparse
import csv
import json
from pathlib import Path
import statistics
from rag_core import Engine, ROOT


def evaluate(mode='BM25',k=5,benchmark=None):
    questions=list(csv.DictReader(open(benchmark or ROOT/'benchmark_questions.csv',encoding='utf-8-sig',newline='')))
    engine=Engine()
    rows=[]
    for item in questions:
        hits,latency=engine.retrieve(item['question'],mode=mode,top_k=k)
        expected=item['expected_document']
        positions=[i+1 for i,h in enumerate(hits) if h['source']==expected]
        rank=positions[0] if positions else None
        rows.append({**item,'mode':mode,'k':k,'hit_at_k':int(rank is not None),
                    'reciprocal_rank':1/rank if rank else 0,'first_rank':rank or '',
                    'retrieval_ms':round(latency,2),
                    'top_sources':' | '.join(f"{h['source']}:p{h['page']}" for h in hits)})
    summary={'evaluation_level':'DOCUMENT (not passage/page relevance)',
             'mode':mode,'k':k,'n_questions':len(rows),
             'document_hit_at_k':sum(r['hit_at_k'] for r in rows)/len(rows),
             'document_mrr_at_k':statistics.mean(r['reciprocal_rank'] for r in rows),
             'mean_retrieval_ms':statistics.mean(r['retrieval_ms'] for r in rows)}
    output=ROOT/'results'
    output.mkdir(exist_ok=True)
    with (output/f"retrieval_{mode.lower()}.csv").open('w',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=rows[0].keys()); writer.writeheader(); writer.writerows(rows)
    (output/f"retrieval_{mode.lower()}_summary.json").write_text(json.dumps(summary,indent=2),encoding='utf-8')
    print(json.dumps(summary,indent=2))
    print('Warning: This is document-level proxy evaluation, NOT formally labelled Recall@5 / MRR.')
    return summary


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--mode',choices=['BM25','Dense','Hybrid'],default='BM25')
    p.add_argument('--k',type=int,default=5)
    p.add_argument('--benchmark',type=Path)
    a=p.parse_args()
    evaluate(a.mode,a.k,a.benchmark)
