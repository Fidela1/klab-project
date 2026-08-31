# Soft Skills for AI Engineers Capstone

## Task 1: Capstone Idea Brainstorm

### Idea 1: AI Property Valuation and Neighborhood Insight Platform

**Problem** : Property owners and sellers in Rwanda often struggle to judge whether an asking price is reasonable. Financial institutions face the same problem when a property is used as security for a loan and needs a defensible value estimate. Value depends on location, land size, building size, bedrooms, condition, accessibility, and proximity to services like schools, hospitals, and markets — too many interacting factors to price by feel. Today, people rely on asking prices, personal judgment, historical sales they've heard about, or a professional valuer.

**Why AI/ML helps**: A fixed pricing rule (e.g. price per square meter by district) can't capture how these factors interact — two houses of the same size in the same neighborhood can differ in value because of condition or road access. Machine learning can learn those interactions directly from historical property records, producing a faster, more consistent reference than manual comparison or a flat formula.

**Possible data**: Property records; price, location, land size, building size, bedrooms, bathrooms, type, year built, condition, accessibility — from public listings, open datasets, or manually collected samples. Neighborhood data (distance to schools, hospitals, transit) from OpenStreetMap.

**Realistic to obtain**: Obtainable, but collecting enough reliable, diverse records across different regions of Rwanda within the project timeline is the main risk.

### Idea 2: AI Student Performance Early-Warning System

Problem: Teachers often identify at-risk students too late — after grades have already dropped — relying mainly on attendance, participation, and personal observation rather than any earlier signal.

Why AI/ML helps: No single metric (attendance, one low grade) reliably predicts risk on its own, but the combination of attendance trends, assignment scores, and study time does — a pattern-recognition problem a static threshold rule handles poorly, since the right threshold varies by student and subject. A model trained on historical outcomes can weigh these factors together and flag risk earlier than a single-metric rule would.

Possible data: Anonymized attendance, prior grades, assignment results, and study time from publicly available educational datasets.

Realistic to obtain: Public datasets exist, but using real student data raises privacy concerns that would need to be resolved before any real deployment.

### Idea 3: AI Waste Classification Assistant

Problem: People often sort waste incorrectly — recyclable, organic, general — because visually similar items belong to different categories and the rules aren't intuitive.

Why AI/ML helps: Waste items vary enormously in appearance within each category (a plastic bottle and a plastic bag look nothing alike but are both "plastic"), which a rule-based system based on simple features can't generalize across. Image classification learns visual patterns directly from labeled examples instead.

Possible data: Publicly available waste-image datasets covering plastic, paper, glass, metal, and food waste.

Realistic to obtain: Relatively accessible, but training and tuning an image classifier well would take more compute and iteration time than the other two ideas.

## Selected Idea

I selected the AI Property Valuation and Neighborhood Insight Platform.

I chose it because it addresses a real problem in Rwanda's property market and serves two distinct stakeholders sellers and financial institutions, rather than one. The tradeoff is data: the other two ideas have easier-to-find, ready-made public datasets, while reliable property data covering different regions of Rwanda is harder to source and may be inconsistent. I judged local relevance and real-world usefulness as worth more than picking the project with the easiest data path.

Task 2: Plain-Language Pitch
AI Property Valuation and Neighborhood Insight Platform

A family in Kigali trying to sell their home often has no reliable way to know if their asking price is fair — they compare it to a neighbor's sale price from two years ago, or trust whatever a broker tells them. Financial institutions face the same guesswork when a property is used as security for a loan and needs a defensible value.

This project is a platform where someone enters basic details about a property — location, size, number of bedrooms, condition, nearby services — and receives an estimated value along with useful context about the neighborhood, like distance to schools, hospitals, and transport.

AI is the right tool here because property value depends on many factors interacting at once — location, size, and condition don't add up in a simple formula — and a model trained on real property data can weigh those factors the way an experienced valuer would, but instantly and consistently.

This isn't meant to replace a professional valuer. It's meant to give sellers a fast, honest reference point before they set a price, and give financial institutions an additional data point when reviewing a property. Success looks like this: a seller in any part of Rwanda can enter their property's details and get a value estimate, with context, that a real valuer would consider reasonable.

Task 4: Project Proposal Documentation
1. Problem Statement and Target User

