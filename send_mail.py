import smtplib
from email.message import EmailMessage

def send_mail(student, teacher, rating, comments):

    address = 'men.stefan@gmail.com'
    password = 'Biedronka123'

    msg = EmailMessage()
    msg['Subject'] = 'Ankieta'
    msg['From'] = address
    msg['To'] = 'men.stefan1@gmail.com'

    msg.add_alternative(f"""\
    <!DOCTYPE html>
    <html>
        <body>
            <h1 style="color:SlateGray;">New feedback submission</h1>
                <ul>
                    <li>Student: {student}</li>
                    <li>Teacher: {teacher}</li>
                    <li>Rating: {rating}</li>
                    <li>Comment: {comments}</li>
                </ul>
        </body>
    </html>
    """, subtype='html')

    # Sending emial
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(address, password)
        smtp.send_message(msg)

