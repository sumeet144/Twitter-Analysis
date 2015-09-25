from mylistener import myListener
import tweepy
import traceback

consumer_key = 'PROVIDE YOUR KEY'
consumer_secret = 'PROVIDE YOUR KEY'

access_token = 'PROVIDE YOUR TOKEN'
access_secret = 'PROVIDE YOUR TOKEN'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def main():
    follow_list = ['@abby_lee_miller','@dancemomholly', '@realniasioux', '@dancemom1313', '@maddieziegler', 
                   '@mackzmusicinc', '@dancemomjill22', '@kk_vertes', '@kiragirard', '@23kalani', 
                   '@dancemomchristi', '@dancemomkelly', '@mssophialucia', '@DanceMoms']
    track_list = ['DanceMoms', 'dance moms', 'Abby Miller', 'dancemoms', 'hate dancing', 'love dancing', 'dancers',
                  'DanceMom', 'dance mom', 'dancemom', 'like watching dancemoms', 'like dancing', 'fighting', 
                  'fighting on dancemoms', 'hate dancemoms show', 'kill dancemoms','drama on dancemoms',
                  'hates abby', 'abusive show', 'little girls cry on show', 'abusive abby', 'rude show', 'awesome dance',
                  'awesome show', 'nasty woman', 'nasty show', 'screaming fights', 'nasty catfight on show', 'love catfight on dancemoms', 'love arguments on dancemoms']
    if follow_list:
        userid_list = []
        username_list = []

        for user in follow_list:
            if user.isdigit():
                userid_list.append(user)
            else:
                username_list.append(user)

        for username in username_list:
            user = api.get_user(username)
            user_id = '%s' %user.id
            userid_list.append(user_id)
        

        follow_list = userid_list
       
    else:
        follow_list = None
    #if track_list:
        #track_list = [k for k in track_list.split(',')]
        #print(track_list)
    #else:   
        #track_list = None

    print('Follow list: ', follow_list, 'Track keywords: ', track_list)
        
    
    listen = myListener(api, 'dancemom')
    stream = tweepy.Stream(auth, listen)
    
    print("Streaming Started")
    try:
        stream.filter(follow = follow_list, track = track_list)
    except:
        #pass
        print("error!")
        print(traceback.format_exc())
        stream.disconnect()
        
if __name__ == '__main__':
    main()