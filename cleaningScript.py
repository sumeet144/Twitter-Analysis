
# coding: utf-8

# In[1]:

import simplejson


# In[73]:

f = open('/home/sumeets/collection/bin/projfiles/dancemom.json')

count = 0
for line in f:
    #count = count + 1
    #print('hi')
    tweet = simplejson.loads(line)
    #print(tweet)
    if  all (k in tweet for k in ('text','user')):
        tweet_line = tweet['text']
        tweet_user = tweet['user']['screen_name']
        #tweet_hashtag = tweet['entities']['hashtags'][0]['text']
        #tweet_media = tweet['entities']['media']
        #tweet_retweet = tweet['retweeted_status']['text']
        #print(tweet_retweet)
        if '@abby_lee_miller' in tweet_line.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif '@dancemomholly' in tweet_line.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif '@realniasioux' in tweet_line.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif '@dancemom1313' in tweet_line.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)  
        elif '@maddieziegler' in tweet_line.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif '@mackzmusicinc' in tweet_line.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)  
        elif '@dancemomjill22' in tweet_line.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif '@kk_vertes' in tweet_line.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif '@kiragirard' in tweet_line.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif '@23kalani' in tweet_line.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif '@dancemomchristi' in tweet_line.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif '@dancemomkelly' in tweet_line.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif '@mssophialucia' in tweet_line.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif '@DanceMoms' in tweet_line.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif 'DanceMoms' in tweet_line.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif 'dance moms' in tweet_line.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif 'Abby Miller' in tweet_line.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif 'dancemoms' in tweet_line.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif 'DanceMom' in tweet_line.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif 'dance mom' in tweet_line.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif 'dancemom' in tweet_line.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif 'abby_lee_miller' in tweet_user.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif 'dancemomholly' in tweet_user.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif 'realniasioux' in tweet_user.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif 'dancemom1313' in tweet_user.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif 'maddieziegler' in tweet_user.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif 'mackzmusicinc' in tweet_user.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif 'dancemomjill22' in tweet_user.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif 'kk_vertes' in tweet_user.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif 'kiragirard' in tweet_user.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif '23kalani' in tweet_user.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif 'dancemomchristi' in tweet_user.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif 'dancemomkelly' in tweet_user.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif 'mssophialucia' in tweet_user.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif 'DanceMoms' in tweet_user.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        #elif 'dancemoms' in tweet_retweet.lower():
        #    with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
        #        a_file.write(line)
        else:
            #print("blahh")
            with open('/home/sumeets/collection/bin/projfiles/discarded.json', mode='a', encoding='utf-8') as b_file:
                b_file.write(line)


# In[98]:

f = open('/home/sumeets/collection/bin/projfiles/next_f1.json')

for line in f:
    tweet = simplejson.loads(line)
    if 'retweeted_status' in tweet.keys():
        tweet_retweet = tweet['retweeted_status']['text']
        
        if 'dancemoms' in tweet_retweet.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif 'dancemom' in tweet_retweet.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif 'dance moms' in tweet_retweet.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif 'dance mom' in tweet_retweet.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        else:
            with open('/home/sumeets/collection/bin/projfiles/discarded.json', mode='a', encoding='utf-8') as b_file:
                b_file.write(line)
    else:
        with open('/home/sumeets/collection/bin/projfiles/discarded.json', mode='a', encoding='utf-8') as b_file:
            b_file.write(line)
            


# In[ ]:

f = open('/home/sumeets/collection/bin/projfiles/discarded_f1.json')

for line in f:
    tweet = simplejson.loads(line)
    if  'entities' in tweet.keys():
        tweet_media = tweet['entities']
        if 'media' in tweet_media:
        if 'dancemoms' in tweet_retweet.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif 'dancemom' in tweet_retweet.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif 'dance moms' in tweet_retweet.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
        elif 'dance mom' in tweet_retweet.lower():
            with open('/home/sumeets/collection/bin/projfiles/sample_output.json', mode='a', encoding='utf-8') as a_file:
                a_file.write(line)
    else:
        with open('/home/sumeets/collection/bin/projfiles/discarded.json', mode='a', encoding='utf-8') as b_file:
            b_file.write(line)
            

