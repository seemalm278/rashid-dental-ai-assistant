from .database import get_connection


def save_appointment(data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO appointments
        (name, phone, date, time, reason)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            data.name,
            data.phone,
            data.date,
            data.time,
            data.reason,
        ),
    )

    conn.commit()
    conn.close()

    return {
        "message": "Appointment request submitted successfully."
    }