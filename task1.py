from socket import *
import ssl
import base64

#Tells user to input information used to connect to the mail server
email = input("Type your email: ")
password = input("Type your web app password: ")
reciever = input("Type recieving email: ")

#Used in the login command
loginInfo = ("\x00" + email + "\x00" + password).encode()
loginInfo = base64.b64encode(loginInfo)

#Messages that will be sent via email
msg = "\r\n I love computer networks!" 
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver mailserver = 

# #Fill in start 
mailserver = "smtp.gmail.com"   #variable that holds the mail server
#Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver

#Fill in start

#Establishes a TCP connection to the mailsever with SSL
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 465))
clientSocket = ssl.wrap_socket(clientSocket)
#Fill in end

#Gets and prints server response for establishing TCP connection
recv = clientSocket.recv(1024).decode()
print(recv)

if recv[:3] != '220':   #if the TCP connection fails, an error message is printed  
    print('220 reply not received from server.')

# Send HELO command and print server response. 
heloCommand = 'HELO Alice\r\n' 
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode() 
print(recv1)

if recv1[:3] != '250':  #prints error message if HELO Command fails
    print('250 reply not received from server.')

#SEND AUTH PLAIN command and get and print server response
authCommand = "AUTH PLAIN ".encode() + loginInfo + "\r\n".encode()  
clientSocket.send(authCommand)  #Logs into mail server using the email and app password user inputted
recv2 = clientSocket.recv(1024).decode()   
print(recv2)

# Send MAIL FROM command and get and print server response.

# Fill in start
mailFromCommand = 'MAIL FROM: <' + email + '>\r\n'  
clientSocket.send(mailFromCommand.encode())     #Sets who the email is from, the email that was used to log in
recv3 = clientSocket.recv(1024).decode()
print(recv3)
# Fill in end

# Send RCPT TO command and print server response.

# Fill in start
rcptToCommand = 'RCPT TO: <' + reciever + '>\r\n'
clientSocket.send(rcptToCommand.encode())   #Sets who the email is to be sent to
recv4 = clientSocket.recv(1024).decode()
print(recv4)
# Fill in end

# Send DATA command and get and print server response.

# Fill in start
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())   #Gets permission from server if the mail can be sent
recv5 = clientSocket.recv(1024).decode()
print(recv5)
# Fill in end

# Send message data.

# Fill in start

clientSocket.send(msg.encode())     #Sets the email message
# Fill in end

# Message ends with a single period.

# Fill in start
clientSocket.send(endmsg.encode())  #Ends the email message
recv6 = clientSocket.recv(1024).decode()
print(recv6)
# Fill in end

# Send QUIT command and gets and prints server response.

# Fill in start
quitCommand = 'QUIT\r\n'
clientSocket(quitCommand.encode())  #Terminates SMTP Session
recv7 = clientSocket.recv(1024).encode()
print(recv7)
# Fill in end