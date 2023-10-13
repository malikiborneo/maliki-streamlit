from constant import *
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components 
import plotly.graph_objects as go 

# Define the main function
def main():
    st.set_page_config(page_title='Reza Maliki Akbar\'s portfolio' , layout="wide", page_icon="👷")
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
    st.image("pictures/RezaMalikiAkbar_Photo.png", caption="Maliki", width=150)
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
    st.subheader('Soft Skills 👔')

    soft_skills = [
        'Problem Solving',
        'Critical Thinking',
        'Analytcal Thinking',
        'Logical',
        'Systematical Thinking',
        'Teamwork',
        'Collaboration',
        'Communication',
        'Adaptability',
        'Attention to Detail',
        'Leadership'
    ]

    num_columns = len(soft_skills)
    columns = st.columns(num_columns)

    for i, softskill in enumerate(soft_skills):
        softskill_html = f"""
        <div style="border: 1px solid #f0f0f0; padding: 8px; border-radius: 4px; text-align: center;">
            {softskill}
        </div>
        """
        columns[i].markdown(softskill_html, unsafe_allow_html=True)
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
    st.header("Education 📖")
    education_data = {
        'Level': ['Vocational High School', 'Associate Degree', 'Bachelor of Engineering', 'Research Exchange (Non-degree)', 'Master'],
        'Institution': ['SMK Negeri 1 Cimahi (STM Negeri Pembangunan Bandung)', 'Politeknik Manufaktur Negeri Bandung (Politeknik Mekanik Swiss-ITB)', 'Institut Teknologi Sepuluh Nopember', 'Kyuwngoon University', 'Monash University'],
        'Field of Study': ['Software Engineering', 'Manufacturing Automation and Mechatronics Engineering', 'Engineering/Applied Physics', 'Aeronautical Engineering', 'Cybersecurity'],
        'Year of Academic': ['2010-2014', '2013-2016', '2017-2020', '2019', '2023-2025']
    }

    education_df = pd.DataFrame(education_data)
    #Reverse order, descending education
    education_df = education_df.iloc[::-1].reset_index(drop=True)
    #st.table(education_df)
    table_html = education_df.to_html(index=False)
    st.markdown(table_html, unsafe_allow_html=True)
    # Display the DataFrame in Streamlit
    #st.write(education_df)
    st.header("Experience")
    st.write("[Professional experience, internships, roles, responsibilities, etc.]")
    st.header("Other Details")
    st.write("[Any other information you'd like to share, such as awards, languages spoken, etc.]")


def projects_page():
    st.title("Projects")
     # Display the main grid of projects
    for i in range(0, len(projects), 3):  # Assuming 3 columns
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(projects):
                project = projects[i + j]
                if cols[j].button("", key=f"img_{i+j}"):  # Empty button as placeholder for image
                    st.session_state.current_project = i + j
                    display_project_details(i + j)
                cols[j].image(project['thumbnail'], use_column_width=True)
                cols[j].write(project['title'])

def display_project_details(index):
    project = projects[index]
    st.title(project['title'])
    st.image(project['thumbnail'], use_column_width=200)
    st.write(project['description'])
    st.markdown(f"[View Project]({project['link']})", unsafe_allow_html=True)  # Add link to the project
    if st.button("Back to Projects"):
        del st.session_state.current_project
        projects_page()

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
    if "current_project" in st.session_state:
        display_project_details(st.session_state.current_project)
    else:
        projects_page()