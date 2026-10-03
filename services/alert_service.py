import smtplib
from email.message import EmailMessage

def check_and_send_alert(user_email, user_threshold, latest_temp, station_name="Global Telemetry"):
    """
    Checks if the latest temperature exceeds the user threshold 
    and sends an email notification.
    """
    if latest_temp < user_threshold:
        return False  # No alert needed

    # Email content
    subject = f"⚠️ CRITICAL OCEAN ALERT: {station_name}"
    body = (
        f"Hello,\n\n"
        f"Your monitoring station ({station_name}) has recorded an extreme temperature "
        f"of {latest_temp}°C, which exceeds your configured threshold of {user_threshold}°C.\n\n"
        f"Please log in to your dashboard to review historical anomalies and reports.\n\n"
        f"Regards,\nOcean Climate Intelligence Platform"
    )

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = "alerts@oceanclimate.internal"
    msg['To'] = user_email

    # SMTP Configuration (Update with your mail server or use local simulation)
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SENDER_EMAIL = "your-email@gmail.com"
    SENDER_PASSWORD = "your-app-password"

    try:
        if SENDER_EMAIL != "your-email@gmail.com":
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
            server.quit()
            print(f"Alert email successfully sent to {user_email}")
        else:
            print(f"[SIMULATION] Alert triggered for {user_email}! Temp: {latest_temp}°C > Threshold: {user_threshold}°C")
        return True
    except Exception as e:
        print(f"Failed to send email alert: {e}")
        return False