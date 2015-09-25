from tweepy import StreamListener
import simplejson
import datetime

class myListener(StreamListener):
    def __init__(self, api = None, fprefix = 'streamer'):
        self.api = api or API()
        self.counter = 0
        self.fprefix = fprefix
        self.output = open(fprefix + '.' + 'json', 'a')
        self.delout = open('delete.txt', 'a')

    def on_data(self, data):
        if 'in_reply_to_status' in data:
            self.on_status(data)
        elif 'delete' in data:
            delete = json.loads(data)['delete']['status']
            if self.on_delete(delete['id'], delete['userid']) is False:
                return False
        elif 'limit' in data:
            if self.on_limit(json.loads(data)['limit']['track']) is False:
                return False
        elif 'warning' in data:
            warning = json.loads(data)['warnings']
            print(warning['message'])
            return False
    
    def on_status(self,status):
        self.output.write(status)
        self.counter += 1
        #print(self.counter)
        if self.counter == 1000:
            self.counter = 0
            with open("healthck.txt", mode='a') as file:
                file.write('Printed string recorded at %s. \n' %(datetime.datetime.now()))
        return  
    
    def on_delete(self, status_id, user_id):
        self.delout.write( str(status_id) + "\n")
        return
    def on_limit(self, track):
        sys.stderr.write('Error: ' +str(status_code) + "\n")
        return False
    def on_error(self, status_code):
        print('An error has occured! Status code = %s' % status_code)
        return True  # keep stream alive
    def on_timeout(self):
        sys.stderr.write("Timeout\n")
        time.sleep(60)
        return
    
        
            
     
