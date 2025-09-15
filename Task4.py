# 1. To-Do List CLI App
import json, os

FILE_NAME = "tasks.json"

def load_tasks():
    return json.load(open(FILE_NAME)) if os.path.exists(FILE_NAME) else []

def save_tasks(tasks):
    json.dump(tasks, open(FILE_NAME, "w"), indent=4)

def show_tasks(tasks):
    if not tasks:
        print("✅ No tasks yet!")
    for i, t in enumerate(tasks, 1):
        status = "✔" if t["done"] else "❌"
        print(f"{i}. {t['title']} [{status}]")

def add_task(tasks):
    tasks.append({"title": input("Task: "), "done": False}); save_tasks(tasks)

def mark_done(tasks):
    show_tasks(tasks)
    n = int(input("Task number: ")) - 1
    tasks[n]["done"] = True; save_tasks(tasks)

def remove_task(tasks):
    show_tasks(tasks)
    n = int(input("Task number: ")) - 1
    tasks.pop(n); save_tasks(tasks)

def main():
    tasks = load_tasks()
    while True:
        print("\n1.Show  2.Add  3.Done  4.Remove  5.Exit")
        c = input("Choice: ")
        if c=="1": show_tasks(tasks)
        elif c=="2": add_task(tasks)
        elif c=="3": mark_done(tasks)
        elif c=="4": remove_task(tasks)
        elif c=="5": break

if __name__ == "__main__": main()
# --------------------------------------------------------
# 2. Quiz Game
questions = [
    {"q": "Capital of India?", "options": ["Delhi","Mumbai","Kolkata"], "a": "Delhi"},
    {"q": "5 + 7 = ?", "options": ["10","12","15"], "a": "12"},
    {"q": "Python creator?", "options": ["Guido","Linus","James"], "a": "Guido"}
]

def run_quiz():
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['q']}")
        for opt in q["options"]: print("-", opt)
        ans = input("Your answer: ")
        if ans == q["a"]:
            print("✅ Correct!"); score += 1
        else:
            print("❌ Wrong! Correct:", q["a"])
    print(f"\nFinal Score: {score}/{len(questions)}")

if __name__ == "__main__": run_quiz()
# ----------------------------------------------------------------
# 3. Weather Info App (API)import requests

API_KEY = "YOUR_API_KEY"  # replace with your key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    r = requests.get(url).json()
    if r.get("cod") != 200:
        print("❌ City not found!")
        return
    print(f"\n🌍 {r['name']}, {r['sys']['country']}")
    print(f"🌡 Temp: {r['main']['temp']}°C")
    print(f"☁ Weather: {r['weather'][0]['description']}")
    print(f"💧 Humidity: {r['main']['humidity']}%")

if __name__ == "__main__":
    city = input("Enter city: ")
    get_weather(city)
# ------------------------------------------------------------------
# 4. File Organizer
import os, shutil

def get_file_type(file):
    ext = file.split(".")[-1].lower()
    types = {
        "images": ["jpg","jpeg","png","gif"],
        "docs": ["pdf","docx","txt"],
        "videos": ["mp4","mkv","avi"]
    }
    for t, exts in types.items():
        if ext in exts: return t
    return "others"

def organize_files(folder):
    for f in os.listdir(folder):
        path = os.path.join(folder, f)
        if os.path.isfile(path):
            ftype = get_file_type(f)
            new_dir = os.path.join(folder, ftype)
            os.makedirs(new_dir, exist_ok=True)
            shutil.move(path, os.path.join(new_dir, f))
            print(f"Moved {f} → {ftype}/")

if __name__ == "__main__":
    folder = input("Enter folder path: ")
    organize_files(folder)
