from redmail import EmailSender


email = EmailSender(
    host='smtp.gmail.com',
    port=587,
    username='pierregia13@gmail.com',
    password='pgny uwym bvwh npxj '
)

email.send(subject="sujet",sender="<FROM>",receivers=['pierregia13@gmail.com'],text="testmail")
