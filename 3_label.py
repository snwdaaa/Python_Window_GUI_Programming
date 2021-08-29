from tkinter import *

root = Tk()

root.title("Nado GUI")
root.geometry("640x480")

# 레이블 : 글자 혹은 이미지를 그저 보여주기만 함. 상호작용은 불가능

# 텍스트
label1 = Label(root, text="안녕하세요")
label1.pack()

# 이미지
photo = PhotoImage(file="image.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    # config : 이미 있는 객체를 수정
    label1.config(text="또 만나요") # text 속성
    
    global photo2 
    photo2 = PhotoImage(file="image2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()