import requests
from flask import Flask, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
from flask_caching import Cache 
#------------------------------------------------------------------------------------------------------------------------------
app = Flask(__name__)
#------------------------------------------------------------------------------------------------------------------------------
#configurations :
app.config['CACHE_TYPE'] = 'simple'
#------------------------------------------------------------------------------------------------------------------------------
#registrations :
app.cache = Cache(app)
CORS(app)
#------------------------------------------------------------------------------------------------------------------------------
#routes :

"""
 method : GET
 parameters :
 returns : a JSON Containing the events of today
"""
@app.route('/')
@app.cache.cached(timeout=300, key_prefix="tosayevents")
def todayEvents():
    #making the request to time.ir and parse it as HTML
    soup = BeautifulSoup(requests.get('https://www.time.ir/').content,'html.parser')
    List = [] 
    #extracting the events
    divs = soup.select("div.eventsCurrentMonthWrapper li")
    for item in divs :
        #note that we only care about the events which filtered through applying the mask
        if(mask(item.contents[1].contents[0].split(' '),'today')):
            List.append({
                'title':sanitizer(item.contents[1].contents[0].replace('\r\n','').strip()),
                'description':sanitizer(item.contents[2].replace("\r\n","").strip())
            })
    return jsonify({'todayEvnents':List})
"""
 method : GET
 parameters :
 returns : a JSON Containing the events of this week
"""
@app.route('/this_week')
@app.cache.cached(timeout=300, key_prefix="thisweekevents")
def thisWeekEvents():
    soup = BeautifulSoup(requests.get('https://www.time.ir/').content,'html.parser')
    List = [] 
    divs = soup.select("div.eventsCurrentMonthWrapper li")
    for item in divs :
        if(mask(item.contents[1].contents[0].split(' '),'this_week')):
            List.append({
                'title':sanitizer(item.contents[1].contents[0].replace('\r\n','').strip()),
                'description':sanitizer(item.contents[2].replace("\r\n","").strip())
            })
    return jsonify({'thisweekEvents':List})
"""
 method : GET
 parameters :
 returns : a JSON Containing the events of this month
"""
@app.route('/this_month')
@app.cache.cached(timeout=300, key_prefix="thismonthevents")
def thisMonthEvents():
    soup = BeautifulSoup(requests.get('https://www.time.ir/').content,'html.parser')
    List = [] 
    divs = soup.select("div.eventsCurrentMonthWrapper li")
    for item in divs :
        if(mask(item.contents[1].contents[0].split(' '),'this_month')):
            List.append({
                'title':sanitizer(item.contents[1].contents[0].replace('\r\n','').strip()),
                'description':sanitizer(item.contents[2].replace("\r\n","").strip())
            })
    return jsonify({'thismonthEvents':List})
#------------------------------------------------------------------------------------------------------------------------------
"""
    Inputs : data (array), condition (string)
    Outputs : True / False (Boolean)
    -*- this function will test whether the condition is met over the input data 
"""
def mask(data,condition):
    _today = today()
    if(condition =='today'):
        if(data[0]== _today[0] and data[1] == _today[1]):
            return True
        else:
            return False
    if(condition == 'this_week'):
        week = this_week(_today[0])
        #if(int(unidecode(data[0]))>= week[0] or int(unidecode(data[0]))<=week[1]):
        if(int(data[0])>= week[0] and int(data[0])<=week[1]):
            return True
        else:
            return False
    else:
        if(data[1]==_today[1]):
            return True
        else:
            return False
#------------------------------------------------------------------------------------------------------------------------------
"""
    Inputs : 
    Outputs : date (array)
    -*- this function will return today date as D M Y
"""
def today():
    soup = BeautifulSoup(requests.get('http://www.time.ir/').content,'html.parser')
    data = soup.select('#ctl00_cphTop_Sampa_Web_View_TimeUI_ShowDate00cphTop_3734_lblShamsi')[0].contents[0].split('-')[1].strip().split(' ')
    return data
#------------------------------------------------------------------------------------------------------------------------------
"""
    Inputs : date
    Outputs : (week_starts_on, week_ends_on) (touple)
    -*- this function will return the start and end dates of the current week.
    -> needs to improve
"""
def this_week(date):
    soup = BeautifulSoup(requests.get('http://www.time.ir/').content,'html.parser')
    data = soup.select('#ctl00_cphTop_Sampa_Web_View_TimeUI_ShowDate00cphTop_3734_lblShamsi')[0].contents[0].split('-')
    DOW = day_of_the_week(data[0])
    week_starts_on = int(data[1].strip().split(' ')[0]) - int(DOW)
    week_ends_on   = int(data[1].strip().split(' ')[0]) + ( 7 - DOW )
    return (week_starts_on, week_ends_on)
#------------------------------------------------------------------------------------------------------------------------------
"""
    Inputs : day_name
    Outputs : day_number (integer)
    -*- this function will return day of the week number.
"""
def day_of_the_week(day_name):
    if day_name.strip() == u'شنبه':
        return 1
    if day_name.strip() == u'یکشنبه':
        return 2
    if day_name.strip() == u'دو شنبه':
        return 3
    if day_name.strip() == u'سه شنبه':
        return 4
    if day_name.strip() == u'چهارشنبه':
        return 5
    if day_name.strip() == u'پنج شنبه':
        return 6
    if day_name.strip() == u'جمعه':
        return 7
#------------------------------------------------------------------------------------------------------------------------------
"""
    Inputs : unicoded_string
    Outputs : sanitized_string (string)
    -*- this function will return the decoded version of its input.
    -> needs improve
"""
def sanitizer(unicoded_string):
    umap = {
        '\u0621':'ء',
        '\u0623':'أ',
        '\u0626':'ئ',
        '\u0624':'ؤ',
        '\u0627':'ا',
        '\u0628':'ب',
        '\u067E':'پ',
        '\u062A':'ت',
        '\u062B':'ث',
        '\u062C':'ج',
        '\u0686':'چ',
        '\u062D':'ح',
        '\u062E':'خ',
        '\u062F':'د',
        '\u0630':'ذ',
        '\u0631':'ر',
        '\u0632':'ز',
        '\u0698':'ژ',
        '\u0633':'س',
        '\u0634':'ش',
        '\u0635':'ص',
        '\u0636':'ض',
        '\u0637':'ط',
        '\u0638':'ظ',
        '\u0639':'ع',
        '\u063A':'غ',
        '\u0641':'ف',
        '\u0642':'ق',
        '\u06A9':'ک',
        '\u06AF':'گ',
        '\u0644':'ل',
        '\u0645':'م',
        '\u0646':'ن',
        '\u0648':'و',
        '\u0647':'ه',
        '\u06CC':'ی',
    }
    for k in umap:
        unicoded_string = unicoded_string.replace(k,umap[k])
    return unicoded_string
#------------------------------------------------------------------------------------------------------------------------------
#bootstrapping the application
if __name__ == '__main__':
    app.run(port=5000,debug=True)