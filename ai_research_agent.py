import streamlit as st
import os
from mem0 import Memory
from multion.client import MultiOn
from openai import OpenAI


# Setting up Streamlit app
st.title("AI Research Agent with Memory")
api_keys = {k: st.text_input(f"{k.capitalize()} API Key", type="password") for k in ['openai','multion']} #description for the app

# Initialize services if API keys are provided
if all(api_keys.values()):      #Configures Mem0 with Qdrant as the vector store
  os.environ['OPENAI_API_KEY'] = api_keys['openai']
  config = {
      "vector_store":{
          "provider":"qdrant",
          "config":{
              "model":"gpt-4o-mini",
              "host":"localhost",
              "port":6333,
              "collection_name":"arxiv"
          
          }
      }
  }
  memory= Memory.from_config(config)  #initialize MultiOn and OpenAI clients
  multion= Multion(api_key=api_keys['multion'])
  openai_client = OpenAI(api_key=api_keys['openai'])
  
  # Create user input and search query fields
user_id= st.sidebar.text_input("Enter your username") #adds a sidebar for user identification
search_query= st.text_input("Research paper search query") #input field for research paper search query


# Function to process search results with GPT-4o_mini
def process_with_gpt4(result):
  prompt = f"""
  Based on the following arXiv search result, provide a proper structured output in markdown that is readable by the users.
  Each paper should have a title,authors,abstract and link.
  Search Result: {result}
  output Format: Table with the following columns: [{{"title":"Paper Title","authors":"Author Names","abstract":"Brief abstract","link":"arXiv link"}}, ...]
  """
  response= openai_client.chat.completions.create(model="gpt-4o-mini",messages=[{"role":"user","content":prompt}],temperature=0.2)
  return response.choices[0].message.content


# Implement the paper search functionality
if st.button('Search for Papers'):
  with st.spinner("Searching and Processing..."):
    relevant_memories = memory.search(search_query,user_id=user_id,limit=3)
    prompt = f"Search for arXiv papers: {search_query}\n User background: {' '.join(mem['text'] for mem in relevant_memories)}"
    result= process_with_gpt4(multion.browse(cmd=prompt,url="https://arxiv.org/"))
    st.markdown(result)


# Adding a memory viewing feature
if st.sidebar.button("View Memory"):
    st.sidebar.write("\n".join([f"- {mem['text']}" for mem in memory.get_all(user_id= user_id)]))