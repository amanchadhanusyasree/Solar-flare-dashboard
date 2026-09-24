import streamlit as st
import pandas as pd
import requests
from datetime import datetime
from zoneinfo import ZoneInfo


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Solar Flare Forecasting",
    page_icon="☀️",
    layout="wide"
)


# ============================================================
# CONSTANTS
# ============================================================

IST = ZoneInfo("Asia/Kolkata")

NOAA_FLARE_URL = (
    "https://services.swpc.noaa.gov/json/"
    "goes/primary/xray-flares-7-day.json"
)

HMI_IMAGE = (
    "https://sdo.gsfc.nasa.gov/assets/img/latest/"
    "latest_1024_HMIIF.jpg"
)

AIA_IMAGE = (
    "https://sdo.gsfc.nasa.gov/assets/img/latest/"
    "latest_1024_0171.jpg"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at 88% 8%,
            rgba(255, 105, 20, 0.13),
            transparent 28%
        ),
        radial-gradient(
            circle at 10% 90%,
            rgba(255, 70, 10, 0.07),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #050812 0%,
            #0a0f1c 50%,
            #080b14 100%
        );
    color: #f5f5f5;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

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
    margin-bottom: 25px;
}

.section-title {
    font-size: 25px;
    font-weight: 700;
    margin-top: 28px;
    margin-bottom: 15px;
}

.card {
    background: rgba(18, 24, 39, 0.92);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 10px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.20);
}

.prediction-card {
    background:
        radial-gradient(
            circle at 50% 0%,
            rgba(255,100,20,0.16),
            transparent 55%
        ),
        #111827;
    border: 1px solid rgba(255,120,30,0.25);
    border-radius: 18px;
    padding: 22px;
    text-align: center;
}

.prediction-label {
    color: #9da6b8;
    font-size: 13px;
    letter-spacing: 1px;
}

.prediction-value {
    font-size: 38px;
    font-weight: 800;
    margin: 8px 0;
}

.prediction-note {
    color: #9da6b8;
    font-size: 13px;
}

.flare-class-card {
    background: #111827;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 12px;
    padding: 12px 15px;
    margin-bottom: 9px;
}

.flare-class-name {
    font-size: 20px;
    font-weight: 750;
}

.flare-class-description {
    color: #9da6b8;
    font-size: 12px;
}

.eval-box {
    background: #111827;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 15px;
    padding: 20px;
    text-align: center;
}

.eval-number {
    font-size: 30px;
    font-weight: 700;
}

.eval-label {
    color: #9da6b8;
    font-size: 13px;
}

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
    'Solar activity monitoring and next-24-hour flare forecasting'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# CURRENT STATUS
# ============================================================

current_time = datetime.now(IST)

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Monitoring",
        "SOLAR ACTIVITY"
    )

with c2:
    st.metric(
        "Forecast Horizon",
        "NEXT 24 HOURS"
    )

with c3:
    st.metric(
        "Updated",
        current_time.strftime(
            "%d %b %Y, %I:%M %p IST"
        )
    )


# ============================================================
# LOAD REAL NOAA FLARE DATA
# ============================================================

