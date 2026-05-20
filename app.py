import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Quality Data Analysis")

st.sidebar.header("Input Data")

# dim input
dim_text = st.sidebar.text_area("Enter dimensions separated by commas",value="10.1, 10.3, 9.8, 10.5, 10.2, 9.7, 10.4, 10.6, 9.9, 10.2")
target = st.sidebar.number_input("Target value",value=10.0, step=0.1)
tolerance = st.sidebar.number_input("Tolerance",value=0.3, step=0.1)

# def input
st.sidebar.header("Defects")
scratches = st.sidebar.number_input("Scratches",value=35, min_value=0)
dents = st.sidebar.number_input("Dents",value=25, min_value=0)
cracks = st.sidebar.number_input("Cracks",value=15, min_value=0)
others = st.sidebar.number_input("Others",value=10, min_value=0)

#fix logic
try:
    dim_list = dim_text.split(",")
    dims = []
    for item in dim_list:
        if item.strip() != "":
            dims.append(float(item))
except ValueError:
    st.error("Enter valid numbers separated by commas")
    st.stop()

if not dims:
    st.error("Please enter dimension values")
    st.stop()

# liimits
lower_limit = target - tolerance
upper_limit = target + tolerance

# stats
mean = np.mean(dims)
minimum = np.min(dims)
maximum = np.max(dims)

# std deviation
if len(dims) > 1:
    std_dev = np.std(dims, ddof=1)
else:
    std_dev = 0

# failed dimensions
failed_dims = []
for dimension in dims:
    if dimension < lower_limit or dimension > upper_limit:
        failed_dims.append(dimension)

# defect types dict
defects_dict = {
    "Scratches": scratches,
    "Dents": dents,
    "Cracks": cracks,
    "Others": others
}

# total defects
total_defect_count = sum(defects_dict.values())

#two column layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Dimension Results")
    st.write("Mean:", round(mean, 2), "mm")
    st.write("Standard deviation:", round(std_dev, 3))
    st.write("Minimum:", round(minimum, 2), "mm")
    st.write("Maximum:", round(maximum, 2), "mm")
    st.write("Lower limit:", lower_limit)
    st.write("Upper limit:", upper_limit)
    
    # check if all dims pass
    if len(failed_dims) == 0:
        st.success("All dimensions are within limit")
    else:
        st.warning("Some values are outside the limit")
        st.write("Failed values:", failed_dims)

with col2:
    st.subheader("Defect Details")
    st.write("Total defects:", total_defect_count)
    
    if total_defect_count > 0:
        # bar chart
        defect_names = list(defects_dict.keys())
        defect_counts = list(defects_dict.values())
        
        fig, ax = plt.subplots()
        ax.bar(defect_names, defect_counts, color='#e74c3c')
        ax.set_ylabel("Count")
        ax.set_title("Defect Count")
        st.pyplot(fig)
        
        # perc breakdown
        st.write("Defect percentage breakdown:")
        for defect_name, defect_count in defects_dict.items():
            percent_value = (defect_count / total_defect_count) * 100
            st.write(f"{defect_name}: {defect_count} ({round(percent_value, 1)}%)")
    else:
        st.info("No defects entered")

# final summary section
st.subheader("Summary")

if len(failed_dims) == 0 and total_defect_count == 0:
    st.success("The batch quality is acceptable")
else:
    # dim fails
    if len(failed_dims) > 0:
        st.write(f"Number of dimension failures: {len(failed_dims)}")
    
    # def analysis
    if total_defect_count > 0:
        # most common def
        max_defect_type = max(defects_dict, key=defects_dict.get)
        st.write(f"Main defect type: {max_defect_type}")
