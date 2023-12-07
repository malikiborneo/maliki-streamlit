from constant import *
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components 
#import plotly.graph_objects as go 

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
    st.sidebar.markdown('[Air Quality Data Analytics Showcase](https://maliki-airquality.streamlit.app/)')

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
    # [My commitment to learning took me to the RevoU bootcamp for Full Stack Data Analytics, where I not only completed the program but also earned a full scholarship. Teamwork is close to my heart, and I've spearheaded robotics projects among other initiatives. My diverse experiences range from collaborating with the Indonesian Navy to developing smart vehicles and pioneering in farming. Additionally, I've taken on international projects, like my work on drones in South Korea. Skilled with tools like Matlab and LabView, I can visualize data effectively, and I'm adept at coding in Python and Java. Beyond these, I excel in problem-solving, sharing insights, and leading teams to success. Now, I'm steering my path towards a new ambition: to excel as a data analyst or delve into data science. With my combined expertise in robots, defense, electronics, and the foundational knowledge from RevoU, I'm eager to bring a unique perspective to the data realm.]
    st.subheader("Hi, I'm Reza Maliki Akbar, you can call me Maliki.")

    st.write("My passion for innovation and technology has led me to diverse experiences, from robotics to data analytics.")
    
    st.write("I've collaborated with esteemed institutions like the Indonesian Navy, developed smart vehicles, and ventured into smart farming. My work isn't limited to Indonesia; I've taken on international challenges, such as drone development in South Korea.")
    
    st.write("My skills aren't just academic. While I'm proficient with Python, Tableau, and LookerStudio, I also value teamwork, problem-solving, and leadership. I've led teams, shared insights, and always aimed for success.")
    
    st.write("Recently, I completed the Full Stack Data Analytics program at RevoU, a notable achievement made even sweeter by earning a full scholarship. Now, I'm setting my sights on a new goal: to make my mark in data analytics and data science. With my diverse background and dedication, I'm excited to bring a fresh perspective to the world of data.")
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
        'Analytical Thinking',
        'Logical Thinking',
        'Systematic Thinking',
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
    st.header("Experience 🗂️")
    
    # Terma A/S Experience
    with st.expander("Field Service Engineer - [Terma A/S](https://www.terma.com/)", expanded=False):
        st.write("Duration: April 2021-April 2023")
        st.markdown("""
        - Handled systems integration of the combat management system and troubleshooting.
        - Collaborated with diverse stakeholders.
        - Produced analytical engineering and RMA reports.
        """)

    # Mechatronics and Industrial Automation Research Centre Experience
    with st.expander("Engineering Analyst - [Mechatronics and Industrial Automation Research Centre, ITS](https://riset.its.ac.id/mechatronics/)", expanded=False):
        st.write("Duration: February 2020-April 2021")
        st.markdown("""
        - Analyzed system requirements.
        - Oversaw programming, system modeling, and simulations.
        - Led and mentored interns and students.
        """)

    # Nixtrain.com Experience
    with st.expander("Freelance IT Tutor - [Nixtrain.com](https://nixtrain.com/)", expanded=False):
        st.write("Duration: August 2020-April 2021")
        st.markdown("""
        - Imparted knowledge on computer networking.
        - Assessed student performances.
        """)

    # Directorate of Metrology Experience
    with st.expander("Metrology and Instrumentation Engineer - [Directorate of Metrology, Ministry of Trade of the Republic of Indonesia](https://metrologi.kemendag.go.id/)", expanded=False):
        st.write("Duration: July-August 2018")
        st.markdown("""
        - Engaged in calibration and verification processes of measurement equipment.
        - Identified, analyzed, and resolved lab-related issues.
        - Developed an innovative wireless hygrometer system.
        """)

    # CV. Accelvico Experience
    with st.expander("System Engineer - CV. Accelvico", expanded=False):
        st.write("Duration: November 2016-March 2017")
        st.markdown("""
        - Analyzed system requirements and provided solutions.
        - Engaged in programming, modeling, and simulations.
        - Established communication channels with end-users.
        """)

    # PT. Astra Otoparts Tbk Experience
    with st.expander("Mechatronics Engineer Intern - [PT. Astra Otoparts Tbk – Engineering Development Centre Division](https://www.aop-edc.com)", expanded=False):
        st.write("Duration: March-December 2015")
        st.markdown("""
        - Led a team focused on developing automation control systems.
        - Collaborated on web information management systems.
        - Contributed to the development of battery management systems.
        """)

    # PT. Walden Global Services Experience
    with st.expander("Web Developer Intern - [PT. Walden Global Services](https://wgs.co.id)", expanded=False):
        st.write("Duration: July-August 2013")
        st.markdown("""
        - Developed web fullingua.com, a language course website.
        - Designed and built the database.
        - Customized template and plugin WordPress.
        """)
    #st.header("Other Details")
    #st.write("[Any other information you'd like to share, such as awards, languages spoken, etc.]")


