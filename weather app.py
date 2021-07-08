import tkinter as tk
import requests

root = tk.Tk()


def Location(entry):
    print(entry)


def test(weather):
    try:
        name = weather['name']
        temp = weather['main']['temp']

        test1 = 'City: %s  \nTemp : %s' % (name, temp)
    except Exception:
        test1 = "Location Not Found......"

    return test1


def weather1(city):
    key = '8f38c3036b95711787bb4fb29c1dde56'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    p = {'APPID': key, 'q': city, 'units': 'imperial'}
    r = requests.get(url, params=p)
    w = r.json()
    label['text'] = test(w)
    print(w['name'])
    print(w['main']['temp'])

frame=tk.Frame(root)
frame.place(relx=0.5,rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
label1 = tk.Label(frame, text='Weather App')
label1.place(relwidth=1, relheight=1)

frame1 = tk.Frame(root)
frame1.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.1, anchor='n')
button = tk.Button(frame1, text="Fetch",command=lambda: weather1(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

entry=tk.Entry(frame1, font=30)
entry.place(relwidth=0.69, relheight=1)

frame2 = tk.Frame(root)
frame2.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.6, anchor='n')

label=tk.Label(frame2)
label.place(relwidth=1, relheight=1)

root.mainloop()
