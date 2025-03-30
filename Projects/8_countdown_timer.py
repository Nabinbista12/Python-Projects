import time

# **Countdown Timer** → Take input and countdown to zero.

def countdown_timer(sec):
    try:
        if sec > 0:
            while sec > 0:
                print(sec)
                sec -= 1
                time.sleep(1)

            print("Time is off")
        else:
            print("Enter positive integer")
    except Exception as e:
        print('Only positive interger are acceptable so enter postive number')
        print("Err:", e)

countdown_timer(10)
