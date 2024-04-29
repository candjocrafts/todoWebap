import streamlit as st
import rhfunctions

todos = rhfunctions.open_file()

# if 'button' not in st.session_state:
#     st.session_state.button = False


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    print(todo)
    todos.append(todo)
    rhfunctions.write_file(todos)


st.title("My Todo App")

st.text_input(label="x", placeholder="Add new todo...", label_visibility="hidden", on_change=add_todo, key='new_todo')
st.subheader("Current to-dos:")

del_button = st.button("Delete selected items")

for i, todo in enumerate(todos):
    chkbxs = st.checkbox(todo, key=f"cb{i}")

    if del_button:
        try:
            for i in range(len(todos)):
                if st.session_state[f"cb{i}"] == True:
                    todos.pop(i)
                    rhfunctions.write_file(todos)
                    del st.session_state[f"cb{i}"]
        except KeyError:
            print("Looks like something got screwed up")


print(st.session_state)

