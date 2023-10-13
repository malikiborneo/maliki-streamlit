from constant import *
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components  

# Define the main function
def main():
    st.set_page_config(page_title='Reza Maliki Akbar\'s portfolio' ,layout="wide", page_icon='👷')
    # Sidebar
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "About", "Projects", "Certifications"])

    # LinkedIn Embed
    #components.html("""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>""")
    #st.sidebar.markdown(components.html("""<div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="dark" data-type="VERTICAL" data-vanity="malikiborneo" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://id.linkedin.com/in/malikiborneo?trk=profile-badge">Reza Maliki Akbar</a></div>"""), unsafe_allow_html=True)
    
    # Sidebar Links
    st.sidebar.markdown('[GitHub](https://github.com/malikiborneo)')
    st.sidebar.markdown('[LinkedIn](https://dk.linkedin.com/in/malikiborneo/)')
    st.sidebar.markdown('E-mail: rezamaliki.akbar@gmail.com')

    # Page Selection
    if page == "Home":
        home_page()
    elif page == "About":
        about_page()
    elif page == "Projects":
        projects_page()
    elif page == "Certifications":
        certifications_page()
    # ... other pages will go here

    # Footer
    st.write("© 2023 Reza Maliki Akbar")

def home_page():
    st.title("Welcome to Reza Maliki Akbar's portfolio!")
    st.write("Hi, I'm Reza Maliki Akbar, you can call me Maliki. [Your brief introduction here, such as what you do, your major accomplishments, etc.]")
    st.subheader('Skills & Tools ⚒️')
    
    skill_col_size = 6  # Assuming you want 6 skills per row, adjust as needed
    rows, cols = len(info['skills']) // skill_col_size, skill_col_size
    skills = iter(info['skills'])
    if len(info['skills']) % skill_col_size != 0:
        rows += 1
    for x in range(rows):
        columns = st.columns(skill_col_size)
        for index_ in range(skill_col_size):
            try:
                columns[index_].button(next(skills))
            except StopIteration:
                break
 #  uploaded_file = st.file_uploader("Upload a CSV/Excel file to visualize", type=["csv", "xlsx"])
# if uploaded_file:
#        if uploaded_file.name.endswith('.csv'):
 #           data = pd.read_csv(uploaded_file)
  #      else:
   #         data = pd.read_excel(uploaded_file)
    #    st.write(data)  # Display the uploaded dataframe

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


def projects_page():
    st.title("Projects")
    st.header("Introduction")
    st.write("[A detailed introduction about yourself, your passion, hobbies, etc.]")
    st.header("Education")
    st.write("[Details about your educational background, degrees, institutions, etc.]")
    st.header("Experience")
    st.write("[Professional experience, internships, roles, responsibilities, etc.]")
    st.header("Other Details")
    st.write("[Any other information you'd like to share, such as awards, languages spoken, etc.]")

def certifications_page():
    st.title("Certifications")
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
