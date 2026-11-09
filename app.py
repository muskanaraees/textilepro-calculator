import streamlit as st

st.set_page_config(
    page_title="TextilePro Calculator",
    page_icon="🧵",
    layout="wide"
)

st.title("🧵 TextilePro Calculator")
st.write("A Complete Textile Engineering Calculation Platform")

st.sidebar.title("TextilePro Menu")

calculator = st.sidebar.selectbox(
    "Select a Section",
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
    st.header("Welcome to TextilePro Calculator")

    st.subheader("About the Developer")
    st.write("**Muskan Abdul Raees**")
    st.write("Textile Engineering Student")
    st.write("Developer of TextilePro Calculator")

    st.write(
        "This application is designed to help "
        "Textile Engineering students perform basic "
        "textile calculations easily."
    )

    st.subheader("Available Calculators")

    st.write("1. Cotton Waste Calculator")
    st.write("2. Yarn Count Calculator")
    st.write("3. Yarn Count Conversion")
    st.write("4. Fabric GSM Calculator")
    st.write("5. Production Calculator")
    st.write("6. Machine Efficiency Calculator")

elif calculator == "Cotton Waste Calculator":
    st.header("Cotton Waste Calculator")

    total_cotton = st.number_input(
        "Enter total cotton weight (kg)",
        min_value=0.0,
        value=100.0
    )

    waste = st.number_input(
        "Enter waste weight (kg)",
        min_value=0.0,
        value=5.0
    )

    if st.button("Calculate Waste"):
        if total_cotton > 0 and waste <= total_cotton:
            percentage = (waste / total_cotton) * 100
            st.success(f"Cotton Waste: {percentage:.2f}%")
        else:
            st.error("Enter valid weights.")

elif calculator == "Yarn Count Calculator":
    st.header("Yarn Count Calculator")

    weight = st.number_input(
        "Enter yarn weight (grams)",
        min_value=0.01,
        value=2.0
    )

    length = st.number_input(
        "Enter yarn length (meters)",
        min_value=0.01,
        value=1000.0
    )

    if st.button("Calculate Tex"):
        tex = (weight * 1000) / length
        st.success(f"Yarn Count: {tex:.2f} Tex")

elif calculator == "Yarn Count Conversion":
    st.header("Yarn Count Conversion")

    count = st.number_input(
        "Enter yarn count",
        min_value=0.01,
        value=20.0
    )

    system = st.selectbox(
        "Select count system",
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

elif calculator == "Fabric GSM Calculator":
    st.header("🧵 Fabric GSM Calculator")

    fabric_weight = st.number_input(
        "Enter fabric weight (grams)",
        min_value=0.01,
        value=150.0
    )

    area = st.number_input(
        "Enter fabric area (square meters)",
        min_value=0.01,
        value=1.0
    )

    if st.button("Calculate GSM"):
        gsm = fabric_weight / area
        st.success(f"Fabric GSM: {gsm:.2f} g/m²")

elif calculator == "Production Calculator":
    st.header("Production Calculator")

    production = st.number_input(
        "Enter production (kg)",
        min_value=0.0,
        value=100.0
    )

    hours = st.number_input(
        "Enter working hours",
        min_value=0.01,
        value=2.0
    )

    if st.button("Calculate Production"):
        rate = production / hours
        st.success(f"Production Rate: {rate:.2f} kg/hour")

elif calculator == "Machine Efficiency Calculator":
    st.header("Machine Efficiency Calculator")

    actual = st.number_input(
        "Enter actual production",
        min_value=0.0,
        value=80.0
    )

    theoretical = st.number_input(
        "Enter theoretical production",
        min_value=0.01,
        value=100.0
    )

    if st.button("Calculate Efficiency"):
        if actual <= theoretical:
            efficiency = (actual / theoretical) * 100
            st.success(f"Machine Efficiency: {efficiency:.2f}%")
        else:
            st.warning(
                "Actual production is greater than theoretical production. "
                "Please check your values."
            )

st.sidebar.markdown("---")
st.sidebar.caption("Developed by Muskan Abdul Raees")
