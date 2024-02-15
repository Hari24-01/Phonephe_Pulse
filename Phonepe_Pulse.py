#Importing the necessary libraries
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
import streamlit as st
from sqlalchemy import create_engine
import pandas as pd
import plotly as py
import plotly.express as px
from streamlit_option_menu import option_menu
from PIL import Image
import mysql.connector as sql
from sklearn import preprocessing
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 



# SETTING PAGE CONFIGURATIONS
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
icon = Image.open(r"C:\Users\hsqua\Desktop\phonepe\Decorative\Splash-Icon.JPG")

st.set_page_config(page_title= "PHONEPE PULSE ANALYSIS | By J HARI HARAN",
                   page_icon= icon,
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                   menu_items={'About': """# This app is created by *J HARI HARAN*"""})
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 

# CREATING OPTION MENU
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
select=option_menu(menu_title=None,options=["HOME","VISUAL"],
                   icons=["house","bar-chart-steps"],
                   default_index=0,
                   orientation="horizontal",
                   styles={"container":{"background-color":"voliet","size":"cover","width":"100%"},
                   "icon": {"color":"black","font-size":"50px"},
                   "nav-link": {"font-size":"50px","text-align":"center","margin":"-2px","--hover-color":"#FFA732"},
                   "nav-link-selected":{"background-color":"#A459D1"}})     
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++       
        

# APPLYING BACKGROUND
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-color: #6C22A6;
opacity: 0.9;
background-image: radial-gradient(circle at center center, #ffffff, #96E9C6), repeating-radial-gradient(circle at center center, #ffffff, #ffffff, 13px, transparent 26px, transparent 13px);
background-blend-mode: multiply;
}}

</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)   
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 

# CONNECTING WITH MYSQL DATABASE
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
Host="localhost"
User="root"
Port=3306
Password=""
Database= "phonepe_pulse"

mydb = sql.connect(host=Host,
                   user=User,
                   port=Port,
                   password=Password,
                   database=Database #SELECT DATABASE FROM SQL SERVER
                  )
connection = create_engine(f"mysql+pymysql://{User}:{Password}@{Host}:{Port}/{Database}")
mycursor = mydb.cursor(buffered=True)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 



#TRANSFER DATA FROM SQL SERVER AS PANDAS DATAFRAME
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    
#agg_user
query = 'SELECT * FROM agg_user'
df=pd.read_sql(query,con=connection)
#____________________________________________________________________________________________
#agg_trans
query1 = 'SELECT * FROM agg_trans'
df1=pd.read_sql(query1,con=connection)
#____________________________________________________________________________________________
#map_tran
query2 = 'SELECT * FROM map_tran'
df2=pd.read_sql(query2,con=connection)
#____________________________________________________________________________________________
#map_user
query3 = 'SELECT * FROM map_user'
df3=pd.read_sql(query3,con=connection)
#____________________________________________________________________________________________
#top_tran
query4 = 'SELECT * FROM top_tran'
df4=pd.read_sql(query4,con=connection)
#____________________________________________________________________________________________
#top_user
query5 = 'SELECT * FROM top_user'
df5=pd.read_sql(query5,con=connection)
#____________________________________________________________________________________________
#india_states_longitude
query6 = 'SELECT * FROM india_states_longitude'
df6=pd.read_sql(query6,con=connection)
#____________________________________________________________________________________________
#state_longitude_latitude	
query7 = 'SELECT * FROM state_longitude_latitude'
df7=pd.read_sql(query7,con=connection)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



#HOME PAGE
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
if select == "HOME":
    title_link = '[PhonePe Pulse 2018-2023](https://github.com/Hari24-01/Phonephe_Pulse.git)'
    st.write(f'# :blue[₹{title_link} :chart_with_upwards_trend:]')
    col1,col2,col3 = st.columns(3,gap= 'medium')
    col1.markdown("### :orange[Domain :]  Fintech")
    col1.markdown("#### :orange[Technologies used :]  Github Cloning, Python, Pandas, MySQL,mysql-connector-python, Streamlit, and Plotly.")
    col1.markdown("#### :orange[Overview :]  To display data and insights in an engaging and aesthetically pleasing way from the Phonepe Pulse Github repository." )
    col2.markdown("#   ")
    col2.markdown("#   ")
    col2.write("#### This data is scraped from the refernce link below :arrow_down:")
    col2.link_button(":blue[Phonepe]","https://www.phonepe.com/pulse/explore/insurance/2023/3/") 
    col2.markdown("#   ")
    col3.markdown("#   ")
    col3.markdown("#   ")
    col3.markdown("![Alt Text](https://miro.medium.com/v2/resize:fit:640/1*E8Ys7gfVryzMjtpYy9Z6gw.gif)")
    
    #SAMPLE GRAPH
    st.subheader(":orange[Top 10 Transaction States]")
    df4=df4.sort_values(by="Transaction_Count")
    result = df4.groupby('States').first().reset_index()
    result_1=result.nlargest(10,'Transaction_Count')
    fig = px.bar(result_1,
                     x=result_1['Transaction_Count'],
                     y=result_1['States'],
                     orientation='h',
                     color=result_1['States']
                    )
    number=int(result["Transaction_Amount"].sum())
    
    total=f"₹{number}"
    st.plotly_chart(fig,use_container_width=True) 
    col1,col2,col3 = st.columns(3,gap= 'medium')
    col1.markdown("### :orange[The above shown Graph is just a model about this of webapp ]   ")
    col1.markdown("##### Select 'VISUAL' menu to know more about the Data.   ")
    with col2:
        st.video("https://github.com/Hari24-01/Phonephe_Pulse/assets/128268647/7ca9ebe5-1885-4228-a42d-e3e081ebe6c0")
    
    with col3:
        st.markdown("### Total amount according to the Graph")
        container=st.container()
        container.markdown(f"### :orange[Amount : :green[{total}]]")
        
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
    

