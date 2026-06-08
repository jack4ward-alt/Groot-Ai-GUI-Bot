from tkinter import *
import os
from groq import Groq

client = Groq(api_key="Your_GROK_API_KEY")

def submit():
    question = entry.get()
    if not question:
        return
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": question}]
    )
    answer = response.choices[0].message.content
    result_text.config(state=NORMAL)
    result_text.delete("1.0", END)
    result_text.insert(END, answer)
    result_text.config(state=DISABLED)

window = Tk()
window.title("AI GUI")
window.geometry("600x400")

# Top row: entry + button
top_frame = Frame(window)
top_frame.pack(fill=X, padx=10, pady=10)

entry = Entry(top_frame, width=50)
entry.pack(side=LEFT)

submit_btn = Button(top_frame, text="↑", command=submit)
submit_btn.pack(side=LEFT, padx=5)

# Answer area below
result_text = Text(window, wrap=WORD, state=DISABLED, padx=10, pady=10)
result_text.pack(fill=BOTH, expand=True, padx=10, pady=(0,10))

scrollbar = Scrollbar(window, command=result_text.yview)
scrollbar.pack(side=RIGHT, fill=Y)
result_text.config(yscrollcommand=scrollbar.set)

window.mainloop()
