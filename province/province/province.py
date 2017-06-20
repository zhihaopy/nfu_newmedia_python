from flask import Flask, render_template, request, escape
#from vsearch import search4letters

app = Flask(__name__)
    
#from pprint import pprint
import json
with open ('data/province_code_name.json') as fp:
    data = json.load(fp)
list_province=[v for k,v in data.items()]

def get_data():
	df=pd.DataFrame.from_csv("fsnd_data.tsv",encoding='utf8',sep='\t')
        


def log_request(req: 'flask_request', res: str) -> None:
    """Log details of the web request and the results."""
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


@app.route('/search_province', methods=['POST'])
def do_search() -> 'html':
    """Extract the posted data; perform the search; return results."""
    province = request.form['province']
    title = '以下是您的结果：'
    #results = str(search4letters(province))
    #log_request(request, results)
    return render_template('results.html',
                           the_title=title,
                           the_province=province)
                           #the_results=results,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='欢迎来到网上省份与互联网普及率搜索!',
						   the_user_province=list_province)
    


@app.route('/viewlog')
def view_the_log() -> 'html':
    """Display the contents of the log file as a HTML table."""
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')       
    return render_template('viewlog.html',
                           the_title='用户您获取了以下的数据：',
                           the_row_titles=titles,
                           the_data=contents,)


if __name__ == '__main__':
    app.run(debug=True)
