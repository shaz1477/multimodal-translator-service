# multimodal-translator-service
Multimodal AI Microservice: LangChain + FastAPI + OpenAI. Real-time translation and Speech-to-Text synthesis with LangSmith observability.
A production-ready Generative AI microservice that orchestrates a multimodal pipeline to translate text and synthesize high-fidelity audio responses. Built using LangChain (LCEL) and FastAPI, this project demonstrates modern LLM orchestration and deployment patterns.

🚀 Features
Multimodal Orchestration: Seamlessly connects GPT-4o for linguistic translation and OpenAI TTS-1 for binary audio generation.

LCEL Implementation: Built using LangChain Expression Language for a declarative, efficient, and readable chain logic.

Production-Ready API: Exposed via FastAPI with integrated LangServe, providing a RESTful interface and an interactive playground.

Full Observability: Integrated with LangSmith for real-time tracing, latency monitoring, and token cost analysis.

Asset Management: Custom Python logic for environment-agnostic file persistence and streaming audio responses.

🛠️ Technical Stack
Frameworks: LangChain, FastAPI, LangServe, Uvicorn

Models: GPT-4o, OpenAI TTS-1 (Alloy Voice)

Observability: LangSmith

Language: Python 3.10+

📋 Architecture
The service follows a linear chain of thought:

Input: User provides target language and source text.

Translation: GPT-4o processes the linguistic transformation.

Synthesis: The translated string is piped into the TTS-1 model.

Persistence: The binary audio stream is saved to the local file system (or cloud storage).

Output: A success message with the file path is returned to the client.

⚙️ Installation & Setup
Clone the repository:

Bash
git clone https://github.com/your-username/multimodal-translator-service.git
cd multimodal-translator-service
Install dependencies:

Bash
pip install -r requirements.txt
Configure Environment Variables:
Create a .env file in the root directory:

Plaintext
OPENAI_API_KEY=your_api_key_here
LANGCHAIN_API_KEY=your_langchain_key_here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=multimodal-translator
Run the Server:

Bash
python main.py
🔍 API Usage
Once the server is running, you can access the interactive playground at:
http://127.0.0.1:8000/chain/playground

Sample Input:

JSON
{
  "language": "hindi",
  "text": "I am having a productive day learning GenAI."
}
Author: Shanavaz Mohammad

Contact: mohammadshanavaz@gmail.com

Master of Science in Information Quality (MSIQ)

Final Professional Tips for your GitHub:
The requirements.txt: Make sure you create this file in the same folder. It should contain:

Plaintext
langchain-openai
langserve[all]
fastapi
uvicorn
python-dotenv
openai