# VISUAL PAGE
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
if select == "VISUAL":
    with st.sidebar:
            selected_1 = option_menu("GRAPH", ["Line-chart","Bar-Chart","Pie-Chart","Map"],
                           
                           icons=["graph-up-arrow","bar-chart-line-fill","pie-chart-fill","map"],
                           default_index=0,
                           orientation="vertical",
                           styles={"container":{"background-color":"black"},"nav-link": {"font-size": "20px", "text-align": "centre", "margin": "0px", 
                                                "--hover-color": "#FFA732"},
                                   "icon": {"color":"black","font-size": "30px"},
                                   "nav-link-selected": {"background-color": "#A459D1"}})  
            
#_______________________________________________________________________________________________    
#MAP PLOT


    if selected_1 == "Map" :
        st.header(":blue[Map Plot]")

        
        df9 = df6.sort_values(by='District')
        df9 = df9.reset_index(drop=True)
        
        df8 = df4.copy()
        
        df8 = df8.groupby(['States','District']).agg({'Transaction_Amount': 'sum','Transaction_Count':'sum'})
        df8["Transaction_Count"]=df8["Transaction_Count"]%100
        df8 = df8.reset_index()
        

        districts_final = pd.merge(df8,df9,
                           how='inner', on=['States','District'])
        
        st.subheader(":orange[Transaction Count of each States]")
        fig_map=px.scatter_geo(districts_final,lat='latitude',lon='longitude',size='Transaction_Count',
                           projection='equirectangular',scope='asia',title='Indian Transaction Percent',
                           color='Transaction_Count',opacity=0.5,size_max=30,color_continuous_scale='Viridis')
        

        fig_map.update_layout(height=650,
                              width=1080,
                              geo=dict(
                                  center=dict(lon=78,lat=22),
                                  projection_scale=2.5,
                                  visible=True),
                               mapbox=dict(style="streets")   
                                  )
        
        fig_map.update_geos(showcoastlines=True,coastlinecolor="black")
        fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

        st.plotly_chart(fig_map)
#_______________________________________________________________________________________________
#BAR PLOT
        

    if selected_1 == "Bar-Chart" :
        st.header(":blue[Bar Chart]")
        bar1=df4.copy()

        st.subheader(":orange[Maximum & Minimum Transaction of each States]")

        result = bar1.groupby(["States"])["Transaction_Count"].max()
        result1=bar1.groupby(["States"])["Transaction_Count"].min()
        result = result.reset_index()
        result=result.nlargest(10,'Transaction_Count')
        result1 = result1.reset_index()
        result1=result1.nsmallest(10,'Transaction_Count')
        
        

        fig_bar = px.bar(result, y=result['Transaction_Count'], x=result['States'], text_auto='.2s',
        title="Maximum Transaction According To Each State",color=result['States'],height=800,width=600)
        fig_bar.update_traces(textfont_size=12, textangle=0, textposition="inside", cliponaxis=False)
        st.plotly_chart(fig_bar,use_container_width=True)
        
        fig_sac = px.bar(result1, y=result1['Transaction_Count'], x=result1['States'], text_auto='.2s',
        title="Minimum Transaction According To Each State",color=result1["States"],height=800,width=600)
        fig_sac.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
        st.plotly_chart(fig_sac,use_container_width=True)

