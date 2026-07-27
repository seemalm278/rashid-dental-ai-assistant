from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.models import ChatRequest, AppointmentRequest
from backend.rag import RAGRetriever
from backend.chat_memory import add_message, get_history
from backend.database import create_table
from backend.appointment import save_appointment
from backend.safety import safety_check

app = FastAPI(
    title="Rashid Dental AI Assistant",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize components
rag = RAGRetriever()
create_table()


@app.get("/")
def home():
    return {
        "message": "Rashid Dental AI Assistant API",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    # Check safety first
    safe, message = safety_check(request.message)

    if not safe:
        return {
            "answer": message,
            "sources": []
        }

    # Get previous conversation
    history = get_history(request.session_id)

    # Generate chatbot response
    response = rag.generate_answer(
        request.message,
        history
    )

    # Save conversation
    add_message(request.session_id, "User", request.message)
    add_message(request.session_id, "Assistant", response["answer"])

    return response
    

@app.post("/appointment")
def appointment(request: AppointmentRequest):

    return save_appointment(request)