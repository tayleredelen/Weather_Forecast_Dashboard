import streamlit as st
import plotly.express as px
from backend import get_data

# plotly is a data visualization library

# adds title, text input, slider, selectbox, and subheader widgets
st.title("Weather forecast for the next days")
place = st.text_input("Place: ")
days = st.slider("Forecast days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} in {place}")

# widgets appear in order written

if place:
    # get the temp/sky data
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            # pulls list of all temp data from dict
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            # create a temperature plot only if we get temperature data
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            # creates line graph
            st.plotly_chart(figure)

        if option == "Sky":
            images = {'Clear': 'images/clear.png',
                      'Clouds': 'images/cloud.png',
                      'Rain': 'images/rain.png',
                      'Snow': 'images/snow.png'}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            # pulls list of weather type data dict
            image_paths = [images[condition] for condition in sky_conditions]
            print(sky_conditions)
            st.image(image_paths, width=115)
    except KeyError:
        st.write("That place does not exist")

