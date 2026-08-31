# Soft Skills for AI Engineers Capstone

## Task 1: Capstone Idea Brainstorm

### Idea 1: AI Property Valuation and Neighborhood Insight Platform

**Problem:**

Rwanda's real estate market is growing rapidly due to urbanization and increasing demand for property. However, existing property-listing platforms mainly show properties and asking prices without explaining how those prices were determined or providing useful information about the surrounding neighborhood, such as access to schools, hospitals, and transportation.

As a result, sellers often have to estimate the value of their properties by comparing them with properties that were sold previously or by relying on the price suggested by a broker. Financial institutions face a similar challenge when a property is used as collateral for a loan because they need a reliable way to assess whether the property's stated value is reasonable. Much of this process remains informal, which can contribute to price mismatches and a lack of trust in the market.

**Why AI/ML helps:**

A simple rule such as "price per square meter by district" would not capture all the factors that influence property value. Two properties with similar sizes in the same area can have very different values because of differences in road access, condition, property type, or proximity to important services.

Machine learning is useful because it can learn how multiple factors interact and identify patterns from property data instead of treating each factor independently. This makes it more suitable for estimating property values than a fixed rule-based formula.

**Possible data:**

The project could use property records containing information such as price or valuation, location, land size, building size, number of bedrooms and bathrooms, property type, year built, condition, and accessibility. Data could come from public property listings, open datasets, and manually collected records where possible.

Neighborhood information, such as distances to schools, hospitals, markets, and transportation, could be obtained from OpenStreetMap or similar geographic data sources.

**Realistic to get:**

The data is potentially obtainable, but the main challenge will be collecting enough reliable and diverse records from different parts of Rwanda, especially outside Kigali.

---

### Idea 2: AI Student Performance Early-Warning System

**Problem:**

Teachers may not always notice that a student is struggling until their grades have already declined. Currently, teachers may rely on attendance, participation, previous grades, and personal observation to identify students who may need additional support.

**Why AI/ML helps:**

No single indicator can reliably identify every student who is at risk. Low attendance alone may not mean a student is struggling, and one poor grade may not tell the whole story. However, combining attendance, grades, assignment performance, and study patterns could reveal trends that are difficult to identify using a single fixed threshold.

Machine learning could help identify these patterns and highlight students who may benefit from early academic support.

**Possible data:**

The system could use anonymized data such as attendance, previous grades, assignment scores, study time, and participation from publicly available educational datasets.

**Realistic to get:**

Public datasets are available, but using real student records would introduce privacy concerns. For a capstone project, using anonymized public data would be more realistic.

---

### Idea 3: AI Waste Classification Assistant

**Problem:**

People often have difficulty determining which waste category an item belongs to, such as recyclable, organic, or general waste. Items within the same category can also look very different. For example, a plastic bottle and a plastic bag are both plastic but have very different appearances.

**Why AI/ML helps:**

Image classification is well suited to this problem because it can recognize objects based on their appearance even when objects within the same category look different. A rule-based system based on fixed shapes, colors, or object descriptions would be difficult to scale to the wide variety of waste items.

**Possible data:**

The project could use publicly available waste-image datasets containing categories such as plastic, paper, glass, metal, and food waste.

**Realistic to get:**

This would be the easiest of the three projects in terms of finding suitable data. However, the tradeoff is that training and testing an image-classification model could require more computing resources and technical work.

### Selected Idea

I selected the **AI Property Valuation and Neighborhood Insight Platform**.

The waste-classification project has the easiest data to obtain, while the student-performance project has a relatively clean machine-learning problem. I am giving up those advantages because the property project addresses a problem that is more relevant to Rwanda and has potential value for two important groups: property sellers and financial institutions.

I also have existing knowledge of the property domain from my previous work, which means I am not starting completely from zero. The main cost of this choice is data availability. I may spend significant time trying to obtain reliable property records from different parts of Rwanda, but I am choosing that challenge because the project's relevance and potential impact are more important to me than choosing a project simply because its data is easier to obtain.

---

## Task 2: Plain-Language Pitch

### AI Property Valuation and Neighborhood Insight Platform

Property sellers in Rwanda often have difficulty determining what their property is actually worth. They may compare their property with one that was sold several years ago, rely on a broker's suggested price, or simply choose a price based on their own judgment. Existing property-listing platforms mainly show properties and asking prices, but they do not provide much information about how a price was determined or what the surrounding neighborhood is like.

Financial institutions face a similar challenge from a different perspective. When someone uses a property as collateral for a loan, the institution needs a reliable reference for determining whether the property's stated value is reasonable.

This project will provide an estimated property value together with useful information about the surrounding area. A user can enter details such as the property's location, size, number of bedrooms, property type, and condition. The platform will then provide an estimated value and neighborhood information, including proximity to schools, hospitals, markets, and transportation.

AI is appropriate because property value depends on many factors working together, and these relationships are difficult to capture with a simple fixed formula.

The platform will not replace professional property valuers. Instead, it will provide an additional reference point that sellers can use when pricing their properties and financial institutions can consider during property-related assessments.

Success means that users across Rwanda can enter property details and receive a reasonable, understandable estimate supported by useful neighborhood information.

---

## Task 4: Project Proposal Documentation

### 1. Problem Statement and Target User

