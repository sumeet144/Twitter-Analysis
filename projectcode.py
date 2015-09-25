
# coding: utf-8

# In[2]:

import json, gzip, os.path

import pygal
import nltk
import pandas as pd
from collections import Counter
from bs4 import BeautifulSoup
from dateutil import parser
import datetime
import pytz
from pytz import timezone
import re    


# In[163]:

file = open("/home/sumeets/collection/bin/projfiles/dancemom_filtered.json","r")


# In[164]:

pytweets = []


# In[165]:

# Plot the most prolific tweeters


for line in file:
    jsn = json.loads(line)
    pytweets.append(jsn)
    
user_count = Counter()
for i in pytweets:
    user_count[ i['user']['screen_name'] ] += 1

barplot = pygal.HorizontalBar( style=pygal.style.SolidColorStyle, x_title='#Number of Tweets' )
topnum = 10
for i in range(topnum):
    barplot.add( user_count.most_common(topnum)[i][0],               [ { 'value': user_count.most_common(topnum)[i][1],                   'label':user_count.most_common(topnum)[i][0]} ] )
    
barplot.config.title = barplot.config.title= "Top " + str(topnum) + " Most Prolific Tweeters"
barplot.config.legend_at_bottom=True

barplot.render_to_file("Top_Tweeters.svg")
    


# In[13]:

# Most popular tweets
# Tweets with RT count > 10
count = Counter([i['text'] for i in pytweets])

frdf = []
for i,j in count.items():
    if j > 10:
        frdf.append([j, i])

df = pd.DataFrame(frdf, index=None, columns=["Count", "Tweet"])
df.sort(columns="Count", inplace=True, ascending=False)

for i,j,k in df.itertuples():
    d = str(j) + "\t" + str(k)
    with open('/home/sumeets/collection/bin/projfiles/populartweets.txt', mode='a', encoding='utf-8') as a_file:
                a_file.write(d)


# In[7]:

# Get the source field from each tweet
source = []
for i in pytweets:
    source.append(i['source'])

# Reduce the source and count
src=Counter(source)

# Convert the "Counter" container to Pandas dataframe for easy manipulation
frame = []
for i,j in src.items():
    soup = BeautifulSoup(i)
    frame.append( [j, soup.getText()])
sourcedf = pd.DataFrame(frame, columns=["COUNT", "SOURCE"])

# A lookup table to normalize the data in the containers we want
#   - all iOS Platforms (iPad, iPhone et. al. goes into iOS etc.)
sourcelookup = { "web": "Web",                              "Twitter for iPhone": "iOS",
                "Twitter for Android": "Android",           "TweetDeck": "TweetDeck",
                "Tweetbot for iOS": "iOS",                  "Twitter for iPad": "iOS",
                "Twitter for Mac": "Mac",                   "Tweetbot for Mac": "Mac",
                "Twitter for Android Tablets": "Android",   "Twitterrific": "iOS",
                "iOS": "iOS",                               u"Plume\xa0for\xa0Android": "Android",
                "YoruFukurou": "Mac",                       "TweetCaster for Android": "Android",
                "Guidebook on iOS": "iOS",                  "Twitter for Android": "Android",
                "UberSocial for iPhone": "iOS",             "Twitterrific for Mac": "Mac"
                }


# A helper function for looking up the table defined above
def translate(txt):
    try:
        return sourcelookup[txt]
    except KeyError:
        return "Other"

# Create a new column with normalized field
sourcedf['NSOURCE']=sourcedf.SOURCE.apply(lambda x: translate(x))

# Groupby the normalized field "NSOURCE"
grouped = sourcedf.groupby(by=["NSOURCE"])

# Create the chart (PieChart)
chart = pygal.Pie( style=pygal.style.SolidColorStyle )

for i in grouped.groups.items():
    chart.add( i[0], grouped.get_group(i[0]).COUNT.tolist() )

chart.config.title="Source of Tweets - Platform Share (in %age)"
chart.render_to_file('TwitterSource.svg')


# In[9]:

#Plot a Time series plot
datetweets = []
for line in file:
    jsn = json.loads(line)
    datetweets.append(jsn)
    
tweet_count = Counter()
tweet_dates = []

for i in pytweets:
    temp_date = parser.parse(i['created_at'])
    pst_date = temp_date.astimezone(timezone('America/Los_Angeles'))
    day_of_week = pst_date.strftime("%A")
    tweet_count[day_of_week] += 1
    #print temp_date , temp_date.strftime("%A")
    #tweet_dates.append(parser.parse(i['created_at']))
    #tweet_count[ i['created_at'] ] += 1

days_of_week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

line_chart = pygal.Line(y_title="#" +" of Tweets",x_title="Days of the week")
line_chart.title = "Tweets Time Series Plot" + "- Week" + " [28-Feb-2015 to 7-Mar-2015]"
line_chart.x_labels = map(str, days_of_week)

line_chart.add("Tweets",tweet_count)

line_chart.render_to_file("timeseries.svg")


# In[172]:

#Top keywords in the collection

for line in file:
    jsn = json.loads(line)
    pytweets.append(jsn)

excl_list = ['is','the','a','in','are','as','be','to','too','am','I','we','it','so','i','your', 'not',
        'rt','you','they','him','her','his','of','RT','I','and','on','my','for','me','that','she','he',
        'all','with',"I'm", 'at','this','have','but','from','&amp','The','up','do','was','IS','will','follow']         

