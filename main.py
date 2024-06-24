from flask import Flask, render_template, jsonify, request
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from langchain.chains.sequential import SimpleSequentialChain
from langchain.agents import AgentType, Agent, Tool, initialize_agent, load_tools

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=['POST'])
def generate():
    if request.method == 'POST':
        title = request.json.get('prompt')
        llm = ChatOpenAI(temperature=0.5, model="gpt-3.5-turbo", openai_api_key ="USER_API_KEY")
        prompt = PromptTemplate.from_template("Write a blog titled {title}. Try your best to make it interesting and engaging for the reader.")
        chain = LLMChain(llm = llm, prompt = prompt)
        blog = chain.invoke(title).get('text', 'invalid title')
        return blog

app.run(host='0.0.0.0', port=81, debug=True)