# -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, escape
from weather_forecast import get_weather, get_form

app=Flask(__name__)

@app.route('/content', methods=['POST'])
def show_content() -> 'html':
    city = request.form['city']
    results = get_weather(city)
    return render_template('results.html',
                           the_title='查询结果',
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
                           #day 2
                          the_day_weather2 = results[27],
                           the_night_weather2 = results[28],
                           the_max2 = results[29],
                           the_min2 = results[30],
                           the_hum2 = results[31],
                           the_pop2 = results[32],
                           the_pcpn2 = results[33],
                           the_dir2 = results[34],
                           the_sc2 = results[35],
                           the_sun_rise2 = results[36],
                           the_sun_set2 = results[37],
                           #day 3
                           the_day_weather3 = results[38],
                           the_night_weather3 = results[39],
                           the_max3 = results[40],
                           the_min3 = results[41],
                           the_hum3 = results[42],
                           the_pop3 = results[43],
                           the_pcpn3 = results[44],
                           the_dir3 = results[45],
                           the_sc3 = results[46],
                           the_sun_rise3 = results[47],
                           the_sun_set3 = results[48],
                           #日期
                           the_date = results[49],
                           the_date2 = results[50],
                           the_date3 = results[51],
                           )

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_city_list = get_form(),
                           the_title='观测站')


if __name__ == '__main__':
    app.run(debug=True)
