import configparser
 
def read_config():

    config = configparser.ConfigParser()
    config.read(r'C:\Users\2donm\Desktop\project_directory\config.ini')

    db_name = config.get('Database', 'db_name')
    db_host = config.get('Database', 'db_host')
    db_port = config.get('Database', 'db_port')
    db_username = config.get('Database', 'db_username')
    db_password = config.get('Database', 'db_password')
 
    config_values = {
        'db_name': db_name,
        'db_host': db_host,
        'db_port': db_port,
        'db_username': db_username,
        'db_password': db_password
    }
 
    return config_values