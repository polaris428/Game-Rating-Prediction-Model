from turtle import st
import pandas as pd
import string

data = pd.read_csv('steam_games.csv',sep=',')
data = data[data['types'] == 'app']
data.drop(columns = ['url','types','name','recent_reviews','desc_snippet','publisher','game_description','minimum_requirements','recommended_requirements','popular_tags','discount_price'],inplace=True) 
#전처리를 시작


data["all_reviews"]=data["all_reviews"].str.extract(r'(\d+%)')
data["all_reviews"]=data["all_reviews"].astype('str').str.replace("%","")

original_price=data["all_reviews"].isin(["nan"])
data=data[~original_price]
data["original_price"]=data["original_price"].astype('str').str.replace("Free","$0")

data["original_price"]=data["original_price"].astype('str').str.replace("$","")

data["developer"]=data["developer"].astype('str').str.strip(string.punctuation)

data["languages"]=data["languages"].astype('str').str.split(",")


    


print("출력시작") 
  
print(data)
#파일로 저장
data.to_csv(
    path_or_buf = '전처리 완료후.csv',
  
)

