
#Loading the environment variable
import os
from dotenv import load_dotenv
load_dotenv()
openai_api_key=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")
from langchain_openai import ChatOpenAI
from openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from fastapi import FastAPI

#Text Generation Model
chat_model=ChatOpenAI(model="gpt-5.4")
chat_model
model=OpenAI()
model

prompt=ChatPromptTemplate.from_messages([
    ("system","Translate the follwing :{language}"),
    ("user","{text}")
])
parser=StrOutputParser()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "output_audio.mp3")

def text_to_speech(translated_text):
    with model.audio.speech.with_streaming_response.create(model="tts-1",voice="alloy",input=translated_text)as response:

        response.stream_to_file(file_path) 
    return f"success. Audio saved at:{file_path}"

chain=prompt|chat_model|parser|RunnableLambda(text_to_speech)

result = chain.invoke({"language": "hindi", "text": "I am not okay.iam having a bad day today "})
print(result)


app=FastAPI(title="Langchain Server",
            version="1.0",
            description="A simple API server using Langchain runnable interfaces")
from langserve import add_routes
#Adding chain routes
add_routes(app,
           chain,
           path="/chain"
           )

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)
