import smtplib, ssl

port = 465  #SSL Port for gmail

#Tells user to enter info that will be used to communicate with server
email = input("Type your email: ")
password = input("Type your web app password: ")
reciever = input("Type recieving email: ")
msg = input("Type a message: ")

context = ssl.create_default_context()  # Creates secure SSL context

#Sends email using inputted fields above via SSL protocol
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(email, password)
    server.sendmail(email, reciever, msg)
        