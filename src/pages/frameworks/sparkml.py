import streamlit as st

def Sparkml():
    st.title("Introduction to SparkML")
    st.write(
        """
        SparkML is a machine learning library for Apache Spark, it will provide a lot of tools to work with machine learning algorithms in a similar way to scikit-learn.

        In this example we will show the Descision Tree Classifier, using the Iris dataset from the UCI Machine Learning Repository.

        The csv it's called 'iris.data'.
        """)
    
    st.code("""
            from pyspark.sql import SparkSession
            from pyspark.ml.feature import VectorAssembler
            from pyspark.ml.classification import DecisionTreeClassifier
            from pyspark.ml.feature import StringIndexer
            """)
    
    st.header("Loading the dataset")
    st.write("""
            ``pyspark.sql`` will be used to load the dataset, ``vectorassembler`` will generate a vector with features to the descision tree, and the ``StringIndexer`` will transform the label to a numeric interpretation.
            """)
    st.code("""
            sc = SparkSession.builder.appName("MyApp").getOrCreate()

            df =sc.read.csv("iris.data", header=False, inferSchema=True)
            """)
    
    st.header("Data Preprocessing")
    st.write("""let's add the tag column to the dataframe""")

    st.code("""
            si_c4 = StringIndexer(inputCol=str(df.columns[-1]), outputCol="label")
            q1 = si_c4.fit(df)
            data_raw = q1.transform(df)
            """)
    
    st.write("it's time to create the vector with the features using the VectorAssembler")
    st.code("""
            feat = data_raw.columns[:-2]
            assembler = VectorAssembler(inputCols=feat, outputCol='features')
            data = assembler.transform(data_raw)
            """)

    st.header("Model Creation")
    st.write("Finally we will create the model using DesitionTreeClassifier")
    st.code("""
            dtc = DecisionTreeClassifier(featuresCol = 'features', labelCol = 'label')
            """)
    
    st.write("To make predictions we will use the fit method to train the model, and then we will use the transform method to make predictions.")
    st.code("""
            model = dtc.fit(data)

            predictions = model.transform(data)

            predictions.show()
            """)