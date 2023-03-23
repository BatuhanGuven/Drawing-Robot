from cgitb import enable
from distutils import text_file
from logging import root
from tkinter import *
from tkinter import filedialog
from turtle import Screen, TurtleScreen, width
import turtle
from tkinter import ttk, messagebox
from time import sleep, time
import ply.lex as lex
import ply.yacc as yacc
import turtle as t

t.Screen()
t.speed("slow")
liste = []

tokens = (
    'NUMBER',
    'LOOP',
    'PEN',
    'COLOR',
    'LEFT_PAREN',
    'RIGHT_PAREN',
    'ROTATE',
    'FORWARD',
    'BACKWARD',
    'COLOR_RED',
    'COLOR_BLUE',
    'COLOR_GREEN'
)

# Regular expression rules for simple tokens

t_LEFT_PAREN = r'\['
t_RIGHT_PAREN = r'\]'
t_LOOP = r'[L]'
t_COLOR = r'[C]'
t_ROTATE = r'[R]'
t_PEN = r'[P]'
t_FORWARD = r'[F]'
t_BACKWARD = r'[B]'
t_COLOR_RED = r'\bRED'
t_COLOR_BLUE = r'\bBLUE'
t_COLOR_GREEN = r'\bGREEN'

# t_COLOR = r'\[] '
# A regular expression rule with some action code

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)  ## skip, ignore or pass over the characters.

lexer = lex.lex()

#########################
# parser
#########################

def p_expr(p):
    '''
    expr : loop
         | frcp
    '''
    p[0] = p[1]


liste = []

def tuple_to_array(a):
    for b in a:
        if isinstance(b, tuple):
            tuple_to_array(b)
        else:
            if b != None:
                liste.append(b)
    return liste

def p_loop(p):
    '''           
    loop : LOOP NUMBER LEFT_PAREN  expr RIGHT_PAREN expr
    '''
    p[0] = p[1], p[2], p[4], p[6]

    exprs = (tuple_to_array(p[4])).copy()

    del liste[:]

    for x in range(0, p[2]-1):        ### number kadar expr yi tekrar et
        for expr in range(0, len(exprs)-1, 2):   ### tekrar işlemini exprin kaç elemanı varsa onların herbirine uygulayabilmek için yazıldı
            print(exprs[expr], exprs[expr+1]) ### şu an hangi kodun koşulduğunu bi
            if exprs[expr] == "F":
                t.forward(exprs[expr+1])
            if exprs[expr] == "R":
                t.right(exprs[expr+1])
            if exprs[expr] == "C":
                t.color(exprs[expr+1])
            if exprs[expr] == "P":
                t.pensize(exprs[expr+1])

def p_frcp(p):
    '''
    frcp : forward expr
         | backward expr
         | rotate expr
         | colorexp expr
         | pen expr
         | empty 
    '''
    if p[1] != None:
        if p[2] != None:
            p[0] = p[1], p[2]

        else:
            p[0] = p[1]


def p_rotate(p):
    '''
    rotate :  ROTATE NUMBER

    '''
    t.right(p[2])

    p[0] = p[1], p[2]
def p_backward(p):
    '''
    backward : BACKWARD NUMBER

    '''
    t.back(p[2])


def p_forward(p):
    '''
    forward :  FORWARD NUMBER

    '''
    p[0] = p[1], p[2]

    t.forward(p[2])

def p_pen(p):
    '''
    pen : PEN NUMBER 

    '''

    p[0] = p[1], p[2]

    t.pensize(p[2])

def p_color(p):
    '''
    colorexp : COLOR COLOR_RED
          | COLOR COLOR_BLUE
          | COLOR COLOR_GREEN
    '''
    p[0] = p[1], p[2]

    t.color(p[2])

def p_empty(p):
    '''
    empty : 

    '''
    p[0] = None

# Build the parser

def button_press(data):
	lexer = lex.lex()
	parser = yacc.yacc()
	yacc.yacc()
	yacc.parse(data)

root = Tk()
root.title('Drawing Robot Application')
root.geometry("1920x1080")

frame_sol = Frame(root, bg="#1d3d02")  # renk
frame_sol.place(relx=0.01, rely=0.01, relwidth=0.485, relheight=0.7)

frame_alt = Frame(root, bg="#ffffff")
frame_alt.place(relx=0.01, rely=0.72, relwidth=0.98, relheight=0.27)

canvas = Canvas(root,width=1000,height= 730)
canvas.grid(row=0,columnspan=6,pady=20,padx=950)

rawTurtleCanvas = turtle.RawTurtle(canvas)

def open_txt():
    text_file = filedialog.askopenfilename(
        initialdir="C:/", title="Open Text File", filetypes=(("Text Files", "*.txt"), ))
    name = text_file
    name = name.replace("C:/", "")
    name = name.replace(".txt", "")
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    button_press(stuff)
    my_text.insert(END, stuff)
    text_file.close()

text_scroll = Scrollbar(frame_sol)
text_scroll.pack(side=RIGHT, fill=Y)
my_text = Text(frame_sol, width=60, height=20, font=("Helvetica", 12), selectbackground="yellow",
               selectforeground="black", yscrollcommand=text_scroll.set, undo=True)
my_text.pack()


text_scroll.config(command=my_text.yview)
open_button = Button(frame_sol, text="Open Text File", command=open_txt)
open_button.pack(pady=20)

root.mainloop()