Property owners and sellers in Rwanda often can't tell whether a property's expected selling price is reasonable. Financial institutions face the same difficulty when evaluating a property offered as loan security. Value depends on location, land size, building size, bedrooms, bathrooms, type, condition, accessibility, and proximity to services — factors that interact in ways a fixed pricing rule can't capture. Today, both groups rely on asking prices, personal judgment, historical sales knowledge, or a professional valuer.

Target users:

Property owners and sellers — need a fast, independent reference for what their property is worth.
Financial institutions — need a consistent additional data point when evaluating property for lending decisions.

The platform will output an estimated property value plus neighborhood context: distance to schools, hospitals, markets, and transportation.

2. Proposed Approach

Collect and clean property records (location, land size, building size, bedrooms, bathrooms, type, year built, condition, accessibility) into a format suitable for machine learning. Start with a simple baseline model to establish a performance floor, then test a Random Forest regressor for the actual value prediction — a good fit given the number of interacting, mostly tabular features.

The trained model takes property characteristics as input and outputs an estimated value. Location data is separately used to compute neighborhood indicators (nearest school, hospital, market, transit) via a geographic data source.

Results are presented as estimates with visible uncertainty, not as guaranteed professional valuations.

3. Data

Core dataset fields: price/valuation amount, location, land size, building size, bedrooms, bathrooms, property type, year built, condition, accessibility, and nearby services.

Sources: public property listings, open datasets, and manually collected sample records from different parts of Rwanda, stored in structured tabular format (CSV) during preparation and training. Neighborhood/service-proximity data from OpenStreetMap or an equivalent geographic source.

Open question: Can enough reliable, diverse property records be collected across different regions of Rwanda within the project timeline? Urban and rural markets likely behave differently, and data quality will need to be checked, not assumed, before training.

4. Success Criteria

The project succeeds if:

A cleaned, documented property dataset covering multiple regions of Rwanda exists for model development.
The model produces value estimates for property data it hasn't seen before.
The model reaches an acceptable predictive performance on standard metrics (MAE, R²).
The system returns understandable neighborhood indicators alongside the estimate.
A user can enter property details and receive an estimate through the platform.
The system clearly communicates the limits of its estimates (not a substitute for a professional valuation).
The output is genuinely useful as an additional reference for sellers and institutions — not just technically functional.
5. Scope Cut

Version one is limited to property valuation and basic neighborhood indicators, deliberately excluding a full marketplace, direct property purchasing, mortgage approval, automated loan decisions, legal services, or professional valuation certification. Cutting these keeps the timeline realistic and puts the available time into data preparation, model development, and evaluation of the core valuation system — the part that actually needs to work well before anything else is worth adding.

Task 5: A Technical Tradeoff, Explained

Subject: Data strategy recommendation — start with an existing dataset, not a from-scratch local collection

I recommend starting with an existing property dataset and supplementing it with locally collected Rwandan data where possible, rather than trying to build the entire dataset from scratch first. This gets us to a working, testable model much sooner.

The real tradeoff is speed versus local accuracy. Collecting our own data from properties across Rwanda would make the system more tailored to the local market, but it takes significant time and the records could be inconsistent or hard to verify — we'd spend most of the project just gathering data before we ever test a model. Starting from an existing dataset gets us a structured, faster starting point, at the cost of it not perfectly reflecting Rwanda's property market on day one.

The main risk with this approach: the initial data may not represent property prices across all regions well, especially the gap between urban and rural markets, which could make early predictions less reliable in underrepresented areas. To manage that, I'll document exactly where the data comes from, check how well different regions are represented before trusting the model's output, evaluate performance by region rather than as one average number, and clearly flag the model's limitations to users. Local data can be folded in as we collect it.

Task 6: Reflection

1. How did your idea change between Task 1 and Task 4? The idea started as a straightforward price predictor. Comparing it against the other two candidates, and thinking through who would actually use it, pushed it into a broader valuation-plus-neighborhood-context platform serving two different stakeholders, and expanded the intended coverage from one city to the whole country. The biggest shift was realizing regional differences in property data and pricing are a real design constraint, not a detail — which is why the proposal now treats "how well does this generalize across regions" as an open question rather than an assumption.

2. What are you least confident about? The availability and quality of property data covering all of Rwanda, not just Kigali. A model is only as good as this data, and I don't yet know how unevenly it's distributed across regions. To get more confident, I need to actually pull together sample records from a few different regions, look at how many exist and how consistent they are, and test whether the model's performance holds up outside the areas best represented in the data — before assuming the dataset is sufficient.