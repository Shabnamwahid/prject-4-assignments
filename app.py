import streamlit as st

# Website Title
st.sidebar.title("Karachi Brands Collection 🛍️")

# Navigation
pages = st.sidebar.radio("Go to", ["Home", "Dresses", "Cart", "Contact"])

# Ladies' Clothing Collection with Realistic Images
dresses = [
    {"name": "Sana Safinaz - Summer Lawn", "price": 5500, "image": "https://masterreplicapakistan.com/wp-content/uploads/2021/04/Eden-Robe.jpg"},
    {"name": "Khaadi - Embroidered Kurta", "price": 4200, "image": "https://th.bing.com/th/id/OIP._u957MN1woscTvbO_hxOtgHaLG?w=1067&h=1600&rs=1&pid=ImgDetMain"},
    {"name": "Gul Ahmed - Digital Print Suit", "price": 4800, "image": "https://th.bing.com/th/id/OIP.x5lxUtAqaw8-Lqag1hGK1gHaLH?rs=1&pid=ImgDetMain"},
    {"name": "Maria B - Luxury Pret", "price": 8500, "image": "https://th.bing.com/th/id/OIP.j0ALkcCkcIahx5JZc2xDMgHaLH?rs=1&pid=ImgDetMain"}
]

# Session State for Cart
if "cart" not in st.session_state:
    st.session_state.cart = []

# Home Page with Stylish Image

    st.title("✨ Karachi Brands Collection ✨")
    st.subheader("Discover exclusive ladies' fashion from top Karachi brands!")
    st.write("Shop the latest trends from **Sana Safinaz, Khaadi, Gul Ahmed, Maria B,** and many more!")
if pages == "Home":
    st.image("https://www.stylesgap.com/wp-content/uploads/2022/02/M-Prints-Maria-B-Printed-Embroidered-Lawn-Collection-2023-2024-24.jpg", 
         width=300,
         use_container_width=True)

# Dresses Page with Realistic Images
elif pages == "Dresses":
    st.title("👗 Ladies' Clothing Collection")
    for dress in dresses:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(dress["image"], width=150)
        with col2:
            st.subheader(dress["name"])
            st.write(f"💰 Price: Rs {dress['price']}")
            if st.button(f"🛒 Add {dress['name']} to Cart", key=dress["name"]):
                st.session_state.cart.append(dress)
                st.success(f"✅ Added {dress['name']} to Cart!")

# Cart Page
elif pages == "Cart":
    st.title("🛍️ Your Shopping Cart")
    if not st.session_state.cart:
        st.write("🛒 Your cart is empty!")
    else:
        total_price = 0
        for item in st.session_state.cart:
            st.write(f"✅ {item['name']} - Rs {item['price']}")
            total_price += item["price"]
        st.subheader(f"🛒 Total: Rs {total_price}")
        if st.button("🛍️ Checkout"):
            st.success("🎉 Thank you for shopping with us!")

# Contact Page
elif pages == "Contact":
    st.title("📞 Contact Us")
    st.write("📍 **Location:** Karachi, Pakistan")
    st.write("📧 **Email:** info@karachibrands.com")
    st.write("📞 **Phone:** +92 300 1234567")
