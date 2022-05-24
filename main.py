from turtle import st
import pandas as pd
import string
import re   
data = pd.read_csv('steam_games.csv',sep=',')
data = data[data['types'] == 'app']
data.drop(columns = ['url','types','name','recent_reviews','desc_snippet','publisher','game_description','minimum_requirements','recommended_requirements','popular_tags','discount_price'],inplace=True) 
#전처리를 시작

data["all_reviews"]=data["all_reviews"].str.extract(r'(\d+%)')
data["all_reviews"]=data["all_reviews"].astype('str').str.replace("%","")

#nan이 들어있는 값 삭세
data=data[data.original_price!="nan"]
data=data[data.all_reviews!="nan"]
#original_price 전처리
data["original_price"]=data["original_price"].astype('str').str.replace("Free","$0")
data["original_price"]=data["original_price"].astype('str').str.replace("0 To Play ","$0")
data["original_price"]=data["original_price"].astype('str').str.replace("$","")
#developer 전처리
data["developer"]=data["developer"].astype('str').str.strip(string.punctuation)
#languages 전처리
data["languages"]=data["languages"].astype('str').str.split(",")


print("출력시작") 
  
print(data)
#파일로 저장
data.to_csv(
    path_or_buf = '전처리 완료후.csv',
  
)

