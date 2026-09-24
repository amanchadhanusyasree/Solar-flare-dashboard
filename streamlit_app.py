# ============================================================
# REAL RECENT SOLAR FLARES - NOAA GOES
# ============================================================

st.markdown(
    '<div class="section-title">🚨 Recent Solar Flares</div>',
    unsafe_allow_html=True
)

NOAA_URL = (
    "https://services.swpc.noaa.gov/json/"
    "goes/primary/xray-flares-7-day.json"
)

try:

    response = requests.get(
        NOAA_URL,
        timeout=15
    )

    response.raise_for_status()

    flare_data = response.json()

    if flare_data:

        df = pd.DataFrame(flare_data)

        # Convert NOAA UTC time to IST
        df["max_time"] = pd.to_datetime(
            df["max_time"],
            errors="coerce",
            utc=True
        )

        df["max_time_ist"] = (
            df["max_time"]
            .dt.tz_convert("Asia/Kolkata")
        )

        # Keep only recent events
        df = df.sort_values(
            "max_time",
            ascending=False
        ).head(10)

        # Display table
        recent_flares = pd.DataFrame({
            "Time (IST)": df["max_time_ist"].dt.strftime(
                "%d %b %Y  %I:%M %p"
            ),
            "Flare Class": df["max_class"],
            "Satellite": "GOES-" + df["satellite"].astype(str)
        })

        st.dataframe(
            recent_flares,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info("No recent solar flare events available.")

except Exception as e:

    st.error(
        "Unable to load live NOAA solar-flare data."
    )
