import yagmail
import os

receiver = "paillasaikumar6@gmail.com"  # receiver email address
body = "Attendence File"  # email body
filename = "StudentDetails"+os.sep+"StudentDetails.csv" 

yag = yagmail.SMTP("paillasaikumar6@gmail.com", "rwva btfi ifxz jmnr")

yag.send(
    to=receiver,
    subject="Attendance Report", 
    contents=body, 
    attachments=filename, 
)

