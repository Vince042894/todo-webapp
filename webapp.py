import streamlit as st
import functions

todos = functions.get_todos()

st.title("My todo App")
st.subheader("This is a my to do app")
st.write("This up is to increase your productivity")


for index, todo in enumerate(todos):
    st.checkbox(todo, key=f"todo_{index}")

st.text_input(label="", placeholder="Add new todo....")
