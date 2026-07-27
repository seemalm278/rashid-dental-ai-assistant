from collections import defaultdict

# Store conversation history by session ID
conversation_history = defaultdict(list)


def add_message(session_id: str, role: str, message: str):
    """
    Store a message in the session history.
    """
    conversation_history[session_id].append({
        "role": role,
        "message": message
    })


def get_history(session_id: str):
    """
    Return the current conversation history.
    """
    return conversation_history[session_id]


def clear_history(session_id: str):
    """
    Clear conversation history.
    """
    conversation_history[session_id] = []