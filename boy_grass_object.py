from pico2d import *
import random


class Grass:
    # 생성자함수 초기화수행
    def __init__(self):
        # grass 객체의 속성을 정의하고 초기화
        self.img = load_image("grass.png")

    def draw(self):
        self.img.draw(400, 30)

    def update(self):
        pass

class Boy:
    def __init__(self):
        self.img = load_image("run_animation.png")
        self.x = random.randint(100,500)
        self.frame = random.randint(0,7)
    def draw(self):
        self.img.clip_draw(self.frame*100,0,100,100,self.x,90)

    def update(self):
        self.x += 5
        self.frame = (self.frame +1) % 8
        pass

class Zombie:
    def __init__(self):
        self.img = load_image("zombie_run_animation.png")
        self.x, self.y = 100, 170
        self.frame = 0

    def draw(self):
        frame_width = self.img.w // 10
        frame_height = self.img.h
        self.img.clip_draw(self.frame*frame_width,0,frame_width,frame_height,self.x,self.y,frame_width // 2, frame_height // 2)

    def update(self):
        self.x += 5
        self.frame = (self.frame +1) % 10


class Ball_S:
    def __init__(self):
        self.img = load_image("ball21x21.png")
        self.x, self.y =random.randint(100,700), 599

    def draw(self):
        self.img.clip_draw(0,0,21,21,self.x,self.y)
        pass
    def update(self):
        self.y -= random.randint(1, 20)
        if (self.y < 60):
            self.y = 60
        pass

class Ball_B:
    def __init__(self):
        self.img = load_image("ball41x41.png")
        self.x, self.y = random.randint(100, 700), 599
    def draw(self):
        self.img.clip_draw(0,0,41,41,self.x,self.y)
        pass
    def update(self):
        self.y -= random.randint(1, 20)
        if(self.y < 60):
            self.y = 60
        pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

def reset_world():
    global running
    global world # 월드 리스트 - 모든 객체들을 갖고있는 리스트

    world = [] # 객체가 하나도 없는 월드
    running = True

    # 땅을 만들고 월드에 추가
    grass = Grass()
    world.append(grass)

    # 소년 11명을 만들고 월드에 추가
    team = [Boy() for i in range(11)]
    world += team # 같은 리스트니까 더해서 추가 해준다.

    zombie = Zombie()
    world.append(zombie)

    ball_types = [Ball_S, Ball_B]
    for i in range(20):
        chose_ball_type = random.choice(ball_types)
        ball = chose_ball_type()
        world.append(ball)


def update_world():
    for game_object in world:
        game_object.update()



def render_world():
    # 월드에 객체들을 그린다.
    clear_canvas()
    for game_object in world:
        game_object.draw()
    update_canvas()

#세상 초기화
reset_world()

#게임 루프 반복
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
