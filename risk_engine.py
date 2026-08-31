
def calculate_risk(r):
    score=0
    if r['credit_score']<600: score+=40
    if r['debt']/max(r['income'],1)>0.4: score+=30
    if r['employment_years']<2: score+=20
    if score<30: return score,'APPROVE'
    elif score<60: return score,'MANUAL REVIEW'
    return score,'REJECT'
