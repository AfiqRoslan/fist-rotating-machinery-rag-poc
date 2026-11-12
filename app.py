"""Streamlit demo: evidence-first engineering-document RAG research system."""
import streamlit as st
from rag_core import Engine, generate_ollama

st.set_page_config(page_title="Industrial Maintenance RAG | FYP 1", page_icon="📘",layout="wide")
st.title("Industrial Maintenance Knowledge Assistant")
st.caption("FYP 1 research prototype | Public U.S. Bureau of Reclamation manuals | NOT TNB REMACO data")
st.info("Research demonstration only. Not approved for operational maintenance decisions or safety-critical use.")

@st.cache_resource(show_spinner="Loading local retrieval index...")
def load_engine():
    return Engine()

try:
    engine=load_engine()
except (FileNotFoundError,ValueError) as exc:
    st.error(str(exc))
    st.code("python download_data.py\npython build_index.py\nstreamlit run app.py",language="powershell")
    st.stop()

with st.sidebar:
    st.header("Experiment settings")
    modes=['BM25','Dense','Hybrid'] if engine.has_dense else ['BM25']
    mode=st.selectbox("Retrieval strategy",modes,index=len(modes)-1)
    top_k=st.slider("Retrieved passages (Top-k)",1,10,5)
    generate=st.toggle("Generate answer using local Ollama",value=True)
    model=st.text_input("Ollama model",value="qwen3:4b",disabled=not generate)
    st.divider()
    st.metric("Indexed PDF documents",len(engine.metadata['documents']))
    st.metric("Text chunks",len(engine.docs))
    st.caption("Dense embedding model: "+str(engine.metadata.get('embedding_model') or 'not built'))
    st.caption("Evaluation: python evaluate.py --mode Hybrid")

examples=[
    "What is static runout in rotating machinery?",
    "What are face-and-rim and reverse-indicator shaft alignment methods?",
    "Why is lubrication important for rotating equipment?",
    "What kinds of maintenance are discussed for large pump units?",
    "What is TNB REMACO's internal maintenance approval process?",
]
example=st.selectbox("Example engineering questions",["(Enter my own question)"]+examples)
def_question=example if example != "(Enter my own question)" else ""
question=st.text_area("Your question",value=def_question,height=100,
                      placeholder="Ask something supported by the maintenance PDFs...")
ask=st.button("Search technical manuals",type="primary",disabled=not question.strip())
if ask:
    with st.spinner(f"Retrieving evidence using {mode}..."):
        try:
            hits,retrieval_ms=engine.retrieve(question,mode,top_k)
        except Exception as exc:
            st.error(str(exc)); st.stop()
    st.write(f"**Retrieval:** {mode} · {len(hits)} passages · {retrieval_ms:.1f} ms (model loading may be included)")
    if generate:
        with st.spinner("Generating evidence-grounded response locally..."):
            try:
                answer,gen_ms=generate_ollama(question,hits,model=model)
                st.subheader("Grounded answer")
                st.write(answer)
                st.caption(f"Generation latency: {gen_ms:.1f} ms | Total (excluding UI): {gen_ms+retrieval_ms:.1f} ms")
            except RuntimeError as exc:
                st.warning(str(exc))
                st.info("Retrieval is functional; the source passages are shown below. To enable responses, start Ollama and pull the chosen model.")
    else:
        st.info("Retrieval-only mode: no generated answer. This is useful for inspecting BM25 / Dense / Hybrid relevance.")
    st.subheader("Source evidence (clickable PDF pages)")
    if not hits:
        st.warning("No sufficiently matching passages found. The corpus cannot answer every question.")
    for n, hit in enumerate(hits,1):
        with st.expander(f"[{n}] {hit['title']} · PDF p.{hit['page']} · score {hit['score']:.3f}",expanded=n==1):
            st.markdown(f"[Open original PDF at page {hit['page']}]({hit['url']}#page={hit['page']})")
            st.write(hit['text'])
            st.caption(f"Retrieval record: {hit['id']}")

st.divider()
st.caption("Scope: document-grounded educational QA only. No internal TNB records, real-time equipment diagnosis, maintenance authorization, or SCADA connection.")
