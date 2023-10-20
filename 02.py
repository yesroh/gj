import streamlit as st
import pandas as pd
import folium
import numpy 
from streamlit_folium import st_folium


df=pd.read_csv("gj.csv")
df1=df.drop(['내용','등록자','시기','출처'],axis=1)
df2=df.drop(['내용','등록자','시기','출처','인물'],axis=1)
st.dataframe(df1)



battle_df=df2.groupby('지역').count().reset_index()
battle_df.rename(columns={'제목':'격전횟수'},inplace=True)
battle_df=battle_df.sort_values(by='격전횟수',ascending = True)
st.dataframe(battle_df)

df2 = pd.DataFrame({'지역' : ['제주특별자치도','대전광역시','세종특별자치시','울산광역시','부산광역시'],'격전횟수':[0,0,0,0,0]}) #df수정가능성있음

battle_df=pd.concat([battle_df,df2],ignore_index=True)

st.dataframe(battle_df)

map_geo = folium.Map(location=[35.5666,126.9784], zoom_start=7)
st_data=st_folium(map_geo,width=700, height=1000)

geo_json = 'TL_SCCO_CTPRVN.json'

folium.GeoJson(geo_json).add_to(map_geo)

folium.Choropleth(geo_data=geo_json,
               data=battle_df,
               columns=['지역','격전횟수'],
               fill_color ='BuPu',
               key_on = 'feature.properties.CTP_KOR_NM',
               legend_name="격전횟수"
               ).add_to(map_geo)

st_map=st_folium(map_geo,width=700, height=1000 )
