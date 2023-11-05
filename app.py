
import requests 
import streamlit  as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":zany_face:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None 
    return r.json()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


lottie_coding = load_lottieurl("https://lottie.host/3acc6384-c473-40cc-898c-0e8963485848/GRmZFiTI6R.json")



with st.container ():
    st.subheader("Hi, I am Jean :wave:")
    st.title("An Established Coder And Also Good In Robotics ")
    st.write("I am passionate about using Python and Arduiono to do cool stuff!")
    st.write("[Learn More >](https://pythonandvba.com)")   


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)    
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
        """
   Here are some things I am currently able to do:
    - I can leverage the power of python into my day-to-day activicties.
    - I can chanell Python and Vba into robotics and coding. 
    - I can use Data Analysis and Data Science to perform meaningful and inspectful analyses.   
    - I can also use Excel for fun different projects in Python. "

     If this sounds interesting to you, consider learning python for yourself.
     """
        )
        st.write("[Youtube Channel >](https://youtube.com/c/CodingIsFun)")
        with right_column:
            st_lottie(lottie_coding, height=300, key='coding')
        

        with st.container():
            st.write("---")
            st.header("Get In Touch With Me!")
            st.write("##")
     

contact_form="""
<form action="https://formsubmit.co/jeanjacob011@gmail.com" method="POST">
      <input type= "hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder = "Your name" required>
     <input type="email" name="email" placeholder = "Your email" required>
     <textarea name= "message" placeholder = "Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column,right_column = st.columns(2)
with left_column:
    st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()



