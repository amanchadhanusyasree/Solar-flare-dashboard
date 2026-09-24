import streamlit as st
import pandas as pd
import requests
from datetime import datetime, timezone

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Solar Flare Forecasting",
    page_icon="☀️",
    layout="wide"
)

# ============================================================
# CUSTOM STYLE
# ============================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 85% 10%, rgba(255,110,20,0.12), transparent 28%),
        radial-gradient(circle at 15% 85%, rgba(255,70,10,0.07), transparent 30%),
        linear-gradient(135deg, #050812 0%, #0a0f1c 50%, #080b14 100%);
    color: #f5f5f5;
}

/* Subtle solar glow */
.stApp::before {
    content: "";
    position: fixed;
    width: 420px;
    height: 420px;
    right: -170px;
    top: 80px;
    border-radius: 50%;
    background: radial-gradient(
        circle,
        rgba(255,120,25,0.13),
        rgba(255,70,10,0.04) 45%,
        transparent 70%
    );
    pointer-events: none;
}

/* Main title */
.main-title {
    font-size: 42px;
    font-weight: 800;
    letter-spacing: -1px;
    margin-bottom: 0;
}

.subtitle {
    color: #a9b1c2;
    font-size: 16px;
    margin-top: 5px;
    margin-bottom: 28px;
}

/* Section headings */
.section-title {
    font-size: 24px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 15px;
}

/* Cards */
.card {
    background: rgba(18, 24, 39, 0.88);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 22px;
    min-height: 150px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.22);
}

/* Observation placeholders */
.observation-box {
    height: 260px;
    border-radius: 14px;
    border: 1px dashed rgba(255,255,255,0.18);
    background:
        radial-gradient(circle at 50% 50%,
        rgba(255,100,20,0.10),
        transparent 45%),
        #0c1220;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: #9da6b8;
}

/* Prediction */
.prediction-card {
    background:
        radial-gradient(circle at 50% 0%,
        rgba(255,100,20,0.18),
        transparent 50%),
        #111827;
    border: 1px solid rgba(255,120,30,0.25);
    border-radius: 18px;
    padding: 28px;
    text-align: center;
}

.prediction-label {
    color: #9da6b8;
    font-size: 14px;
    letter-spacing: 1px;
}

.prediction-value {
    font-size: 55px;
    font-weight: 800;
    margin: 5px 0;
}

.prediction-note {
    color: #9da6b8;
    font-size: 13px;
}

/* Flare scale */
.scale-box {
    background: #111827;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 20px;
}

.scale-item {
    padding: 10px 14px;
    margin: 7px 0;
    border-radius: 9px;
    background: rgba(255,255,255,0.04);
}

