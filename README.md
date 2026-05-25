# 🛍️ Retail Sales Data Agent

> A working Data Agent built on **Databricks AI/BI** that lets any business user ask plain-English questions about retail sales performance and receive clear, data-backed answers — no SQL required.

## Objective

Build a Retail Sales Data Agent on Databricks using a provided retail transactions dataset. The agent helps a store manager, business owner, or executive ask questions about shop performance and receive useful business insights in plain language, backed by real data.


## Tools Used

| Tool | Purpose |
|------|---------|
| **Databricks AI/BI** | Platform for hosting the Data Agent and querying the dataset |
| **Databricks SQL Warehouse** | Executes queries against the retail_sales_data table |
| **Delta Lake** | Storage format for the registered retail_sales_data table |
| **Claude (Anthropic)** | LLM powering the agent's reasoning and natural language responses |
| **GitHub** | Version control and project submission |


## Dataset Overview

The dataset is a CSV file of retail sales transactions loaded into Databricks as a registered Delta table named **retail_sales_data**.

| Column | Type | Description |
|--------|------|-------------|
| `Transaction ID` | String | Unique identifier for each sale |
| `Date` | Date | Date the transaction occurred |
| `Customer ID` | String | Unique identifier per customer |
| `Gender` | String | Customer gender — Male or Female |
| `Age` | Integer | Customer age in years |
| `Product Category` | String | Category of the product sold |
| `Quantity` | Integer | Number of units purchased |
| `Price per Unit` | Decimal | Price of a single unit (ZAR) |
| `Total Amount` | Decimal | Full transaction value — primary revenue metric |

### What the data supports

- **Sales analysis** — revenue totals, transaction counts, average order value
- **Time trends** — daily, weekly, monthly, quarterly, seasonal patterns
- **Product performance** — category rankings by revenue and volume
- **Customer behaviour** — spend tiers, age groups, gender patterns
- **Cross-cuts** — e.g. which category sells best to women aged 25–34


## The 10-Step Process

### Step 1 · Upload the Dataset
The retail sales CSV was uploaded into Databricks using the Data tab → Create Table → Upload File. The row count and file size were confirmed against the original CSV before proceeding.

### Step 2 · Review the Dataset
Each column was inspected for data type, sample values, and any quality issues. `df.printSchema()` and `df.describe()` were run to understand the shape of the data, identify the range of ages, and confirm product categories.

### Step 3 · Prepare the Table
The dataset was registered as a named Delta table — **retail_sales_data** — in the default schema. Descriptions were added to the table and to each column so the agent reads the data structure correctly.

### Step 4 · Create the Data Agent
A new Data Agent was created inside Databricks AI/BI and named **Retail Sales Insights Agent**. The retail_sales_data table was connected as the data source. A connectivity test confirmed the agent could query the table before instructions were added.

### Step 5 · Write the Agent Instructions
The agent instructions were written from scratch following the BrightLearn 8-section framework. They cover role, dataset rules, supported question types, response structure, trend rules, data quality, ambiguity handling, and recommendation guidelines. Full instructions are in `agent_instructions.txt` and `docs/Agent_Instructions.docx`.

### Step 6 · Test with 10 Questions
Ten original business questions were asked covering total revenue, category performance, gender patterns, age-group behaviour, spend tiers, seasonal trends, and an intentionally ambiguous question to test clarification behaviour.

### Step 7 · Validate 3 Answers
Three answers were independently checked against the source data using direct SQL aggregations and manual table filtering in Databricks. Verdicts (correct / partially correct / incorrect) are documented in the write-up.

### Step 8 · Write-Up Document
A full Word document was compiled covering all steps, the agent instructions in full, all 10 questions and answers, 3 validations, key insights, business recommendations, and a conclusion.

### Step 9 · Push to GitHub
All project files were pushed to this public GitHub repository.

### Step 10 · Submit via BrightLearn Portal
The repository link was submitted via the BrightLearn Portal before the 24 May 2026 deadline.

---

## Agent Instructions

The full instructions are in `agent_instructions.txt`. A summary of each section:

| Section | What it covers |
|---------|---------------|
| **01 · Role** | The agent is a Retail Performance Intelligence Agent serving store managers, business owners, and executives |
| **02 · Dataset** | Uses only retail_sales_data; all nine columns described |
| **03 · Question Types** | Sales, trends, AOV, products, spend tiers, age groups, gender, cross-analysis |
| **04 · Response Structure** | Direct answer → supporting metrics → business insight → recommendation (when data supports it) |
| **05 · Trend Rules** | Period comparisons, seasonal groupings (Summer/Autumn/Winter/Spring), strongest and weakest identification |
| **06 · Data Quality** | No fabrication, flag anomalies, zero-row rule, missing-value handling |
| **07 · Ambiguity** | Ask before guessing — examples: "best customers", "recent sales", "selling well" |
| **08 · Recommendations** | Only when data clearly supports an action; always cite the evidence |
| **09 · Communication** | Professional, direct, business language — never SQL terms or database jargon |


##  Sample Questions Tested

| # | Question | Type |
|---|---------|------|
| Q1 | What is the total revenue generated across the entire dataset? | Simple — baseline |
| Q2 | Which product category generated the highest total revenue? | Category ranking |
| Q3 | How does revenue compare across months? Which was strongest and weakest? | Monthly trend |
| Q4 | What is the average transaction value overall and by product category? | AOV breakdown |
| Q5 | Do male or female customers spend more on average? Break it down by category. | Gender × category |
| Q6 | Which age group spends the most in total? Show all age groups. | Age group analysis |
| Q7 | What share of customers fall into each spend tier, and which tier drives the most revenue? | Spend tier segmentation |
| Q8 | Is there a seasonal pattern in sales? Which season performs best and worst? | Seasonal analysis |
| Q9 | Which product category sells best to customers aged 18–34? Does it differ for older customers? | Age × category cross-cut |
| Q10 | I want to understand our best customers. Who should we focus on? | Ambiguous — tests clarification |



## ✅ Key Insights

> Replace with your actual findings once the agent has been tested.

1. **Top category** — [Category name] generated the highest total revenue at R [amount], accounting for [x]% of all sales.
2. **Strongest period** — [Month/Season] was the strongest sales period with R [amount] in revenue.
3. **Gender patterns** — [Male/Female] customers have a higher average transaction value at R [amount] vs R [amount].
4. **Age group** — The [x–x] age group contributes the most total revenue at R [amount] ([x]% of total).
5. **Spend tiers** — High spenders (R500+) represent [x]% of transactions but account for [x]% of total revenue.

---

## 💡 Business Recommendations

> Replace with your actual recommendations based on your agent's findings.

1. **Prioritise the top category** in promotional and stock planning — particularly heading into peak season.
2. **Create a retention offer for high spenders** — they drive a disproportionate share of revenue despite being a smaller customer group.
3. **Target under-represented age groups** with category-specific promotions to broaden the revenue base.
4. **Review the lowest-performing category** — consider repricing, bundling, or repositioning to recover underperforming revenue.

---

## 📝 Validation Summary

| # | Question Validated | Method Used | Verdict |
|---|-------------------|-------------|---------|
| V1 | Total revenue (Q1) | SQL: `SELECT SUM(Total_Amount) FROM retail_sales_data` | Correct |
| V2 | Top category (Q2) | SQL: `GROUP BY Product_Category ORDER BY SUM(Total_Amount) DESC` | Correct |
| V3 | Monthly trend (Q3) | SQL: `GROUP BY MONTH(Date) ORDER BY month` + manual filter check | Correct |

