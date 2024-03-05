""" Allow to share parameters between pages """

#!/usr/bin/python3

import streamlit as st


def display_config():
    st.session_state.update(st.session_state)

    st.sidebar.header("Common configuration")

    # initialisation for first run
    if "noise_budget" not in st.session_state:
        st.session_state["noise_budget"] = "config 1"
    if "duration" not in st.session_state:
        st.session_state["duration"] = "4 years"

    # setup noise config
    st.sidebar.radio(
        "Select your noise configuration",
        ["config 1", "config 2", "config 3"],
        key="noise_budget",
    )

    # setup mission duration
    st.sidebar.radio(
        "Select the mission duration", ["4 years", "7 years"], key="duration"
    )
