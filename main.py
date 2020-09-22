import requests,random,re
from flask import Flask ,render_template,request

app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def home():
	import requests,random,re
	main_list={"all":"https://api.atik.cf/inshorts/all",
				"national":"https://api.atik.cf/inshorts/national",
				"business":"https://api.atik.cf/inshorts/business",
				"sports":"https://api.atik.cf/inshorts/sports",
				"world":"https://api.atik.cf/inshorts/world",
				"politics":"https://api.atik.cf/inshorts/politics",
				"technology":"https://api.atik.cf/inshorts/technology",
				"startup":"https://api.atik.cf/inshorts/startup",
				"entertainment":"https://api.atik.cf/inshorts/entertainment",
				"science":"https://api.atik.cf/inshorts/science",
				"automobile":"https://api.atik.cf/inshorts/automobile"}
	tag=['all', 'national', 'buisness', 'sports', 'world', 'politics', 'technology', 'startup', 'entertainment',
	     'science', 'automobile']
	main_list_selection=random.choice([i for i in range(0,11)])
	url=main_list[tag[main_list_selection]]
	data=requests.get(url).json()
	news_selection=random.choice([i for i in range(0,len(data['articles']))])
	news=data['articles'][news_selection]
	# news['title']=re.sub(' +', ' ', news['title'])[1:-1:1]
	news['tag']=tag[main_list_selection]
	return render_template('index.html',news=news)
