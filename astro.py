{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'1-20': '水瓶座',\n",
       " '10-24': '天蝎座',\n",
       " '11-23': '射手座',\n",
       " '12-22': '摩羯座',\n",
       " '2-19': '双鱼座',\n",
       " '3-21': '白羊座',\n",
       " '4-20': '金牛座',\n",
       " '5-21': '双子座',\n",
       " '6-22': '巨蟹座',\n",
       " '7-23': '狮子座',\n",
       " '8-23': '处女座',\n",
       " '9-23': '天秤座'}"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "astro_dates_start={x['date'].split('~')[0]:x['astroname'] for x in data['result']}\n",
    "astro_dates_start"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{datetime.datetime(1900, 1, 20, 0, 0): '水瓶座',\n",
       " datetime.datetime(1900, 2, 19, 0, 0): '双鱼座',\n",
       " datetime.datetime(1900, 3, 21, 0, 0): '白羊座',\n",
       " datetime.datetime(1900, 4, 20, 0, 0): '金牛座',\n",
       " datetime.datetime(1900, 5, 21, 0, 0): '双子座',\n",
       " datetime.datetime(1900, 6, 22, 0, 0): '巨蟹座',\n",
       " datetime.datetime(1900, 7, 23, 0, 0): '狮子座',\n",
       " datetime.datetime(1900, 8, 23, 0, 0): '处女座',\n",
       " datetime.datetime(1900, 9, 23, 0, 0): '天秤座',\n",
       " datetime.datetime(1900, 10, 24, 0, 0): '天蝎座',\n",
       " datetime.datetime(1900, 11, 23, 0, 0): '射手座',\n",
       " datetime.datetime(1900, 12, 22, 0, 0): '摩羯座'}"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "start_date_2_astro = {datetime.strptime(k, '%m-%d'):v for k,v in astro_dates_start.items()}\n",
    "start_date_2_astro"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[datetime.datetime(1900, 1, 20, 0, 0),\n",
       " datetime.datetime(1900, 2, 19, 0, 0),\n",
       " datetime.datetime(1900, 3, 21, 0, 0),\n",
       " datetime.datetime(1900, 4, 20, 0, 0),\n",
       " datetime.datetime(1900, 5, 21, 0, 0),\n",
       " datetime.datetime(1900, 6, 22, 0, 0),\n",
       " datetime.datetime(1900, 7, 23, 0, 0),\n",
       " datetime.datetime(1900, 8, 23, 0, 0),\n",
       " datetime.datetime(1900, 9, 23, 0, 0),\n",
       " datetime.datetime(1900, 10, 24, 0, 0),\n",
       " datetime.datetime(1900, 11, 23, 0, 0),\n",
       " datetime.datetime(1900, 12, 22, 0, 0)]"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "start_dates = sorted(list(start_date_2_astro.keys()))\n",
    "start_dates"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "from datetime import datetime\n",
    "def find_astro(month, day):\n",
    "    user_input = datetime.strptime('{m}-{d}'.format(m=month, d=day), '%m-%d')\n",
    "    return (start_date_2_astro[ start_dates[len([ user_input>=x for x in start_dates if (user_input>=x) == True])-1] ])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
