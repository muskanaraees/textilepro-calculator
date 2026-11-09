import streamlit as st

st.set_page_config(
    page_title="TextilePro Calculator",
    page_icon="🧵",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #F3F7FA;
}
h1 {color: #123B5D;}
h2, h3 {color: #176B87;}
div.stButton > button {
    background-color: #176B87;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 8px 20px;
}
</style>
""", unsafe_allow_html=True)

st.title("🧵 TextilePro Calculator")
st.subheader("Complete Textile Engineering Calculator")

st.markdown("""
### Welcome to TextilePro!
A simple calculation platform for Textile Engineering students.
""")

st.sidebar.title("⚙️ Calculator Menu")

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

if calculator == "Home":
    

    

    st.divider()

    st.subheader("About the Developer")

    st.markdown("""
    ### Muskan Abdul Raees
    **Textile Engineering Student**

    Developer of TextilePro Calculator.

    This project helps Textile Engineering students
    perform basic textile calculations easily.
    """)

    st.divider()
    st.subheader("Available Calculators")

    col1, col2 = st.columns(2)

    with col1:
        st.info("☁️ Cotton Waste Calculator")
        st.info("🧶 Yarn Count Calculator")
        st.info("🏭 Production Calculator")

    with col2:
        st.info("🧵 Fabric GSM Calculator")
        st.info("⚙️ Machine Efficiency Calculator")

elif calculator == "Cotton Waste Calculator":
    st.header("☁️ Cotton Waste Calculator")

    input_weight = st.number_input(
        "Input Cotton Weight (kg)", min_value=0.0
    )
    waste_weight = st.number_input(
        "Waste Weight (kg)", min_value=0.0
    )

    if st.button("Calculate Waste"):
        if input_weight > 0 and waste_weight <= input_weight:
            result = waste_weight / input_weight * 100
            st.success(f"Waste Percentage: {result:.2f}%")
        else:
            st.error("Enter valid weights.")

    st.caption("Formula: (Waste Weight / Input Weight) × 100")

elif calculator == "Yarn Count Calculator":
    st.header("🧶 Yarn Count Calculator")

    weight = st.number_input("Yarn Weight (grams)", min_value=0.0)
    length = st.number_input("Yarn Length (meters)", min_value=0.0)

    if st.button("Calculate Tex"):
        if weight > 0 and length > 0:
            result = weight * 1000 / length
            st.success(f"Yarn Count: {result:.2f} Tex")
        else:
            st.error("Enter valid values.")

    st.caption("Formula: Tex = Weight (g) × 1000 / Length (m)")
    elif calculator == "Yarn Count Conversion":
        st.subheader("Yarn Count Conversion")

        count = st.number_input("Enter yarn count:", min_value=0.01, value=20.0)
        system = st.selectbox("Select count system:", ["Tex", "Denier", "Ne", "Nm"])

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
            else:
                st.write(f"Tex: {1000 / count:.2f}")
                st.write(f"Denier: {9000 / count:.2f}")
                st.write(f"Ne: {count / 1.693:.2f}")

    elif calculator == "Fabric GSM Calculator":
        st.header("🧵 Fabric GSM Calculator")

    weight = st.number_input("Fabric Weight (grams)", min_value=0.0)
    area = st.number_input("Fabric Area (square meters)", min_value=0.0)

    if st.button("Calculate GSM"):
        if weight > 0 and area > 0:
            result = weight / area
            st.success(f"Fabric GSM: {result:.2f} g/m²")
        else:
            st.error("Enter valid values.")

    st.caption("Formula: GSM = Weight / Area")

elif calculator == "Production Calculator":
    st.header("🏭 Production Calculator")

    quantity = st.number_input("Total Production (kg)", min_value=0.0)
    hours = st.number_input("Working Hours", min_value=0.0)

    if st.button("Calculate Production"):
        if quantity > 0 and hours > 0:
            result = quantity / hours
            st.success(f"Production Rate: {result:.2f} kg/hour")
        else:
            st.error("Enter valid values.")

    st.caption("Formula: Production Rate = Production / Hours")

elif calculator == "Machine Efficiency Calculator":
    st.header("⚙️ Machine Efficiency Calculator")

    actual = st.number_input("Actual Production", min_value=0.0)
    theoretical = st.number_input("Theoretical Production", min_value=0.0)

    if st.button("Calculate Efficiency"):
        if theoretical > 0 and actual <= theoretical:
            result = actual / theoretical * 100
            st.success(f"Machine Efficiency: {result:.2f}%")
        else:
            st.error("Enter valid production values.")

    st.caption("Formula: (Actual Production / Theoretical Production) × 100")

st.divider()

st.markdown("""
<div style="text-align:center; padding:15px;">
    <h4 style="color:#123B5D;">TextilePro Calculator</h4>
    <p>Developed by <b>Muskan Abdul Raees</b></p>
    <p>Textile Engineering Project</p>
</div>
""", unsafe_allow_html=True)
