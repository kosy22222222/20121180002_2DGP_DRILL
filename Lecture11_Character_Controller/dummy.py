class Player:
    name = 'player' #클래스 변수. 참고로 타입으로 하고 클래스 변수 출력도 네임 말고 타입으로 하면 안됨

    def __init__(self): #여기 있는 셀프 마이로 다 바꿔서 해도 됨
        self.x = 100 #셀프는 그냥 클래스 안에서 자기자신을 전달하기 위한 수단..?


    def where(self):
        print(self.x)


player = Player()
player.where()

print(Player.name) #클래스 변수 출력
print(player.name)#네임이라는 객체 변수가 없으면 같은 이름의 클래스 변수가 선택됨.

Player.where(player) #걍 웨어 괄호 안에 아무것도 안 넣으면 출력 안됨. 플레이어 넣어야 출력댐. 이게 원칙적인 파이썬에의 멤버함수호출
player.where() #->Player.where(player)과 동일