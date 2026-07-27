# 🦷 Rashid Dental AI Assistant

An AI-powered dental clinic chatbot built with **FastAPI, Google Gemini, RAG (Retrieval-Augmented Generation), FAISS, PostgreSQL, and a responsive web interface**.

The Rashid Dental AI Assistant is designed to help clinic visitors get reliable information about dental services, appointments, clinic details, and frequently asked questions. The chatbot retrieves information from a verified Markdown-based knowledge base and uses an AI model to generate natural, context-aware responses.

The system also includes conversation memory, appointment request handling, safety guardrails, source-aware responses, and protection against unsupported medical advice.

---

## 🚀 Project Overview

The goal of this project is to develop a safe and professional AI assistant that can be embedded into a dental clinic website.

The chatbot can:

- Welcome website visitors professionally
- Identify itself as an AI assistant
- Answer clinic-related questions
- Retrieve information from Markdown knowledge-base files
- Provide source-aware responses
- Explain dental services
- Provide clinic information and opening hours
- Explain the appointment process
- Collect appointment requests
- Maintain conversation context
- Display suggested questions
- Handle unavailable information safely
- Refuse medical diagnosis requests
- Avoid recommending medications
- Recognize urgent dental warning signs
- Provide human assistance and contact guidance
- Protect appointment and user information

---

# ✨ Key Features

## 🤖 AI Chatbot

The chatbot uses Google Gemini to generate natural-language responses based on retrieved clinic information.

It is designed to provide concise and professional answers while following strict safety instructions.

---

## 📚 Retrieval-Augmented Generation (RAG)

The chatbot uses a RAG pipeline to answer questions using the clinic's Markdown knowledge base.

The process is:

```text
User Question
      ↓
Question Embedding
      ↓
FAISS Vector Search
      ↓
Relevant Knowledge Chunks
      ↓
Context + Conversation History
      ↓
Gemini AI
      ↓
Source-Aware Response
