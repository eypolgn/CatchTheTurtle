import turtle
import random

# Ekran oluşturma
win = turtle.Screen()
win.title("Kaplumbağa Yakalama Oyunu")
win.bgcolor("light blue")
win.setup(width=600, height=600)

# Score ve Time metinlerini göstermek için kullanılan Turtle
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(0, 260)
score_turtle.write("Score: 0", align="center", font=("Courier", 16, "normal"))

time_turtle = turtle.Turtle()
time_turtle.hideturtle()
time_turtle.penup()
time_turtle.goto(0, 230)
time_turtle.write("Time: 30", align="center", font=("Courier", 16, "normal"))

# Score ve zamanı başlatma
score = 0
time_remaining = 30

# Yeşil kaplumbağa oluşturma
def green_turtle():
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("green")
    t.shapesize(1,1,1)
    t.penup()
    x = random.randint(-280, 280)
    y = random.randint(-280, 0)
    t.goto(x, y)
    t.onclick(lambda x, y, t=t: increase_score(t))
    return t

# Puanı arttırma fonksiyonu
def increase_score(turtle):
    global score
    score += 1
    score_turtle.clear()
    score_turtle.write("Score: {}".format(score), align="left", font=("Courier", 16, "normal"))
    turtle.clear()
    turtle.hideturtle()
    green_turtle()

# Zamanı azaltma fonksiyonu
def decrease_time():
    global time_remaining
    time_remaining -= 1
    time_turtle.clear()
    time_turtle.write("Time: {}".format(time_remaining), align="center", font=("Courier", 16, "normal"))
    if time_remaining <= 0:
        end_game()
    else:
        win.ontimer(decrease_time, 500)  # 0.5 saniyede bir güncelle

# Oyunu bitirme fonksiyonu
def end_game():
    win.clear()
    win.bgcolor("red")
    win.title("Game Over")
    end_text = turtle.Turtle()
    end_text.hideturtle()
    end_text.penup()
    end_text.goto(0, 0)
    end_text.write("Game Over!\nYour Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

# İlk kaplumbağamızı oluşturma
current_turtle = green_turtle()

# Zamanlayıcıyımızı başlatma
decrease_time()

win.mainloop()
