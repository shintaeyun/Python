class Email:
  sender = ""
  
  def send_mail(self, recv, subject, contents):
    print("From:\t" + self.sender)
    print("To:\t" + recv)
    print("Subject:" + subject)
    print("Contents")
    print(contents)
    print("-"*20)
  
e = Email()
e.sender = "airim@naver.com"
recv_list = ["gwangjuai_1@likelion.net", "gwangjuai_2@likelion.net"]

for recv in recv_list:
  e.send_mail(recv, "광주 인공지능 사관학교에 오신것을 환영합니다.",
              "이번 온라인 강의는 함수와 클래스 입니다.")
