# Deep Research AI Agent

A powerful AI-driven research assistant built with LangGraph, Tavily, and Streamlit. This agent decomposes complex research queries, conducts thorough web searches, and generates comprehensive answers.

## 🌟 Features

- **Query Decomposition**: Breaks down complex research questions into manageable sub-queries
- **Automated Web Research**: Leverages Tavily API for high-quality web search results
- **Answer Synthesis**: Generates comprehensive answers based on collected research
- **Interactive UI**: User-friendly Streamlit interface for easy interaction
- **Real-time Updates**: Provides status updates throughout the research process

## 🛠️ Technology Stack

- **LangGraph**: For creating the agent workflow and managing state
- **Tavily API**: For web search and information retrieval
- **Streamlit**: For the interactive web interface
- **Python**: Core programming language
- **dotenv**: For environment variable management

## 📋 Prerequisites

- Python 3.8+
- Tavily API key

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/deep-research-ai-agent.git
   cd deep-research-ai-agent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your Tavily API key:
   ```
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

## 💻 Usage

### Running Locally

Start the Streamlit app:
```bash
streamlit run streamlit_app.py
```

### Using the Research Agent

1. Enter your research query in the text input field
2. Click "Start Research"
3. Watch as the agent:
   - Decomposes your query into sub-questions
   - Conducts research on each sub-question
   - Synthesizes the findings into a comprehensive answer

## 🏗️ Project Structure

```
deep-research-ai-agent/
├── deep_research_agent/
│   ├── agents/
│   │   ├── decomposition_agent.py  # Handles query breakdown
│   │   ├── research_agent.py       # Conducts web research
│   │   └── drafting_agent.py       # Synthesizes final answer
│   ├── graph/
│   │   ├── graph.py                # LangGraph workflow definition
│   │   └── state.py                # State management
│   ├── app.py                      # Streamlit UI implementation
│   ├── main.py                     # Core functionality
│   └── requirements.txt            # Package dependencies
├── streamlit_app.py                # Entry point for Streamlit Cloud
├── requirements.txt                # Project dependencies
└── README.md                       # Project documentation
```

## 🌐 Deployment

This application can be deployed on Streamlit Cloud:

1. Push your code to GitHub
2. Sign up for [Streamlit Cloud](https://streamlit.io/cloud)
3. Create a new app pointing to your repository
4. Set the main file path to `streamlit_app.py`
5. Add your Tavily API key as a secret in the Streamlit Cloud dashboard

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- [LangGraph](https://github.com/langchain-ai/langgraph) for the agent workflow framework
- [Tavily](https://tavily.com/) for the research API
- [Streamlit](https://streamlit.io/) for the web interface framework
#
