######################################################
# Project: Project 2
# UIN: 662842791
# repl.it URL: https://replit.com/@CS111-Fall2021/Project-2-AdamNimer1#main.py

######################################################

import turtle
import random

s = turtle.Screen()

t1 = turtle.Turtle()


def main(): 

  # sets screen
  s = turtle.Screen()
  s.setup(350,350)
  s.screensize(300,300)

  #sets start screen
  t1.hideturtle()
  s.tracer(0)
  s.bgcolor('lightblue')
  t1.penup()
  t1.goto(-30,85)
  t1.write('Jaws', font=('Helvetica', 20))
  t1.goto(-80,-100)
  t1.write('Press Enter to Begin', align='left', font=('Helvetica'))
  t1.goto(-85,-150)
  t1.write('Created by: Adam Nimer', align='left', font=('Helvetica', 10)) 
  t1.hideturtle()

  t1.goto(-120,0)
  t1.write('Use the arrow keys to touch the\n treasure chest and level up.', font=('Helvetica'))
  t1.goto(-130,-25)
  t1.write('Avoid swimming near the sharks.',  font=('Helvetica'))

  #waits for input from user. used input() as an alternative way to get game started. Also, clears start screen objects.
  input()
  s.clear()

  # sets background picture and sets tracer to 0 
  s.bgpic("Gifs/picbackground.gif")
  s.tracer(0)

  # sets screen size variables, and x and y coords
  w, h = s.screensize()
  x = random.randint((-w/2),w/2)
  x1 = random.randint(-75, 75)
  y = (100)


  # creates game objects dict
  game_objects = [{"t": turtle.Turtle(),"x":x, "y":y, "radius": 50, "image":"Gifs/shark.gif", "type":"shark1"}]

  # appends more game objects such as treasure, sharks, etc.
  game_objects.append({"t": turtle.Turtle(),"x":x, "y":y-50, "radius": 50, "image":"Gifs/reversed_shark.gif", "type":"shark2"})
  for obj in game_objects:
    s.addshape(obj["image"])
    obj["t"].shape(obj["image"])

  game_objects.append({"t": turtle.Turtle(),"x":x, "y":y-100, "radius": 50, "image":"Gifs/reversed_shark.gif", "type":"shark3"})
  for obj in game_objects:
    s.addshape(obj["image"])
    obj["t"].shape(obj["image"])

  game_objects.append({"t": turtle.Turtle(),"x":x, "y":y-150, "radius": 50, "image":"Gifs/shark.gif", "type":"shark4"})
  for obj in game_objects:
    s.addshape(obj["image"])
    obj["t"].shape(obj["image"])

  game_objects.append({"t": turtle.Turtle(),"x":x1, "y":150, "radius": 15, "image":"Gifs/treasure.gif", "type":"treasure"})
  for obj in game_objects:
    s.addshape(obj["image"])
    obj["t"].shape(obj["image"])  


  game_objects.append({"t": turtle.Turtle(),"x":0, "y":-150, "radius": 15, "image":"Gifs/swimmer.gif", "type":"swimmer"})
  for obj in game_objects:
    s.addshape(obj["image"])
    obj["t"].shape(obj["image"])  

  # sets scores variables
  score = -10
  score1 = 10
  score_count = 0
  lives = 7
  level = 0
  
  # writes variable score, lives, and level on screen
  t1.goto(-150,150)
  t1.write ('Score:' + str(score))
  t1.goto(105,150)
  t1.write('Lives:' + str(lives))
  t1.goto(-150,-150)
  t1.write('Level:' + str(level))

  # defines game state.
  game_state = "play"

  # sets up loop to begin game.
  while (game_state != "over"):
    # clear prior drawings    

    # loop through the game objects
    for obj in game_objects:
      obj["t"].clear()

    # updates x variable for each harm object
    for obj in game_objects:
      if (obj["type"] == "shark1"):
        obj["x"] += .28
      elif (obj["type"] == "shark2"):
        obj["x"] -= .09
      elif (obj["type"] == "shark3"):
        obj["x"] -= .29
      elif (obj["type"] == "shark4"):
        obj["x"] += .10

      # defines onkey events.
      for obj in game_objects:
        if (obj["type"] == "swimmer"):
          def up():
            obj['y'] += 20
          def left():
            obj['x'] -= 20
          def right():
            obj['x'] += 20
          def down():
            obj['y'] -= 20

      # connects defs to keys
      s.listen()
      s.onkey(up,'Up')
      s.onkey(left,'Left')
      s.onkey(right,'Right')
      s.onkey(down,'Down')
    

    # loop through the game objects and handle the edge condition
    for obj in game_objects:
      if (obj["type"] == "shark1") and obj['x'] > (w/2+obj['radius']) :
        obj['x'] = -w/1.4
      elif (obj["type"] == "shark2") and obj['x'] < (-w/2-obj['radius']):
        obj['x'] = w/1.4
      elif (obj["type"] == "shark3") and obj['x'] < (-w/2-obj['radius']):
        obj['x'] = w/1.4
      elif (obj["type"] == "shark4") and obj['x'] > (w/2+obj['radius']) :
        obj['x'] = -w/1.4
    
    # collision detection for harm objects. Determines whether swimmer(player) is touching shark(harm object) Also updates variables, writes updated variables on screen, and resets player to bottom lane. 
    for obj in game_objects:
      if obj['type'] != ['swimmer']:
        if obj['type'] == 'shark1' or obj['type'] == 'shark2' or obj['type'] == 'shark3' or obj['type'] == 'shark4':
          if (game_objects[5]['t'].distance(obj['t']) < 34):
            lives -= 1
            t1.clear()
            t1.goto(-150,150)
            t1.write ('Score:' + str(score))
            t1.goto(105,150)
            t1.write('Lives:' + str(lives))
            t1.goto(-150,-150)
            t1.write('Level:' + str(level))
            game_objects[5]['x']=0
            game_objects[5]['y']=-150
    
    # collision detection for treasure. Determines whether swimmer(player) is touching treasure(token to score) Also updates variables, writes updated variables on screen, resets player to bottom lane, and changes x position of treasure.
    for obj in game_objects:  
      if obj['type'] == 'treasure':
        if (game_objects[5]['t'].distance(obj['t']) <26):
          score_count += 1
          score += 10
          level += 1          
          t1.clear()
          t1.goto(-150,150)
          t1.write ('Score:' + str(score))
          t1.goto(105,150)
          t1.write('Lives:' + str(lives))
          t1.goto(-150,-150)
          t1.write('Level:' + str(level))
          game_objects[5]['x']=0
          game_objects[5]['y']=-150
          game_objects[4]['x']= random.randint(-75,75)
          # speed will increase if score is greater than last score
        if score_count > 1:
          for obj in game_objects:
            if (obj["type"] == "shark1"):
              obj["x"] += .23
            elif (obj["type"] == "shark2"):
              obj["x"] -= .42
            elif (obj["type"] == "shark3"):
              obj["x"] -= .29
            elif (obj["type"] == "shark4"):
              obj["x"] += .39
        if score_count > 2:
          for obj in game_objects:
            if (obj["type"] == "shark1"):
              obj["x"] += .1
            elif (obj["type"] == "shark2"):
              obj["x"] -= .22
            elif (obj["type"] == "shark3"):
              obj["x"] -= .23
            elif (obj["type"] == "shark4"):
              obj["x"] += .12
        if score_count > 4:
          for obj in game_objects:
            if (obj["type"] == "shark1"):
              obj["x"] += .12
            elif (obj["type"] == "shark2"):
              obj["x"] -= .32
            elif (obj["type"] == "shark3"):
              obj["x"] -= .29
            elif (obj["type"] == "shark4"):
              obj["x"] += .39        
        if score_count > 7:
          for obj in game_objects:
            if (obj["type"] == "shark1"):
              obj["x"] += .63
            elif (obj["type"] == "shark2"):
              obj["x"] -= .72
            elif (obj["type"] == "shark3"):
              obj["x"] -= .59
            elif (obj["type"] == "shark4"):
              obj["x"] += .69     
        if score_count > 10:
          for obj in game_objects:
            if (obj["type"] == "shark1"):
              obj["x"] += .89
            elif (obj["type"] == "shark2"):
              obj["x"] -= .72
            elif (obj["type"] == "shark3"):
              obj["x"] -= .59
            elif (obj["type"] == "shark4"):
              obj["x"] += .69  

    # if player loses all lives, the screen will clear and the end lose screen will load. 
    if lives == 0:
      game_state = 'over'
      s.clear()
      s.bgcolor('red')
      s.tracer(0)
      t1.goto(-104,50)
      t1.write('GAME OVER' + ' ', align='left', font=('Helvetica', 25))
      t1.goto(-88,0)
      t1.write('You made it to level' + ' ' + str(level), align='left', font=('Helvetica'))
      t1.goto(-60,-25)
      t1.write('Your score is' + ' ' + str(score), align='left', font=('Helvetica'))
      t1.goto(-87,-50)
      t1.write("Good try, play again!",  align='left', font=('Helvetica'))
      break

    # render
    for obj in game_objects:
      t = obj["t"]
      x = obj["x"]
      y = obj["y"]

      t.goto(x, y)

    s.update()


main()
