import json
import tempfile
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import fitz
from rag_core import BM25, chunks_from_text, pdf_to_chunks, Engine, make_prompt, rrf_ranking, generate_ollama


def test_chunks_keep_page_metadata():
    t=' '.join(['Bearing vibration inspection lubrication']*100)
    c=chunks_from_text(t,'x.pdf','Test Manual',3,size=50,overlap=10,url='http://example.org/a.pdf')
    assert len(c)>1 and all(d['page']==3 for d in c)
    assert all(d['source']=='x.pdf' for d in c)


def test_bm25_prioritizes_relevant_document():
    docs=['motor shaft rotating alignment and indicator measurements',
          'oil lubrication grease selection maintenance','remote apple orchard bicycles']
    scores=BM25(docs).scores('motor shaft alignment')
    assert scores[0]>max(scores[1:])


def test_rrf_merges_and_deduplicates():
    r=rrf_ranking([[2,1,0],[1,2,3]],3)
    assert [x[0] for x in r][:2]==[1,2]


def test_can_parse_real_pdf_pages():
    with tempfile.TemporaryDirectory() as temp:
        p=Path(temp)/'demo.pdf'
        d=fitz.open()
        page=d.new_page()
        for n in range(15):
            page.insert_text((40,50+n*22),'This document explains shaft alignment and bearing maintenance procedures.')
        d.save(p); d.close()
        chunks,info=pdf_to_chunks(p,'Sample','https://example.com')
        assert len(chunks)>0 and info['pages']==1
        assert chunks[0]['page']==1


def test_engine_bm25_with_offline_toy_index():
    with tempfile.TemporaryDirectory() as tmp:
        folder=Path(tmp)
        docs=[{'id':'d1','source':'a.pdf','title':'Shaft','page':2,'url':'https://example.com/a.pdf',
               'text':'Rotating shaft alignment is checked with precision indicators.'},
              {'id':'d2','source':'b.pdf','title':'Lubrication','page':6,'url':'https://example.com/b.pdf',
               'text':'Lubrication maintenance involves grease and oil.'}]
        (folder/'chunks.json').write_text(json.dumps({'chunks':docs,'metadata':{'documents':[1,2], 'embedding_model':None}}))
        e=Engine(folder)
        results,ms=e.retrieve('shaft alignment',mode='BM25',top_k=1)
        assert results[0]['id']=='d1'
        assert 'PDF page 2' in make_prompt('alignment',results)[1]['content']
        assert ms>=0


def test_tnb_specific_question_refuses_on_public_corpus():
    answer,latency=generate_ollama(
        "What is TNB REMACO's internal maintenance approval policy?",
        [{"title":"Public manual","page":1,"text":"bearing lubrication"}])
    assert "not verified TNB REMACO records" in answer
    assert latency==0
