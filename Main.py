from datetime import datetime
import json


def numberToStatus(number):
    if number == 1:
        return 'todo'
    elif number == 2:
        return 'in-progress'
    elif number == 3:
        return 'done'

def valideitor(description,status):
    if (description and isinstance(description,str)) and status in [1,2,3]:
        return True
    return False

def idRequest():
    try:
        ids=int(input('inside the required ID'))
        return ids
    except:
        return idRequest()

def idCont():
    if tasks:
        return tasks[-1]['id']+1
    return 1


def addTask():
    id=idCont()
    description=input('A short description of the task: ')
    status=int(input('The status of the task (1-todo, 2-in-progress, 3-done) :'))
    createdAt= datetime.now().strftime("%d/%m/%Y %H:%M")
    updateAt=datetime.now().strftime("%d/%m/%Y %H:%M")
    vali=valideitor(description,status)
    if vali:
        status=numberToStatus(status)
        task={'id':id,
            'description':description,
            'status':status,
            'createdAt':createdAt,
            'updateAt':updateAt}
        tasks.append(task)

def updateTask():
    id=idRequest()
    for task in tasks:
        if task['id']== id:
            description=input('A short description of the task: ')
            status=int(input('The status of the task (1-todo, 2-in-progress, 3-done) :'))
            updateAt=datetime.now().strftime("%d/%m/%Y %H:%M")
            vali=valideitor(description,status)
            if vali:
                status=numberToStatus(status)
                task['description']=description
                task['status']=status
                task['updateAt']=updateAt

def deleteTask():
    id=idRequest()
    for i,task in enumerate(tasks):
        if task['id']== id:
            del tasks[i]

def alterStatusTask():
    id=idRequest()
    for task in tasks:
        if task['id']== id:
            status=int(input('The status of the task (2-in-progress, 3-done) :'))
            status=numberToStatus(status)
            task['status']=status

def listTaskAll():
    for task in tasks:
        print(task)
        print('='*50)

def listTaskTodo():
    for task in tasks:
        if task['status']== 'todo':
            print(task)

def listTaskInProgress():
    for task in tasks:
        if task['status']== 'in-progress':
            print(task)
            
def listTaskDone():
    for task in tasks:
        if task['status']== 'done':
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
        print("file is don't exist")
        save(task,path)
        return array


FILE_PATH='Task.json'
tasks=load([],FILE_PATH)


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
        '1':lambda:addTask(),
        '2':lambda:updateTask(),
        '3':lambda:deleteTask(),
        '4':lambda:alterStatusTask(),
        '5':lambda:listTaskAll(),
        '6':lambda:listTaskDone(),
        '7':lambda:listTaskTodo(),
        '8':lambda:listTaskInProgress()
    }

    try:
        commands=commands.get(option)
        commands()
    except TypeError:
        continue
    save(tasks,FILE_PATH)