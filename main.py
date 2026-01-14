#Version 1.0
#14/01/2026
#Vinicius Camparini Siqueira

from datetime import datetime
import json
import sys

def numberToStatus(number):
    if number == 1:
        return 'todo'
    elif number == 2:
        return 'in-progress'
    elif number == 3:
        return 'done'
    return 'unknown'


def valideitor(description,status):
    return description.strip() and isinstance(description,str) and status in [1,2,3]

def idValideitor(taskID):
    return taskID>0



def idCont(tasks):
    if tasks:
        return tasks[-1]['taskID']+1
    return 1


def addTaskInput(tasks):
    try:
        description=input('A short description of the task: ')
        status=int(input('The status of the task (1-todo, 2-in-progress, 3-done) :'))
    except ValueError:
        print('Data entered incorrectly (number description status(1-all, 2-in-progress, 3-done))')
        return
    if valideitor(description,status):
        addTask(tasks,description,status)
        return
    print('The information provided is incorrect')

def addTaskArgv(tasks,descri,stt):
    if valideitor(descri,stt):
        addTask(tasks,descri,stt)
        return
    print('The information provided is incorrect')

def addTask(tasks,descri,stt):
    status=numberToStatus(stt)
    task={'taskID':idCont(tasks),
        'description':descri,
        'status':status,
        'createdAt':datetime.now().strftime("%d/%m/%Y %H:%M"),
        'updateAt':datetime.now().strftime("%d/%m/%Y %H:%M")}
    tasks.append(task)

def updateTaskInput(tasks):
    try:
        taskID=int(input('Insert the required ID: '))
        description=input('A short description of the task: ')
        status=int(input('The status of the task (1-todo, 2-in-progress, 3-done) :'))
    except ValueError:
        print('Data entered incorrectly (number description status(1-all, 2-in-progress, 3-done))')
        return
    if (idValideitor(taskID) and valideitor(description,status)):
        updateTask(tasks,taskID,description,status)
        return
    print('The information provided is incorrect')

def updateTaskArgv(tasks,taskID,descri,stt):
    if (idValideitor(taskID) and valideitor(descri,stt)):
        updateTask(tasks,taskID,descri,stt)
        return
    print('The information provided is incorrect')


def updateTask(tasks,taskID,descri,stt):
    for task in tasks:
        if task['taskID']== taskID:
            status=numberToStatus(stt)
            task['description']=descri
            task['status']=status
            task['updateAt']=datetime.now().strftime("%d/%m/%Y %H:%M")
            print(f"Task updated successfully (ID: {taskID})")
            return
    print("The ID does not exist")

def deleteTaskInput(tasks):
    try:
        taskID=int(input('Insert the required ID: '))
    except ValueError:
        print('ID must be a number')
        return
    if idValideitor(taskID) :
        deleteTask(tasks,taskID)
        return
    print('The information provided is incorrect')


def deleteTaskArgv(tasks,taskID):
    if idValideitor(taskID):
        deleteTask(tasks,taskID)
        return
    print('The information provided is incorrect')

def deleteTask(tasks,taskID):
    for i,task in enumerate(tasks):
        if task['taskID']== taskID:
            del tasks[i]
            print(f"Task deleted successfully (ID: {taskID})")
            return
    print("The ID does not exist")

def alterStatusTaskInput(tasks):
    try:
        taskID=int(input('Insert the required ID: '))
        status=int(input('The status of the task (2-in-progress, 3-done) :'))
    except ValueError:
        print('ID must be a number')
        return
    if idValideitor(taskID) and status in [1,2,3]:
        alterStatusTask(tasks,taskID,status)
        return
    print('The information provided is incorrect')

def alterStatusTaskArgv(tasks,taskID,stt):
    if idValideitor(taskID) and stt in [1,2,3]:
        alterStatusTask(tasks,taskID,stt)
        return
    print('The information provided is incorrect')


def alterStatusTask(tasks,taskID,stt):
    for task in tasks:
        if task['taskID']== taskID:
            status=numberToStatus(stt)
            task['status']=status
            print(f"Task alter status successfully (ID: {taskID})")
            return
    print("The ID does not exist")

def listTask(tasks,status):
    for task in tasks:
        if status == 'all' or task['status']== status:
            print(task)

def save(task,path):
    with open (path,'w',encoding='utf-8') as arquivo:
        json.dump(task,arquivo,indent=2,ensure_ascii=False)

def load(task,path):
    array=[]
    try:
        with open (path,'r', encoding='utf-8') as file:
            array=json.load(file)
        return array
    except FileNotFoundError:
        print('ile does not exist')
        save(task,path)
        return array


FILE_PATH='Task.json'
tasks=load([],FILE_PATH)

if len(sys.argv)<2:
    print('You can do it using positional arguments.')
    print('python main.py <action> [argument]')
else:

    command=sys.argv[1]

    if command == 'add':
        try:
            addTaskArgv(tasks,sys.argv[2],int(sys.argv[3]))
            sys.exit()
        except ValueError:
            print('Data entered incorrectly (number description status(1-all, 2-in-progress, 3-done))')
        sys.exit()

    if command == 'update':
        try:
            updateTaskArgv(tasks,int(sys.argv[2]),sys.argv[3],int(sys.argv[4]))
            sys.exit()
        except ValueError:
            print('Data entered incorrectly (number description status(1-all, 2-in-progress, 3-done))')

    if command == 'delete':
        try:
            deleteTaskArgv(tasks,int(sys.argv[2]))
            sys.exit()
        except ValueError:
            print('ID must be a number')
    
    if command == 'alterstatus':
        try:
            alterStatusTaskArgv(tasks,int(sys.argv[2]),int(sys.argv[3]))
            sys.exit()
        except ValueError:
            print('ID and status must be numbers')
        except IndexError:
            print('You must provide ID and status (2-in-progress, 3-done)')
            
    if command == 'list':
        try:
            listTask(tasks,sys.argv[2])
            sys.exit()
        except IndexError:
            print('Please specify which status you would like (all, todo, in-progress, done)')
        
while True:
    print('1 - Add')
    print('2 - Update')
    print('3 - delete')
    print('4 - Mark a task as in progress or done')
    print('5 - list all')
    print('6 - List all tasks that are done')
    print('7 - List all tasks that are not done')
    print('8 - List all tasks that are in progress')
    option=input('Choose between 1-8: ')

    commands={
        '1':lambda:addTaskInput(tasks),
        '2':lambda:updateTaskInput(tasks),
        '3':lambda:deleteTaskInput(tasks),
        '4':lambda:alterStatusTaskInput(tasks),
        '5':lambda:listTask(tasks,'all'),
        '6':lambda:listTask(tasks,'done'),
        '7':lambda:listTask(tasks,'todo'),
        '8':lambda:listTask(tasks,'in-progress')
    }

    try:
        commands=commands.get(option)
        commands()
    except TypeError:
        continue
    save(tasks,FILE_PATH)