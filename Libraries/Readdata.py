import configparser

def data1(section, key):
    config=configparser.ConfigParser()
    config.read("C:/Users/User/PycharmProjects/giyhubpr/Configuration/Basics.cfg")
    return config.get(section, key)
#print(data1('info', 'Browser'))


def data2(section, key):
    config=configparser.ConfigParser()
    config.read("C:/Users/User/PycharmProjects/giyhubpr/Configuration/Elements.cfg")
    return config.get(section, key)
#print(data2('info2', 'username'))
