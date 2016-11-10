"""
Copyright [2016] [Nicholas Tran - nicholastran2000 at yahoo dot com]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""
"""

Input triangle, circle, or square to output a design using right, left
and forward with the shapes inputed above.

"""

import turtle

def draw_square(some_turtle):
    for i in range(0,4):
        some_turtle.forward(100)
        some_turtle.right(90)

        
def draw_circle(draw_circ):
    draw_circ.circle(100)

def draw_triangle(draw_tri):
    draw_tri.right(180)
    count = 0
    while (count < 2):
        draw_tri.forward(100)
        draw_tri.left(90)
        count = count + 1
    draw_tri.left(45)
    draw_tri.forward(141.4)

def draw_art():
    shape = input('Enter triangle, square, or cicle: ')
    
    window = turtle.Screen()
    window.bgcolor("red")
    
    if shape == 'square':
        sqr = turtle.Turtle()
        sqr.shape("turtle")
        sqr.color("blue")
        sqr.speed(20)
        for i in range(0,36):
            draw_square(sqr)
            sqr.right(10)
    else:
        if shape == 'circle':
            circ = turtle.Turtle()
            circ.shape("arrow")
            circ.color("blue")
            circ.speed(20)
            for i in range(0, 36):
                draw_circle(circ)
                circ.right(10)
        else:
            if shape == 'triangle':
               tri = turtle.Turtle()
               tri.shape("classic")
               tri.color("green")
               tri.speed(20)
               for i in range(0, 36):   
                   draw_triangle(tri)
                   tri.right(10)
            else:
                window.exit()

    window.exitonclick()

draw_art();
    
