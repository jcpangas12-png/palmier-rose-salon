import streamlit as st
import urllib.parse

# 1. Page Configuration & Theme Settings
st.set_page_config(page_title="Palmier Rose Booking Portal", page_icon="💅", layout="centered")

# Elegant Pink/Gold Custom CSS to match a high-end beauty salon profile
st.markdown("""
    <style>
    .main { background-color: #fff5f5; color: #4a2c2c; }
    h1 { color: #d4a373; text-align: center; font-family: 'Georgia', serif; font-weight: bold; }
    p { text-align: center; font-size: 16px; color: #6b5b5b; }
    div.stButton > button:first-child {
        background-color: #d4a373; color: white; font-weight: bold;
        font-size: 18px; border-radius: 20px; width: 100%; height: 50px;
        box-shadow: 0px 4px 10px rgba(212, 163, 115, 0.4); border: none;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌹 Palmier Rose Nail & Beauty Portal 🌹")
st.write("Select your desired treatments below to build your custom appointment request instantly via WhatsApp!")

st.write("---")

# 2. Main Treatments Selection
st.subheader("1. Select Main Treatments")
nail_services = {
    "None": 0,
    "Gel Overlay (Hands) - R250": 250,
    "Acrylic Overlay & Gel Toes Combo - R350": 350,
    "Gel Overlay Combo (Hands & Feet) - R480": 480,
    "Full Sculpting Gel / Polygel Set - R400": 400
}
selected_nail = st.selectbox("Choose a main treatment tier:", list(nail_services.keys()))
total_bill = nail_services[selected_nail]

st.write("---")

# 3. Optional Beauty Add-ons
st.subheader("2. Add Optional Beauty Add-ons")
add_nail_art = st.checkbox("Custom Nail Art (+R60)")
add_pedicure = st.checkbox("Full Spa Pedicure (+R150)")
add_tinting = st.checkbox("Brow & Lash Tinting Combo (+R120)")
add_massage = st.checkbox("30-Minute Professional Massage (+R250)")

selected_addons = []
if add_nail_art:
    total_bill += 60
    selected_addons.append("Custom Nail Art")
if add_pedicure:
    total_bill += 150
    selected_addons.append("Full Spa Pedicure")
if add_tinting:
    total_bill += 120
    selected_addons.append("Brow & Lash Tinting Combo")
if add_massage:
    total_bill += 250
    selected_addons.append("30-Min Massage")

st.write("---")

# 4. Booking Time & Date
st.subheader("3. Preferred Appointment Details")
booking_date = st.text_input("Preferred Date (e.g., Saturday 10 Oct):", value="As soon as possible")
booking_time = st.text_input("Preferred Time (e.g., 11:30 AM):", value="Anytime today")

st.write("---")

# 5. Display Dynamic Bill Total
st.markdown(f"<h2 style='text-align: center; color: #d4a373;'>Total Amount: R{total_bill}</h2>", unsafe_allow_html=True)

# 6. Formatting WhatsApp String Output Logic
addons_text = ", ".join(selected_addons) if selected_addons else "None"

raw_message = (
    f"*🌹 PALMIER ROSE APPOINTMENT REQUEST 🌹*\n"
    f"-------------------------------------\n"
    f"*Main Service:* {selected_nail}\n"
    f"*Add-ons Selected:* {addons_text}\n"
    f"-------------------------------------\n"
    f"*Requested Date:* {booking_date}\n"
    f"*Requested Time:* {booking_time}\n"
    f"-------------------------------------\n"
    f"*Estimated Total:* R{total_bill}\n"
    f"-------------------------------------\n"
    f"_Please check availability and confirm my slot!_"
)

# Safe URL encoding for browser strings
encoded_message = urllib.parse.quote(raw_message)

# Palmier Rose verified WhatsApp Business line
salon_number = "27681103101"
whatsapp_url = f"https://wa.me/{salon_number}?text={encoded_message}"

# Clickable Booking Action Button
st.link_button("💝 REQUEST APPOINTMENT VIA WHATSAPP", whatsapp_url)
