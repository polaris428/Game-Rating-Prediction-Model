from turtle import st
import pandas as pd

data = pd.read_csv('steam_games.csv',sep=',')
data = data[data['types'] == 'app']
data.drop(columns = ['url','types','name','recent_reviews','desc_snippet','publisher','game_description','minimum_requirements','recommended_requirements','popular_tags','discount_price'],inplace=True) 
#전처리를
data["original_price"]=data["original_price"].astype('str').str.replace("Free","$0")

data["original_price"]=data["original_price"].astype('str').str.replace("$","")
print("출력시작") 
  
print(data)
#파일로 저장
data.to_csv(
    path_or_buf = '전처리 완료후.csv',
  
)

