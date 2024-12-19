# README for 10 Academy Week 2 Challenge

This README file provides an overview of the tasks in the Week 2 Challenge, including setup instructions, steps for each task, and final deliverables.

## **Project Structure**

```
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows
│       ├── unittests.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
│   ├── __init__.py
├── notebooks/
│   ├── __init__.py
│   └── README.md
├── tests/
│   ├── __init__.py
└── scripts/
    ├── __init__.py
    └── README.md
```

## **Environment Setup**

1. **Install Required Tools**:
   - Python 3.8 or later
   - PostgreSQL database

2. **Install Required Python Libraries**:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn SQLAlchemy streamlit
   ```

3. **Database Setup**:
   - Load the provided SQL file into a PostgreSQL database.
   - Update the database connection string in the code.

4. **CI/CD and Docker**:
   - Include CI/CD workflows using GitHub Actions.
   - Create a Dockerfile for containerizing the project.

## **Tasks Overview**

### **Task 1: User Overview Analysis**

#### **Objective**
Analyze user behavior and provide insights into the top handsets, manufacturers, and user activities.

#### **Steps**
1. Identify top 10 handsets and top 3 handset manufacturers.
2. List top 5 handsets for each of the top 3 manufacturers.
3. Aggregate user data:
   - Number of sessions.
   - Total session duration.
   - Total download, upload, and data volume.
4. Perform exploratory data analysis:
   - Univariate, bivariate, and graphical analyses.
   - Identify correlations.
5. Perform dimensionality reduction using PCA.

#### **Deliverables**
- Python scripts for analysis.
- Slides with visualizations and insights.
- Recommendations for marketing strategies.

---

### **Task 2: User Engagement Analysis**

#### **Objective**
Track user engagement metrics and classify users based on engagement levels.

#### **Steps**
1. Aggregate metrics per customer ID (sessions, duration, traffic).
2. Normalize metrics and perform k-means clustering (k=3).
3. Compute statistics for each cluster and interpret results.
4. Identify top 10 most engaged users per application.
5. Visualize the top 3 most used applications.

#### **Deliverables**
- Python scripts for clustering and visualization.
- Slides with analysis and interpretations.

---

### **Task 3: Experience Analytics**

#### **Objective**
Analyze network performance and device characteristics to understand user experience.

#### **Steps**
1. Aggregate average metrics (TCP retransmission, RTT, throughput) per customer.
2. Compute and list top, bottom, and frequent values for each metric.
3. Analyze throughput and retransmission distributions per handset type.
4. Perform k-means clustering (k=3) to group users by experience.

#### **Deliverables**
- Python scripts for experience metrics and clustering.
- Slides with findings and interpretations.

---

### **Task 4: Satisfaction Analysis**

#### **Objective**
Combine engagement and experience metrics to analyze customer satisfaction.

#### **Steps**
1. Assign engagement and experience scores using Euclidean distance.
2. Calculate satisfaction score as the average of engagement and experience scores.
3. Predict satisfaction score using a regression model.
4. Perform k-means clustering (k=2) on satisfaction scores.
5. Export final table to a MySQL database.

#### **Deliverables**
- Python scripts for satisfaction analysis.
- Database export and screenshot.
- Slides with analysis and insights.

---

### **Task 5: Dashboard Development**

#### **Objective**
Develop a Streamlit dashboard to visualize data insights interactively.

#### **Steps**
1. Create pages for each task (User Overview, Engagement, Experience, Satisfaction).
2. Add visualizations (charts, tables) to each page.
3. Deploy the dashboard to a hosting platform (e.g., Heroku or Netlify).

#### **Deliverables**
- Functional Streamlit dashboard.
- Public deployment link or screenshots.

---

## **Final Deliverables**

1. Python scripts for all tasks.
2. Slides summarizing findings from all tasks.
3. GitHub repository link with project files.
4. Streamlit dashboard (deployed or screenshots).
5. MySQL database table export with satisfaction scores.

---

## **References**
- Exploratory Data Analysis in Python
- Univariate and Bivariate Analysis
- Correlation Analysis
- Principal Component Analysis (PCA)
- K-means Clustering


