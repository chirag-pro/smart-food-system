import streamlit as st
import difflib

Menu = {
    "Pizza": 120,
    "Momos": 80,
    "Samosa": 20,
    "Idli": 20,
    "Vada Pav": 30,
    "Soya Champ": 100,
    "White Sauce Pasta": 120,
    "Red Sauce Pasta": 130,
    "Ras Malai": 40,
    "Rabri": 30,
    "Gulab Jamun": 20
}

if "cart" not in st.session_state:
    st.session_state.cart = {}

st.title("🍽️ Smart Food Ordering Kiosk")

st.subheader("Select Order Type")
order_type = st.radio("", ["Dine-in 🍽️", "Takeaway 🛍️", "Pickup 🚗"])

arrival_time = st.text_input("Enter arrival time (optional, in minutes):")

st.subheader("📜 Menu")

cols = st.columns(3)

for i, (item, price) in enumerate(Menu.items()):
    with cols[i % 3]:
        st.markdown(f"### {item}")
        st.write(f"Rs{price}")
        if st.button(f"➕ Add {item}", key=item):
            st.session_state.cart[item] = st.session_state.cart.get(item, 0) + 1

st.subheader("🔍 Search Item")
search = st.text_input("Type item name")

if search:
    matches = difflib.get_close_matches(search.title(), Menu.keys(), n=1, cutoff=0.6)
    if matches:
        st.success(f"Did you mean: {matches[0]}?")
        if st.button("Add Suggested Item"):
            st.session_state.cart[matches[0]] = st.session_state.cart.get(matches[0], 0) + 1
    else:
        st.error("Item not found")

st.subheader("🛒 Your Cart")

total = 0

if st.session_state.cart:
    for item, qty in st.session_state.cart.items():
        price = Menu[item]
        st.write(f"{item} x{qty} = Rs{price * qty}")
        total += price * qty

    gst = total * 0.05
    final_total = total + gst

    st.markdown(f"### Subtotal: Rs{total}")
    st.markdown(f"### GST (5%): Rs{gst:.2f}")
    st.markdown(f"## 💰 Total: Rs{final_total:.2f}")

    if st.button("❌ Clear Cart"):
        st.session_state.cart = {}

    if st.button("✅ Place Order"):
        st.success("🎉 Order Placed Successfully!")
        st.write(f"Order Type: {order_type}")
        if arrival_time:
            st.write(f"Arrival Time: {arrival_time} minutes")
        st.session_state.cart = {}

else:
    st.write("Cart is empty.")
