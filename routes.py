from pkgapp import app
from flask import Flask,session,redirect
from flask import render_template
from flask import request
from pkgapp import Q_set_gen as qcg
from pkgapp.dbUpdater import DBUpdater
import time

@app.route('/')
@app.route('/index')
def index():
    session.clear()
    session['results']=[]
    session['user_id']=1
    return render_template('start.html')

@app.route('/start', methods=['GET', 'POST'])
def startpage():
    #session['results']=[]
    session['timer']=time.time()
    session['q_no']=1
    session['publisher']=request.form['Pub']
    session['book']=request.form['Book']
    session['total_q']=request.form['q_count']
    session['year']=request.form['Year']
    session['section']=request.form['Section']
    session['report']={}
    print("Year : {} | Section : {}".format(session['year'],session['section']))
    qcg_obj=qcg.QsetGenrator()
    session['q_list']=qcg_obj.create_test_set(session['publisher'],session['book'],session['year'],session['section'],session['total_q'])
    #session['set_no']=random.randint(1,len(session['q_list'])//session['total_q'])
    #session['q_set']=session['q_list'][(session['set_no']-1)*session['total_q']:session['set_no']*session['total_q']]
    #session['total_q_cset']=len(session['q_set'])
    image='a'#'og_'+session['year']+'_'+session['section']+'_'+session['q_list'][0].strip()+".GIF"
    print(len(session['q_list']))
    question=session['q_list'][0]
    #print(str(question))
    #return "Please Work" #str(question)
    return render_template('index.html',question=question,next_question='/question/1')

@app.route('/question/<int:q_no>', methods=['GET', 'POST'])
def question(q_no):
    if(q_no>len(session['q_list']) or q_no<0):
        return "Invalid Request"


    timeDelta=time.time()-session['timer']
    session['timer']=time.time()
    q_answered=request.form['prev_question']
    Choice_sel=request.form['Choice']
    result_dict={'q_id':session['q_list'][q_no-1]['id'],\
    'user_id':session['user_id'],\
    'Choice_sel':Choice_sel,\
    'timeDelta':timeDelta,\
    'q_no':q_answered,\
    'correct_ans':session['q_list'][q_no-1]['Correct_ans']
    }
    print(str(result_dict))
    results=session['results']
    results.append(result_dict)
    session['results']=results
    #print("Q :"+str(q_no)+" " +str(question))
    next_question='/index'
    if(len(session['q_list'])>q_no):
        next_question='/question/'+str(q_no+1)
        question=session['q_list'][q_no]
    elif(len(session['q_list'])==q_no):
        #Code for db commit
        print(len(session['results']))
        print("session['results'] :"+str(session['results']))
        dbu=DBUpdater()
        dbu.updateResults(session['results'])
        return render_template('report.html',report_dic=session['results'])
    else :
        next_question='/index'
    return render_template('index.html',question=question,next_question=next_question)


def objtodic(QBobject):
    QBdict={}
    for attr, value in QBobject.__dict__.items():
        QBdict[attr]= value

    return QBdict