@st.cache_data(ttl=300)
def load_flare_data():

    response = requests.get(
        NOAA_FLARE_URL,
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    return pd.DataFrame(data)


flare_df = pd.DataFrame()
noaa_available = False

try:

    flare_df = load_flare_data()

    if not flare_df.empty:

        flare_df["max_time"] = pd.to_datetime(
            flare_df["max_time"],
            errors="coerce",
            utc=True
        )

        flare_df["max_time_ist"] = (
            flare_df["max_time"]
            .dt.tz_convert(IST)
        )

        flare_df = flare_df.sort_values(
            "max_time",
            ascending=False
        )

        noaa_available = True

except Exception:
    noaa_available = False


# ============================================================
# SOLAR OBSERVATIONS
# ============================================================

st.markdown(
    '<div class="section-title">🔭 Solar Observations</div>',
    unsafe_allow_html=True
)

obs1, obs2 = st.columns(2)


# ---------------- HMI ----------------

with obs1:

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.subheader("HMI Magnetogram")

    st.image(
        HMI_IMAGE,
        use_container_width=True,
        caption="NASA SDO / HMI — Line-of-Sight Magnetogram"
    )

    st.caption(
        "Real solar magnetic-field observation from SDO/HMI."
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# ---------------- AIA ----------------

with obs2:

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.subheader("AIA UV Observation")

    st.image(
        AIA_IMAGE,
        use_container_width=True,
        caption="NASA SDO / AIA — 171 Å"
    )

    st.caption(
        "Real ultraviolet solar observation from SDO/AIA."
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

# ============================================================
# FLARE PREDICTION
# ============================================================

st.markdown(
    '<div class="section-title">🔥 Flare Prediction</div>',
    unsafe_allow_html=True
)

# ------------------------------------------------------------
# SAMPLE CURRENT FLARE
# ------------------------------------------------------------

st.markdown("""
<div class="card">

    <div style="color:#9da6b8; font-size:14px; letter-spacing:1px;">
        CURRENT OBSERVED FLARE
    </div>

    <div style="
        font-size:42px;
        font-weight:800;
        margin-top:6px;
    ">
        A
    </div>

    <div style="color:#9da6b8; font-size:13px;">
        Sample observation for dashboard demonstration
    </div>

</div>
""", unsafe_allow_html=True)


# ------------------------------------------------------------
# NEXT 24-HOUR PREDICTION
# ------------------------------------------------------------

p1, p2 = st.columns([1, 1.7])

with p1:

    st.markdown("""
    <div class="prediction-card">

        <div class="prediction-label">
            NEXT 24-HOUR FLARE PREDICTION
        </div>

        <div class="prediction-value">
            —
        </div>

        <div class="prediction-note">
            Model prediction will appear after trained-model inference
        </div>

    </div>
    """, unsafe_allow_html=True)


# ------------------------------------------------------------
# FIVE FLARE CLASSES
# ------------------------------------------------------------

with p2:

    st.markdown("""
    <div class="scale-box">

        <h3>Solar Flare Classes</h3>

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
# MODEL EVALUATION
# ============================================================

st.markdown(
    '<div class="section-title">📊 Model Evaluation</div>',
    unsafe_allow_html=True
)

e1, e2, e3, e4 = st.columns(4)

with e1:

    st.markdown(
        """
        <div class="eval-box">
            <div class="eval-number">—</div>
            <div class="eval-label">TSS</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with e2:

    st.markdown(
        """
        <div class="eval-box">
            <div class="eval-number">—</div>
            <div class="eval-label">Accuracy</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with e3:

    st.markdown(
        """
        <div class="eval-box">
            <div class="eval-number">—</div>
            <div class="eval-label">Precision</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with e4:

    st.markdown(
        """
        <div class="eval-box">
            <div class="eval-number">—</div>
            <div class="eval-label">Recall</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.caption(
    "Evaluation metrics will be populated after the forecasting "
    "model is trained and validated."
)


# ============================================================
# RECENT FLARE ACTIVITY
# ============================================================

st.markdown(
    '<div class="section-title">'
    '📈 Recent Flare Activity'
    '</div>',
    unsafe_allow_html=True
)


def flare_level(flare_class):

    if not isinstance(flare_class, str):
        return None

    try:

        letter = flare_class[0].upper()
        number = float(flare_class[1:])

        base = {
            "A": 0,
            "B": 1,
            "C": 2,
            "M": 3,
            "X": 4
        }

        if letter not in base:
            return None

        return base[letter] + number / 10

    except Exception:

        return None


if noaa_available:

    graph_df = flare_df.copy()

    graph_df["Activity Level"] = (
        graph_df["max_class"]
        .apply(flare_level)
    )

    graph_df = graph_df.dropna(
        subset=[
            "max_time",
            "Activity Level"
        ]
    )

    graph_df = graph_df.sort_values(
        "max_time"
    )

    if not graph_df.empty:

        chart_data = graph_df[
            [
                "max_time",
                "Activity Level"
            ]
        ].copy()

        chart_data = chart_data.set_index(
            "max_time"
        )

        chart_data.index = (
            chart_data.index
            .tz_convert(IST)
        )

        chart_data.columns = [
            "Flare Activity"
        ]

        st.line_chart(
            chart_data,
            use_container_width=True
        )

        st.caption(
            "Activity level derived from the observed "
            "NOAA GOES flare class."
        )

    else:

        st.info(
            "No valid flare activity data available."
        )

else:

    st.info(
        "Recent flare activity chart is unavailable "
        "because NOAA data could not be loaded."
    )


# ============================================================
# DATA SOURCES
# ============================================================

st.markdown("---")

st.markdown(
    '<div class="footer">'
    'Solar imagery: NASA Solar Dynamics Observatory '
    '(SDO/HMI + SDO/AIA)'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="footer">'
    'Flare observations: NOAA / SWPC GOES'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="footer">'
    'All dashboard times are displayed in IST (UTC+05:30)'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="footer">'
    'Solar Flare Forecasting System — SIH Software Prototype'
    '</div>',
    unsafe_allow_html=True
)