/* Footer */
.footer {
    text-align: center;
    color: #70798b;
    font-size: 12px;
    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">☀️ Solar Flare Forecasting</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Solar observation, flare activity and deep-learning based forecasting'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# TOP STATUS
# ============================================================

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Monitoring", "SOLAR ACTIVITY")

with c2:
    st.metric("Forecast Window", "24 HOURS")

with c3:
    current_time = datetime.now(timezone.utc).strftime("%d %b %Y, %H:%M UTC")
    st.metric("Dashboard Time", current_time)


# ============================================================
# SOLAR OBSERVATIONS
# ============================================================

st.markdown(
    '<div class="section-title">🔭 Solar Observations</div>',
    unsafe_allow_html=True
)

obs1, obs2 = st.columns(2)

with obs1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("HMI Magnetogram")

    st.markdown("""
    <div class="observation-box">
        <div>
            <b>HMI observation</b><br>
            Connect HMI magnetogram data here
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.caption("Magnetic-field observation")

    st.markdown('</div>', unsafe_allow_html=True)


with obs2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("AIA UV Observation")

    st.markdown("""
    <div class="observation-box">
        <div>
            <b>AIA UV observation</b><br>
            Connect AIA UV data here
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.caption("Ultraviolet solar observation")

    st.markdown('</div>', unsafe_allow_html=True)


# ============================================================
# PREDICTION
# ============================================================

st.markdown(
    '<div class="section-title">🔥 Flare Prediction</div>',
    unsafe_allow_html=True
)

p1, p2 = st.columns([1, 1.6])

with p1:

    st.markdown("""
    <div class="prediction-card">

        <div class="prediction-label">
            MODEL PREDICTION
        </div>

        <div class="prediction-value">
            —
        </div>

        <div class="prediction-note">
            Waiting for trained model
        </div>

    </div>
    """, unsafe_allow_html=True)


with p2:

    st.markdown("""
    <div class="scale-box">

    <h4>Solar Flare Classes</h4>

    <div class="scale-item">
    <b>A</b> — Lowest X-ray flare class
    </div>

    <div class="scale-item">
    <b>B</b> — Low-level flare activity
    </div>

    <div class="scale-item">
    <b>C</b> — Moderate flare activity
    </div>

    <div class="scale-item">
    <b>M</b> — Strong flare activity
    </div>

    <div class="scale-item">
    <b>X</b> — Highest flare class
    </div>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# REAL RECENT SOLAR FLARES
# ============================================================

st.markdown(
    '<div class="section-title">🚨 Recent Solar Flares</div>',
    unsafe_allow_html=True
)

# NOAA/SWPC GOES flare feed
NOAA_URL = (
    "https://services.swpc.noaa.gov/json/"
    "goes/secondary/xray-flares-7-day.json"
)

try:

    response = requests.get(NOAA_URL, timeout=10)
    response.raise_for_status()

    flare_data = response.json()

    if flare_data:

        df = pd.DataFrame(flare_data)

        # ----------------------------------------------------
        # Identify useful columns safely
        # ----------------------------------------------------

        possible_class_columns = [
            "max_class",
            "max_class_xray",
            "class",
            "event_class"
        ]

        class_column = None

        for col in possible_class_columns:
            if col in df.columns:
                class_column = col
                break

        # ----------------------------------------------------
        # Convert time column
        # ----------------------------------------------------

        time_columns = [
            "max_time",
            "begin_time",
            "start_time",
            "event_time"
        ]

        time_column = None

        for col in time_columns:
            if col in df.columns:
                time_column = col
                break

        if time_column:
            df["Time"] = pd.to_datetime(
                df[time_column],
                errors="coerce",
                utc=True
            )

        # ----------------------------------------------------
        # Keep only classified flares
        # ----------------------------------------------------

        if class_column:

            df["Flare Class"] = (
                df[class_column]
                .astype(str)
                .str.upper()
            )

            # Keep A/B/C/M/X classifications
            df = df[
                df["Flare Class"].str.match(
                    r"^[ABCMX][0-9]"
                )
            ]

        # ----------------------------------------------------
        # Sort newest first
        # ----------------------------------------------------

        if "Time" in df.columns:

            df = df.sort_values(
                "Time",
                ascending=False
            )

        # Show latest 10
        df = df.head(10)

        # ----------------------------------------------------
        # Display table
        # ----------------------------------------------------

        display_columns = []

        if "Time" in df.columns:
            display_columns.append("Time")

        if "Flare Class" in df.columns:
            display_columns.append("Flare Class")

        # Region if available
        for possible_region in [
            "region",
            "active_region",
            "region_number"
        ]:
            if possible_region in df.columns:
                df["Active Region"] = df[possible_region]
                display_columns.append("Active Region")
                break

        if display_columns:

            display_df = df[display_columns].copy()

            if "Time" in display_df.columns:
                display_df["Time"] = display_df["Time"].dt.strftime(
                    "%d %b %Y  %H:%M UTC"
                )

            st.dataframe(
                display_df,
                use_container_width=True,
                hide_index=True
            )

        else:
            st.info(
                "NOAA returned flare data, but the current "
                "field structure could not be displayed."
            )

    else:

        st.info("No recent classified flare events returned.")

except Exception as e:

    st.warning(
        "Live NOAA flare data could not be loaded right now."
    )

    st.caption(
        "The dashboard will continue to work. "
        "Check the NOAA data connection later."
    )


# ============================================================
# FLARE ACTIVITY
# ============================================================

st.markdown(
    '<div class="section-title">📈 Recent Flare Activity</div>',
    unsafe_allow_html=True
)

try:

    if "df" in locals() and "Time" in df.columns:

        graph_df = df.dropna(subset=["Time"]).copy()

        if "Flare Class" in graph_df.columns:

            # Convert A/B/C/M/X class to approximate numeric level
            # for visualization only.
            def flare_level(value):

                try:
                    letter = value[0]
                    number = float(value[1:])

                    base = {
                        "A": 0,
                        "B": 1,
                        "C": 2,
                        "M": 3,
                        "X": 4
                    }

                    return base.get(letter, 0) + number / 10

                except:
                    return None

            graph_df["Activity Level"] = (
                graph_df["Flare Class"]
                .apply(flare_level)
            )

            graph_df = graph_df.dropna(
                subset=["Activity Level"]
            )

            graph_df = graph_df.sort_values("Time")

            if not graph_df.empty:

                chart_df = graph_df[
                    ["Time", "Activity Level"]
                ].set_index("Time")

                st.line_chart(
                    chart_df,
                    use_container_width=True
                )

                st.caption(
                    "Activity level is derived from the observed "
                    "GOES flare classification for visualization."
                )

            else:
                st.info("Not enough classified events for the graph.")

        else:
            st.info("Flare classification data unavailable.")

    else:
        st.info("Waiting for live flare data.")

except Exception:

    st.info(
        "The activity graph will appear when valid flare "
        "classification data is available."
    )


# ============================================================
# DATA SOURCE
# ============================================================

st.markdown("---")

st.markdown(
    '<div class="footer">'
    'Recent flare events: NOAA / Space Weather Prediction Center '
    'GOES X-ray observations'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="footer">'
    'Solar Flare Forecasting System — Software Prototype'
    '</div>',
    unsafe_allow_html=True
)
