import threading

def print_number():
    for i in range(1,6):
        print("Thread 1:", i)

def print_letter():
    for letter in 'ABCDE':
        print("Thread 2:", letter)

Thread1 = threading.Thread(target=print_number())

Thread2 = threading.Thread(target=print_letter())

Thread1.start()

Thread2.start()

Thread1.join()

Thread2.join()
