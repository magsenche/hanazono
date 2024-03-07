# Streamlit
Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. In just a few minutes you can build and deploy powerful data apps.

## How to use it
Run your app:
```shell
streamlit run app.py
```

### Write magic
There are two ways to write things:

```python
st.title('🦜🔗 Quickstart App')
st.write("Welcome to your app")
st.markdown("it **also** support ~~markdown~~")
```

or using [magic](https://docs.streamlit.io/library/api-reference/write-magic/magic) that allows you to write almost anything (markdown, data, charts) without having to type an explicit command at all

```python
"Welcome to your app" # Write the text
import pandas as pd
df = pd.DataFrame({'col1': [1,2,3]})
df  # 👈 Draw the dataframe

x = 10
'x', x  # 👈 Draw the string 'x' and then the value of x
```


### Widgets
=== "Text input"
    ```python
    openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')
    ```
=== "Button"
    ```python title=""
    if st.button("Press me"):
        # Do something
    ```

More about [widget behavior](https://docs.streamlit.io/library/advanced-features/widget-behavior)

### Session state
[Session State](https://docs.streamlit.io/library/api-reference/session-state) is a way to share variables between reruns, for each user session.

!!! note "What is a session?"
    A session is a single instance of viewing an app. If you view an app from two different tabs in your browser, each tab will have its own session. So each viewer of an app will have a Session State tied to their specific view. Streamlit maintains this session as the user interacts with the app. If the user refreshes their browser page or reloads the URL to the app, their Session State resets and they begin again with a new session.

For example, to select a player from a list:
```python title=""
if "is_selected" not in st.session_state:
    st.session_state.is_selected = False
selected_player = st.selectbox(
    "How are you?",
    players_role.keys(),
    None,
    placeholder="Select a name",
    disabled=st.session_state.is_selected,
)
st.session_state.is_selected = True
```

You can also [use Callbacks to update Session State](https://docs.streamlit.io/library/api-reference/session-state#use-callbacks-to-update-session-state)

```python title=""
def form_callback():
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)

with st.form(key='my_form'):
    slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
    checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)
```

### Cache
[Cache management](https://docs.streamlit.io/library/advanced-features/caching)

## Resources

- [Langchain + Streamlit](https://docs.streamlit.io/knowledge-base/tutorials/llm-quickstart)
- [Cheatsheet](https://docs.streamlit.io/library/cheatsheet)