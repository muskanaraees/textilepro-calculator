import streamlit as st

st.set_page_config(
    page_title="TextilePro Calculator",
    page_icon="🧵",
    layout="wide"
)

# Professional Design
st.markdown("""
<style>
.stApp {
    background-color: #F5F8FA;
}
h1, h2, h3 {
    color: #12304A;
}
section[data-testid="stSidebar"] {
    background-color: #12304A;
}
section[data-testid="stSidebar"] * {
    color: white;
}
.stButton > button {
    background-color: #008C95;
    color: white;
    border-radius: 8px;
    border: none;
    font-weight: bold;
}
.stButton > button:hover {
    background-color: #006B73;
    color: white;
}
div[data-testid="stMetric"] {
    background-color: white;
    padding: 15px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.title("🧵 TextilePro Calculator")
st.caption("Your Textile Engineering Calculation Platform")
st.markdown("---")

# Sidebar
st.sidebar.title("🧵 TextilePro")
st.sidebar.caption("Engineering Tools")

calculator = st.sidebar.selectbox(
    "Select Calculator",
    [
        "Home",
        "Cotton Waste Calculator",
        "Yarn Count Calculator",
        "Yarn Count Conversion",
        "Fabric GSM Calculator",
        "Production Calculator",
        "Machine Efficiency Calculator"
    ]
)

# Home
if calculator == "Home":
    st.header("Welcome to TextilePro Calculator")

    st.subheader("About the Developer")
    st.write("**Muskan Abdul Raees**")
    st.write("Textile Engineering Student")
    st.write("Developer of TextilePro Calculator")

    st.write(
        "This application is designed to help "
        "Textile Engineering students perform basic "
        "textile calculations easily and accurately."
    )

    st.markdown("---")
    st.subheader("Available Calculators")

    col1, col2 = st.columns(2)

    with col1:
        st.info("🧶 Cotton Waste Calculator")
        st.info("📏 Yarn Count Calculator")
        st.info("🔄 Yarn Count Conversion")

    with col2:
        st.info("🧵 Fabric GSM Calculator")
        st.info("🏭 Production Calculator")
        st.info("⚙️ Machine Efficiency Calculator")

    st.markdown("---")
    st.write("Select a calculator from the sidebar to begin.")

# Cotton Waste
elif calculator == "Cotton Waste Calculator":
    st.header("Cotton Waste Calculator")

    total = st.number_input(
        "Total Cotton Weight (kg)",
        min_value=0.0,
        value=100.0
    )

    waste = st.number_input(
        "Waste Weight (kg)",
        min_value=0.0,
        value=5.0
    )

    if st.button("Calculate Waste"):
        if total > 0 and waste <= total:
            result = (waste / total) * 100
            st.success(f"Cotton Waste: {result:.2f}%")
        else:
            st.error("Please enter valid weights.")

# Yarn Count
elif calculator == "Yarn Count Calculator":
    st.header("Yarn Count Calculator")

    weight = st.number_input(
        "Yarn Weight (grams)",
        min_value=0.01,
        value=2.0
    )

    length = st.number_input(
        "Yarn Length (meters)",
        min_value=0.01,
        value=1000.0
    )

    if st.button("Calculate Tex"):
        tex = (weight * 1000) / length
        st.success(f"Yarn Count: {tex:.2f} Tex")

# Yarn Count Conversion
elif calculator == "Yarn Count Conversion":
    st.header("Yarn Count Conversion")

    count = st.number_input(
        "Enter Yarn Count",
        min_value=0.01,
        value=20.0
    )

    system = st.selectbox(
        "Select Count System",
        ["Tex", "Denier", "Ne", "Nm"]
    )

    if st.button("Convert"):
        if system == "Tex":
            st.write(f"Denier: {count * 9:.2f}")
            st.write(f"Ne: {590.5 / count:.2f}")
            st.write(f"Nm: {1000 / count:.2f}")

        elif system == "Denier":
            st.write(f"Tex: {count / 9:.2f}")
            st.write(f"Ne: {5315 / count:.2f}")
            st.write(f"Nm: {9000 / count:.2f}")

        elif system == "Ne":
            st.write(f"Tex: {590.5 / count:.2f}")
            st.write(f"Denier: {5315 / count:.2f}")
            st.write(f"Nm: {count * 1.693:.2f}")

        elif system == "Nm":
            st.write(f"Tex: {1000 / count:.2f}")
            st.write(f"Denier: {9000 / count:.2f}")
            st.write(f"Ne: {count / 1.693:.2f}")

# Fabric GSM
elif calculator == "Fabric GSM Calculator":
    st.header("🧵 Fabric GSM Calculator")

    weight = st.number_input(
        "Fabric Weight (grams)",
        min_value=0.01,
        value=150.0
    )

    area = st.number_input(
        "Fabric Area (square meters)",
        min_value=0.01,
        value=1.0
    )

    if st.button("Calculate GSM"):
        gsm = weight / area
        st.success(f"Fabric GSM: {gsm:.2f} g/m²")

# Production
elif calculator == "Production Calculator":
    st.header("Production Calculator")

    production = st.number_input(
        "Production (kg)",
        min_value=0.0,
        value=100.0
    )

    hours = st.number_input(
        "Working Hours",
        min_value=0.01,
        value=2.0
    )

    if st.button("Calculate Production"):
        rate = production / hours
        st.success(f"Production Rate: {rate:.2f} kg/hour")

# Machine Efficiency
elif calculator == "Machine Efficiency Calculator":
    st.header("Machine Efficiency Calculator")

    actual = st.number_input(
        "Actual Production",
        min_value=0.0,
        value=80.0
    )

    theoretical = st.number_input(
        "Theoretical Production",
        min_value=0.01,
        value=100.0
    )

    if st.button("Calculate Efficiency"):
        if actual <= theoretical:
            efficiency = (actual / theoretical) * 100
            st.success(f"Machine Efficiency: {efficiency:.2f}%")
        else:
            st.warning(
                "Actual production exceeds theoretical production. "
                "Please check your values."
            )

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("Developed by Muskan Abdul Raees")
st.sidebar.caption("Textile Engineering Project")
