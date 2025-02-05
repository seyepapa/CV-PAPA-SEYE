import streamlit as st

# Configuration de la page
st.set_page_config(page_title="CV de Papa SEYE", layout="wide")

# Style CSS pour colorer les en-têtes
st.markdown("""
<style>
h1 {
    color: #2E86C1;
}
h2 {
    color: #1ABC9C;
    background-color: #ECF0F1;
    padding: 10px;
    border-radius: 5px;
}
h3 {
    color: #E67E22;
    background-color: #FDE3A7;
    padding: 5px;
    border-radius: 5px;
}
</style>
""", unsafe_allow_html=True)

# Informations personnelles
st.title("Papa SEYE")
st.markdown("**Data Engineer / Data Scientist**")
st.markdown("📞 +221 77 761 14 04 | 📧 papaseye296@gmail.com")
st.markdown("**Proile LinkdIn** : https://www.linkedin.com/in/papa-seye-96259212b/")
st.markdown(" **Proile Guithub** https://github.com/seyepapa")
st.markdown("🏠 Rue 27X18, Médina, Dakar, Sénégal")

# Section PRINCIPALES COMPETENCES

st.header("RESUME")
st.markdown("**Data Engineer / Data Scientist**, spécialisé en **Big Data**, **ingénierie des données** et **intelligence artificielle**. Expérience dans la conception et l’optimisation de data lakes, **ETL** et entrepôts de données en environnement **on-premise** et **cloud**. Maîtrise des technologies **Hadoop**, **Spark**, **Kafka**, **SQL**, **NoSQL**, **Python** et **Power BI** pour le traitement et la visualisation des données. Compétences en **LLM**, **LangChain** et **Streamlit** pour le développement d’applications basées sur l’**IA** générative. Passionné par l’innovation et la mise en place de solutions analytiques et intelligentes.")
st.header("PRINCIPALES COMPETENCES")

# Sous-section COMPETENCES
st.subheader("COMPETENCES")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Bases de Données :**")
    st.markdown("- Relationnelles : MySQL, Postgres, SQL Server")
    st.markdown("- NoSQL : HBase, MongoDB, Cassandra")

    st.markdown("**Outils et Technologies :**")
    st.markdown("- HDFS, MapReduce, Tez, Yarn, Apache Spark, HBase, Hive, Flume, Sqoop, Impala, Presto, Phoenix, Drill, Oozie, Cloudera Manager, Hortonworks Ambari, Hue, Pyspark, Zookeeper, Elasticsearch, Logstash, Kibana, Jupyter Notebook, Putty")

    st.markdown("**ETL :**")
    st.markdown("- Nifi, DBT, Apache Airflow, Pandas")

    st.markdown("**Langage de programmation :**")
    st.markdown("- Python, Scala, R")

with col2:
    st.markdown("**Cloud :**")
    st.markdown("- AWS (EC2, S3 bucket, EMR, Kinesis, DynamoDB, Glue), Bigquery, Snowflake")

    st.markdown("**Maitrise des environnements :**")
    st.markdown("- Linux, Windows, Redhat")

    st.markdown("**Dataviz :**")
    st.markdown("- Power BI, Kibana, Google Data Studio, Matplotlib, Seaborn")

    st.markdown("**DevOps :**")
    st.markdown("- Docker, Docker-compose, Git, CI/CD, Kubernetes")

    st.markdown("**Data Science :**")
    st.markdown("- Nettoyage des données, Formatages, Normalisation, Machine Learning")

    st.markdown("**Webscraping :**")
    st.markdown("- Request, Beautifulsoup")

st.markdown("---")

# Section CERTIFICATION
st.header("CERTIFICATION")
st.markdown("- Python for Data Analysis, Data visualization with python, Machine Learning with python")
st.markdown("- Devenir expert en Power BI")
st.markdown("- The Ultimate Hands-On Hadoop : Tame your Big Data (Udemy)")
st.markdown("- Scala Programmer for Data Science")
st.markdown("- Spark Overviews, Spark Fundamental 1, Spark Fundamental 2")
st.markdown("- Hadoop – Foundations – Level 1 & 2")
st.markdown("- Hadoop – Programming – Level 1, Hadoop – Administration – Level 1")
st.markdown("- Using HBase for Real-time Access to your Big Data")
st.markdown("- Hadoop Data Access using Hive")
st.markdown("- R for Data science")
st.markdown("- SQL for Data Science et SQL Server")
st.markdown("- Build Your Own ChatBot - IBM, Build your ChatBot with Python - DATACAMP")
st.markdown("**___________________________________________________________________________________________________________________________________________**")

# Section EXPERIENCE PROFESSIONNELLE
st.header("EXPERIENCE PROFESSIONNELLE")

