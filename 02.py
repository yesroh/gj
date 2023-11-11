import streamlit as st
import pandas as pd
import folium
import numpy as np
from streamlit_folium import st_folium

tab1,tab2,tab3=st.tabs(['Projects','Description','Introduction'])

with tab1:
  df=pd.read_csv("gj.csv")
  df1=df.drop(['내용','등록자','시기','출처'],axis=1)
  df2=df.drop(['내용','등록자','시기','출처','인물'],axis=1)
  st.subheader('데이터 수집')
  st.text('1950~51년 사이의 전투 데이터 N개를 수집')
  st.dataframe(df1) #제목,지역,인물(df)

  battle_df=df2.groupby('지역').count().reset_index()
  battle_df.rename(columns={'제목':'격전횟수'},inplace=True)

  #st.dataframe(battle_df)#격전횟수 없는지역 추가X

  df2 = pd.DataFrame({'지역' : ['제주특별자치도','대전광역시','세종특별자치시','울산광역시','부산광역시'],'격전횟수':[0,0,0,0,0]}) #격전횟수 0인 지역 df에 추가

  battle_df=pd.concat([battle_df,df2],ignore_index=True)
  battle_df=battle_df.sort_values(by='격전횟수',ascending = True)
  st.subheader('지역별 격전 횟수')
  st.text('격전이 일어나지 않은 지역은 격전횟수 0으로 데이터프레임에 추가')
  st.dataframe(battle_df)#추가한 df


  st.bar_chart(battle_df,x='지역',y='격전횟수')

  map_geo = folium.Map(location=[35.5666,126.9784], zoom_start=7)
  #st_data=st_folium(map_geo,width=700, height=1000)#지도

  geo_json = 'TL_SCCO_CTPRVN.json'

#folium.GeoJson(geo_json).add_to(map_geo)

  folium.Choropleth(geo_data=geo_json,
                 data=battle_df,
                 columns=['지역','격전횟수'],
                 fill_color ='BuPu',
                 key_on = 'feature.properties.CTP_KOR_NM',
                 legend_name="격전횟수"
                 ).add_to(map_geo)
  st.subheader('지역별 격전 횟수 시각화')
  st_map=st_folium(map_geo,width=700, height=1000 )#시각화 지도

  #st.bar_chart(data=df,x='시기',y=['승','패'],color=['#ff0000','#0000ff']) df수정 후 실행해야함


with tab2:
  #6.25 전쟁을 주제로 포트폴리오를 만든 이유 설명 (~~~)
  st.title("6.25전쟁")
  st.text('''6.25전쟁은 제2차 세계대전이 끝난 직후 미국과 소련의 자유민주주의와 공산주의의 첫 번째 전쟁입니다.
6.25전쟁에서 기록되고 기록되지 않은 전쟁이 있겠지만 
가장 중요한 구국의 3대 전투에 대해 소개해 드리겠습니다.''')
  col1,col2 = st.columns([2,1])
  col1.subheader('다부동 전투')         
  col1.text('''6.25전투중 가장 치열했던 전투 중 하나로 꼽히는 다부동 전투입니다.
이 전투에서 패배를 하게되면 북의 통일이 되는 상황이기에 가장 중요한 전투였습니다.
또한 다부동 전투를 이끌던 백선엽 장군의 명언 "내가 후퇴하면 나를 쏴라"라는 말을 해 장병들의 사기를 돋았습니다.''')
  col2.image('다부동전투.jpeg')
  col1  ,col2 = st.columns([2,1])
  col1.subheader('인천상륙작전')
  col1.text('''맥아더 장군의 지휘하에 서울 탈환 작전의 밑거름이 되었고,
5000/1의 확률로 성공한 이 작전이 북한군과의 전세를 뒤바꾸는 중요한 전투였습니다.
또한 이 전투를 통해 38선을 넘어 북진을 하게 만드는 변곡점같은 전투였습니다.''')
  col2.image('인천상륙작전.jpeg')
  col1  ,col2 = st.columns([2,1]) 
  col1.subheader('장진호전투')
  col1.text('''북에서 펼쳐진 가장 큰 싸움으로 이 전투는 북한군이 한반도 북부로의 진군을 중단시키려는 시도와 
유엔군이 그 진군을 중지시키려는 시도 간의 충돌로 시작되었습니다.
유엔군이 중공군에 포위되어 격전을 벌여 승리하였고,이 전투를 기점으로 량걍도 지역까지 진출하는 계기가 되었으며
중공군과 북한군에 큰 피해를 입혔습니다.''')
  col2.image('장진호전투.jpeg')
  
  # 6.25 전쟁에 대해 조사해보면서 든 견해 ()
  # ex. 역사를 잊은 민족에게 미래는 없다라는 말과 같이 역사, 즉 인류 사회의 변천 데이터를 수집하여 
  # 미래에 어떻게 지혜롭고 현명하게 행동해야 하는지 결론을 도출해낼 수 있는 프로그래머 (데이터 분석가)가 되고 싶습니다.

with tab3:
  col1  ,col2 = st.columns([2,1])
  col1.subheader("프로그래머를 꿈꾸는 민경주입니다.")
  col1.text('''프로그래밍에 높은 관심을 가지고 있으며, 
AI와 SW기술에 많은 흥미를 가지고 있습니다.''')
  col1.text('''새로운 기술을 찾고 접목하여 
기존의 문제를 효과적으로 해결하는일을 좋아합니다. ''')
  col1.link_button('Go to my github',url='https://github.com/minkyungjoo08/-')
  col2.image("사진.jpg")

  st.divider() 

  col1, col2, col3 = st.columns(3)

  col1.metric("Name", "KyungJoo Min")
  col2.metric("Birth", "2008. 09. 14")
  col3.metric("Address", "Seoul, Korea")

  col1, col2, col3 = st.columns(3)

  col1.text("학교: 양정중학교 재학중")
  col2.text("E-Mail: minkyungjoo08@gmail.com")
  col3.text("Github: github.com/minkyungjoo08")
