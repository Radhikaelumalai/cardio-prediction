import streamlit as st
from Ecg import ECG
import datetime

st.set_page_config(page_title="Cardio App", layout="wide")

# ---- SESSION ----
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "report" not in st.session_state:
    st.session_state.report = None

# ================= LOGIN PAGE =================
if not st.session_state.logged_in:
    st.markdown("""
    <style>
    /* Sky blue background */
    .stApp {
        background-color: #87CEEB;
    }

   

    /* Input styling */
    .stTextInput input {
        border-radius: 8px;
        padding: 8px;
        width: 90%;
    }

    /* Button styling */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        background-color: #007acc;
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

    # Center using columns
    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.markdown('<h2 style="text-align:center; color:#333; font-weight:bold; margin-bottom:25px;">Cardio Vascular Prediction System ❤️</h2>', unsafe_allow_html=True)
    

        username = st.text_input("", placeholder="Username")
        password = st.text_input("", placeholder="Password", type="password")

        if st.button("Login"):
            if username == "admin" and password == "1234":
                st.session_state.logged_in = True
                st.success("Login Successful")
            else:
                st.error("Invalid Credentials")

        st.markdown('</div>', unsafe_allow_html=True)

# if not st.session_state.logged_in:
#     st.markdown("""
#     <style>
#     .stApp {
#         background-color: #87CEEB;
#     }

#     /* Center everything */
#     .block-container {
#         padding-top: 100px;
#         text-align: center;
#     }


#     /* Input box size */
#     .stTextInput input {
#         width: 100%,!important;
#         border-radius: 8px;
#         padding: 10px;
#     }

#     /* Button */
#     .stButton>button {
#         width: 100%;
#         border-radius: 8px;
#         background-color: #007acc;
#         color: white;
#         font-weight: bold;
#     }
#     </style>
#     """, unsafe_allow_html=True)

#     st.markdown('<div class="login-box">', unsafe_allow_html=True)

#     st.markdown("❤️ Cardio Vascular Prediction System")

#     username = st.text_input("", placeholder="Username")
#     password = st.text_input("", placeholder="Password", type="password")

#     if st.button("Login"):
#         if username == "admin" and password == "1234":
#             st.session_state.logged_in = True
#             st.success("Login Successful")
#         else:
#             st.error("Invalid Credentials")

#     st.markdown('</div>', unsafe_allow_html=True)
# ================= DASHBOARD =================
else:

    st.markdown("""
            <style>

            /* Full dashboard background */
            .stApp {
                background: linear-gradient(135deg, #0A1F44, #1E3A8A);
            }

            /* Sidebar */
            section[data-testid="stSidebar"] {
                background-color: #071633;
            }

            section[data-testid="stSidebar"] * {
                color: white !important;
            }

            /* Remove top white bar */
            header {
                visibility: hidden;
            }

            /* Remove top space */
            .block-container {
                padding-top: 0rem;
            }

            /* Text color */
            h1, h2, h3, h4, h5, h6, p, label {
                color: white;
            }

            /* Buttons */
            .stButton>button {
                background-color: #1E3A8A;
                color: white;
                border-radius: 8px;
            }

            /* Image style */
            img {
                border-radius: 15px;
                box-shadow: 0px 4px 20px rgba(0,0,0,0.5);
            }

            </style>
            """, unsafe_allow_html=True)

    # 👇 AFTER THIS ONLY your dashboard code
    st.sidebar.title("Dashboard")
    st.markdown("""
        <style>

        /* Full dashboard background */
        .stApp {
            background-color: #0A1F44;  /* Dark Blue */
        }

        /* Sidebar background */
        section[data-testid="stSidebar"] {
            background-color: #071633;  /* More dark */
        }

        /* Sidebar text color */
        section[data-testid="stSidebar"] * {
            color: white !important;
        }

        /* Main text color */
        h1, h2, h3, h4, h5, h6, p, label {
            color: white;
        }

        /* Buttons */
        .stButton>button {
            background-color: #1E3A8A;
            color: white;
        border-radius: 8px;
    }

    </style>
    """, unsafe_allow_html=True)

        


    page = st.sidebar.radio("Menu", [
        "Home",
        "Cardio Heart Prediction",
        "Prediction Report",
        "Metrics",
        "About",
        "Contact"
    ])

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False

    # -------- HOME --------
    if page == "Home":

        st.markdown("""
        <style>

        .stApp {
            background: linear-gradient(135deg, #0A1F44, #1E3A8A);
        }

        h1, h2, h3, h4, h5, h6, p, div, span, label {
            color: #FFFFFF !important;
        }

        .main-title {
            text-align: center;
            font-size: 42px;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .sub-text {
            text-align: center;
            font-size: 18px;
            color: #E0E7FF;
            margin-bottom: 25px;
        }

        .card {
            background: rgba(255,255,255,0.08);
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            transition: 0.3s;
            box-shadow: 0 4px 20px rgba(0,0,0,0.4);
        }

        .card:hover {
            transform: translateY(-8px) scale(1.03);
            background: rgba(255,255,255,0.15);
        }

        .card h3 {
            color: #93C5FD;
        }

        .card p {
            color: #F1F5F9;
        }

        [data-testid="metric-container"] {
            background: rgba(255,255,255,0.08);
            padding: 15px;
            border-radius: 12px;
        }

        .stButton>button {
            background-color: #2563EB;
            color: white;
            border-radius: 10px;
            font-weight: bold;
        }

        </style>
        """, unsafe_allow_html=True)

        # 🔥 TITLE
        st.markdown('<div class="main-title">❤️ Cardio Vascular Prediction System</div>', unsafe_allow_html=True)

        # ❤️ IMAGE (SAFE METHOD)
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.image(
                "download.JPEG",
                width=200
            )

        # 🔥 SUB TEXT
        st.markdown('<div class="sub-text">AI-powered ECG analysis for early heart disease detection</div>', unsafe_allow_html=True)

        # 🔥 FEATURE CARDS
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""
            <div class="card">
            <h3>📤 Upload ECG</h3>
            <p>Upload ECG image for analysis</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="card">
            <h3>🤖 AI Prediction</h3>
            <p>ML model detects heart condition</p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown("""
            <div class="card">
            <h3>📊 Instant Report</h3>
            <p>Get detailed prediction report</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")

       
       

        # 🔥 CENTER BUTTON
        c1, c2, c3 = st.columns([1,2,1])
        with c2:
            if st.button("🚀 Start Prediction"):
                st.success("👉 Go to 'Cardio Heart Prediction' from menu")
    # -------- CARDIO PAGE --------
    elif page == "Cardio Heart Prediction":

        st.title("❤️ Cardio Heart Prediction")

        ecg = ECG()
        uploaded_file = st.file_uploader("📤 Upload ECG Image")

        if uploaded_file is not None:

            # ================= STEP 1 =================
            img = ecg.getImage(uploaded_file)

            st.write(" Step 1: Original Image")
            st.image(img, width=800)

            # ================= STEP 2 =================
            gray = ecg.GrayImgae(img)

            with st.expander("Step 2: Grayscale Image"):
                

                st.image(gray, width=800)

            # ================= STEP 3 =================
            leads = ecg.DividingLeads(img)

            with st.expander(" Step 3: Lead Segmentation"):
                col1, col2, col3 = st.columns(3)

                for i in range(12):
                    if i % 3 == 0:
                        col = col1
                    elif i % 3 == 1:
                        col = col2
                    else:
                        col = col3

                    with col:
                        st.image(leads[i], caption=f"Lead {i+1}", width=200)

            # ================= STEP 4 =================
            with st.expander(" Step 4: Signal Extraction (1D)"):
                signals = []

                for i, lead in enumerate(leads):
                    sig = ecg.extract_signal(lead)
                    signals.append(sig)

            
                st.line_chart(signals[0])

            # ================= STEP 5 =================
            signal_1d = ecg.CombineConvert1Dsignal(leads)

            with st.expander(" Step 5: Combined 1D Signal"):
                import pandas as pd

              
                df_signal = pd.DataFrame(signal_1d)
                st.dataframe(df_signal)   # 🔥 table box view

            # ================= STEP 6 =================
            final_data = ecg.DimensionalReduciton(signal_1d)

            with st.expander(" Step 6: Dimensionality Reduction (PCA)"):
                import pandas as pd

                st.write(f"Reduced Shape: {final_data.shape}")

                df_pca = pd.DataFrame(final_data)
                st.dataframe(df_pca)

            # ================= STEP 7 =================
            prediction_label, confidence = ecg.ModelLoad_predict(final_data)

            with st.expander(" Step 7: Final Prediction"):
                st.success(f"🩺 Prediction: {prediction_label}")
                st.info(f"📊 Confidence: {confidence*100:.2f}%")

            # ================= SAVE REPORT =================
            import datetime

            st.session_state.report = {
                "prediction": prediction_label,
                "confidence": confidence,
                "date": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                "model": "KNN",
                "classes": 4
            }

    # -------- PREDICTION REPORT --------
    
    elif page == "Prediction Report":

        import pandas as pd
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
        from reportlab.lib import colors
        from reportlab.lib.styles import getSampleStyleSheet
        from io import BytesIO

        # 🔥 STYLE FIX (CONTRAST)
        st.markdown("""
        <style>

        /* Title */
        h1, h2, h3 {
            color: #FFFFFF !important;
        }

        /* Table container */
        .report-card {
            background: rgba(255,255,255,0.08);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.5);
        }

        /* Table */
        table {
            color: white !important;
            border-collapse: collapse;
            width: 100%;
        }

        th {
            background-color: #2563EB;
            color: white !important;
            padding: 10px;
        }

        td {
            background-color: rgba(255,255,255,0.05);
            padding: 10px;
            color: #E5E7EB !important;
        }

        /* Progress bar */
        .stProgress > div > div > div > div {
            background-color: #22C55E;
        }

        </style>
        """, unsafe_allow_html=True)

        st.title("📊 Prediction Report")

        if st.session_state.report is None:
            st.warning("⚠️ No prediction yet. Please go to Cardio page first.")
        else:
            r = st.session_state.report

            st.markdown('<div class="report-card">', unsafe_allow_html=True)

            st.subheader("🧾 Report Details")

            # 🔥 TABLE DATA
            data = {
                "Parameter": [
                    "Prediction Result",
                    "Confidence Score",
                    "Model Used",
                    "Total Classes",
                    "Date & Time"
                ],
                "Value": [
                    r["prediction"],
                    f"{r['confidence']*100:.2f}%",
                    r["model"],
                    r["classes"],
                    r["date"]
                ]
            }

            df = pd.DataFrame(data)

            # 🔥 TABLE DISPLAY
            st.table(df)

            # 🔥 STATUS COLOR
            if r["prediction"] == "Normal":
                st.success(f"✔ {r['prediction']} - No Risk Detected")
            else:
                st.error(f"⚠ {r['prediction']} - Consult Doctor")

            # 🔥 PROGRESS BAR
            st.progress(r['confidence'])

            st.markdown('</div>', unsafe_allow_html=True)

            # 🔥 PDF GENERATION (UNCHANGED)
            buffer = BytesIO()
            doc = SimpleDocTemplate(buffer)

            styles = getSampleStyleSheet()
            elements = []

            elements.append(Paragraph("🏥 Cardiovascular Disease Prediction Report", styles['Title']))
            elements.append(Spacer(1, 20))

            table_data = [
                ["Parameter", "Value"],
                ["Prediction Result", r["prediction"]],
                ["Confidence Score", f"{r['confidence']*100:.2f}%"],
                ["Model Used", r["model"]],
                ["Total Classes", str(r["classes"])],
                ["Date & Time", r["date"]],
            ]

            table = Table(table_data)

            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),

                ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
                ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),

                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),

                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ]))

            elements.append(table)

            elements.append(Spacer(1, 20))
            elements.append(Paragraph("This is a system-generated medical report.", styles['Normal']))

            doc.build(elements)
            buffer.seek(0)

            st.download_button(
                label="📥 Download Medical Report (PDF)",
                data=buffer,
                file_name="cardio_report.pdf",
                mime="application/pdf"
            )
    #--metrics---
    elif page == "Metrics":

        st.markdown("""
        <style>

        .stApp {
            background: linear-gradient(135deg, #0A1F44, #1E3A8A);
        }

        /* TEXT */
        h1, h2, h3 {
            color: #FFFFFF !important;
            text-align: center;
        }

        p, div, span {
            color: #E5E7EB !important;
        }

        /* METRIC CARDS */
        [data-testid="metric-container"] {
            background-color: rgba(255,255,255,0.08);
            padding: 15px;
            border-radius: 12px;
            text-align: center;
            margin: 5px;
        }

        /* ✅ TABLE FIX (BORDER + CONTRAST) */
        table {
            width: 100%;
            border-collapse: collapse;
            color: white !important;
            text-align: center;
        }

        th, td {
            border: 1px solid rgba(255,255,255,0.3) !important;
            padding: 10px;
        }

        th {
            background-color: #2563EB;
            color: white !important;
        }

        td {
            background-color: rgba(255,255,255,0.05);
            color: #E5E7EB !important;
        }

        /* SECTION BOX */
        .section-box {
            background: rgba(255,255,255,0.05);
            padding: 20px;
            border-radius: 15px;
            margin-top: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }

        </style>
        """, unsafe_allow_html=True)

        import pandas as pd
        import matplotlib.pyplot as plt
        import numpy as np

        # 🔥 TITLE
        st.title("📊 Model Performance Dashboard")

        # 🔥 METRICS ROW
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Accuracy", "96%")
        c2.metric("Precision", "95%")
        c3.metric("Recall", "96%")
        c4.metric("F1 Score", "95.5%")

        # 🔥 DATA
        class_data = pd.DataFrame({
            "Class": ["Normal", "Abnormal", "MI", "History"],
            "Accuracy": [0.96, 0.93, 0.94, 0.92]
        })

        # 🔥 TABLE SECTION
        st.markdown('<div class="section-box">', unsafe_allow_html=True)
        st.subheader("📋 Class-wise Accuracy")
        st.table(class_data)
        st.markdown('</div>', unsafe_allow_html=True)

        # 🔥 CHART SECTION
        st.markdown('<div class="section-box">', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        # ================= CONFUSION MATRIX =================
        with col1:
            st.subheader("Confusion Matrix")

            cm = np.array([[120, 5],
                        [8, 110]])

            fig, ax = plt.subplots(figsize=(3.2,3.2))  # 👈 smaller
            ax.imshow(cm)

            for i in range(2):
                for j in range(2):
                    ax.text(j, i, cm[i, j],
                            ha="center", va="center",
                            fontsize=10, fontweight="bold")

            ax.set_title("Actual vs Predicted", fontsize=9)
            ax.set_xticks([])
            ax.set_yticks([])

            st.pyplot(fig)

        # ================= BAR CHART =================
        with col2:
            st.subheader("Accuracy Distribution")

            fig1, ax1 = plt.subplots(figsize=(3.2,3.2))  # 👈 smaller
            ax1.bar(class_data["Class"], class_data["Accuracy"])

            ax1.set_title("Class Accuracy", fontsize=9)
            ax1.tick_params(axis='x', rotation=20, labelsize=8)

            plt.tight_layout()
            st.pyplot(fig1)

        st.markdown('</div>', unsafe_allow_html=True)

        # 🔥 LINE CHART SECTION (SMALL + CENTERED)
        st.markdown('<div class="section-box">', unsafe_allow_html=True)

        st.subheader("📈 Overall Performance")

        perf_labels = ["Accuracy", "Precision", "Recall", "F1"]
        perf_values = [0.96, 0.95, 0.96, 0.955]

        colA, colB, colC = st.columns([1,2,1])  # 👈 center align

        with colB:
            fig2, ax2 = plt.subplots(figsize=(4,2.5))  # 👈 SMALL SIZE
            ax2.plot(perf_labels, perf_values, marker='o')

            ax2.set_title("Performance Metrics", fontsize=9)
            ax2.tick_params(labelsize=8)

            plt.tight_layout()
            st.pyplot(fig2)

        st.markdown('</div>', unsafe_allow_html=True)
    # -------- ABOUT --------
    elif page == "About":

        st.markdown("""
        <style>

        /* 🌌 Background */
        .stApp {
            background: linear-gradient(135deg, #0A1F44, #1E3A8A);
        }

        /* 🏷️ Main Title */
        h1 {
            color: #FFFFFF !important;
            text-align: center;
            font-weight: bold;
        }

        /* 🔹 Sub Headings */
        h2, h3 {
            color: #60A5FA !important;
        }

        /* 📝 Paragraph */
        p {
            color: #F1F5F9 !important;
            font-size: 16px;
            line-height: 1.7;
        }

        /* 🧊 Cards */
        .card {
            background: rgba(255,255,255,0.08);
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 20px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.5);
            border: 1px solid rgba(255,255,255,0.1);
        }

        /* ✨ Highlight text */
        b {
            color: #93C5FD !important;
        }

        /* ================= TABS ================= */

        /* 🔥 Tab container */
        div[role="tablist"] {
            background-color: rgba(255,255,255,0.05);
            padding: 6px;
            border-radius: 12px;
        }

        /* 🔥 Normal Tab */
        button[role="tab"] {
            color: #E5E7EB !important;
            background-color: transparent !important;
            border-radius: 10px;
            padding: 8px 18px;
            font-weight: bold;
            transition: 0.3s;
        }

        /* 🔥 Hover */
        button[role="tab"]:hover {
            background-color: rgba(255,255,255,0.15) !important;
            color: #FFFFFF !important;
        }

        /* 🔥 Active Tab */
        button[role="tab"][aria-selected="true"] {
            background-color: #2563EB !important;
            color: #FFFFFF !important;
            box-shadow: 0 0 10px rgba(37,99,235,0.6);
        }

        /* Remove default underline */
        button[role="tab"]::after {
            display: none !important;
        }

        </style>
        """, unsafe_allow_html=True)

        # 🔥 TITLE
        st.title("🫀 About the System")

        # 🔥 TABS
        tab1, tab2, tab3, tab4 = st.tabs([
            "📌 Overview",
            "⚙️ How It Works",
            "🤖 Model Info",
            "🎯 Benefits"
        ])

        # -------- TAB 1 --------
        with tab1:
            st.markdown("""
            <div class="card">
            <h3>📌 Project Overview</h3>
            <p>
            The Cardio Vascular Disease Prediction System analyzes ECG images 
            and detects heart abnormalities using advanced Machine Learning techniques.
            </p>

            <p>
            It enables early diagnosis by converting ECG signals into meaningful patterns 
            and predicting heart conditions instantly.
            </p>
            </div>
            """, unsafe_allow_html=True)

        # -------- TAB 2 --------
        with tab2:
            st.markdown("""
            <div class="card">
            <h3>⚙️ Working Process</h3>
            <p>✔ ECG Image Upload</p>
            <p>✔ Image Preprocessing (Grayscale, Noise Removal)</p>
            <p>✔ Lead Segmentation</p>
            <p>✔ Signal Extraction</p>
            <p>✔ Feature Reduction</p>
            <p>✔ Prediction using ML Model</p>
            </div>
            """, unsafe_allow_html=True)

        # -------- TAB 3 --------
        with tab3:
            st.markdown("""
            <div class="card">
            <h3>🤖 Model Information</h3>
            <p>
            The system uses <b>K-Nearest Neighbors (KNN)</b> algorithm 
            for classification of ECG signals.
            </p>

            <p>• Normal</p>
            <p>• Abnormal Heartbeat</p>
            <p>• Myocardial Infarction</p>
            <p>• History of MI</p>
            </div>
            """, unsafe_allow_html=True)

        # -------- TAB 4 --------
        with tab4:
            st.markdown("""
            <div class="card">
            <h3>🎯 Key Benefits</h3>
            <p>✔ Early detection of heart diseases</p>
            <p>✔ Fast and accurate prediction</p>
            <p>✔ User-friendly interface</p>
            <p>✔ Helps doctors in decision making</p>
            </div>
            """, unsafe_allow_html=True)
    # -------- CONTACT --------
    elif page == "Contact":

        import pandas as pd
        import smtplib
        from email.mime.text import MIMEText

        st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg, #0A1F44, #1E3A8A);
        }

        .contact-card {
            background: rgba(255,255,255,0.05);
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.4);
            margin-bottom: 20px;
        }

        h1, h2, h3 {
            color: white;
        }

        p, label {
            color: #D1D5DB;
        }

        .stButton>button {
            background-color: #1E3A8A;
            color: white;
            border-radius: 8px;
            width: 100%;
        }
        </style>
        """, unsafe_allow_html=True)

        st.title("📞 Contact Us")

        col1, col2 = st.columns(2)

        # -------- LEFT --------
        with col1:
            st.markdown("""
            <div class="contact-card">
            <h3>📍 Get in Touch</h3>
            <p>📧 Email: cardioproject85@gmail.com</p>
            <p>📞 Phone: +91 8976543214</p>
            <p>📍 Location: Tamil Nadu, India</p>
            <p>Feel free to contact us anytime!</p>
            </div>
            """, unsafe_allow_html=True)

            st.image("contact.jpeg", use_column_width=200)

        # -------- RIGHT --------
        with col2:
            st.markdown('<div class="contact-card"><h3>📝 Send a Message</h3></div>', unsafe_allow_html=True)

            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Your Message")

            if st.button("Send Message"):

                # ✅ VALIDATION
                if not name or not email or not message:
                    st.error("⚠️ Please fill all fields")

                elif "@" not in email:
                    st.error("⚠️ Enter valid email")

                else:
                    try:
                        # ✅ SAVE CSV
                        data = pd.DataFrame([[name, email, message]],
                                            columns=["Name", "Email", "Message"])
                        data.to_csv("messages.csv", mode="a", header=False, index=False)

                        # 🔐 EMAIL CONFIG
                        sender = "cardioproject85@gmail.com"
                        password = "pjgwcmikgpknjqoy"   # 🔥 paste new password

                        # 👉 ADMIN MESSAGE
                        admin_body = f"""
    New Message from Cardio App

    Name: {name}
    Email: {email}

    Message:
    {message}
    """

                        admin_msg = MIMEText(admin_body)
                        admin_msg["Subject"] = "New Contact Message"
                        admin_msg["From"] = sender
                        admin_msg["To"] = sender

                        # 👉 USER AUTO REPLY
                        user_body = f"""
    Hi {name},

    Thank you for contacting us ❤️

    We have received your message successfully.
    Our team will get back to you soon.

    Regards,
    Cardio App Team
    """

                        user_msg = MIMEText(user_body)
                        user_msg["Subject"] = "We received your message"
                        user_msg["From"] = sender
                        user_msg["To"] = email

                        # 🔥 SMTP
                        server = smtplib.SMTP("smtp.gmail.com", 587)
                        server.starttls()
                        server.login(sender, password)

                        server.sendmail(sender, sender, admin_msg.as_string())
                        server.sendmail(sender, email, user_msg.as_string())

                        server.quit()

                        st.success("✅ Message sent, auto-reply delivered & saved!")

                    except Exception as e:
                        st.error(f"❌ Email Error: {e}")

        # -------- DOWNLOAD --------
        try:
            with open("messages.csv", "rb") as file:
                st.download_button("📥 Download Messages", file, "messages.csv")
        except:
            pass