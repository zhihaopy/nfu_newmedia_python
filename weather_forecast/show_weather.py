 # -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, escape
from weather_forecast import get_weather

app = Flask(__name__)

@app.route('/content', methods=['POST'])
def show_content() -> 'html':
    city = request.form['city']
    results = get_weather(city)
    return render_template('results.html',
                           the_results=results,
                           the_city = city,
                           the_lat = results[1],
                           the_lon = results[2],
                           the_day_weather = results[3],
                           the_night_weather = results[4],
                           the_max = results[5],
                           the_min = results[6],
                           the_hum = results[7],
                           the_pop = results[8],
                           the_pcpn = results[9],
                           the_dir = results[10],
                           the_sc = results[11],
                           the_sun_rise = results[12],
                           the_sun_set = results[13],
                           the_comf = results[14],
                           the_comf_details = results[15],
                           the_drsg = results[16],
                           the_drsg_details = results[17],
                           the_flu = results[18],
                           the_flu_details = results[19],
                           the_sport = results[20],
                           the_sport_details = results[21],
                           the_trav = results[22],
                           the_trav_details = results[23],
                           the_uv = results[24],
                           the_uv_details = results[25],
                           the_update = results[26],

                           )

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='观测站')


if __name__ == '__main__':
    app.run(debug=True)
