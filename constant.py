import pandas as pd
edu = [['B.Tech','CSE','2020','IIIT Jabalpur','8.1 CGPA'],['12th','Science','2016','Bhavan\'s KDKVM', '94.2%'],['10th','-','2012','Bhavan\'s KDKVM','10 CGPA']]

info = {'name':'Mehul Gupta', 'Brief':'Associate Data Scientist @ DBS Bank with 4+ years of professional experience looking out to solve complex business problems using AI; Experienced in developing data-driven solutions for automating digitalization of health documents reducing manual efforts by 100% for lab reports & 50% for prescriptions; Love to learn new things. Building NLP pipelines for Financial articles at DBS Bank right now !! ','photo':{'path':'abc.jpg','width':150}, 'Mobile':'8103795345','Email':'mehulgupta2016154@gmail.com','Medium':'https://medium.com/@mehulgupta_7991/about','City':'Nagda, Madhya Pradesh','Stackoverflow_flair':'''<a href="https://stackoverflow.com/users/8422170/mehul-gupta"><img src="https://stackoverflow.com/users/flair/8422170.png?theme=clean" width="250" height="70"  alt="profile for Mehul Gupta at Stack Overflow, Q&amp;A for professional and enthusiast programmers" title="profile for Mehul Gupta at Stack Overflow, Q&amp;A for professional and enthusiast programmers"></a>''','edu':pd.DataFrame(edu,columns=['Qualification','Stream','Year','Institute','Score']),'skills':['C & C++','RDBMS','Google Spreadsheets','LookerStudio','XLMiner Analysis','R','Python','Java','SQL','MySQL','Google BigQuery','Tableau','Linux','Matlab','Streamlit','Flask','Tensorflow','NI LabView'],'achievements':['Top AI writer @ Medium with 100+ blogs','1.8k+ reputation points on Stackoverflow','Guest speaker, Neo4j','TCS humAIn Finalist,2019','Shikshan Bharati Kulapati K.M. Munshi Award in Mathematics,2014','Bharatiya Vidya Bhavan Shri C. Subramaniam Award for excellence in character, 2009 & 2012','Certificate of Merit(Proficiency in Co-curricular activities) for Declamation and Extempore'],'youtube_url':'https://www.youtube.com/channel/UCQoNosQTIxiMTL9C-gvFdjA','youtube_about':'https://www.youtube.com/@datascienceinyourpocket/about','publication_url':'https://medium.com/data-science-in-your-pocket/tagged/beginner'}

projects = [
 {
        'title': 'Business Problem - Reducing Employee Attrition at XYZ Ltd.',
        'thumbnail': 'pictures/proj1.png',
        'description': 'The problem I am addressing is the current attrition rate of 15% at XYZ Ltd., a large company with 4,000 employees. This high turnover rate is causing operational disruptions and increasing hiring costs, impacting business productivity and profits.\n\nMy challenge was to identify the reasons behind this attrition and suggest solutions. My aim was to reduce the attrition rate from 15% to 10% within a year by implementing strategies based on data insights. This aligns with XYZ Ltd.&apos;s business stability goals.',
        'link': 'https://docs.google.com/presentation/d/1PmwnqEXnCG6cHHo55-KO8ROMkzI4N4DquAVzv4ajGfk/edit#slide=id.gc6f9e470d_0_37'
    },
    {
        'title': 'Strategic Analysis of Luxury Brand Prioritization for Luxura',
        'thumbnail': 'pictures/proj2.png',
        'description': 'Luxura faces a challenge in determining which luxury brand, be it Adibi, Balena, or Celinna, should be prioritized in marketing efforts. Customer preferences, partnership fees, and each brand&apos;s growth contribution are crucial factors in this decision-making process.',
        'link': 'https://docs.google.com/presentation/d/1v34qeS2UNdNpNVnf-CGNciE0-3DdI2e2Z1KkDiZJ-7Y/edit?usp=sharing'
    },
    {
        'title': 'TheLook Product and Retention Analysis 2023',
        'thumbnail': 'pictures/proj3.png',
        'description': 'In 2023, I used SQL BigQuery to analyze TheLook&apos;s data to tackle upcoming challenges. I identified underperforming product categories from the past year and studied 2022 customer retention trends. The goal was to improve resource allocation and profitability.',
        'link': 'https://docs.google.com/presentation/d/1ftBYTuoWqJKnRW5GuBEzDqwKHJ2wckhK-syojU-fgWs/edit?usp=sharing'
    },
    {
        'title': 'RevoBank Promotion Analysis and Customer Segmentation',
        'thumbnail': 'pictures/proj4.png',
        'description': 'Using Google Colab and Python, I analyzed RevoBank&apos;s transaction data to evaluate their promotion program. I assessed the sales impact, cost, and revenue from the promotion. I also segmented RevoShop&apos;s credit card users based on various attributes. This segmentation highlighted opportunities to personalize the rewards program for different customer segments, using clustering, EDA, and propensity model evaluations.',
        'link': 'https://docs.google.com/presentation/d/1X5XJdX9oyyKQTGHLy6uPmZU35bqnTItYUCSFCDrmbBI/edit?usp=sharing'
    },
    {
        'title': 'Samba Commerce: Sales and Customer Insights Dashboard',
        'thumbnail': 'pictures/proj5.png',
        'description': 'I created a Tableau dashboard for Samba Commerce, a leading e-commerce platform in Brazil. The dashboard tracks sales metrics, spotlights top-selling products, and offers insights to refine inventory decisions.\n\nUsing the dashboard, I analyzed customer behaviors, like purchase frequency and preferred payment methods, to enhance Samba&apos;s marketing strategies. I also studied order delivery trends to address inefficiencies and provided an overview of payment trends to guide the company&apos;s financial planning.',
        'link': 'https://docs.google.com/presentation/d/1ArybK0VyZwjB2Wu_zei4FLBMh3AutJ355BHyuUkIZDY/edit?usp=sharing'
    },
    {
        'title': 'Pizzain Yuk: Sales Analysis and Strategy Formulation',
        'thumbnail': 'pictures/proj6.png',
        'description': 'Pizzain Yuk experienced a revenue decline recently, with a -3.03% drop over several months. While there was a 1.4% increase in the 2nd quarter, revenue fell by -1.6% in the 3rd quarter and further to -2.8% in the 4th quarter. Factors like product offerings, pricing, and sales timings influenced this downturn.\n\nFrom my analysis, I proposed strategies to enhance revenue:\n\n- Launch targeted ads or promotions during peak hours (16-19 PM).\n- Conduct regular sales evaluations for timely adjustments.\n- Adjust operational hours to cater to late-night customers, possibly from 10 PM to midnight.\n- Offer discounts or packages on weekends, leveraging Friday&apos;s high order rate.\n- Introduce size variations for the &apos;brie carre&apos; pizza and provide offers for the &apos;Greek Pizza XXL&apos;.\n\nThese strategies aim for a 20% revenue increase within a year.',
        'link': 'https://drive.google.com/file/d/1v_HStoqAZ-Husq8ghG_Kj8dMsjwopioV/view'
    }
]