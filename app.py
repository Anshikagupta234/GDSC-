import streamlit is st
st.title('Demo App')
st.write('This is a demo app')

with st.sidebar:
      st.write('This is a sidebar')
  col1,col2 = st.columns(2)
with col1:
a = st.number_input('enter a value',value=10)
b = st.text_input('enter a text ) 
c = st.selectbox(lable 'choose',options=[1,2,3]                 
sub = st.buttom(lable 'submit')
   if sub:
        st.balloons()
        st:write(a)
        st:write(b)
print(a)
     
