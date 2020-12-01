#Tip run on wayscript to send WhatsApp messages everyday
import os
from twilio.rest import Client
import datetime
data = datetime.datetime.today()
datetime.datetime(data.year,data.month,data.day,data.hour,data.minute)
index = datetime.datetime.today().weekday()
ACCOUNT_SID = "<ACCOUNT_SID>"
AUTH_TOKEN = "<AUTH_TOKEN>"
client = Client(ACCOUNT_SID,AUTH_TOKEN)
day_name= ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday','Monday']
print(day_name[index])
print(index)
if day_name[index] == 'Sunday':
  client.messages.create( body="Morning sir (JARVIS)" ,
                         to="whatsapp:+27762621248",
                from_="whatsapp:+14155238886")
if day_name[index] == 'Monday':
  client.messages.create( body= "Morning sir (JARVIS) , STK P1 8:00 - 8:50 , OBS L1 9:00 - 9:50 , BAM L1 11:00 - 11:50 , FRK 14:00 - 15:50 ,  BAM P1 16:00 - 16:50",
                         to="whatsapp:+27762621248",
                from_="whatsapp:+14155238886")
if day_name[index] == 'Tuesday':
  client.messages.create( body="Morning sir (JARVIS) , STK P1 8:00 - 8:50 , FRK T1 10:00 - 11:50 , BAM L2 12:00 - 12:50 , LST 13:00 - 14:50 ,  BAM P1 16:00 - 16:50" ,
                         to="whatsapp:+27762621248",
                from_="whatsapp:+14155238886")

if day_name[index] == 'Wednesday':
  client.messages.create( body="Morning sir (JARVIS) , FRK T2 8:00 - 8:50 , STK T1 9:00 - 9:50 , STK L2 13:00 - 13:50 , OBS L2 14:00 - 14:50" ,
                         to="whatsapp:+27762621248",
                from_="whatsapp:+14155238886")
if day_name[index] == 'Thursday':
  client.messages.create( body="Morning sir (JARVIS) , FRK L2 8:00 - 9:50 , LST L2 11:00 - 12:50 , AIM P1 13:00 - 14:50 , OBS T1 15:00 - 16:50" ,
                         to="whatsapp:+27762621248",
                from_="whatsapp:+14155238886")
if day_name[index] == 'Friday':
  client.messages.create( body="Morning sir (JARVIS) ,BAM L3 13:00 - 13:50" ,
                         to="whatsapp:+27762621248",
                from_="whatsapp:+14155238886")
if day_name[index] == 'Saturday':
  client.messages.create( body="Morning sir (JARVIS)" ,
                         to="whatsapp:+27762621248",
                from_="whatsapp:+14155238886")
