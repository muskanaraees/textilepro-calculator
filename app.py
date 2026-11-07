import streamlit as st

st.set_page_config(
    page_title="TextilePro Calculator",
    page_icon="🧵",
    layout="wide"
)

st.title("🧵 TextilePro Calculator")
st.write("A Complete Textile Engineering Calculator")

st.sidebar.title("Select Calculator")

calculator = st.sidebar.selectbox(
    "Choose a calculation",
    [
        "Cotton Waste Calculator",
        "Yarn Count Calculator",
        "Fabric GSM Calculator",
        "Production Calculator",
        "Machine Efficiency Calculator"
    ]
)

if calculator == "Cotton Waste Calculator":
    st.header("Cotton Waste Calculator")

    input_weight = st.number_input(
        "Enter Input Cotton Weight (kg)", min_value=0.0
    )
    waste_weight = st.number_input(
        "Enter Waste Weight (kg)", min_value=0.0
    )

    if st.button("Calculate Waste"):
        if input_weight > 0 and waste_weight <= input_weight:
            waste_percent = (waste_weight / input_weight) * 100
            st.success(f"Cotton Waste: {waste_percent:.2f}%")
        else:
            st.error("Please enter valid weights.")

elif calculator == "Yarn Count Calculator":
    st.header("Yarn Count Calculator")
    weight = st.number_input("Enter Yarn Weight (grams)", min_value=0.0)
    length = st.number_input("Enter Yarn Length (meters)", min_value=0.0)

    if st.button("Calculate Yarn Count"):
        if weight > 0 and length > 0:
            tex = (weight * 1000) / length
            st.success(f"Yarn Count: {tex:.2f} Tex")
        else:
            st.error("Enter valid values.")

elif calculator == "Fabric GSM Calculator":
    st.header("Fabric GSM Calculator")
    weight = st.number_input("Fabric Weight (grams)", min_value=0.0)
    area = st.number_input("Fabric Area (square meters)", min_value=0.0)

    if st.button("Calculate GSM"):
        if weight > 0 and area > 0:
            gsm = weight / area
            st.success(f"Fabric GSM: {gsm:.2f} g/m²")
        else:
            st.error("Enter valid values.")

elif calculator == "Production Calculator":
    st.header("Production Calculator")
    quantity = st.number_input("Production (kg)", min_value=0.0)
    hours = st.number_input("Working Hours", min_value=0.0)

    if st.button("Calculate Production"):
        if quantity > 0 and hours > 0:
            production = quantity / hours
            st.success(f"Production Rate: {production:.2f} kg/hour")
        else:
            st.error("Enter valid values.")

elif calculator == "Machine Efficiency Calculator":
    st.header("Machine Efficiency Calculator")
    actual = st.number_input("Actual Production", min_value=0.0)
    theoretical = st.number_input("Theoretical Production", min_value=0.0)

    if st.button("Calculate Efficiency"):
        if theoretical > 0 and actual <= theoretical:
            efficiency = (actual / theoretical) * 100
            st.success(f"Machine Efficiency: {efficiency:.2f}%")
        else:
            st.error("Please enter valid values.")

st.divider()
st.caption("TextilePro Calculator | Textile Engineering Project")
