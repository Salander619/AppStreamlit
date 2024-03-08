""" Allow to share parameters between pages """

#!/usr/bin/python3

import streamlit as st


class ConfigManager:
    """Setup the configuration throught st_session_state"""

    def __init__(self, name_fom, use_noise_config, use_duration_config):
        self.name = name_fom

        self.use_noise_config = use_noise_config
        self.use_duration_config = use_duration_config

    def display_config(self):
        """display the configuration and modification widget"""
        st.session_state.update(st.session_state)

        st.sidebar.header(self.name + " configuration")

        # initialisation for first run
        if "noise_budget" not in st.session_state:
            st.session_state["noise_budget"] = "fom"
        if "duration" not in st.session_state:
            st.session_state["duration"] = "4 years"

        # setup noise config
        if self.use_noise_config:
            st.sidebar.radio(
                "Select your noise configuration",
                ["config 1", "config 2", "config 3"],
                key="noise_budget",
            )

        # setup mission duration
        if self.use_duration_config:
            st.sidebar.radio(
                "Select the mission duration", ["4 years", "7 years"], key="duration"
            )
