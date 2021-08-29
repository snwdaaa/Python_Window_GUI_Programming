from tkinter import *

root = Tk()

root.title("제목 없음 - Windows 메모장") # 프로그램 표시 이름
root.geometry("640x480")
root.resizable(True, True) # 프로그램 창의 x, y 크기 변경 가능

# 메뉴
menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_edit = Menu(menu, tearoff=0)
menu_template = Menu(menu, tearoff=0)
menu_view = Menu(menu, tearoff=0)
menu_help = Menu(menu, tearoff=0)

menu.add_cascade(label="파일", menu=menu_file)
menu.add_cascade(label="편집", menu=menu_edit)
menu.add_cascade(label="서식", menu=menu_template)
menu.add_cascade(label="보기", menu=menu_view)
menu.add_cascade(label="도움말", menu=menu_help)

root.config(menu=menu) # root에 menu 설정

# 파일 메뉴 구현(열기, 저장, 끝내기)
def OpenFile():
    file = open("mynote.txt", 'r')
    data = file.read() # txt 파일의 내용을 읽어온다

    # textArea의 기존 내용을 지운 후, 파일의 내용을 입력
    textArea.delete("1.0", END)
    textArea.insert("1.0", data)

def SaveFile():
    file = open("mynote.txt", 'w')
    currentText = textArea.get("1.0", END) # 1행의 0열부터 마지막까지 모든 내용을 읽어들인다
    file.write(currentText) # 읽어들인 내용을 txt 파일에 저장한다

menu_file.add_command(label="열기", command=OpenFile)
menu_file.add_command(label="저장", command=SaveFile)
menu_file.add_command(label="끝내기", command=root.quit)

# 프로그램 입력 본문
# 입력 부분과 스크롤 바를 프레임으로 묶어줌
inputFrame = Frame(root)
inputFrame.pack()

# 스크롤 바
scrollBar = Scrollbar(inputFrame)
scrollBar.pack(side="right", fill="y")

# 메모장 입력 부분은 텍스트 사용
textArea = Text(inputFrame, width=640, height=480, yscrollcommand=scrollBar.set)
textArea.pack()

scrollBar.config(command=textArea.yview) # 스크롤 바를 textArea와 연동

root.mainloop() # 루프