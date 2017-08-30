#ConfigParser Module
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
print('Sections in the INI File:',config.sections())
print(config['bitbucket.org']['User'])
print(config['DEFAULT']['Compression'])
topsecret=config['topsecret.server.com']
print(topsecret['ForwardX11'])
print(topsecret['Port'])
