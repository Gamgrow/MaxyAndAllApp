
import Take_command
import smtplib  # for email send

class sendmail():
    def sendmail(email, subject, contant, name):
        from email.message import EmailMessage
        email_id = "lalitmaxbusiness@gmail.com"
        email_pas = "iwitlggtpqxppmup"

        msg = EmailMessage()
        msg["subject"] = subject
        msg["from"] = "Lalit kumar yadav"
        msg["to"] = email
        msg.set_content(contant)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(email_id, email_pas)
            smtp.send_message(msg)
            print("sent mail succesfully...")
            Take_command.speak("sent mail succesfully")