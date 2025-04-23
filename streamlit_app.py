import sys
import os
from pathlib import Path

# Add the project root to the Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

# Import the Streamlit app from the deep_research_agent package
from deep_research_agent.app import *

# This file serves as the entry point for Streamlit Cloud deployment
# The import statement above will execute the Streamlit app code