#_______________________________________________________________________________________________
#LINE PLOT
        

    if selected_1 == "Line-chart":
        title_html = '''
            <h1 style="text-align: center; color: blue;">
            <a href="https://github.com/Hari24-01/Phonephe_Pulse.git" target="_blank" rel="noopener noreferrer" style="text-decoration: none; color: orange;">
            ₹PhonePe Pulse 2018-2023 Analysis
            </a>
            </h1>
            '''
        st.markdown(title_html, unsafe_allow_html=True)

        st.header(":orange[Line Chart]") 
        st.subheader("Transaction Done By Different Quarters & Type")
        Quarter = st.radio(
                    "##### :grey[Select Quarter]",
                    ["Q1", "Q2", "Q3","Q4"],
                    index=0,horizontal=True
                    )
        
        Type = st.selectbox(
            "##### :grey[Select Transaction_Type]",
            options=["Merchant payments", "Peer-to-peer payments", "Recharge & bill payments", "Financial Services", "Others"],
            index=0)
        
            
        if Quarter == "Q1":
            quar=1
        elif Quarter == "Q2":
            quar=2     
        elif Quarter == "Q3":
            quar=3   
        elif Quarter == "Q4":
            quar=4 
            
        lin1=df.copy()

        lin1_quar=lin1[ lin1["Quarters"].isin([quar])]
        lin1_quar=lin1_quar[ lin1_quar["Transaction_Type"].isin([Type])]
        # lin1_quar=lin1_quar[ lin1_quar["States"].isin([State])]
        lin1_quar = lin1_quar.sort_values(['States','Transaction_Amount'])
        fig_line = px.line(lin1_quar, x=lin1_quar["States"], y=lin1_quar["Transaction_Amount"],line_group=lin1_quar["Transaction_Year"],
                            color=lin1_quar["States"], markers=True)
        fig_line.update_layout(xaxis_title='Amount', yaxis_title='States')      
        st.plotly_chart(fig_line,use_container_width=True)


        st.subheader(" Percentage of Yearly Transaction of all the State")
        Avg=df.copy()
        Avg = Avg.sort_values(['States'])

        state = st.selectbox(
            "##### :orange[Select State]",
            options=["madhya-pradesh","ladakh","jammu-&-kashmir","andhra-pradesh","jharkhand"
                    "assam","meghalaya","haryana","himachal-pradesh","punjab","karnataka","mizoram",
                    "nagaland","west-bengal","tamil-nadu","chhattisgarh","puducherry","tripura","bihar",
                    "rajasthan","sikkim","odisha","goa","uttar-pradesh","lakshadweep","gujarat","dadra-&-nagar-haveli-&-daman-&-diu",
                    "chandigarh","delhi","arunachal-pradesh","kerala","andaman-&-nicobar-islands","telangana","maharashtra",
                    "uttarakhand","manipur"],
            index=0)

        le = preprocessing.LabelEncoder()
        cols = ["States","Transaction_Type"]

        Avg[cols] = Avg[cols].apply(le.fit_transform)
        result = Avg.groupby(["States", "Transaction_Year"]).agg("mean")

        result = result.reset_index()
        #Avg['States'] = Avg['States'].astype(str)
        values_to_change = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,35]
        State = ["madhya-pradesh","ladakh","jammu-&-kashmir","andhra-pradesh","jharkhand"
                "assam","meghalaya","haryana","himachal-pradesh","punjab","karnataka","mizoram",
                "nagaland","west-bengal","tamil-nadu","chhattisgarh","puducherry","tripura","bihar",
                "rajasthan","sikkim","odisha","goa","uttar-pradesh","lakshadweep","gujarat","yamunotri","dadra-&-nagar-haveli-&-daman-&-diu",
                "chandigarh","delhi","arunachal-pradesh","kerala","andaman-&-nicobar-islands","telangana","maharashtra",
                "uttarakhand","manipur"
                ]
        State.sort()
        result['States'] = result['States'].replace(values_to_change, State)
        result_state=result[ result["States"].isin([state])]
        fig_line = px.line(result_state, x=result_state["Transaction_Year"], y=result_state["Transaction_Amount"]%100
                           ,markers=dict(symbol='diamond',size=8)) 
        txt=state.capitalize()
        fig_line.update_layout(title=dict(text=txt,x=0.4,y=0.95,font=dict(color='orange'))
                                ,yaxis_title='Percentage')     
        st.plotly_chart(fig_line,use_container_width=True)
        
#_______________________________________________________________________________________________
#PIE PLOT


    if selected_1 == "Pie-Chart" :
        st.header(":blue[Pie Chart]")
        
        pie1=df3.copy()
        
        pie1=pie1.groupby(["States"]).sum(['RegisteredUsers'])
        pie1=pie1.reset_index()
        pie1=pie1.nlargest(10,'RegisteredUsers')
        
        st.subheader(":orange[Top 10 State User's]")
        fig_pie = px.pie(pie1, values=pie1["RegisteredUsers"]%100, names=pie1["States"], title="Percentage of User's In Each State")
        fig_pie.update_traces(textinfo='label+percent')
        st.plotly_chart(fig_pie,use_container_width=True)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
