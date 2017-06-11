# -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, escape, url_for, send_file
from lookup_longitude_latitude import get_img

app = Flask(__name__)



@app.route('/pick_city', methods=['POST'])
def do_search() -> 'html':
    """Extract the posted data; perform the search; return results."""
    city=request.form['city']
    title = '以下是您的结果：'
    results = get_img(city)
    return render_template('results.html',
                           the_title=title,
                           the_city=city,
                           the_results=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='广东省城市地图！')


# 这里我们接受一个 filename 檔名变量，http://127.0.0.1:5000/img/檔名
@app.route('/maps/<filename>')  # filename
def get_image(filename):        # filename
    # 傳送mimetype="image/"
    # 假定都是image/png格式
    import os.path
    
    return send_file(os.path.join("maps",filename), mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)
