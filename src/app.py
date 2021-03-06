import json
from DataStructures import Queue
from sms import send

lista = []
# there queue has to be declared globally (outside any other function)
# that way all methods have access to it
queue = Queue(mode="LIFO",current_queue= lista)
    
def print_queue():
    # you must print on the console the entire queue list
    print("Printing the entire list...")
    print(queue.get_queue())

def add(nombre):
    queue.enqueue(nombre)
    x = queue.size() - 1
    send(nombre + ' tienes '+ str(x) + ' personas por delante')
    pass 

def dequeue():
    send(queue.dequeue() + ' Ven a comer')
    pass

def save():
    file = open('lista.json','w+')
    file.write(json.dumps(queue.get_queue()))
    file.close()
    pass

def load(ruta):
    with open(ruta) as contenido:
        resultado = json.load(contenido)
        queue._queue = resultado
    print(resultado)
    pass 
        
    
print("\nHello, this is the Command Line Interface for a Queue Managment application.")
stop = False
while stop == False:
    
    print('''
What would you like to do (type a number and press Enter)?
- Type 1: For adding someone to the Queue.
- Type 2: For removing someone from the Queue.
- Type 3: For printing the current Queue state.
- Type 4: To export the queue to the queue.json file.
- Type 5: To import the queue from the queue.json file.
- Type 6: To quit
    ''')

    option = int(input("Enter a number:"))
    # add your options here using conditionals (if)
    if option == 3:
        print_queue()
    elif option == 1:
        print('Coloque su nombre')
        nombre = input()
        add(nombre)    
    elif option ==2:
        dequeue()
    elif option ==4:
        save()
    elif option ==5:
        ruta = 'lista.json'
        load(ruta)
    elif option == 6:
        print("Bye bye!")
        stop = True
    else:
        print("Not implemented yet or invalid option "+str(option))
