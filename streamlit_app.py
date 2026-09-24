# ============================================================
# FLARE PREDICTION — OUR SIH MODEL
# ============================================================

st.markdown(
    '<div class="section-title">🔥 Flare Prediction</div>',
    unsafe_allow_html=True
)

p1, p2 = st.columns([1, 1.7])

# ---------------- MODEL OUTPUT ----------------

with p1:

    st.markdown("""
    <div class="prediction-card">

        <div class="prediction-label">
            NEXT 24-HOUR M/X FLARE RISK
        </div>

        <div class="prediction-value">
            —
        </div>

        <div class="prediction-note">
            Awaiting trained model inference
        </div>

    </div>
    """, unsafe_allow_html=True)


# ---------------- MODEL PIPELINE ----------------

with p2:

    st.markdown("""
    <div class="card">

        <h3>Multimodal Forecasting Pipeline</h3>

        <p>
        <b>HMI Magnetogram Sequences</b>
        → CNN
        → Spatial Magnetic Features
        </p>

        <p>
        <b>20 SHARP Features</b>
        +
        <b>3 Recent Flare-History Features</b>
        </p>

        <p style="font-size:22px; text-align:center;">
        ↓
        </p>

        <p style="text-align:center;">
        <b>Feature Fusion → LSTM</b>
        </p>

        <p style="font-size:22px; text-align:center;">
        ↓
        </p>

        <p style="text-align:center;">
        <b>Next 24-Hour M/X Flare Risk</b>
        </p>

    </div>
    """, unsafe_allow_html=True)
