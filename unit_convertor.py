#project 1: unit convertor
#Build a unit convertor using python and streamlit

import streamlit as st
st.markdown(
    """
    <style>
    body{
        background-color: #1e1e2f;
        color: white
    }
    .stApp{
        background-color: linear-gradient(135deg, #bcbcbc, #cfe2f3);
        padding:30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
    h1{
        text-align:center;
        font-size: 36px;
        color:white;
    }
     .stButton > button {
        background: linear-gradient(45deg, #0b5394, rgb(40, 17, 77));
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        transition: 0.3s;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
    }
    .stButton > button:hover {
        background: linear-gradient(45deg, rgb(40, 17, 77), #0b5394);
        transform: scale(1.05);
        color: white;
    }
    .result{
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background-color: rgba(255, 255, 255, 0.1);
        padding:10px;
        color:Blue;
        margin-top: 20px;
        border-radius: 5px;
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
    }
    .footer{
        text-align: center;
        font-size: 14px;
        color:black;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1>Unit Convertor using python and streamlit</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight, and temperature.")
conversion_type=st.sidebar.selectbox("Select the conversion Type",["Length","Weight","Temperature"])

value =st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)

col1,col2=st.columns(2)

if conversion_type=="Length":
    with col1:
        from_unit=st.selectbox("From Unit",["Meter","Kilometer","Centimeter","Millimeter","Micrometer","Nanometer", "Mile","Yard","Foot","Inch","Nautical Mile"])
    with col2:
        to_unit=st.selectbox("To Unit",["Meter","Kilometer","Centimeter","Millimeter","Micrometer","Nanometer", "Mile","Yard","Foot","Inch","Nautical Mile"])
elif conversion_type=="Weight":
    with col1:
        from_unit=st.selectbox("From Unit",["Kilogram","Gram","Milligram","Microgram","Pound","Ounce","Tonne","Stone","Pound","Ounce","Tonne","Stone"])
    with col2:
        to_unit=st.selectbox("To Unit",["Kilogram","Gram","Milligram","Microgram","Pound","Ounce","Tonne","Stone","Pound","Ounce","Tonne","Stone"])
elif conversion_type=="Temperature":
    with col1:
        from_unit=st.selectbox("From Unit",["Celsius","Fahrenheit","Kelvin"])
    with col2:
        to_unit=st.selectbox("To Unit",["Celsius","Fahrenheit","Kelvin"])
def convert_length(value, from_unit, to_unit):
    length_units ={
        'Meter':1, 'Kilometer':0.001, 
        'Centimeter':100, 'Millimeter':1000,
        'Micrometer':1000000, 'Nanometer':1000000000,
        'Mile':1609.34, 'Yard':0.9144, 'Foot':0.3048,
        'Inch':0.0254, 'Nautical Mile':1852
        }

    return value * length_units[from_unit] / length_units[to_unit]
def convert_weight(value, from_unit, to_unit):
    weight_units={
        'Kilogram':1, 'Gram':0.001,
        'Milligram':0.000001, 'Microgram':0.000000001,
        'Pound':0.453592, 'Ounce':0.0283495,
        'Tonne':1000, 'Stone':6.35029
    }
    return value * weight_units[from_unit] / weight_units[to_unit]
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15   
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15

 #button for conversion       
if st.button("⚗️Convert"):
    if conversion_type=="Length":
        result=convert_length(value, from_unit, to_unit)
    elif conversion_type=="Weight":
        result=convert_weight(value, from_unit, to_unit)
    elif conversion_type=="Temperature":
        result=convert_temperature(value, from_unit, to_unit)

    st.markdown(f"<div class='result'>{result} {to_unit}</div>", unsafe_allow_html=True)
st.markdown(
    """
    <div class='footer'>
    <p>Developed by <Link href='https://github.com/nidajumail'>@Nida Jumail</Link></p>
    </div>
    """,
    unsafe_allow_html=True
)
        

    
    
    











