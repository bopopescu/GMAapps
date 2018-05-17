from pkgapp import app,db
from pkgapp.models import QuestionBank as qb
from random import shuffle
class QsetGenrator:

    def create_test_set(self,publisher,book,year,section,q_count):
        q_list=[]
        print("{} {} {} {} {} ".format(publisher,book,year,section,q_count))
        all_Qs = qb.query.filter_by(Publisher=publisher ,\
        Book = book,\
        Year = year,\
        Section = section\
        ).all()
        for q in all_Qs :
            a_dict={}
            a_dict['q_text']=q.q_text
            a_dict['id']=q.id
            a_dict['q_no']=q.q_no
            a_dict['A']=q.A
            a_dict['B']=q.B
            a_dict['C']=q.C
            a_dict['D']=q.D
            a_dict['E']=q.E
            a_dict['Correct_ans']=q.Correct_ans
            q_list.append(a_dict)
            shuffle(q_list)
        #print("Inside Q_set gen- q_lits is :"+str(q_list))
        return q_list[:int(q_count)]
