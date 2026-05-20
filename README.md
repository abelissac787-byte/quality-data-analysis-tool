# Data Analysis & Automation Tool

##Setup

Open terminal and run:
```bash
pip install streamlit numpy matplotlib
cd your-folder-path
streamlit run app.py
```

The app opens at `localhost:8501`

##How to Use

**Sidebar**
- Enter measurements separated by commas (e.g., 10.1, 10.3, 9.8)
- Enter the target value
- Enter the tolerance
- Enter defect counts: scratches, dents, cracks, others

**Results**
- Average, std deviation, minimum, and maximum measurement values
- Values that are outside the allowed range
- Total defect count
- Defect breakdown and chart

**Summary**
- Quick overview of whether the batch is acceptable or has issues

## Common Mistakes

- Use commas between measurement values
- Enter only numbers in the measurement field
- Enter at least one measurement value
