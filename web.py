import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['input'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

logo = '4042.png'

st.image(logo)
st.subheader("Increase productivity and track upcoming tasks")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Write a todo",
              label_visibility='hidden',
              placeholder="Add new todo...",
              on_change=add_todo, key='input')