st.subheader("Data Engineer")
st.markdown("**Atos Sénégal** (depuis février 2023)")
st.markdown("Projet: Mise en place d’un outil d’aide à la décision")
st.markdown("- Collecte des données en temps réels")
st.markdown("- Calcul des KPIs")
st.markdown("**Environnement technique :** Hadoop, Nifi, Kafka, spark/scala, spark streaming, ubuntu")

st.subheader("Data Scientist / Data Engineer")
st.markdown("**Port Autonome de Dakar (PAD)** (depuis Janvier 2021)")
st.markdown("Projet: Mise en place de ChatBot")
st.markdown("- Collecte des questions et réponses")
st.markdown("- Mise en place du chatbot")
st.markdown("**Environnement technique:** Python, SQL, Postgresql, pandas, Ubuntu, Docker, Docker-compose, Git, Gitlab, Rasa, Rasa X, ymal, NLP, PuTTy, SSH")

st.markdown("Projet: Mise en place d’un modèle de Prédiction du chiffre d’affaires du PAD")
st.markdown("- Collecte des données")
st.markdown("- Centralisation des données dans Mysql")
st.markdown("- Nettoyage et formatage des données")
st.markdown("- Mettre en place le modèle de prédiction")
st.markdown("**Environnement technique:** Python, Pandas, SQL, Mysql, Power BI, Matplotlib, Seaborn, Git, Gitlab, Jupyter Notebook, Facebook Prophet, Séries Temporelles")

st.subheader("Data Engineer")
st.markdown("**ADNCORP** (juillet 2018-octobre 2018)")
st.markdown("Projet : Mise en place d’un Datawarehouse et Machine Learning")
st.markdown("- Collecte et stockage des données dans hadoop")
st.markdown("- Préprocessing, Processing des données avec Spark/Scala")
st.markdown("- Ingestion des données dans Hive")
st.markdown("- Stockage des données dans Mysql en utilisant Sqoop")
st.markdown("- Mise en place d’un modèle de prédiction")
st.markdown("**Environnement technique:** Hadoop, Hive, Sqoop, Hbase, Spark/Scala Spark Mllib, SparkSQL, RDD, DataFrame, SQL, Ubuntu, Machine learning (knn, Regression logistique, SVM) sklearn, pandas, scala, jupyter notebook, git, github")

st.subheader("Stagiaire (Big Data Analytics)")
st.markdown("**NEUROTECH** (Mai 2017 - Novembre 2018)")
st.markdown("Projet : Développement des tableaux de bords d’aide à la prise de décision pour le service marketing et commercial")
st.markdown("- Recueil et analyse des besoins")
st.markdown("- Identification des sources de données")
st.markdown("- Centralisation des données")
st.markdown("- Classification des clients par chiffre d’affaires")
st.markdown("- Présentation des données dans des tableaux de bord")
st.markdown("**Environnement technique :** Salesforce CRM, Salesforce Analytics, Salesforce Connect, Salesforce Discovery, Python (numpy, pandas, matplotlib, sklearn), SQL")

st.markdown("Projet personnel : Mise en pratique des outils de data engineering")
st.markdown("- Collecte de données en utilisant le webscraping")
st.markdown("- Nettoyage et formatage des données")
st.markdown("- Analyse des données")
st.markdown("- Stockage des données dans Hbase")
st.markdown("- Stockage des données dans hive")
st.markdown("- Déplacer les données de Hadoop vers Mysql et vice versa en utilisant Sqoop")
st.markdown("- Interroger les données avec apache pig, spark")
st.markdown("- Datavisualisation")
st.markdown("**Environnement technique :** Python, Sql, Power BI, Cloudera, Hadoop, HDFS, Hue, Hive, Sqoop, Impala, Drill, Phoenix, Sqoop, Hbase, Hive, MapReduce, Tez, request, Beautifulsoup, pyspark")
st.markdown("**___________________________________________________________________________________________________________________________________________**")

# Section ETUDES ET FORMATIONS
st.header("ETUDES ET FORMATIONS")

st.markdown("**Master Big Data et Sécurité Informatique**")
st.markdown("2016-2018 | AIMS-SENEGAL (African Institute for Mathematical Sciences)")

st.markdown("**Maitrise de Mathématiques Appliquées et Informatique**")
st.markdown("2015-2016 | UGB-Sénégal (Université Gaston Berger de Saint-Louis)")

st.markdown("**Licence de Mathématiques Appliquées et Informatique**")
st.markdown("2013-2014 | UGB-Sénégal (Université Gaston Berger de Saint-Louis)")

st.markdown("**DEUG Mathématiques, Physique et Informatique**")
st.markdown("2013-2014 | UGB-Sénégal (Université Gaston Berger de Saint-Louis)")

# Section Langues
st.header("Langues")
st.markdown("- Français")
st.markdown("- Anglais")
st.markdown("**___________________________________________________________________________________________________________________________________________**")
# Section Centres d'intérêt
st.header("Centres d'intérêt")
st.markdown("- Formations")
st.markdown("- Sports")
st.markdown("- Lecture")