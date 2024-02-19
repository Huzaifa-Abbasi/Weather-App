from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
    try:
        city=textfield.get()
        geolocator= Nominatim(user_agent="geoapiExercises")
        location= geolocator.geocode(city)
        obj= TimezoneFinder()
        result= obj.timezone_at(lng=location.longitude,lat=location.latitude)
    

        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="Current Weather")

        #Weather #api 
        api= f"https://api.openweathermap.org/data/2.5/weather?q="+city+'&appid=d5f75ae354299306026836269eb0a502'
        json_data = requests.get(api).json()
        condition = json_data["weather"][0]["main"]
        description = json_data['weather'][0]['description']
        temp = int ((json_data[ 'main']["temp"]-273.15))
        pressure = json_data[ 'main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data[ 'wind']['speed']

        t.config(text=(temp,"º"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,'º'))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry!!")


#search box
# copy the path of search image and paste it in 1st line in (file = ..........)
Search_image=PhotoImage(file="D:/QUEST/PF (PROJECTS)/Python Weather App/search.png")
myimage=Label(image=Search_image, borderwidth=-8)
myimage.place(x=400,y=80)

textfield=tk.Entry(root, justify="center" ,width=16, font=("poppins" ,25, "bold"),bg="#404048" ,border=0, fg="white")
textfield.place(x=460,y=99)
textfield.focus()

# copy the path of search_icon and paste it in 1st line in (file = ..........)
Search_icon=PhotoImage(file="D:/QUEST/PF (PROJECTS)/Python Weather App/search_icon.png")
myimage_icon=Button(image=Search_icon, borderwidth=0, cursor= "hand2", bg="#404040",command=getWeather)
myimage_icon.place (x=765,y=90)

#logo
# copy the path of logo image and paste it in 1st line in (file = ..........)
Logo_image=PhotoImage(file="D:/QUEST/PF (PROJECTS)/Python Weather App/logo.png")
logo=Label(image=Logo_image, borderwidth=0)
logo.place(x=150,y=100)

Logo_image2=PhotoImage(file="D:/QUEST/PF (PROJECTS)/Python Weather App/logo.png")
logo=Label(image=Logo_image, borderwidth=0)
logo.place(x=150,y=100)

#Bottom box
# copy the path of box image and paste it in 1st line in (file = ..........)
Frame_image=PhotoImage (file="D:/QUEST/PF (PROJECTS)/Python Weather App/box.png")
frame_myimage=Label(image=Frame_image, borderwidth=0)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"), borderwidth=0)
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20), borderwidth=0)
clock.place(x=30,y=130)

 #label
label0 = Label(root, text = "Qᴜᴇꜱᴛ ᴡᴇᴀᴛʜᴇʀ ᴀᴘᴘ", font = ("ARIAL",35, 'bold'),fg = "black" )
label0.place(x = 230,y=1)

label1=Label(root, text= "WIND" ,font=("Helvetica" ,15, 'bold'),fg="white",bg= "#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root, text= "HUMIDITY" , font=("Helvetica" ,15, 'bold'),fg="white",bg="#1ab5ef")
label2.place(x=225,y=400)

label3=Label(root, text= "DESCRIPTION", font=("Helvetica" ,15, "bold"),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4=Label(root, text= "PRESSURE",font=("Helvetica" ,15, "bold"),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15, 'bold'))
c.place(x=400,y=250)

w=Label(text="...",font=("arial",20, "bold"),bg="#1ab5ef")
w.place(x=129,y=430)
h=Label(text="...",font=("arial",20, "bold"),bg="#1ab5ef")
h.place(x=280,y=430)
d=Label(text="...",font=("arial",20, "bold"),bg="#1ab5ef")
d.place(x=450,y=430)
p=Label(text="...",font=("arial",20, "bold"),bg="#1ab5ef")
p.place(x=670,y=430)

root.mainloop()