import streamlit as st
import datetime
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt


st.set_page_config(layout = "wide", page_title= 'Tech Dashboard')

st.markdown('<style>div.block-container{padding-top:1rem;</style>}',unsafe_allow_html=True)



def load_data(data):
    return pd.read_csv(data)


def main():
    st.title('Tech Workers App')
    tech = load_data('salaries_clean.csv')
    menu = ['Home', 'Countries', 'States', 'About']


    st.sidebar.image('Tech Image.png', width = 200)
    choice = st.sidebar.selectbox('Menu', menu)
    color = st.sidebar.color_picker('color',value ='#2980B9')
    

    if choice == 'Home':
       with st.expander('Data view'):
           st.dataframe(tech)

       fig = px.scatter_mapbox(tech,lat='location_latitude', lon= 'location_longitude', hover_name ='location_state',hover_data=['location_country','location_name'],
                               color_discrete_sequence=[color],zoom =1,height = 700)
       fig.update_layout(mapbox_style = 'open-street-map')
       st.plotly_chart(fig)
    

    elif choice == 'Countries':
       countries_list= tech['location_country'].unique().tolist()
       selected_country =st.multiselect('country',countries_list, default = ['GR'])
       with st.expander('Data view'):
              df = tech[tech['location_country'].isin(selected_country)]
              st.dataframe(df)
          

       fig = px.scatter_mapbox(df,lat='location_latitude', lon= 'location_longitude', hover_name ='location_state',hover_data=['location_country','location_name'],
                               color_discrete_sequence=[color],zoom =1,height = 700)
       fig.update_layout(mapbox_style = 'open-street-map')
       st.plotly_chart(fig)
        


    elif choice == 'States':
       states_list= tech['location_state'].unique().tolist()
       selected_state =st.multiselect('states',states_list, default = ['OK'])
       with st.expander('Data view'):
              df = tech[tech['location_state'].isin(selected_state)]
              st.dataframe(df)
          

       fig = px.scatter_mapbox(df,lat='location_latitude', lon= 'location_longitude', hover_name ='location_state',hover_data=['location_country','location_name'],
                               color_discrete_sequence=[color],zoom =1,height = 700)
       fig.update_layout(mapbox_style = 'open-street-map')
       st.plotly_chart(fig)
        
   

    else:
        
        st.markdown("<h4 style = 'margin: -30px; color:#2980B9 ; text-align: center; font-family: cursive '>Built By Chiemeziem Okeke</h4>", unsafe_allow_html = True)
        st.markdown("<br>", unsafe_allow_html= True)
        st.image('Tech_cus4.png', width = 500)
        st.markdown("<br>", unsafe_allow_html= True)
        st.subheader ('About')
        st.write('The global tech industry is a dynamic and diverse ecosystem, this project aims to understand the landscape of tech workers in different countries and provides valuable insights into the variations in demographics.')
     
    



        
if __name__ == "__main__":
    main()









