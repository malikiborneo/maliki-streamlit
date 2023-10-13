import streamlit as st
import pandas as pd
import streamlit.components.v1 as components  

# Define the main function
def main():
    st.set_page_config(page_title='Reza Maliki Akbar\'s portfolio' ,layout="wide",page_icon='👨‍🔬')
    # Sidebar
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "About", "Skills", "Projects", "Certifications", "Blog", "Contact"])

    # LinkedIn Embed
    components.html("""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>""")
    linkedin = components.html("""<div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="dark" data-type="VERTICAL" data-vanity="malikiborneo" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://id.linkedin.com/in/malikiborneo?trk=profile-badge">Reza Maliki Akbar</a></div>""")

    st.sidebar.markdown(linkedin, unsafe_allow_html=True)
    
    # Sidebar Links
    st.sidebar.markdown('[GitHub](https://github.com/your_username)')
    st.sidebar.markdown('[Stack Overflow](https://stackoverflow.com/users/your_user_id)')
    st.sidebar.markdown('[Medium](https://medium.com/@your_username)')
    st.sidebar.markdown('Email: your_email@example.com')

    # Page Selection
    if page == "Home":
        home_page()
    elif page == "About":
        about_page()
    # ... other pages will go here

    # Footer
    st.write("© 2023 Reza Maliki Akbar")

def home_page():
    st.title("Welcome to My Portfolio!")
    st.write("Hi, I'm [Your Name]. [Your brief introduction here, such as what you do, your major accomplishments, etc.]")
    
    uploaded_file = st.file_uploader("Upload a CSV/Excel file to visualize", type=["csv", "xlsx"])
    if uploaded_file:
        if uploaded_file.name.endswith('.csv'):
            data = pd.read_csv(uploaded_file)
        else:
            data = pd.read_excel(uploaded_file)
        st.write(data)  # Display the uploaded dataframe

def about_page():
    st.title("About Me")
    st.header("Introduction")
    st.write("[A detailed introduction about yourself, your passion, hobbies, etc.]")
    st.header("Education")
    st.write("[Details about your educational background, degrees, institutions, etc.]")
    st.header("Experience")
    st.write("[Professional experience, internships, roles, responsibilities, etc.]")
    st.header("Other Details")
    st.write("[Any other information you'd like to share, such as awards, languages spoken, etc.]")

if __name__ == "__main__":
    main()
