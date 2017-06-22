from input_data import get_dict_ename,change_name,get_dict_hero
from flask import Flask, render_template, request, escape

dict_ename = get_dict_ename()
list_name = list()
for ename in dict_ename:
    list_name.append(dict_ename[ename]['cname'])
    list_name.append(dict_ename[ename]['title'])
    
app = Flask(__name__)

@app.route('/')
@app.route('/entry')

def entry_page() -> 'html':
    output_prompt = '请输入你想要搜索的英雄名'
    return render_template('entry.html',
                           the_output_prompt=output_prompt,
                           the_list_name = list_name,
                           the_entry_title='英雄联盟英雄技能信息')


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    hero_name = request.form['input_hero_name']
    output_prompt_error = '请输入正确的英雄名或称号，如“盖伦”，“德玛西亚之力”'
    dict_hero = get_dict_hero(hero_name)
    if 'error' in dict_hero:
        return render_template('entry.html',
                               the_entry_title='英雄联盟英雄技能信息',
                               the_output_prompt_error=output_prompt_error,
                               )
    else:
        dict_ename = get_dict_ename()
        hero_ename = change_name(hero_name)
        return render_template('results.html',
                               the_title=dict_ename[hero_ename]['title'],
                               the_cname=dict_ename[hero_ename]['cname'],
                               output_vidio = dict_hero['data'][0]['skins'][0]['source'],
                               output_skill_passive_name = dict_hero['data'][0]['passive']['name'],
                               output_skill_passive_description = dict_hero['data'][0]['passive']['description'],
                               output_skill_1_name = dict_hero['data'][0]['spells'][0]['name'],
                               output_skill_1_tooltip = dict_hero['data'][0]['spells'][0]['tooltip'],
                               output_skill_2_name = dict_hero['data'][0]['spells'][1]['name'],
                               output_skill_2_tooltip = dict_hero['data'][0]['spells'][1]['tooltip'],
                               output_skill_3_name = dict_hero['data'][0]['spells'][2]['name'],
                               output_skill_3_tooltip = dict_hero['data'][0]['spells'][2]['tooltip'],
                               output_skill_4_name = dict_hero['data'][0]['spells'][3]['name'],
                               output_skill_4_tooltip = dict_hero['data'][0]['spells'][3]['tooltip'],
                               )


if __name__ == '__main__':
    app.run(debug=True)

