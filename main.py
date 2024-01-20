import random
class Kris:
    def __init__(self, name):
        self.name=name
        self.gladness=50
        self.progress=0
        self.alive=True

    def to_study(self):
        print("Час вчитися!!")
        self.progress+=4
        self.gladness-=8
    def to_sleep(self):
        print("Я хочу спати")
        self.progress+=1
        self.gladness-=1
    def to_chill(self):
        print("Час відпочинку")
        self.progress-=2
        self.gladness+=2
    def to_music(self):
        print("Беремо навушнички і йдемо слухати музику!!")
        self.gladness+=1
        self.progress-=2
    def to_walk(self):
        print("Йдемо гуляти з друзяками!! хепі хепі хепі")
        self.progress+=0.1
        self.gladness+=2
    def to_homework(self):
        print("блін.. ну чому так домашки багато?? плак плак")
        self.progress+=2
        self.gladness-=10
    def to_phone(self):
        print("Час посидіти в телефончику!!")
        self.progress+=1
        self.gladness+=2
    def is_alive(self):
        if self.progress<-0.5:
            print("Вигнати зі школи!!!")
            self.alive=False
        elif self.gladness<=0:
            print("Дипресія.. смерть.. повіситись.")
            self.alive=False
        elif self.progress>25:
            print("Пройшла школу!! япі япі япі")
            self.alive=False
    def end_of_day(self):
        print(f"Gladness - {self.gladness}")
        print(f"Progress - {round(self.progress,2)}")

    def live(self,day):
        day="Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube=random.randint(1,7)
        if live_cube==1:
            self.to_study()
        elif live_cube==2:
            self.to_sleep()
        elif live_cube==3:
            self.to_chill()
        elif live_cube==4:
            self.to_music()
        elif live_cube==5:
            self.to_walk()
        elif live_cube==6:
            self.to_homework()
        elif live_cube==7:
            self.to_phone()
        self.end_of_day()
        self.is_alive()
kris=Kris(name="Kris")
for day in range(365):
    if kris.alive==False:
        break
    kris.live(day)