from flask import Flask
from pytrends.request import TrendReq
from io import BytesIO
import matplotlib.pyplot as plt
import os
import base64
import numpy as np
from timer_log import timed , count_dict, count_function,run_100times

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

@app.route('/countDict', methods=["GET"])
@timed
def countDict():
  method_dict = count_dict('t8.shakespeare.txt')
  return method_dict

@app.route('/countFunc', methods=["GET"])
@timed
def countFunc():
  method_func = count_function('t8.shakespeare.txt')
  return method_func


@app.route('/experiment', methods=["GET"])
#@timed
def experiment():
  dictionary , function = run_100times()

  dictionnary_mean = str("dictionnary mean : ",np.mean(dictionary))
  counter_mean= str("Function mean : ",np.mean(function))

  dictionnary_var = str("dictionnary variance : ",np.std(dictionary))
  counter_var= str("Function variance : ",np.std(function))

  x = np.linspace(0,100, 100)

  plt.plot(x, dictionary)
  plt.plot(x, function)

  plt.legend(["dictionnary", "fonction counter"], loc ="upper right")
  plt.xlabel('n times ')
  plt.ylabel('times')


  B = BytesIO()
  plt.savefig(B, format='png')
  B.seek(0)

  chart = base64.b64encode(B.getvalue()).decode()
  plt.clf()

  return dictionnary_mean,counter_mean,dictionnary_var,counter_var,'<img src="data:image/png;base64,{}">'.format(chart)


