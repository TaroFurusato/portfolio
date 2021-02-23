from portfolio import db
from datetime import datetime

class Skil( db.Model):
    __tablename__ = 'entries' 
    id = db.Column( db.Integer, primary_key = True) 
    
    s_date = db.Column(db.DateTime, nullable=False) # 実績期間
    e_date = db.Column(db.DateTime) # 実績期間
    project = db.Column(db.String(100), nullable=False)  # 案件
    category = db.Column( db.Integer, nullable=False)  # カテゴリ
    os = db.Column( db.Integer, nullable=False) # OS
    skil = db.Column(db.String(100), nullable=False) # スキル
    
    def __init__( self, s_date = None, project = None, category = None, os = None, skil = None, e_date = None ): 
        self.s_date = s_date 
        self.e_date = e_date 
        self.project = project 
        self.category = category
        self.os = os
        self.skil = skil

    def __repr__( self): 
        return '<Entry id:{} s_date:{} project:{} category:{} os:{} skil:{} e_date:{}>'. format( self.id, self.s_date, self.project, self.category, self.os, self.skil, self.e_date)


