import pandas as pd
edu = [['B.Tech','CSE','2020','IIIT Jabalpur','8.1 CGPA'],['12th','Science','2016','Bhavan\'s KDKVM', '94.2%'],['10th','-','2012','Bhavan\'s KDKVM','10 CGPA']]

info = {'name':'Mehul Gupta', 'Brief':'Associate Data Scientist @ DBS Bank with 4+ years of professional experience looking out to solve complex business problems using AI; Experienced in developing data-driven solutions for automating digitalization of health documents reducing manual efforts by 100% for lab reports & 50% for prescriptions; Love to learn new things. Building NLP pipelines for Financial articles at DBS Bank right now !! ','photo':{'path':'abc.jpg','width':150}, 'Mobile':'8103795345','Email':'mehulgupta2016154@gmail.com','Medium':'https://medium.com/@mehulgupta_7991/about','City':'Nagda, Madhya Pradesh','Stackoverflow_flair':'''<a href="https://stackoverflow.com/users/8422170/mehul-gupta"><img src="https://stackoverflow.com/users/flair/8422170.png?theme=clean" width="250" height="70"  alt="profile for Mehul Gupta at Stack Overflow, Q&amp;A for professional and enthusiast programmers" title="profile for Mehul Gupta at Stack Overflow, Q&amp;A for professional and enthusiast programmers"></a>''','edu':pd.DataFrame(edu,columns=['Qualification','Stream','Year','Institute','Score']),'skills':['C & C++','RDBMS','Google Spreadsheets','LookerStudio','XLMiner Analysis','R','Python','Java','SQL','MySQL','Google BigQuery','Tableau','Linux','Matlab','Streamlit','Flask','Tensorflow','NI LabView'],'achievements':['Top AI writer @ Medium with 100+ blogs','1.8k+ reputation points on Stackoverflow','Guest speaker, Neo4j','TCS humAIn Finalist,2019','Shikshan Bharati Kulapati K.M. Munshi Award in Mathematics,2014','Bharatiya Vidya Bhavan Shri C. Subramaniam Award for excellence in character, 2009 & 2012','Certificate of Merit(Proficiency in Co-curricular activities) for Declamation and Extempore'],'youtube_url':'https://www.youtube.com/channel/UCQoNosQTIxiMTL9C-gvFdjA','youtube_about':'https://www.youtube.com/@datascienceinyourpocket/about','publication_url':'https://medium.com/data-science-in-your-pocket/tagged/beginner'}

projects = [
    {
        'title': 'Business Problem - Reducing Employee Attrition at XYZ Ltd.',
        'thumbnail': 'pictures/proj1.png',
        'description': 'The problem we are addressing is the current attrition rate of 15% at XYZ Ltd., a large company with 4.000 employees. This high turnover rate is creating operational disruptions and elevating hiring costs, thus impacting business productivity and profits.&lt;br&gt; The challenge is to identify the reasons behind this attrition and suggest actionable solutions. Aim to reduce the attrition rate from 15% to 10% within a year, by implementing strategies based on data insights. This aligns with XYZ Ltd. business stability goals.',
        'link' : 'https://docs.google.com/presentation/d/1PmwnqEXnCG6cHHo55-KO8ROMkzI4N4DquAVzv4ajGfk/edit#slide=id.gc6f9e470d_0_37'
    },
    {
        'title': 'Strategic Analysis of Luxury Brand Prioritization for Luxura',
        'thumbnail': 'pictures/proj2.png',
        'description': 'Luxura key issue is to identify which luxury brand, be it Adibi, Balena, or Celinna, should receive prioritization in marketing efforts, given that customer preferences, partnership fees, and each brand&apos;s contribution to growth all play pivotal roles in this decision-making process.',
        'link' : 'https://docs.google.com/presentation/d/1v34qeS2UNdNpNVnf-CGNciE0-3DdI2e2Z1KkDiZJ-7Y/edit?usp=sharing'
    },
    {
        'title': 'TheLook&apos;s Product and Retention Analysis 2023',
        'thumbnail': 'pictures/proj3.png',
        'description': 'Using SQL BigQuery, I analyzed TheLook&apos;s data to tackle upcoming 2023 challenges. We identified underperforming product categories from the past year and studied customer retention trends from 2022. The goal was to improve resource allocation and boost profitability.',
        'link' : 'https://docs.google.com/presentation/d/1ftBYTuoWqJKnRW5GuBEzDqwKHJ2wckhK-syojU-fgWs/edit?usp=sharing'
    },
    {
        'title': 'RevoBank Promotion Analysis and Customer Segmentation',
        'thumbnail': 'pictures/proj4.png',
        'description': 'Using Google Colab and Python, I analyzed RevoBank&apos;s transaction data to assess the performance of their promotion program.&lt;br&gt; I determined the sales impact, cost, and revenue generated by the promotion. Further, I segmented RevoShop&apos;s credit card users into distinct categories based on various attributes. This segmentation helped pinpoint opportunities to personalize the rewards program for different customer groups, utilizing clustering, EDA, and propensity model evaluations.',
        'link' : 'https://docs.google.com/presentation/d/1X5XJdX9oyyKQTGHLy6uPmZU35bqnTItYUCSFCDrmbBI/edit?usp=sharing'
    },
    {
        'title': 'Samba Commerce: Sales and Customer Insights Dashboard',
        'thumbnail': 'pictures/proj5.png',
        'description': 'I developed a Tableau dashboard for Samba Commerce, a prominent e-commerce platform in Brazil. This dashboard effectively tracks sales metrics, highlights popular products, and offers insights to optimize inventory decisions.</>Through the dashboard, I analyzed customer behaviors, including their buying frequency and preferred payment methods, aiming to enhance Samba&apos;s marketing strategies.&lt;br&gt; Additionally, I examined order delivery patterns to pinpoint and rectify any inefficiencies, while also providing a comprehensive view of payment trends to inform the company&apos;s financial strategies.',
        'link' : 'https://docs.google.com/presentation/d/1ArybK0VyZwjB2Wu_zei4FLBMh3AutJ355BHyuUkIZDY/edit?usp=sharing'
    },
    {
        'title': 'Pizzain Yuk: Analysis of Pizza Sales',
        'thumbnail': 'pictures/proj6.png',
        'description': 'Pizzain Yuk has recently faced a revenue decline, with a -3.03% decrease over recent months. Although there was a slight upturn in the 2nd quarter with a 1.4% increase, the revenue decreased by -1.6% in the 3rd quarter and further declined by -2.8% in the 4th quarter. Several factors, such as product offerings, pricing, and sale timings, might be influencing this drop. Based on the analysis,&lt;br&gt;We&apos;ve devised strategies to boost revenue:&lt;br&gt;Launch targeted advertisements or promotions, especially during peak hours of 16-19 PM.&lt;br&gt; Implement regular sales evaluations, whether quarterly, monthly, or weekly, for quicker adjustments.&lt;br&gt; Adjust operational hours, possibly from 10 PM to midnight, to cater to late-night customers.&lt;br&gt; Offer discounts or bundled packages on weekends, capitalizing on Friday&apos;s peak order rate.&lt;br&gt; Introduce size variations for the &apos;brie carre&apos; pizza and promotional offers for the &apos;Greek Pizza XXL&apos;.&lt;br&gt; With these strategies, the objective is to achieve a 20% revenue increase within the next year.',
        'link' : 'https://drive.google.com/file/d/1v_HStoqAZ-Husq8ghG_Kj8dMsjwopioV/view'
    }
]
