import streamlit as st

def evaluate_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Include at least one digit.")

    special_characters = "!@#$%^&*"
    if any(c in special_characters for c in password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    return score, feedback


# Streamlit UI
st.set_page_config(page_title="Password Strength Meter")
st.title("🔐 Password Strength Meter")
password = st.text_input("Enter your password", type="password")

if st.button("Check Strength"):
    if password:
        score, feedback = evaluate_password(password)
        if score <= 2:
            st.error("🔴 Password Strength: WEAK")
        elif score <= 4:
            st.warning("🟠 Password Strength: MODERATE")
        else:
            st.success("🟢 Password Strength: STRONG\n\n✅ Great job! Your password is secure.")

        if score < 5:
            st.subheader("🔧 Suggestions to improve your password:")
            for item in feedback:
                st.write(f"- {item}")
    else:
        st.warning("Please enter a password to check.")
