from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import textwrap
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.prompts.chat import SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.schema import Document

load_dotenv()

app = Flask(__name__)
CORS(app)

# Config LangChain API
os.environ["LANGCHAIN_ENDPOINT"] = os.getenv("LANGCHAIN_ENDPOINT")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def create_db_from_youtube_video_url(video_url):
    loader = YoutubeLoader.from_youtube_url(video_url)
    transcript_docs = loader.load()
    transcript_text = "\n".join([doc.page_content for doc in transcript_docs])

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=100)
    doc_obj = Document(page_content=transcript_text)
    docs = text_splitter.split_documents([doc_obj])  

    # additional_info = Document(page_content="")
    # docs.append(additional_info)

    db = FAISS.from_documents(docs, embeddings)
    return db

def get_response_from_query(db, query, k=4):
    docs = db.similarity_search(query, k=k)
    docs_page_content = " ".join([d.page_content for d in docs])

    chat = ChatOpenAI(model="llama-3.2-1b-instruct",
                      api_key="fake-key",
                      base_url="http://192.168.1.110:1234/v1")

    template = """
        You are a helpful assistant that can answer questions about YouTube videos
        based on the video's transcript: {docs}
        
        Only use the factual information from the transcript to answer the question.
        
        If you feel like you don't have enough information to answer the question, say "I don't know".
        """

    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    human_message_prompt = HumanMessagePromptTemplate.from_template("Answer the following question: {question}")

    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    chain = LLMChain(llm=chat, prompt=chat_prompt)

    response = chain.run(question=query, docs=docs_page_content)
    return response.replace("\n", ""), docs

def add_custom_document_to_db(db, file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    doc = Document(page_content=text)
    db.add_documents([doc])

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    video_url = data.get("video_url")
    query = data.get("query")

    if not video_url or not query:
        return jsonify({"error": "Missing video_url or query"}), 400

    db = create_db_from_youtube_video_url(video_url)
    add_custom_document_to_db(db, "custom_text.txt")
    response, docs = get_response_from_query(db, query)

    references = [{"index": i+1, "content": doc.page_content} for i, doc in enumerate(docs)]

    return jsonify({
        "response": response,
        "references": references
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
