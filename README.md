# TRAVEL PREDICTION USING ML 

![image](https://github.com/franciskyalo/travelprediction/assets/94622826/b0446c7d-d615-4d2f-8a7e-6e9ca2e5d90c)


Project Overview: 

ExploreXperience, a prominent tour company, has been actively offering travel insurance to its customers, particularly in the context of the ongoing Covid-19 pandemic. In an effort to strategically target potential customers interested in purchasing travel insurance post-pandemic, the company is leveraging past sales data for in-depth analysis.

Significance of Data Utilization: 

The paramount importance of data in this initiative cannot be overstated. Data-driven insights play a pivotal role in comprehending customer behavior, preferences, and emerging trends. By delving into historical sales records, ExploreXperience extracts valuable intelligence on customer demographics, buying patterns, and the effectiveness of previous insurance offerings. This data empowers the company to pinpoint key indicators that signify a customer's inclination towards acquiring travel insurance.

Implications of Analysis: 

The implications of this data-driven analysis are profound for ExploreXperience. It enables the company to make informed, targeted marketing efforts, optimizing resources and increasing the likelihood of a successful campaign. Accurately identifying potential customers enhances revenue streams while solidifying customer trust and loyalty. This strategic use of data ensures that ExploreXperience remains agile and responsive to changing market dynamics, securing its position as a forward-thinking industry leader.

Main Objective: 

The primary goal of this project is to develop a predictive model capable of identifying customers who are more likely to purchase the travel insurance package. This model will facilitate the delivery of targeted marketing messages to the identified customer segment.

Other Objectives: 

In addition to the main objective, the project will include an exploratory data analysis to derive insights and recommendations regarding the factors that significantly influence whether a customer will choose to buy or not buy the travel insurance package.

Metric for Success: 

The project's success will be contingent on the model achieving an accuracy rate of 90% and a recall rate exceeding 80%. Furthermore, successful deployment into a production environment is a crucial criterion for considering the project accomplished.

Data Understanding

This dataset consists of 1987 records and 10 columns with the following information:

Unnamed: Data entry identifier.
Age: Customer's age.
Employment Type: Sector of customer's employment.
GraduateOrNot: Indicates if the customer is a college graduate.
AnnualIncome: Yearly income in Indian Rupees (rounded to the nearest 50 thousand Rupees).
FamilyMembers: Number of members in the customer's family.
ChronicDisease: Presence of major diseases or conditions.
FrequentFlyer: Derived from the customer's history of booking air tickets at least four times in the last two years (2017-2019).
EverTravelledAbroad: Indicates if the customer has traveled to a foreign country, not necessarily using the company's services.
TravelInsurance: Specifies if the customer purchased a travel insurance package during the introductory offering in 2019.
MODELLING:

Oversampling for Minority Class using SMOTE: Employing the Synthetic Minority Over-sampling Technique (SMOTE) to address the class imbalance by generating synthetic instances of the minority class. This ensures a more representative training dataset.

Establishing a Baseline with Logistic Regression: Initially, establishing a baseline using logistic regression as a benchmark. This serves as a foundational model against which the performance of other, more complex models will be compared.

Exploring Alternative Models: Investigating a range of alternative models to discern their efficacy in comparison to the baseline. This includes the examination of random forest classifier, support vector classifier, Adaboost classifier, and XGBoost classifier. Each model will be assessed based on its ability to capture the nuances of the data and make accurate predictions.

Hyperparameter Fine-Tuning: For the top-performing model(s) identified during the exploration phase, engaging in a meticulous process of hyperparameter fine-tuning. This involves optimizing the configuration of model parameters to enhance both prediction accuracy and recall, thereby achieving a well-balanced and robust predictive model.

Performance Evaluation of Default and Tuned Models: Rigorously evaluating the performance of both the default and tuned versions of the best-performing models. This evaluation will encompass various metrics, prioritizing not only overall prediction accuracy but also recall, given the importance of correctly identifying instances of the minority class.

Selection of the Most Effective Model: Based on the thorough evaluation results, selecting the model that most effectively aligns with the business objective. This entails a holistic consideration of model performance, striking a balance between accuracy and the ability to correctly identify instances of interest, crucial for addressing the underlying business problem.

Recommendations for ExploreXperience:

Target the Private Sector: Focus marketing efforts on the private sector, where 28% of travel insurance purchases originated. Tailor strategies to address the concerns or preferences of the 42.63% of private sector customers who did not buy insurance.

Leverage Education Level: Recognize the influence of education level on insurance decisions. With graduates showing a 30.75% purchase rate compared to 4.98% for non-graduates, ExploreXperience can create targeted campaigns to attract and convert non-graduate customers.

Consider Chronic Disease Status: Pay attention to customers with chronic diseases, as only 10% have purchased travel insurance. This presents an opportunity to provide tailored insurance offerings or additional benefits. Addressing concerns or reservations may increase adoption in this segment.

Engage Frequent Flyers: Recognize that only 12% of frequent flyers purchased travel insurance. Design promotions or packages specifically for this group, emphasizing the benefits of insurance for frequent travelers to boost conversion rates.

Promote Travel Abroad Experiences: Capitalize on the 15% higher likelihood of travel insurance purchase among customers who have traveled abroad. Emphasize the value of insurance for international travel, including features such as medical coverage, trip cancellation protection, and assistance services tailored for overseas trips.

Educate Non-Travelers on Insurance Benefits: Run awareness campaigns targeting the 60% of customers who have not traveled abroad and have not purchased travel insurance. Highlight the importance of insurance for domestic trips, covering unexpected events like trip cancellations, medical emergencies, or lost luggage.

Customer Feedback and Customization: Gather feedback from customers who did not purchase insurance to understand concerns or reasons for their decision. Use this information to customize insurance offerings, address objections, and enhance the overall value proposition, fostering a customer-centric approach.


```
code
```
