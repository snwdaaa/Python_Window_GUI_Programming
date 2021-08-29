# tkinter -> 윈도우 모듈
from tkinter import *
import tkinter.messagebox as msgbox # 메시지 박스는 tkinter.messagebox 모듈에 있음

root = Tk()

root.title("Nado GUI") # 프로그램 창 타이틀
root.geometry("640x480") # 첫 실행시 프로그램 창 크기 설정. 가로 x 세로 크기 지정

# 메시지 박스 : 팝업으로 뜨는 메시지 창

# 기차 예매 시스템
def info():
    # 함수 showinfo(title, message) : 창 이름은 title, 내용은 message
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")

def warn():
    # 함수 showwarning(title, message) : 창 이름은 title, 내용은 message
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")

def error():
    # 함수 showerror(title, message) : 창 이름은 title, 내용은 message
    msgbox.showerror("에러", "결제 오류가 발생했습니다.")

def okcancel():
    # askokcancel : 사용자에게 OK 또는 Cancel을 누를 지 물어보는 창
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")

def retrycancel():
    # askretrycancel : 사용자에게 Retry 또는 Cancel을 누를 지 물어보는 창
    response = msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")

    # 재시도 -> 1 
    # 취소 -> 0
    if(response == 1):
        print("재시도")
    elif(response == 0):
        print("취소")

def yesno():
    # askyesno : 사용자에게 Yes 또는 No를 누를 지 물어보는 창
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?")

def yesnocancel():
    # askyesnocancel : 사용자에게 Yes 또는 No 또는 Cancel을 누를 지 물어보는 창
    # 이런 식으로 사용자의 선택에 따른 값을 변수로 가져올 수 있다
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다.\n저장 후 프로그램을 종료하시겠습니까?")

    # 네 : 저장 후 종료 -> True 반환
    # 아니오 : 저장 하지 않고 종료 -> False 반환
    # 취소 : 프로그램 종료 취소 -> None 반환
    # 이때 True -> 1, False -> 0, None -> 그 외
    if(response == 1):
        print("예")
    elif(response == 0):
        print("아니오")
    else:
        print("취소")

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()

Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()

root.mainloop() # 창이 닫히지 않도록 루프 돌림