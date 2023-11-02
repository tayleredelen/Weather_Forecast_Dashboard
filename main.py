import streamlit as st
import plotly.express as px

# plotly is a data visualization library

st.title("Weather forecast for the next days")
place = st.text_input("Place: ")
days = st.slider("Forecast days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} in {place}")


# widgets appear in order written

def get_data(days):
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperatures = [67, 69, 65]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


d, t = get_data(days)
figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (F)"})
# creates line graph
st.plotly_chart(figure)

