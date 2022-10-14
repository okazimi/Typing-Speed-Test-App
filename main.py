from tkinter import *
from timeit import default_timer as timer
from random_word import *

# GLOBAL VARIABLES
# INITIALIZE TKINTER HOME WINDOW
home_window = Tk()
# INITIALIZE LABEL TO DISPLAY EACH WORD
x2 = None
# INITIALIZE AND OBTAIN RANDOM WORD
r = RandomWords()
word = r.get_random_word()
# INITIALIZE NUMBER OF CORRECT WORDS TYPED
words_count = 0


def home_screen():
    # REFERENCE GLOBAL VARIABLE
    global home_window

    # SET SIZE OF WINDOW
    home_window.geometry("450x200")
    # SET WINDOW TITLE
    home_window.title("Home")

    # LABELS AND BUTTON TO BEGIN TEST
    x1 = Label(home_window, text="Welcome to the Speed Test", font="times 20")
    x1.place(x=70, y=50)
    x1 = Label(home_window, text="How fast can you correctly type 20 words?", font="times 14")
    x1.place(x=60, y=100)
    b1 = Button(home_window, text="Go", command=game, width=12, bg='white')
    b1.place(x=175, y=150)

    # RUN WINDOW
    home_window.mainloop()


# PYTHON TYPING SPEED TEST FUNCTION
def game():
    # REFERENCE GLOBAL VARIABLES
    global word, x2

    # INITIALIZE TKINTER TEST WINDOW
    test_window = Tk()
    # SET SIZE OF WINDOW
    test_window.geometry("450x200")
    # SET WINDOW TITLE
    test_window.title("Testing Window")

    # CREATE LABEL TO DISPLAY EACH WORD
    x2 = Label(test_window, text=word, font="times 20")

    # START TIMER
    start = timer()

    # FUNCTION FOR CHECKING USER INPUTS
    def check(event):
        # REFERENCE GLOBAL VARIABLES
        global home_window, word, words_count, x2

        # USER PROPERLY TYPED WORD
        if entry.get().lower() == word:
            # GET NEXT WORD
            word = r.get_random_word()
            # INCREMENT WORDS COUNT
            words_count += 1
            # UPDATE LABEL TEXT
            x2['text'] = word
            # CLEAR ENTRY BOX
            entry.delete(0, END)
        # USER DID NOT PROPERLY TYPE WORD
        elif entry.get().lower() != word:
            # GET NEXT WORD
            word = r.get_random_word()
            # UPDATE LABEL TEXT
            x2['text'] = word
            # CLEAR ENTRY BOX
            entry.delete(0, END)
        # CHECK IF USER HAS COMPLETED TEST
        if words_count == 3:
            # GET END TIME
            end = timer()
            # CREATE POP-UP WINDOW TO INFORM USER OF RESULTS
            pop = Toplevel(home_window)
            pop.geometry("400x200")
            pop.title("Test Results")
            Label(pop, text=f"Result: {end-start:.2f} seconds", font=('times 18')).place(x=100, y=90)
            # DESTROY TEST WINDOW
            test_window.destroy()
            # RESET WORD COUNT
            words_count = 0

    # CONFIGURE LABEL TO DISPLAY EACH WORD
    x2.place(x=160, y=20)
    # LABEL TO INFORM USER WHERE TO TYPE
    x3 = Label(test_window, text="Type Here 👉", font="times 18")
    x3.place(x=50, y=75)
    # ENTRY BOX FOR USER INPUT
    entry = Entry(test_window, width=30)
    entry.place(x=230, y=85)
    # BUTTON TO SUBMIT INPUT
    b2 = Button(test_window, text="Done", command=check, width=12, bg='grey')
    b2.place(x=180, y=150)
    # ENABLE USER TO SUBMIT ANSWER BY PRESSING ENTER
    test_window.bind('<Return>', check)

    # COMMAND TO RUN TKINTER WINDOW
    test_window.mainloop()


# START TEST
home_screen()
