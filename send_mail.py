import smtplib
from email.message import EmailMessage

def send_mail(student, teacher, rating, comments):

    address = 'yourmail@gmail.com' # 
    password = 'yourpassword'

    msg = EmailMessage()
    msg['Subject'] = 'Survey'
    msg['From'] = address
    msg['To'] = 'receiver@gmail.com'

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