user_count = Counter()
for i in pytweets:
    split_text = i['text'].split()
    for j in split_text:
        if j in excl_list:
            pass
        else:
            user_count[j] += 1
            #to generate tag clouds
            with open('/home/sumeets/collection/bin/projfiles/tag_cloud.txt', mode='a', encoding='utf-8') as a_file:
                s = re.sub("[^A-Za-z]", "", j) #remove spceial characters
                a_file.write(str(s) + "\t")            

#Plot top 10 keywords bar chart
barplot = pygal.Bar( style=pygal.style.SolidColorStyle,y_title="# of times repeated", x_title="Words within Tweet Text" )
topnum = 10
for i in range(topnum):
    barplot.add( user_count.most_common(topnum)[i][0],               [ { 'value': user_count.most_common(topnum)[i][1],                   'label':user_count.most_common(topnum)[i][0]} ] )
    #print(str(user_count.most_common(topnum)[i][0]) + ":" + str(user_count.most_common(topnum)[i][1]))
    
barplot.config.title = barplot.config.title= "Top " + str(topnum) + " Keywords"
barplot.config.legend_at_bottom=True

barplot.render_to_file("Top_Keywords.svg")


# In[113]:

#Stackbar chart for Name mentions and Handle mentions

stackedbar_chart = pygal.StackedBar(style=pygal.style.SolidColorStyle, x_label_rotation=50,legend_at_bottom=True, 
                                    x_title='Characters on the Show',y_title='# of mentions', label_font_size=12)
stackedbar_chart.title = 'Twitter Name Mentions versus Twitter Handle Mentions'
names = ["Abby","Holly","Nia","Melissa","Maddie","Mackenzie","Jill","Kendall","Kira",
         "Kalani","Cathy","Vivi","Christi","kelly","Sophia","Chloe"]
stackedbar_chart.x_labels = map(str, names)
stackedbar_chart.add('Name Mentions', [1279, 445, 1955, 127, 876, 184, 347, 225, 51, 242, 41, 6, 251, 44, 10, 509])
stackedbar_chart.add('Handle Mentions',  [2008, 2888, 2209, 1248, 2842, 1210, 416, 478, 152, 285, 33, None, 
                                                  1742, 207, 48, 211])
stackedbar_chart.render_to_file("Mentions.svg")


# In[77]:

import pandas as pd
from pandas.tseries.resample import TimeGrouper
from pandas.tseries.offsets import DateOffset
import vincent
import nltk
from nltk.corpus import stopwords
from nltk import FreqDist


# In[15]:

#Create hourly timeline for tweets
flyers = pd.read_csv('/home/sumeets/filter2.csv')
flyers['created_at'] = pd.to_datetime(pd.Series(flyers['created_at']))
flyers.set_index('created_at', drop=False, inplace=True)
flyers.index = flyers.index.tz_localize('GMT').tz_convert('America/Los_Angeles')
flyers.index = flyers.index - DateOffset(hours = 12)
flyers.index


# In[96]:

#half-hourly count of the tweets
flyers1m = flyers['created_at'].resample('60t', how='count')


# In[100]:

for line in flyers1m.keys():
    with open('/home/sumeets/count4.txt', mode='a', encoding='utf-8') as a_file:
                a_file.write(str(line)+ "\n")


# In[116]:

vincent.core.initialize_notebook()
area = vincent.Area(flyers1m)
area.colors(brew='Spectral')
area.display()


# In[138]:

#find frequency of the keywords
fighting = pd.read_csv('/home/sumeets/fighting.csv')
stop = ['is','the','a','in','are','as','be','to','too','am','I','we','it','so','i','your', 'not',
        'rt','you','they','him','her','his','of','RT','I','and','on','my','for','me','that','she','he' ]
text = fighting['Text']

tokens = []
for txt in text.values:
    tokens.extend([t.lower().strip(":,.") for t in txt.split()])

filter_tokens = [w for w in tokens if not w in stop]


# In[139]:

freq_fighting = nltk.FreqDist(filter_tokens)
freq_fighting


# In[148]:

#find frequency of the keywords
dancing = pd.read_csv('/home/sumeets/filter2.csv')
stop = ['is','the','a','in','are','as','be','to','too','am','I','we','it','so','i','your', 'not',
        'rt','you','they','him','her','his','of','RT','I','and','on','my','for','me','that','she','he' ]
text = dancing['text']

tokens = []
for txt in text.values:
    tokens.extend([t.lower().strip(":,.") for t in txt.split()])

filtered_tokens = [w for w in tokens if not w in stop]


# In[161]:

freq_dancing = nltk.FreqDist(filtered_tokens)
freq_dancing
for key in freq_dancing.fromkeys:
    print(key)
#with open('/home/sumeets/collection/tag_cloud.txt', mode='a', encoding='utf-8') as a_file:
                #s = re.sub("[^A-Za-z]", "", j) #remove spceial characters
 #               a_file.write(str(freq_dancing.values))


# In[142]:

flyers = pd.read_csv('/home/sumeets/filter2.csv')
flyers['created_at'] = pd.to_datetime(pd.Series(flyers['created_at']))
flyers.set_index('created_at', drop=False, inplace=True)
flyers.index = flyers.index.tz_localize('GMT').tz_convert('America/Los_Angeles')
flyers.index = flyers.index - DateOffset(hours = 12)
flyers.index


# In[147]:

#print(flyers['text'])
flyers1m = flyers['created_at'].resample('60t', how='count')


# In[145]:

flyers1m


# In[ ]:



