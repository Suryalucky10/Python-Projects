class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
    def still_has_q(self):
        return self.question_number < len(self.question_list)

    def next_q(self):
        current_q=self.question_list[self.question_number]
        self.question_number+=1
        user_ans=input(f"Q.{self.question_number}){current_q.text}")
        self.check_ans(user_ans,current_q.answer)
    score=0
    def check_ans(self,user_ans,correct_ans):
        if user_ans.lower()==correct_ans.lower():
            print("you got it right.")
            self.score+=1
        else:
            print("That is wrong!")
        print(f"the correct answer is {correct_ans}")
        print(f"your current score is {self.score}/{self.question_number}.")
        print("\n"*5)