Rwanda's property market is growing rapidly, but existing property-listing platforms generally focus on displaying properties and asking prices rather than explaining how those prices were determined or providing useful information about the surrounding neighborhood.

As a result, property sellers often rely on comparisons with previous sales, personal judgment, or broker recommendations when deciding how much to ask for their property. Financial institutions face a similar challenge when properties are used as collateral because they need a reliable reference for assessing whether a property's stated value is reasonable.

Property value depends on multiple factors, including location, land and building size, number of bedrooms and bathrooms, property type, condition, accessibility, and proximity to important services. These factors are not currently combined into one consistent and understandable estimate.

**Target users:**

* **Property sellers** — need an independent reference when deciding how to price their property.
* **Financial institutions** — need an additional consistent reference when assessing properties used as loan collateral.

The platform will provide an estimated property value together with neighborhood context, including proximity to schools, hospitals, markets, and transportation.

### 2. Proposed Approach

The project will collect property records containing information such as location, land size, building size, bedrooms, bathrooms, property type, year built, condition, accessibility, and other relevant characteristics.

The collected data will be cleaned, explored, and transformed into a format suitable for machine-learning analysis. A simple baseline model will first be developed to provide a reference point for performance. A Random Forest regression model will then be evaluated because it is well suited to tabular data containing multiple property characteristics.

The model will take property characteristics as inputs and produce an estimated property value.

Location information will also be used to obtain neighborhood indicators, such as the distance to the nearest school, hospital, market, and transportation point, using an appropriate geographic data source.

The estimated value and neighborhood indicators will be presented through a user-friendly interface. The system will communicate that its output is an estimate and not a certified professional valuation.

### 3. Data

The main dataset will contain fields such as:

* Property price or valuation
* Location
* Land size
* Building size
* Number of bedrooms
* Number of bathrooms
* Property type
* Year built
* Property condition
* Accessibility
* Nearby services

Property data may come from public property listings, open datasets, and manually collected records from different parts of Rwanda.

Neighborhood and proximity information may be obtained from OpenStreetMap or another appropriate geographic data source.

The property data will initially be stored in a structured format such as CSV during data preparation and model training.

**Open question:**

Can enough reliable and diverse property records be obtained from different parts of Rwanda before the project deadline? Property markets in urban and rural areas may behave differently, so data quality and regional representation will need to be evaluated rather than assumed.

### 4. Success Criteria

The project will be considered successful if:

1. A cleaned and documented dataset containing property records from more than one region of Rwanda is created.
2. The model produces reasonable estimates for property data that it has not seen during training.
3. The model achieves an acceptable level of performance based on metrics such as Mean Absolute Error (MAE) and R².
4. Neighborhood indicators are returned in a format that is understandable to non-technical users.
5. A user can enter property details through the interface and receive an estimated value.
6. The system clearly communicates its limitations and does not present the estimate as a replacement for professional valuation.
7. The output provides useful information for property sellers and financial institutions rather than being technically accurate without practical value.

### 5. Scope Cut

Version one will focus on **property valuation and basic neighborhood information across Rwanda**.

The project will deliberately exclude:

* A complete real-estate marketplace
* Direct property purchasing
* Mortgage approval
* Automated loan decisions
* Legal services
* Professional valuation certification

These features are outside the core purpose of the first version. The priority is to ensure that the property valuation system has reliable data, reasonable predictive performance, and useful neighborhood information before expanding into additional services.

---

## Task 5: A Technical Tradeoff, Explained

### Subject: Recommendation on Property Data

My recommendation is to start with an existing property dataset and gradually add relevant Rwandan property data rather than trying to build the entire dataset from scratch. This will allow us to begin testing the system sooner and spend more time improving the core project.

The main tradeoff is **speed versus how closely the data represents Rwanda's property market**. Collecting all the data ourselves could produce information that is more relevant to Rwanda, but it would take a significant amount of time and the records could be inconsistent or difficult to verify. Starting with an existing dataset gives us a faster and more structured foundation, although it may not accurately represent all regions of Rwanda.

The main risk is that the initial dataset may contain more information about certain areas, especially urban locations, than others. As a result, predictions could be less reliable in regions that are poorly represented.

To reduce this risk, I will document where the data comes from, check how different regions are represented, evaluate the model's performance across regions rather than relying only on one overall score, and clearly communicate areas where the estimates may be less reliable. Local Rwandan data can then be added as it becomes available.

---

## Task 6: Reflection

### 1. How did your idea change between Task 1 and Task 4?

The idea started as a relatively simple project focused on predicting property prices. After considering the different users and comparing it with the other two ideas, I developed it into a broader property valuation and neighborhood insight platform. I also expanded the scope from focusing on Kigali to covering the whole of Rwanda. The biggest shift was realizing that regional differences in property data are an important part of the problem and need to be considered in the design rather than treated as a minor limitation.

### 2. What am I least confident about?

The part of my proposal I am least confident about is whether I can obtain enough reliable property data from outside Kigali. The model's quality will depend heavily on the quality and diversity of the data used to train it, and I do not yet know how much the available data will be concentrated in the capital. To become more confident, I need to collect or identify sample records from several regions, examine their quantity and consistency, and evaluate whether the model performs reasonably well across different areas of Rwanda.
