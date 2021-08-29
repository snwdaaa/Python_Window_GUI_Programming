from tkinter import *

root = Tk()

root.title("Nado GUI")
root.geometry("640x480")

# 버튼 추가
btn1 = Button(root, text="버튼1") # root에 "버튼1"이 쓰여진 버튼 선언
btn1.pack() # 버튼 선언 후 pack 함수를 실행해야 윈도우에 나타남

# padx와 pady : 버튼의 크기를 가운데 텍스트를 기준으로 padding한 것으로 결정. 즉 텍스트의 길이에 따라 버튼의 크기도 달라짐
# width와 height : 절대적이고 고정적인 버튼 자체의 크기. 텍스트가 길어지면 텍스트가 잘림.
btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4")
btn4.pack()

# fg : foreground, 글자색
# bg : background, 버튼 배경색
btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

# 이미지로 버튼 만들기
photo = PhotoImage(file="image.png") # PhotoImage(file="경로"). 해당 경로의 이미지를 가져와 변수에 저장함
btn6 = Button(root, image=photo) # Button의 image 속성
btn6.pack()

# 버튼 동작 만들기
def btncmd():
    print("버튼이 클릭됨")

btn7 = Button(root, text = "동작하는 버튼", command=btncmd) # Button의 command 속성
btn7.pack()

root.mainloop()