import threading
import time

class Philosopher(threading.Thread):

    def __init__(self, _id, forks):
        threading.Thread.__init__(self, name="Fil+osofo "+str(_id), target=Philosopher.run)
        self.id = int(_id)
        self.nIzq = (_id + 1) % 5
        self.forks = forks
        self.thinking = True
        self.eating = False
        self.hungry = False
        self.dead = False
        self.name = ""
        self.timesAte = 0

        self.eatTime = 0.5
        self.thinkTime = 2
        self.hungerTime = 10

        self.rightFork = False
        self.leftFork = False
    
    def setName(self,_name):
        self.name = _name

    def setDead(self,_dead):
        self.dead = _dead

    def setState(self,_state):
        self.state = _state

    def setTimesAte(self, _times):
        self.timesAte = _times

    def takeLeftFork(self):
        print("Filósofo "+str(self.id)+" trata de tomar el tenedor izquierdo")
        try:
            self.forks[self.id].acquire()
            print("Filósofo "+str(self.id)+" tiene el tenedor izquierdo")
            self.leftFork = True
        except:
            print("Filósofo "+str(self.id)+" no pudo tomar el tenedor izquierdo")

    def takeRightFork(self):
        print("Filósofo "+str(self.id)+" trata de tomar el tenedor derecho")
        try:
            self.forks[self.nIzq].acquire()
            print("Filósofo "+str(self.id)+" tiene el tenedor derecho")
            self.rightFork = True
        except:
            print("Filósofo "+str(self.id)+" no pudo tomar el tenedor derecho")

    def leaveLeftFork(self):
        if(self.leftFork):
            print("Filósofo "+str(self.id)+" deja el tenedor izquierdo")
            self.forks[self.id].release()
            self.leftFork = False

    def leaveRightFork(self):
        if(self.rightFork):
            print("Filósofo "+str(self.id)+" deja el tenedor derecho")
            self.forks[self.nIzq].release()
            self.rightFork = False

    def eat(self):
        print("Filósofo "+str(self.id)+" está comiendo")
        time.sleep(self.eatTime)
        self.setTimesAte(self.timesAte + 1)

    def think(self):
        print("Filósofo "+str(self.id)+" está pensando")
        time.sleep(self.thinkTime)

    def hunger(self):
        print("Filósofo "+str(self.id)+" no pudo comer")
        self.hungerTime-=1
        if(self.hungerTime == 0):
            self.dead = True
            print("Filósofo "+str(self.id)+" murió de hambre")

    def run(self):
        while(self.timesAte < 5 and not self.dead):
            self.think()
            self.takeLeftFork()
            self.takeRightFork()
            if(self.leftFork and self.rightFork):
                self.eat()
            else:
                self.hunger()
            self.leaveLeftFork()
            self.leaveRightFork()
        print("Filósofo "+str(self.id)+" ha comido 5 veces ya")