def projects_page():
    st.title("Projects")
    st.write("_[Please double click the button to have better view and performance]_")
    # Display the main grid of projects
    if "current_project" in st.session_state:
        display_project_details(st.session_state.current_project)
    else:
        # Display the main grid of projects
        for i in range(0, len(projects), 3):  # Assuming 3 columns
            cols = st.columns(3)
            for j in range(3):
                if i + j < len(projects):
                    project = projects[i + j]
                    cols[j].image(project['thumbnail'], use_column_width=True)
                    cols[j].markdown(f"**{project['title']}**", unsafe_allow_html=True)
                    
                    # Button to navigate to project details
                    if cols[j].button(f"Go to {project['title']}", key=f"img_{i+j}"):
                        st.session_state.current_project = i + j
                        display_project_details(i + j)


def display_project_details(index):
    project = projects[index]
    st.subheader(project['title'])
    st.image(project['thumbnail'], use_column_width=True)
    st.write(project['description'])
    st.markdown(f"[View Project]({project['link']})", unsafe_allow_html=True)
    
    if st.button("Back to Projects"):
        del st.session_state.current_project
        projects_page()

def certifications_page():
    st.title("Certifications")
    certifications = [
        {"name": "RevoU Full Stack Data Analytics", "organization":"RevoU", "year": "2023"},
        {"name": "USINDO GRASP Critical Thinking & Digital Literacy Course", "organization":"USINDO", "year": "2023"},
        {"name": "Deep Learning", "organization": "Nvidia Deep Learning Institute", "year": "2022"},
        {"name": "CCNA Network Engineer", "organization": "Digitalent Scholarship", "year": "2022"},
        {"name": "Scrum Fundamentals Certified", "organization": "SCRUMstudy", "year": "2021"},
        {"name": "Agile Development Using Scrum Framework", "organization": "Sanbercode", "year": "2021"},
        {"name": "AWS Cloud Foundations and Developing", "organization":"Amazon Web Services", "year": "2021"},
        {"name": "Certified Data Scientist (R Language)", "organization": "DQLab", "year": "2021"},
        {"name": "R Fundamental for Data Science", "organization": "DQLab", "year": "2021"},
        {"name": "Data Visualization in Data Science using R", "organization": "DQLab", "year": "2021"},
        {"name": "Data Science in Marketing: Customer Segmentation", "organization": "DQLab", "year": "2021"},
        {"name": "Statistics using R for Data Science", "organization": "DQLab", "year": "2021"},
        {"name": "Project Machine Learning for Retail with R: Product Packaging", "organization": "DQLab", "year": "2021"},
        {"name": "Introduction to Data Science with R", "organization": "DQLab", "year": "2021"},
        {"name": "Introduction to Data Science with Python", "organization": "DQLab", "year": "2021"},
        {"name": "Fundamental SQL Using SELECT Statement", "organization": "DQLab", "year": "2021"},
        {"name": "Project: Data Scientist Assessment Using R", "organization": "DQLab", "year": "2021"},
        {"name": "Project Analisa Klasifikasi Pinjaman untuk Sektor UMKM", "organization": "DQLab", "year": "2021"},
        {"name": "Intermediate Machine Learning", "organization": "Dicoding", "year": "2021"},
        {"name": "Practical DevOps IBM Cloud", "organization": "Dicoding", "year": "2021"},
        {"name": "Dart Programming and Development", "organization": "Dicoding", "year": "2021"},
        {"name": "Kotlin Programming and Development", "organization": "Dicoding", "year": "2021"},
        {"name": "Back-End Application Development", "organization": "Dicoding", "year": "2021"},
        {"name": "Android Developer", "organization": "Dicoding", "year": "2020"},
        {"name": "CCNA Cybersecurity Operations", "organization": "Digitalent Scholarship", "year": "2020"},
        {"name": "ICSI Certified Network Security Specialist", "organization":"ICSI", "year": "2020"},
        {"name": "Fortinet’s Network Security Expert | NSE Network Security 1-2 Associate","organization":"Fortinet",  "year": "2020"},
        {"name": "Microsoft Office Specialist – Microsoft Word 2010", "organization": "Certiport Pearson Vue", "year": "2010"}
    ]

    for cert in certifications:
        with st.expander(f"{cert['name']} ({cert['year']})", expanded=False):
            if "organization" in cert:
                st.write(f"Organization: {cert['organization']}")
            st.write(f"Year: {cert['year']}")

if __name__ == "__main__":
    main()
