import streamlit as st
from components.link import CLink_icon
def Spark():
    st.title("Introduction to Spark")
    CLink_icon("Docker - spark", "https://hub.docker.com/r/apache/spark-py", "devicon-docker-plain colored")
    st.write(
        """
        Apache Spark is an open-source, distributed computing framework, designed for processing large-scale data efficiently.  It enables parallel data processing across clusters of machines, optimizing performance for big data workloads. It uses RDD (resilient distributed dataset) as data structure, which is a fault-tolerant collection of elements that can be processed in parallel. Spark supports various programming languages, including Scala, Java, Python, and R, making it versatile for data processing tasks. It provides high-level APIs for data manipulation and supports SQL queries, machine learning, and graph processing. Spark's in-memory computing capabilities significantly enhance performance compared to traditional disk-based processing frameworks like Hadoop MapReduce.

        Has the advantage of being horizontally scalable, so, if an operation is to expensive, we can add more machines to increase the capacity of the cluster, and the operation will be distributed across the machines.
        
        Originally developed in Scala, Spark also offers a python API called PySpark, allowing developers to leverage its capabilities using python.
        """
        )
    

    st.header("Installing Spark")
    st.write("""
        The easiest way to install Spark is using Docker. You can run the following command to start a Spark container:
             """)
    st.code("""
        docker run --name spark -d -p 4040:4040 -p 7077:7077 -p 8080:8080 -it apache/spark /opt/spark/bin/spark-shell
            """)
    st.write("""
        Remember `-p <host_port>:<container_port>` is to expose the port of the container to the host machine.
        And `-it` flag is to execute a command on the container interactively, P.E `/bin/bash` or `/opt/spark/bin/spark-shell`.
             
        Now you can acces to spark using pyspark on python, if you want to make a dev-container you must create a net with docker, bun for this example we will use the default net and a local python environment.
        """)
    



    st.header("First steps with PySpark")
    st.code("""
            pip install pyspark
            """)
    
    st.write("""
             Now let's create a simple example, first we neet a sparksession, and create a connection to the spark cluster, then we can create or read a dataframe to work with it.
             """)
    st.code("""
            from pyspark.sql import SparkSession

            spark = SparkSession.builder.appName("MyDockerSparkApp").getOrCreate()

            df = spark.createDataFrame([(1, "foo"), (2, "bar")], ["id", "value"])
            df.show()
            """)
    
    st.write("""
             As we can see, df.show is like pd.DataFrame.head(), show some rows of the dataframe.
                
             Now let's read a csv file.
                """)
    st.code("""
            df = spark.read.csv("file.csv", header=True) # si header = False, se asigan como _ci con i de 0 a n
            df.show()
            """)
    
    st.write("""
            Finally we will see how to use the select and distinct methods to select a column and get the distinct values of that column.
            """)
    st.code("""
            select('data_c1').disctinct().show()
            """)
    
    st.header("group operations")
    st.write("""
             To make a simple group operation, we can use mean with groupBy, use iris for this examples.
             """)
    st.code("""
            from pyspark.sql import SparkSession
            sc = SparkSession.builder.appName("MyApp").getOrCreate()
            
            df =sc.read.csv("iris.data", header=False, inferSchema=True)
            
            df.groupBy("_c4").mean().show()
            """)