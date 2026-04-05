import streamlit as st
from database import create_table, add_complaint, get_all_complaints, update_status
from ai_model import categorize_complaint

create_table()

menu = ["Student", "Admin"]
choice = st.sidebar.selectbox("Select User", menu)

# ---------------- STUDENT PAGE ----------------
if choice == "Student":
    st.title("🏫 Hostel / College Complaint App")

    name = st.text_input("Enter your name", key="student_name")
    room = st.text_input("Enter room number", key="student_room")
    complaint_text = st.text_area("Write your complaint", key="student_complaint")

    if st.button("Submit Complaint", key="submit_complaint"):
        if name and room and complaint_text:
            category = categorize_complaint(complaint_text)
            add_complaint(name, room, complaint_text, category)
            st.success("Complaint submitted successfully!")
            st.write("Detected Category:", category)
        else:
            st.warning("Please fill all fields")

# ---------------- ADMIN PAGE ----------------
elif choice == "Admin":
    st.title("Admin Dashboard")

    complaints = get_all_complaints()

    for idx, comp  in enumerate(complaints):
        st.write("ID:", comp[0])
        st.write("Name:", comp[1])
        st.write("Room:", comp[2])
        st.write("Complaint:", comp[3])
        st.write("Category:", comp[4])
        st.write("Status:", comp[5])

        new_status = st.selectbox(
            "Update Status",
            ["Pending", "In Progress", "Resolved"],
            key=f"select_{idx}_{comp[0]}"
        )

        if st.button("Update", key=f"button_{comp[0]}"):
            update_status(comp[0], new_status)
            st.success("Status Updated")

        st.write("---")

    for comp in complaints:
        st.write("ID:", comp[0])
        st.write("Name:", comp[1])
        st.write("Room:", comp[2])
        st.write("Complaint:", comp[3])
        st.write("Category:", comp[4])
        st.write("Status:", comp[5])

        new_status = st.selectbox(
            "Update Status",
            ["Pending", "In Progress", "Resolved"],
            key=f"select_{comp[0]}"
        )

        if st.button("Update", key=f"button_{idx}_{comp[0]}"):
            update_status(comp[0], new_status)
            st.success("Status Updated")

        st.write("---")