// ==========================================
// RASHID DENTAL AI ASSISTANT
// FRONTEND CHATBOT
// ==========================================


// ==========================================
// API CONFIGURATION
// ==========================================

// Local FastAPI backend
const API_URL = "http://127.0.0.1:8000";


// ==========================================
// DOM ELEMENTS
// ==========================================

const chatToggle = document.getElementById("chat-toggle");
const chatWindow = document.getElementById("chat-window");
const closeChat = document.getElementById("close-chat");

const chatBox = document.getElementById("chat-box");

const messageInput = document.getElementById("message");
const sendButton = document.getElementById("send");

const suggestions = document.querySelectorAll(".suggestion");

const appointmentButton =
    document.getElementById("appointment-btn");

const appointmentForm =
    document.getElementById("appointment-form");

const submitAppointment =
    document.getElementById("submit-appointment");

const cancelAppointment =
    document.getElementById("cancel-appointment");

const appointmentStatus =
    document.getElementById("appointment-status");


// ==========================================
// SESSION MANAGEMENT
// ==========================================

// Create a unique session ID for this visitor

let sessionId = localStorage.getItem(
    "rashidDentalSessionId"
);

if (!sessionId) {

    sessionId =
        "session_" +
        Date.now() +
        "_" +
        Math.random()
            .toString(36)
            .substring(2, 10);

    localStorage.setItem(
        "rashidDentalSessionId",
        sessionId
    );
}


// ==========================================
// OPEN CHAT
// ==========================================

chatToggle.addEventListener(
    "click",
    function () {

        chatWindow.style.display = "flex";

        chatToggle.style.display = "none";

        messageInput.focus();

    }
);


// ==========================================
// CLOSE CHAT
// ==========================================

closeChat.addEventListener(
    "click",
    function () {

        chatWindow.style.display = "none";

        chatToggle.style.display = "flex";

    }
);


// ==========================================
// ADD USER MESSAGE
// ==========================================

function addUserMessage(message) {

    const messageElement =
        document.createElement("div");

    messageElement.className = "user";

    messageElement.textContent = message;

    chatBox.appendChild(
        messageElement
    );

    scrollToBottom();
}


// ==========================================
// ADD BOT MESSAGE
// ==========================================

function addBotMessage(
    answer,
    sources = []
) {

    const messageElement =
        document.createElement("div");

    messageElement.className = "bot";

    // Main answer

    const answerElement =
        document.createElement("div");

    answerElement.textContent = answer;

    messageElement.appendChild(
        answerElement
    );


    // ======================================
    // DISPLAY SOURCES
    // ======================================

    if (
        sources &&
        sources.length > 0
    ) {

        const sourcesElement =
            document.createElement("div");

        sourcesElement.className =
            "sources";

        const title =
            document.createElement("strong");

        title.textContent =
            "Source: ";

        sourcesElement.appendChild(
            title
        );


        const sourceText =
            document.createElement("span");

        sourceText.textContent =
            sources.join(", ");

        sourcesElement.appendChild(
            sourceText
        );


        messageElement.appendChild(
            sourcesElement
        );
    }


    chatBox.appendChild(
        messageElement
    );

    scrollToBottom();
}


// ==========================================
// SHOW TYPING INDICATOR
// ==========================================

function showTyping() {

    const typingElement =
        document.createElement("div");

    typingElement.className =
        "typing";

    typingElement.id =
        "typing-indicator";


    typingElement.innerHTML = `
        <span></span>
        <span></span>
        <span></span>
    `;


    chatBox.appendChild(
        typingElement
    );

    scrollToBottom();
}


// ==========================================
// REMOVE TYPING INDICATOR
// ==========================================

function removeTyping() {

    const typingElement =
        document.getElementById(
            "typing-indicator"
        );

    if (typingElement) {

        typingElement.remove();

    }
}


// ==========================================
// SCROLL CHAT TO BOTTOM
// ==========================================

function scrollToBottom() {

    chatBox.scrollTop =
        chatBox.scrollHeight;

}


// ==========================================
// SEND MESSAGE
// ==========================================

