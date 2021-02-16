import sys
clients = [
    {
        'name': 'pablo',
        'company': 'Google',
        'email': 'pablo@email.com',
        'position': 'Software engineer',
    },
    {
        'name': 'ricardo',
        'company': 'Facebook',
        'email': 'ricardo@email.com',
        'position': 'Data engineer',

    }

]
def create_client(client):
    global clients
    if client not in clients:  
        clients.append(client)
        
    else:
        print('Client already is in the client\'s list')


def list_clients():
    for idx, client in enumerate(clients):
        print('{uid}| {name} |{company}| {email}| {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position'] ))

def update_client(client_id):
    global clients  
    client_id = int(client_id)

    if client_id > len(clients):
        return
    
    client_to_update = clients[client_id]
    print(f'{client_id}: {client_to_update["name"]}')

    choise = input('Is the cliend do you want to Update? [y/n]')
    
    if choise == 'y':
        choise = input(f"client name: { client_to_update['name'] } \n Update name? [y/n]")
        if choise == 'y':
            client_to_update['name'] = _get_client_field('name')

        choise = input(f"client company: { client_to_update['company'] } \n Update company? [y/n]")
        if choise == 'y':
            client_to_update['company'] = _get_client_field('company')

        choise = input(f"client email: { client_to_update['email'] } \n Update email [y/n]")
        if choise == 'y':
            client_to_update['email'] = _get_client_field('email')

        choise = input(f"client position: { client_to_update['position'] } \n Update position [y/n]")
        if choise == 'y':

            client_to_update['position'] = _get_client_field('position')
    else:
        print('Client is not updated')


def delete_client(client_id):
    global clients
    client_id = int(client_id)

    if client_id > len(clients):
        return

    print(f'{client_id}: {clients[client_id]["name"]}')
    
    choise = input('Is the cliend do you want to delete? [y/n]')
    
    if choise == 'y':
        client_deleted = clients.pop(client_id)
        print(client_deleted)
    else:
        print('Client isnt in client list ')
def search_client(client_name):
    for client in clients:
        if client != client_name:
            continue
        else:
            return True 

def _get_client_field(field_name):
    field =None 
    while not field:
        field = input('what is the client {}?'.format(field_name))
    
    return field 

def _get_client_name():
    client_name= None
    while not client_name: 
        client_name= input('What is the client name? ' )
        if client_name=='exit':
            client_name = None
            break 

    if not client_name:
            sys.exit()

    return client_name


def _print_welcome():
    print('Welcome to Julio ventas :v')
    print('º'*50)
    print('what would you like to do today? ')
    print('[C]reate client')
    print('[L]ist client')
    print('[U]pdate client')
    print('[D]elete client ')
    print('[S]earch client')


if __name__=='__main__':
    _print_welcome()
    command=input()
    comand = command.upper()


    if command== 'C':
        client={
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
        create_client(client)
        list_clients()
    elif command=='L':
        list_clients()
    elif command == 'D':
        list_clients()
        id_client = input('What is the client ID do you want to Delete? ')
        delete_client(id_client)
        list_clients() 
    elif command =='U':
        list_clients()
        id_client = input('What is the client ID do you want to Update? ')
        update_client(id_client)
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print('The client is in clients list')
        else:
            print('The client {} is not in our clients list'.format(client_name))
    else:
        print('Invalid command')


    