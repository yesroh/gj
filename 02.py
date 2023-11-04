'''
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
'''


import streamlit as st
import pandas as pd
import folium
import numpy 
from streamlit_folium import st_folium

with tab1:
  col1  ,col2 = st.columns([2,1])

  col1.subhead("프로그래머를 꿈꾸는 민경주입니다.")
  col1.text('''프로그래밍에 높은 관심을 가지고 있으며,
AI와 SW기술에 많은 흥미를 가지고 있습니다.
      ''')
  col1.text('''새로운 기술을 찾고 접목하여 기존의
문제를 효과적으로 해결하는일을 좋아합니다. ''')

  col1.write("""<a href="https://minkyungjoo.streamlit.app/""")

  col2.image("학생증")

  st.divider()

  col1, col2, col3 = st.columns(3)

  col1.metric("Name", "KyungJoo Min")
  col2.metric("Birth", "2008. 09. 14")
  col3.metric("Address", "Seoul, Korea")

  col1, col2, col3 = st.columns(3)

  col1.text("학교: 양정중학교 재학중")
  col2.text("E-Mail: minkyungjoo08@gmail.com")
  col3.text("Github: github.com/minkyungjoo08")

with tab2
  col1  ,col2 = st.columns([2,1)]

  col1.subhead("6.25전쟁")
  col1.text('''우리 민족이 겪은 분단의 고통과 슬픔에 대해 잘 알아야 될 필요가 있다고 생각합니다.''')
  col1.text('''새로운 기술을 찾고 접목하여 기존의
문제를 효과적으로 해결하는일을 좋아합니다. ''')
with tab3:
  df=pd.read_csv("gj.csv")
  df1=df.drop(['내용','등록자','시기','출처'],axis=1)
  df2=df.drop(['내용','등록자','시기','출처','인물'],axis=1)
  st.dataframe(df1) #제목,지역,인물(df)




  battle_df=df2.groupby('지역').count().reset_index()
  battle_df.rename(columns={'제목':'격전횟수'},inplace=True)
  battle_df=battle_df.sort_values(by='격전횟수',ascending = True)
  st.dataframe(battle_df)#격전횟수 없는지역 추가X

  df2 = pd.DataFrame({'지역' : ['제주특별자치도','대전광역시','세종특별자치시','울산광역시','부산광역시'],'격전횟수':[0,0,0,0,0]}) #df수정가능성있음

  battle_df=pd.concat([battle_df,df2],ignore_index=True)

  st.dataframe(battle_df)#추가한것

  map_geo = folium.Map(location=[35.5666,126.9784], zoom_start=7)
  st_data=st_folium(map_geo,width=700, height=1000)#지도

  geo_json = 'TL_SCCO_CTPRVN (2).json'

#folium.GeoJson(geo_json).add_to(map_geo)

  folium.Choropleth(geo_data=geo_json,
                 data=battle_df,
                 columns=['지역','격전횟수'],
                 fill_color ='BuPu',
                 key_on = 'feature.properties.CTP_KOR_NM',
                 legend_name="격전횟수"
                 ).add_to(map_geo)

  st_map=st_folium(map_geo,width=700, height=1000 )#시각화 지도
