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
        print('{}: {}'.format(idx, client['name']))

def update_client(client_name, updated_client_name):
    global clients
    if client_name in clients:  
        index = clients.indes(client_name)
        clients[index]= updated_name
    else:
        print('Client is not in clients list')


def delete_client(client_name):
    global clients
    if client_name in clients:
        clients.remove(client_name)
    else:
        print('Client is not in clients list')
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
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients() 
    elif command =='U':
        client_name = _get_client_name()    
        updated_client_name= input('What is the update client name ')
        update_client(client_name, updated_client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print('The client is in clients list')
        else:
            print('The client {} is not in our clients list'.format(client_name))
    else:
        print('Invalid command')


    