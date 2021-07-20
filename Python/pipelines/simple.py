import os


def do_ping(arg):
    return f'Pong, {arg}'


def do_ls(arg):
    return '\n'.join(os.listdir(arg))


dispatch = {
    'ping': do_ping,
    'ls': do_ls
}

def process_network_command(command, arg):
    print(dispatch[command](arg))

# process_network_command('key', 'value')
process_network_command('ping', '0.0.0.0')
process_network_command('ls', 'C:\\Users\\about\\Documents\\Estudos\\Python\\pipelines')