async function sendMessage() {

    const message =
        messageInput.value.trim();


    // Don't send empty messages

    if (!message) {

        return;

    }


    // Display user message

    addUserMessage(
        message
    );


    // Clear input

    messageInput.value = "";


    // Disable input

    messageInput.disabled =
        true;

    sendButton.disabled =
        true;


    // Show typing

    showTyping();


    try {

        const response =
            await fetch(
                `${API_URL}/chat`,
                {

                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({

                        session_id:
                            sessionId,

                        message:
                            message

                    })

                }
            );


        // Check API response

        if (!response.ok) {

            throw new Error(
                "Server error"
            );

        }


        const data =
            await response.json();


        // Remove typing indicator

        removeTyping();


        // Display AI answer

        addBotMessage(

            data.answer,

            data.sources

        );


    }

    catch (error) {

        console.error(
            "Chat Error:",
            error
        );


        removeTyping();


        addBotMessage(

            "Sorry, I'm unable to connect to the clinic assistant right now. Please try again later or contact the clinic directly."

        );

    }


    // Enable input again

    messageInput.disabled =
        false;

    sendButton.disabled =
        false;


    messageInput.focus();

}


// ==========================================
// SEND MESSAGE BUTTON
// ==========================================

sendButton.addEventListener(

    "click",

    sendMessage

);


// ==========================================
// PRESS ENTER TO SEND
// ==========================================

messageInput.addEventListener(

    "keydown",

    function (event) {

        if (
            event.key === "Enter"
        ) {

            event.preventDefault();

            sendMessage();

        }

    }

);


// ==========================================
// SUGGESTED QUESTIONS
// ==========================================

suggestions.forEach(

    function (button) {

        button.addEventListener(

            "click",

            function () {

                const question =
                    button.textContent.trim();


                // Special appointment handling

                if (
                    question ===
                    "Book Appointment"
                ) {

                    messageInput.value =
                        "I would like to book an appointment.";

                }

                else {

                    messageInput.value =
                        question;

                }


                messageInput.focus();


                // Automatically send

                sendMessage();

            }

        );

    }

);

// ==========================================
// OPEN APPOINTMENT FORM
// ==========================================

appointmentButton.addEventListener(
    "click",
    function () {

        appointmentForm.style.display =
            "block";

        appointmentButton.style.display =
            "none";

        scrollToBottom();

    }
);


// ==========================================
// CANCEL APPOINTMENT
// ==========================================

cancelAppointment.addEventListener(
    "click",
    function () {

        appointmentForm.style.display =
            "none";

        appointmentButton.style.display =
            "inline-block";

        appointmentStatus.textContent =
            "";

    }
);


// ==========================================
// SUBMIT APPOINTMENT
// ==========================================

submitAppointment.addEventListener(
    "click",
    async function () {

        const name =
            document.getElementById(
                "appointment-name"
            ).value.trim();

        const phone =
            document.getElementById(
                "appointment-phone"
            ).value.trim();

        const date =
            document.getElementById(
                "appointment-date"
            ).value;

        const time =
            document.getElementById(
                "appointment-time"
            ).value;

        const reason =
            document.getElementById(
                "appointment-reason"
            ).value.trim();


        // Validate fields

        if (
            !name ||
            !phone ||
            !date ||
            !time ||
            !reason
        ) {

            appointmentStatus.textContent =
                "Please complete all fields.";

            appointmentStatus.style.color =
                "#d92d20";

            return;

        }


        // Disable button

        submitAppointment.disabled =
            true;

        submitAppointment.textContent =
            "Submitting...";


        try {

            const response =
                await fetch(
                    `${API_URL}/appointment`,
                    {

                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({

                            name:
                                name,

                            phone:
                                phone,

                            date:
                                date,

                            time:
                                time,

                            reason:
                                reason

                        })

                    }
                );


            if (!response.ok) {

                throw new Error(
                    "Appointment request failed"
                );

            }


            const data =
                await response.json();


            appointmentStatus.textContent =
                data.message ||
                "Appointment request submitted successfully.";

            appointmentStatus.style.color =
                "#087ea4";


            // Clear form

            document.getElementById(
                "appointment-name"
            ).value = "";

            document.getElementById(
                "appointment-phone"
            ).value = "";

            document.getElementById(
                "appointment-date"
            ).value = "";

            document.getElementById(
                "appointment-time"
            ).value = "";

            document.getElementById(
                "appointment-reason"
            ).value = "";


        }

        catch (error) {

            console.error(
                "Appointment Error:",
                error
            );

            appointmentStatus.textContent =
                "Unable to submit appointment request. Please try again.";

            appointmentStatus.style.color =
                "#d92d20";

        }


        submitAppointment.disabled =
            false;

        submitAppointment.textContent =
            "Submit Request";

    }
);