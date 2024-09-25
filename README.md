# AI_Research_Agent
AI Research Agent with memory using GPT-4o-mini and vector bases to search relevant papers based on interest.

# The project utilizes the following python libraries
  * Streamlit for building web application
  * OpenAI for using GPT-4o-mini
  * MultiOn for accessing ArXiv and getting data(Internet of Agent)
  * Mem0 for personalised memory layer

# Overview
AI Research Agent with memory using GPT-4o-mini and vector bases to search relevant papers based on interest.User input and query fields are created in the web application using streamlit which provides a separate sidebar for user identification and research paper query.
Services are initilized when APIs are provided. MemO is configured with Qdrant as the vector store and MultiOn and OpenAI are initilized as clients. A function to process search results with GPT-4o-mini is defined which creates a structured prompt for GPT and processes arXiv search results into a readable format, returning a markdown-formatted table of research papers.

# Paper Search Functionality
The paper search functionality retrieves relevant user memories and constructs a search prompt with user context. It uses MultiOn to browse ArXiv and GPT-4o-mini to process results which are displayed in the streamlit interface.


