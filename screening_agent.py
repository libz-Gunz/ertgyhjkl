
from agent.risk_engine import calculate_risk

class LoanScreeningAgent:
    def process(self, df):
        df = df.copy()
        scores=[]
        decisions=[]
        for _, r in df.iterrows():
            score, decision = calculate_risk(r)
            scores.append(score)
            decisions.append(decision)
        df["risk_score"]=scores
        df["decision"]=decisions
        return df
