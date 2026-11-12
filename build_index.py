"""Extract public PDFs into page-cited text chunks and transformer embeddings."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import numpy as np
from rag_core import ROOT, pdf_to_chunks, INDEX


def build(pdf_dir: Path, bm25_only: bool, model_name: str, index_dir: Path = INDEX):
    sources = json.loads((ROOT/'sources.json').read_text(encoding='utf-8'))
    chunks, processed = [], []
    for source in sources:
        file_path = pdf_dir/source['filename']
        if not file_path.exists():
            print(f"[MISSING] {file_path.name}")
            continue
        new, stats = pdf_to_chunks(file_path, source['title'], source['url'])
        print(f"[PARSED] {stats['filename']}: {stats['pages']} pages -> {stats['chunks']} chunks")
        chunks.extend(new)
        processed.append(stats)
    if not chunks:
        raise SystemExit("No readable PDFs. Run: python download_data.py (or copy the PDFs manually)")
    index_dir.mkdir(parents=True, exist_ok=True)
    metadata = {"built_utc": datetime.now(timezone.utc).isoformat(),
                "embedding_model": None if bm25_only else model_name,
                "documents": processed,
                "total_chunks": len(chunks),
                "corpus_source": "U.S. Bureau of Reclamation; NOT TNB REMACO"}
    # Deleting stale dense index is essential when source data or embedding model changes.
    dense_file = index_dir/'embeddings.npy'
    dense_file.unlink(missing_ok=True)
    (index_dir/'chunks.json').write_text(json.dumps({"chunks":chunks,"metadata":metadata},
                                                     ensure_ascii=False,indent=2), encoding='utf-8')
    if not bm25_only:
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer(model_name)
        print(f"[EMBED] {len(chunks)} chunks using {model_name}")
        matrix = model.encode([c['text'] for c in chunks],batch_size=32,
                              normalize_embeddings=True,show_progress_bar=True)
        np.save(dense_file,np.asarray(matrix,dtype=np.float32))
    print(f"[DONE] {len(chunks)} indexed chunks. Metadata: {index_dir/'chunks.json'}")
    if bm25_only:
        print("[INFO] BM25-only index: Dense and Hybrid will be unavailable.")
    return metadata


if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--pdf-dir',type=Path,default=ROOT/'data'/'pdfs')
    p.add_argument('--bm25-only',action='store_true')
    p.add_argument('--model',default='sentence-transformers/all-MiniLM-L6-v2')
    a=p.parse_args()
    build(a.pdf_dir,a.bm25_only,a.model)
