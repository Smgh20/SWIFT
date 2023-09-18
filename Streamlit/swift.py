import streamlit as st
import datetime
from PIL import Image
ensam=Image.open("ensam.png")
col1, col2, col3 = st.columns(3)

with col1:
    st.write('')

with col2:
    st.write('')

with col3:
    st.image(ensam , width=320 )

st.title("SWIFT")
st.markdown("<h1 style='text-align: center; color: blue;'>Autonomous tool-carring robots</h1>", unsafe_allow_html=True)
html_temp = """ 
<div style="background-color:blue;"><p style=color:white;font- size:50px;">PROJET D'INITIATION IA</p></div>
"""
st.markdown(html_temp, unsafe_allow_html=True)

img= Image.open("igv.png")
img2=Image.open("iiiigv.jpg")
soso = Image.open("soso.jpg")
sasa= Image.open("sasa.jpg")
didij=Image.open("didij.jpg")
col1, col2, col3 = st.columns(3)

with col1:
    st.image(img2 , width=400)

with col3:
    st.image(img , width=320 )

with col2:
    st.write(' ')

st.sidebar.header("About")
st.sidebar.text("""
This interface allows you to enter 
the coordinates of the operator 
responsible for maintenance and 
to determine the tools and follow 
the path of the robot.
        """)
activities=["HOME","Operator coordinate","Tools","Pathfinding"]
choise= st.sidebar.selectbox("**Select your box:**", activities)
st.sidebar.text("ENSAM MEKNES")
st.sidebar.text("GI_IA_4A")

if choise == 'HOME':
    st.write("**INTRODUCTION**")
    st.write("""
Nowadays, maintenance is at the heart of any
industrial activity and constitutes a major challenge
for business productivity. In this regard,
several technologies have been developed during
of recent years in order to guarantee the good
maintenance management as well as facilitating
considerably the work of the field teams.
One of the maintenance issues is
to the repetitive travel of the team to
bring back the necessary tools in order to accomplish a
repair stain which results in a loss of
term of time and effort. Where did the idea come from?
SWIFT which aims to limit these movements.
""")
    st.write("**GOAL OF THE PROJECT**")
    st.write("""
This solution is effective to
minimize downtime which
causes heavy additional costs and losses
for the company.
    """)


if choise== 'Operator coordinate':
    firstname= st.text_input("**Enter your name:**","operator name")
    list=['sanae', 'khadija','sana']
    if firstname in list:
        st.success("Accepted")
        st.text("Hello Madame")

        if firstname == list[0]:
            st.image(soso , width=360)
        elif firstname == list[1]:
            st.image(didij , width=100)
        elif firstname== list[2]:
            st.image(sasa , width=200)

        today = st.date_input("**Today is:**", datetime.datetime.now())
        time=st.time_input("**The time is:**", datetime.time())
        poste= st.radio("**Out of order post:**",("POST1","POST2","POST3","POST4","POST5"))
        

    else:
        st.warning("You don't have the access")
if choise == 'Tools':
    tool = st.multiselect('**Select tools:**', ['Wrench','Screw Driver','Hammer','Tool Box'])
    
    st.number_input("**Number of wrench**:",0,5)
    number = st.number_input("**Number of Screw Driver**:",0,5)
    number = st.number_input("**Number of Hammer**:",0,5)
    number = st.number_input("**Number of Tool box**:",0,5)
#if choise == 'Pathfinding':
    #video_file = open("path_simulation.mp4", 'rb')
    #video_bytes = video_file.read()
    #st.image(img) 
    #st.video(video_bytes)'''
