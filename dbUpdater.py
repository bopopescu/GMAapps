from pkgapp import app,db
from pkgapp.models import Results

class DBUpdater:

    def updateResults(self,results_list):
        for result_dict in results_list:
            result=Results.query.filter_by(q_id=result_dict['q_id'],user_id=result_dict['user_id']).first()
            ch_selected=result_dict['Choice_sel']+","+str(result_dict['timeDelta'])
            if(result==None):
                new_result=Results(	user_id=result_dict['user_id'] ,q_id=result_dict['q_id'],	ans_selected=ch_selected,attempCount=1)
                db.session.add(new_result)
            else:
                old_result=result.ans_selected
                old_result+='|'+ch_selected
                result.ans_selected=old_result
                result.attempCount+=1
        db.session.commit()
