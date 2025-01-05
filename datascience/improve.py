import streamlit as st
import pandas as pd

st.title("Data Cleaning Page")
st.info("This data cleaning is only for numerical variables")

st.markdown("### Upload Your Dataset")
data_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"],
    help="Upload a CSV file to view and analyze its contents"
)

def preview(df):
    st.dataframe(df, width=1000, height=300)

def removedf(DataFrame):
    st.warning("Remove rows using dropna")
    return DataFrame.dropna()

def replacedf(DataFrame):
    st.warning("You can choose to fill empty rows")
    option = st.selectbox("Choose the fill", ("fill", "forward fill", "backward fill"))
    if option == "fill":
        x = st.text_input("Enter the integer value to fill")
        if st.button("Submit Fill"):
            return DataFrame.fillna(x)
    elif option == "forward fill":
        return DataFrame.ffill()
    else:
        return DataFrame.bfill()

def replace_sf(DataFrame):
    numeric_columns = DataFrame.select_dtypes(include=['float64', 'int64']).columns
    x = st.multiselect("Select columns for fill input", options=numeric_columns)
    y = st.text_input("Enter the integer value to fill")
    if st.button("Submit Specific Fill", key="specific_fill_button"):
        # Fill missing values and return DataFrame
        DataFrame[x] = DataFrame[x].fillna(float(y))  # Ensure y is converted to numeric
        st.success("Empty values filled successfully!")
    return DataFrame

def replaceAGGREGATION(DataFrame):
    columns = DataFrame.select_dtypes(include=['float64', 'int64']).columns
    z = st.multiselect("Select columns for aggregation", options=columns, key="multiselect_fill_input")
    option = st.selectbox("Select the aggregation function", ("Mean", "Median", "Mode"), key="selectbox_aggregation_function")
    if st.button("Apply Aggregation", key="aggregation_button"):
        if option == "Mean":
            mean_values = DataFrame[z].mean()
            DataFrame[z] = DataFrame[z].fillna(mean_values)
        elif option == "Median":
            median_values = DataFrame[z].median()
            DataFrame[z] = DataFrame[z].fillna(median_values)
        else:
            mode_values = DataFrame[z].mode().iloc[0]
            DataFrame[z] = DataFrame[z].fillna(mode_values)
        st.success(f"Aggregation ({option}) applied successfully!")
    return DataFrame

def duplicate1(DataFrame):
    return DataFrame.drop_duplicates()

def clean(DataFrame):
    st.info("Choose an operation to remove or replace empty cells")
    option = st.selectbox("Select option", ["Removerow", "Replacevalue", "ReplaceSpecificcolumn", "AggregationMeanMedianMode"], key="data_cleaning_operation")
    if option == "Removerow":
        DataFrame = removedf(DataFrame)
    elif option == "Replacevalue":
        DataFrame = replacedf(DataFrame)
    elif option == "ReplaceSpecificcolumn":
        DataFrame = replace_sf(DataFrame)
    else:
        DataFrame = replaceAGGREGATION(DataFrame)
    st.dataframe(DataFrame, width=1000, height=235)
    return DataFrame

if data_file is not None:
    try:
        df = pd.read_csv(data_file)
        if st.button("Preview Dataset"):
            preview(df)
        DataFrame = clean(df)
        st.download_button(
            label="Download Data as CSV",
            data=DataFrame.to_csv(index=False).encode('utf-8'),
            file_name='processed_dataset.csv',
            mime='text/csv'
        )
        st.info("You can also find duplicates and clean them")
        if st.button("Check Duplicates"):
            st.session_state.duplicates_exist = DataFrame.duplicated().any()

        if st.session_state.get("duplicates_exist", False):
            st.write("Duplicates available")
            if st.button("Clean duplicate"):
                duplicatefile = duplicate1(DataFrame)
                st.success("Duplicates cleaned successfully!")
                st.dataframe(duplicatefile)
        else:
            st.write("No duplicates found")

    except Exception as e:
        st.error(f"Error reading the file: {str(e)}")
else:
    st.warning("Please upload a CSV file to begin")
