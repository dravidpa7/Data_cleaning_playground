import streamlit as st
import pandas as pd

# Initialize session state at the top of the file
if 'processed_df' not in st.session_state:
    st.session_state.processed_df = None

st.title("Data cleaning page")
st.info("This data cleaning only for numerical variable")

st.markdown("### Upload Your Dataset")
data_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"],
    help="Upload a CSV file to view and analyze its contents"
)


def preview(df):
    st.dataframe(df,width=1000,height=300)

def removedf(df):
    st.warning("Remove rows by using dropna")
    return df.dropna()

def replacedf(df):
    try:
        st.warning("You can choose your fill empty rows")
        option = st.selectbox(
            "Choose the fill",
            ("fill","forward fill","backward fill")
        )
        
        if option == "fill":
            x = st.text_input("Enter the integer value to fill ")
            try:
                # Convert input to float to validate numeric input
                x = float(x) if x else None
            except ValueError:
                st.warning("Please enter a valid numeric value")
                return df
                
        if st.button("Apply Changes"):
            if option == "fill" and x is not None:
                df.fillna(x, inplace=True)
            elif option == "forward fill":
                df.ffill(inplace=True)
            else:
                df.bfill(inplace=True)
            
            st.session_state.processed_df = df
            st.success("Changes applied successfully!")
            
        return df
    except Exception as e:
        st.warning("An error occurred while processing. Please check your inputs.")
        return df

def replace_sf(df):
    try:
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
        x = st.multiselect(
            "Select columns for fill input",
            options=numeric_columns,
            default=numeric_columns[:2] if len(numeric_columns) >= 2 else numeric_columns
        )

        y = st.text_input("Enter the integer value to fill")
        try:
            # Validate numeric input
            y = float(y) if y else None
        except ValueError:
            st.warning("Please enter a valid numeric value")
            return df
            
        if st.button("Apply Changes"):
            if y is not None and x:
                df[x] = df[x].fillna(y)
                st.session_state.processed_df = df
                st.success("Changes applied successfully!")
            else:
                st.warning("Please select columns and enter a valid value")
                
        return df
    except Exception as e:
        st.warning("An error occurred while processing. Please check your inputs.")
        return df

def replaceAGGREGATION(df):
    try:
        columns = df.select_dtypes(include=['float64', 'int64']).columns
        
        z = st.multiselect(
            "Select columns for fill input",
            options=columns,
            default=columns[:2] if len(columns) >= 2 else columns,
            key="multiselect_fill_input"
        )
        
        option = st.selectbox(
            "Select the aggregation function",
            ("Mean", "Median", "Mode"),
            key="selectbox_aggregation_function"
        )
        
        if st.button("Apply Changes"):
            if not z:
                st.warning("Please select at least one column")
                return df
                
            if option == "Mean":
                mean_values = df[z].mean()
                df[z] = df[z].fillna(mean_values)
            elif option == "Median":
                median_values = df[z].median()
                df[z] = df[z].fillna(median_values)
            else:
                mode_values = df[z].mode().iloc[0]
                df[z] = df[z].fillna(mode_values)
            
            st.session_state.processed_df = df
            st.success("Changes applied successfully!")
            
        return df
    except Exception as e:
        st.warning("An error occurred while processing. Please check your inputs.")
        return df

def duplicate1(df):
    try:
        # Remove duplicates inplace and update the session state
        df.drop_duplicates(inplace=True)
        st.session_state.processed_df = df
        return df
    except Exception as e:
        st.warning("An error occurred while removing duplicates.")
        return df

def clean(df):
    try:
        st.info("Choose one of the operation to remove or replace the data from empty cell")
        option = st.selectbox(
            "Select option",
            ["Removerow", "Replacevalue", "ReplaceSpecificcolumn", "AggregationMeanMedianMode"],
            key="choose data operation"
        )
        
        if option == "Removerow":
            if st.button("Apply Changes"):
                df.dropna(inplace=True)
                st.session_state.processed_df = df
                st.success("Empty rows removed successfully!")
                
        elif option == "Replacevalue":
            df = replacedf(df)
        elif option == "ReplaceSpecificcolumn":
            df = replace_sf(df)
        else:
            df = replaceAGGREGATION(df)
            
        st.dataframe(df, width=1000, height=235)
        return df
        
    except Exception as e:
        st.warning("An error occurred while processing. Please check your inputs and try again.")
        return df


if data_file is not None: 
    try:
        # Load the data only if we haven't processed it yet
        if st.session_state.processed_df is None:
            st.session_state.processed_df = pd.read_csv(data_file)
        
        df = st.session_state.processed_df  # Use the stored DataFrame
        
        if st.button("Preview dataset"):
            preview(df)

        DataFrame = clean(df)
        st.session_state.processed_df = DataFrame  # Store the cleaned DataFrame

        st.info("Check for duplicates in your dataset")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            if st.button("Check & Remove Duplicates"):
                num_duplicates = DataFrame.duplicated().sum()
                if num_duplicates > 0:
                    st.warning(f"Found {num_duplicates} duplicate rows")
                    DataFrame = duplicate1(DataFrame)
                    st.success("Duplicates removed successfully!")
                    st.session_state.processed_df = DataFrame  # Update session state
                    # Show updated preview after removing duplicates
                    st.subheader("Updated Dataset Preview (After Removing Duplicates)")
                    preview(DataFrame)
                else:
                    st.success("No duplicates found in the dataset")

        with col2:
            if st.session_state.processed_df is not None:
                st.download_button(
                    label="💾 Download Processed Data",
                    data=st.session_state.processed_df.to_csv(index=False).encode('utf-8'),
                    file_name='processed_dataset.csv',
                    mime='text/csv',
                    help="Download your processed dataset as a CSV file"
                )

        # Show final preview of the data
        st.subheader("Current Dataset Preview")
        st.dataframe(st.session_state.processed_df, width=1000,height=235)
        
        # Add information about current dataset size
        st.info(f"Current dataset size: {len(st.session_state.processed_df)} rows")
        
        # Add a reset button
        if st.button("Reset All Changes"):
            st.session_state.processed_df = pd.read_csv(data_file)
            st.success("Dataset has been reset to original state")
            st.rerun()

    except Exception as e:
        st.error("An error occurred during processing. Please try again.")

else:
    st.warning("Please upload a CSV file to begin")