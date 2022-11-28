from flask import (
    Blueprint, render_template, redirect, url_for, jsonify,
    request, flash, session
)
from ..models import db, maths, science

quizz_bp = Blueprint(
    'quizz_bp',
    __name__
)


# Change the colour of question buttons and disable
def setStatus(qlist):
    qAttempt=[]
    strval=session['result'].strip()
    ans=strval.split(',')

    for i in range(int(len(ans)/2)):
        qAttempt.append(int(ans[2*i]))
    
    for rw in qlist:
        if rw.qid in qAttempt:
            rw.bcol='green'   # set color
            rw.status='disabled' # disable




@quizz_bp.route('/quizz', methods=['GET', 'POST'])
def quizz():
    subject= request.form.get('sub')
    if subject == 'Maths':
        questList=maths.query.filter_by(subject=subject).all()
        quest=maths.query.filter_by(subject=subject).first()
    else:
        questList=science.query.filter_by(subject=subject).all()
        quest=science.query.filter_by(subject=subject).first()
    return render_template("quizz/dashboard.html",questList=questList, quest=quest)

@quizz_bp.route('/showQuest/<string:subject>,<int:qid>')
def showQuest(subject,qid):
    if subject == 'Maths':
        questList=maths.query.filter_by(subject=subject).all()
        quest=maths.query.filter_by(qid=qid).first()
    else:
        questList=science.query.filter_by(subject=subject).all()
        quest=science.query.filter_by(qid=qid).first()
    setStatus(questList)
    return render_template("quizz/dashboard.html",questList=questList, quest=quest)

@quizz_bp.route('/saveAns', methods=['POST'])
def saveAns():
    qid=request.form.get('qid')
    ans=request.form.get('answer')
    sub=request.form.get('subject')
    #update the question id and its selected answer in session variable result
    res=session['result']
    res= res+qid+','+ans+','
    session['result']=res

    if sub == 'Maths':
        questList=maths.query.filter_by(subject=sub).all()
        quest=maths.query.filter_by(qid=qid).first()
    else:
        questList=science.query.filter_by(subject=sub).all()
        quest=science.query.filter_by(qid=qid).first()
    setStatus(questList)
    
    return render_template("quizz/dashboard.html",questList=questList, quest=quest)

@quizz_bp.route('/logout')
def logout():
    #calculate result
    count=0
    txt="" 
    strval=session['result'].strip()
    #split result string by ','
    ans=strval.split(',')
    for i in range(int(len(ans)/2)):
        qd=ans[2*i] # get question id
        qn=ans[2*i+1]  # get the sorresponding answer
        tt=int(qd)

        quest_science=science.query.filter_by(qid=tt).first()
        quest_maths=maths.query.filter_by(qid=tt).first()
        actans_maths=quest_maths.answer
        actans_science=quest_science.answer
        if (actans_maths==int(qn) or actans_science==int(qn)):#compare correct answer in questions table with answer chosen by user
            count=count+1 # increment counter
    txt=txt+'You have '+ str(count)+ ' correct questions out of '+ str(int(len(ans)/2))+ ' questions ' # set the result statement
    return render_template("quizz/result.html",txt=txt)




