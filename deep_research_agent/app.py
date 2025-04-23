import streamlit as st
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent 
sys.path.insert(0, str(project_root))

try:
    from deep_research_agent.main import run_graph
except ImportError as e:
    st.error(f"Failed to import 'run_graph'. Ensure main.py is structured correctly and dependencies are installed. Error: {e}")
    st.stop() 

st.set_page_config(page_title="Deep Research Agent", layout="wide")
st.title("🧠 Deep Research Agent")
st.caption("Enter a query to start the research process using LangGraph and Tavily.")

query = st.text_input("Enter your research query:", key="query_input")

if st.button("Start Research", key="start_button"):
    if not query:
        st.warning("Please enter a query.")
    else:
        st.success(f"Starting research for: \"{query}\"")

        status_placeholder = st.empty()
        decomposition_placeholder = st.empty()
        results_placeholder = st.empty()
        error_placeholder = st.empty()

        final_answer = None

        with st.spinner("Research in progress..."):
            try:
                for step_type, step_output in run_graph(query):
                    if step_type == "status":
                        status_placeholder.info(f"Status: {step_output}")
                    elif step_type == "decomposition":
                        with decomposition_placeholder.expander("View Sub-queries"):
                            st.write(step_output)
                    elif step_type == "research":
                        pass
                    elif step_type == "draft":
                        final_answer = step_output
                        status_placeholder.empty()
                        decomposition_placeholder.empty()
                    elif step_type == "error":
                        error_placeholder.error(f"Error: {step_output}")
                        break 

            except Exception as e:
                 error_placeholder.error(f"An unexpected error occurred in the Streamlit app: {e}")

        if final_answer:
            results_placeholder.markdown("### Research Results")
            results_placeholder.markdown(final_answer)
        elif not error_placeholder.empty(): 
             pass 
        else:
            results_placeholder.warning("No answer was generated.")

st.markdown("---")
