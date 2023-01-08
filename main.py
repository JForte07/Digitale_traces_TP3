from flask import Flask
from pytrends.request import TrendReq
from io import BytesIO
import matplotlib.pyplot as plt
import os
import base64
from timer_log import timed

app = Flask(__name__)

@app.route('/', methods=["GET"])
@timed
def google_trend():
    pytrends = TrendReq(hl='en-US', tz=360)
    # set the keyword & timeframe
    pytrends.build_payload(["Taylor Swift"], timeframe="all")
    # get the interest over time
    iot = pytrends.interest_over_time() 
    #related_queries = pytrends.related_queries()
    #v = related_queries.values()

    #  trend comparison time serie with a chart 
    plt.plot(iot['Taylor Swift'])
    plt.xlabel('Date')
    plt.ylabel('Trend')

    
    B = BytesIO()
    plt.savefig(B, format='png')
    B.seek(0)

    chart = base64.b64encode(B.getvalue()).decode()
    plt.clf()

    return '<img src="data:image/png;base64,{}">'.format(chart)



