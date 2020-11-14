import smtplib             # pip install smtplib                         

sender_email = "abc@gmail.com"
rec_email = "xyz@gmail.com", "efg@gmail.com"         #recivers email id  
password = input(str("pls enter your password : "))  #prompts to write sender email password  
message = "hello this message is sent using python"

server = smtplib.SMTP('smtp.gmail.com', 587)      # port address 587
server.starttls()
server.login(sender_email, password)
print("login success")
server.sendmail(sender_email, rec_email, message)
print("email has been sent to ", rec_email)
