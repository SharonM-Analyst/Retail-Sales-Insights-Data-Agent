# 🛍️ Retail Sales Data Agent

> A working Data Agent built on **Databricks AI/BI** that lets any business user ask plain-English questions about retail sales performance and receive clear, data-backed answers no SQL required.


![ML Workflow](https://github.com/SharonM-Analyst/Bank-Fraud-Detection/blob/6e7b483b5b061be774355510f4398485a6e5ae79/0.%20ELT%20Pipeline/1.%20Architecture/Untitled%20Diagram.gif)









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
The agent instructions were written from scratch following the BrightLearn 8-section framework. They cover role, dataset rules, supported question types, response structure, trend rules, data quality, ambiguity handling, and recommendation guidelines. 

### Step 6 · Test with 10 Questions
Ten original business questions were asked covering total revenue, category performance, gender patterns, age-group behaviour, spend tiers, seasonal trends, and an intentionally ambiguous question to test clarification behaviour.

### Step 7 · Validate 3 Answers
Three answers were independently checked against the source data using direct SQL aggregations and manual table filtering in Databricks. Verdicts (correct / partially correct / incorrect) are documented in the write-up.


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

#### Sales Performance

•	Q4 and Q2 together account for 55% of annual revenue — plan promotions and inventory peaks around these windows.
•	September is a structural low; targeted campaigns are needed to defend this month.
•	Saturday is the highest-value shopping day by AOV — weekend offers should be premium-positioned.

####  Product Category
•	No single category dominates year-round — all three require separate seasonal planning cycles.
•	Beauty achieves the highest AOV despite the lowest transaction count, signalling quality-conscious buyers worth nurturing.
•	Clothings volume leadership (894 units) with lower AOV suggests a high-frequency, lower-basket segment suited to loyalty incentives.

#### Customer Behaviour
•	No single age group consistently dominates — the top three (45-54, 25-34, 35-44) are within 0.4% of each other, creating a diversified customer base.
•	18-24 buyers spend significantly per order but transact infrequently — activation campaigns could unlock substantial value.
•	Seniors are a hidden weekend opportunity with the highest weekend AOV of any age group.
•	The 25-44 female segment shows the strongest gender revenue lead — a prime target for female-focused campaigns.

#### Spending Tier
•	The business is structurally dependent on High Spenders (85% of revenue from 35% of customers) — this is both a strength and a concentration risk.
•	The September collapse among High Spenders (–63%) is the single most critical event in the data and demands an active retention or engagement strategy.
•	Medium Spenders represent the most accessible upsell opportunity — converting even 20% of this group to High Spender thresholds would add approximately R10,000 in revenue.

#### Cross Analysi
•	Three age groups (18-24, 25-34, and 45-54) deviate from the overall Electronics-first ranking, highlighting generational differences.
•	Young and Mature Adults Favor Beauty, possibly for different reasons like cosmetics for youth and premium wellness for older customers.
•	The 25-34 segment’s strong Clothing preference signals a prime target for fashion-focused marketing.
•	Seniors prioritize Electronics significantly more, suggesting a focus on technology rather than personal care.
•	These insights emphasize the need for age-specific marketing and inventory strategies rather than a one-size-fits-all approach based on overall category trends.


## Business Recommendations

1.	Protect High Spenders with a VIP programme
They drive 85% of revenue but experienced a 63% September collapse. Launch a tiered VIP programme offering exclusive early access, personalised service, and a September reactivation campaign (targeted email, bonus rewards) to defend this critical group.

2.	Build a September-specific campaign across all segments
September is the weakest month by revenue (R23,620) and the worst month for High Spenders. This seasonal disengagement event needs to be countered with a time-limited promotion, flash sale, or loyalty bonus running throughout September.

3.	Create age-segmented category marketing
Three of five age groups deviate from the overall category ranking. Run Beauty-first campaigns for 18-24 and 45-54 groups; fashion-led campaigns for 25-34; technology-led campaigns for 35-44 and 55-64. One-size messaging leaves revenue on the table.

4.	Upsell Medium Spenders to the High Spender tier
Medium Spenders (R100-R499) represent 30% of transactions but only 11% of revenue. A targeted upgrade nudge
•	Free shipping over R500, bundle discount at checkout, or loyalty point acceleration above R500 
5.	Activate the 18-24 segment with frequency incentives
Young Adults have the highest AOV in the dataset (R501) but the lowest transaction volume. They are high value when they shop. A subscription model, early-access privilege, or birthday campaign would increase their purchase frequency without discounting their basket size.

6.	Launch a senior’s weekend programme
55-64 Seniors have the highest weekend AOV of any age group (R561) and spend 45% more on weekends than weekdays. A dedicated weekend promotion, weekend-only bundle, or in-store experience designed for this group would amplify their natural behaviour.

7.	Deploy gender-specific campaigns by age band
Female-focused marketing is most effective for ages 25-44 (females lead by up to 9.4%). Male-focused campaigns are better suited to 18-24 and 45-54 groups. Gender-neutral messaging is optimal for 55-64 (only 0.4% gap). Align creative assets and targeting to these patterns.

8.	Invest on Saturday as a premium shopping event
Saturday has the highest AOV (R525) and highest total revenue (R78,815) of any day. Position Saturday as a premium in-store or online experience.
•	Exclusive Saturday drops.
•	weekend-only bundles.
•	highlighted collections.

9.	Align inventory and promotions to category seasonality
Electronics peaks in Summer and Winter; Clothing peaks in Autumn and Spring; Beauty is relatively stable with a Mature Adults peak. Stock planning, markdown timing, and promotional budgets should reflect these cycles rather than treating all three categories identically.

10.	Investigate and monetise male Beauty buyers
Male customers in Beauty have an AOV of R487 the highest of any gender-category pair despite lower transaction frequency. This signals a high-intent, under-served segment. 
•	A targeted male grooming or wellness sub-range with direct marketing could significantly grow Beauty revenue.
•	Introduce new products that will attract female, trending make up lines and hire influencers who have big numbers on TikTok, Instagram, YouTube to promote the products


## Validation Summary

| # | Question Validated | Method Used | Verdict |
|---|-------------------|-------------|---------|
| V1 | Total revenue (Q1) | SQL: `SELECT SUM(Total_Amount) FROM retail_sales_data` | Correct |
| V2 | Top category (Q2) | SQL: `GROUP BY Product_Category ORDER BY SUM(Total_Amount) DESC` | Correct |
| V3 | Monthly trend (Q3) | SQL: `GROUP BY MONTH(Date) ORDER BY month` + manual filter check | Correct |

