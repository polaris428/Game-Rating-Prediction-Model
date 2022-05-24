from turtle import st
import pandas as pd

data = pd.read_csv('steam_games.csv',sep=',')
data = data[data['types'] == 'app']
data.drop(columns = ['url','types','name','recent_reviews','desc_snippet','publisher','game_description','minimum_requirements','recommended_requirements','popular_tags','discount_price'],inplace=True) 
print("출력시작") 

print(data)

