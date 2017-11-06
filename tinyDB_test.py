import configparser
import datetime
#user name and pass from a config.ini
class db_User:
    def access():
        config = configparser.ConfigParser()
        config.read('config.ini')
        config.sections()
        for key in config['DEFAULT']: 
            print(key)

    def __init__(self,config):
        self.config = config

#tracks time
class db_timer:
    def track_time():
        dt = datetime.datetime.now()
        current_date = str(dt.month)+"-"+str(dt.day)+"-"+str(dt.year)
        current_time = str(dt.hour)+"."+str(dt.minute)+"."+str((dt.second)

        #print(current_date)
        print(current_time)

def main():
    db_timer.track_time()
    db_User.access()


if __name__ == "__main__":
    main()
