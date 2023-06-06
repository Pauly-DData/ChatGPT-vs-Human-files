from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

# create a list of URLs to scrape
urls = [
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Intro%20to%20Python%20for%20Data%20Science/Instructions/Chapter1.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Intro%20to%20Python%20for%20Data%20Science/Instructions/Chapter2.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Intro%20to%20Python%20for%20Data%20Science/Instructions/Chapter3.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Intro%20to%20Python%20for%20Data%20Science/Instructions/Chapter4.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Intermediate%20Python%20for%20Data%20Science/Instructions/Chapter%201-Matploblib.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Intermediate%20Python%20for%20Data%20Science/Instructions/Chapter%202-Dictionaries%20%26%20Pandas.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Intermediate%20Python%20for%20Data%20Science/Instructions/Chapter%203-Logic%2C%20Control%20Flow%20and%20Filtering%20.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Intermediate%20Python%20for%20Data%20Science/Instructions/Chapter%204%20-%20Loops.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Intermediate%20Python%20for%20Data%20Science/Instructions/Chapter%204-Loops.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Intermediate%20Python%20for%20Data%20Science/Instructions/Chapter%205%20-%20Case%20Study',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Intermediate%20Python%20for%20Data%20Science/Instructions/Chapter%205%20-%20Case%20Study:%20Hacker%20Statistics.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Python%20Data%20Science%20Toolbox%20pt1/Instructions/Chapter%201%20-%20%20Writing%20Your%20Own%20Functions',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Python%20Data%20Science%20Toolbox%20pt1/Instructions/Chapter%202%20Default%20arguments%2C%20variable-length%20arguments%20and%20scope.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Python%20Data%20Science%20Toolbox%20pt1/Instructions/Chapter%203%20-%20Lambda%20functions%20and%20error-handling.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Python%20Data%20Science%20Toolbox%20pt2/Instructions/Chapter%201Using%20iterators%20in%20PythonLand.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Python%20Data%20Science%20Toolbox%20pt2/Instructions/Chapter%202%20List%20comprehensions%20and%20generators.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Python%20Data%20Science%20Toolbox%20pt2/Instructions/Chapter%203%20Bringing%20it%20all%20together!.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Importing%20Data%20in%20Python%20pt1/Instructions/Chapter%201%20-%20Introduction%20and%20flat%20files.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Importing%20Data%20in%20Python%20pt1/Instructions/Chapter%202%20-%20Importing%20data%20from%20other%20file%20types.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Importing%20Data%20in%20Python%20pt1/Instructions/Chapter%203%20-%20Working%20with%20relational%20databases%20in%20Python.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Importing%20Data%20in%20Python%20pt1/Instructions/Chapter%201%20-%20Introduction%20and%20flat%20files.md', 
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Importing%20Data%20in%20Python%20pt1/Instructions/Chapter%202%20-%20Importing%20data%20from%20other%20file%20types.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Importing%20Data%20in%20Python%20pt1/Instructions/Chapter%203%20-%20Working%20with%20relational%20databases%20in%20Python.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Importing%20Data%20in%20Python%20pt2/Instructions/Chapter%201%20-%20Importing%20data%20from%20the%20Internet.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Importing%20Data%20in%20Python%20pt2/Instructions/Chapter%202%20-%20Interacting%20with%20APIs%20to%20import%20data%20from%20the%20web.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Importing%20Data%20in%20Python%20pt2/Instructions/Chapter%203%20-Diving%20deep%20into%20the%20Twitter%20API.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Cleaning%20Data%20in%20Python/Instructions/Chapter%201%20-%20Exploring%20your%20data.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Cleaning%20Data%20in%20Python/Instructions/Chapter%202%20-%20Tidying%20data%20for%20analysis.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Cleaning%20Data%20in%20Python/Instructions/Chapter%203%20-%20Combining%20data%20for%20analysis.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Cleaning%20Data%20in%20Python/Instructions/Chapter%204%20-%20Cleaning%20data%20for%20analysis.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Pandas%20Foundations/Instructions/Chapter%201%20-%20Data%20ingestion%20%26%20inspection.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Pandas%20Foundations/Instructions/Chapter%202%20-%20Exploratory%20data%20analysis.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Pandas%20Foundations/Instructions/Chapter%203%20-%20Time%20series%20in%20pandas.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Pandas%20Foundations/Instructions/Chapter%204%20-%20Case%20Study%20-%20Sunlight%20in%20Austin.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Manipulating%20DataFrames%20with%20pandas/Instructions/Chapter%201%20-%20Extracting%20and%20transforming%20data.md'
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Manipulating%20DataFrames%20with%20pandas/Instructions/Chapter%202%20-%20Advanced%20indexing.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Manipulating%20DataFrames%20with%20pandas/Instructions/Chapter%203%20-%20Rearranging%20and%20reshaping%20data.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Manipulating%20DataFrames%20with%20pandas/Instructions/Chapter%204%20-%20Grouping%20data.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Manipulating%20DataFrames%20with%20pandas/Instructions/Chapter%205%20-%20Bringing%20it%20all%20together.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Merging%20DataFrames%20with%20pandas/Instructions/Chapter%201%20-%20Preparing%20data.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Merging%20DataFrames%20with%20pandas/Instructions/Chapter%202%20-%20Concatenating%20data.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Merging%20DataFrames%20with%20pandas/Instructions/Chapter%203%20-%20Merging%20data.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Merging%20DataFrames%20with%20pandas/Instructions/Chapter%204%20-%20Case%20Study%20-%20Summer%20Olympics.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Introduction%20to%20Databases%20in%20Python/Instructions/Chapter%201%20-%20Basics%20of%20Relational%20Databases.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Introduction%20to%20Databases%20in%20Python/Instructions/Chapter%202%20-%20Applying%20Filtering%2C%20Ordering%20and%20Grouping%20to%20Queries.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Introduction%20to%20Databases%20in%20Python/Instructions/Chapter%203%20-%20Advanced%20SQLAlchemy%20Queries.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Introduction%20to%20Databases%20in%20Python/Instructions/Chapter%204%20-%20Creating%20and%20Manipulating%20your%20own%20Databases.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Introduction%20to%20Databases%20in%20Python/Instructions/Chapter%205%20-%20Putting%20it%20all%20together.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Introduction%20to%20Data%20Visualizaion%20with%20Python/Instructions/Chapter%201%20-%20Customizing%20plots.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Introduction%20to%20Data%20Visualizaion%20with%20Python/Instructions/Chapter%202%20-%20Plotting%202D%20arrays.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Introduction%20to%20Data%20Visualizaion%20with%20Python/Instructions/Chapter%203%20-%20Statistical%20plots%20with%20Seaborn.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Introduction%20to%20Data%20Visualizaion%20with%20Python/Instructions/Chapter%204%20-%20Analyzing%20time%20series%20and%20images.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Statistical%20Thinking%20in%20Python%20(Part%201)/Instructions/Chapter%201%20-%20Graphical%20exploratory%20data%20analysis.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Statistical%20Thinking%20in%20Python%20(Part%201)/Instructions/Chapter%202%20-%20Quantitative%20exploratory%20data%20analysis.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Statistical%20Thinking%20in%20Python%20(Part%201)/Instructions/Chapter%203%20-%20Thinking%20probabilistically--%20Discrete%20variables.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Statistical%20Thinking%20in%20Python%20(Part%201)/Instructions/Chapter%204%20-%20Thinking%20probabilistically--%20Continuous%20variables.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Statistical%20Thinking%20in%20Python%20(Part%202)/Instructions/Chapter%201%20-%20Parameter%20estimation%20by%20optimization.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Statistical%20Thinking%20in%20Python%20(Part%202)/Instructions/Chapter%202%20-%20Bootstrap%20confidence%20intervals.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Statistical%20Thinking%20in%20Python%20(Part%202)/Instructions/Chapter%203%20-%20Introduction%20to%20hypothesis%20testing.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Statistical%20Thinking%20in%20Python%20(Part%202)/Instructions/Chapter%204%20-%20Hypothesis%20test%20examples.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Supervised%20Learning%20with%20scikit-learn/Instructions/Chapter%201%20-%20Classification.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Supervised%20Learning%20with%20scikit-learn/Instructions/Chapter%202%20-%20Regression.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Supervised%20Learning%20with%20scikit-learn/Instructions/Chapter%203%20Fine-tuning%20your%20model.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Supervised%20Learning%20with%20scikit-learn/Instructions/Chapter%204%20Preprocessing%20and%20pipelines.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Machine%20Learning%20with%20Experts-School%20Budgets/Instructions/Chapter%201%20-%20Exploring%20the%20raw%20data.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Machine%20Learning%20with%20Experts-School%20Budgets/Instructions/Chapter%202%20-%20Creating%20a%20simple%20first%20model.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Machine%20Learning%20with%20Experts-School%20Budgets/Instructions/Chapter%203%20-%20Improving%20your%20model.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Machine%20Learning%20with%20Experts-School%20Budgets/Instructions/Chapter%204%20-%20Learning%20from%20the%20experts.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Unsupervised%20Learning%20in%20Python/Instructions/Chapter%201%20-%20Clustering%20for%20dataset%20exploration.md'
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Unsupervised%20Learning%20in%20Python/Instructions/Chapter%202%20-%20Visualization%20with%20hierarchical%20clustering%20and%20t-SNE.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Unsupervised%20Learning%20in%20Python/Instructions/Chapter%203%20-%20Decorrelating%20your%20data%20and%20dimension%20reduction.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Unsupervised%20Learning%20in%20Python/Instructions/Chapter%204%20-%20Discovering%20interpretable%20features.md'
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Deep%20Learning%20in%20Python/Instructions/Chapter%201%20-%20Basics%20of%20deep%20learning%20and%20neural%20networks.md', 
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Deep%20Learning%20in%20Python/Instructions/Chapter%202%20-%20Optimizing%20a%20neural%20network%20with%20backward%20propagation.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Deep%20Learning%20in%20Python/Instructions/Chapter%203%20-%20Building%20deep%20learning%20models%20with%20keras.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Deep%20Learning%20in%20Python/Instructions/Chapter%204%20-%20Fine-tuning%20keras%20models.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Network%20Analysis%20in%20Python%20(Part%201)/Instructions/Chapter%201%20-%20Introduction%20to%20networks.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Network%20Analysis%20in%20Python%20(Part%201)/Instructions/Chapter%202%20-%20Important%20nodes.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Network%20Analysis%20in%20Python%20(Part%201)/Instructions/Chapter%203%20-%20Structures.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Network%20Analysis%20in%20Python%20(Part%201)/Instructions/Chapter%204%20-%20Bringing%20it%20all%20together.md'
    
    ]

s = Service(r"C:/Users/1948NM/Documents/Information Management/Thesis/Code/chromedriver.exe")

# create an empty dataframe to store the scraped data
df = pd.DataFrame(columns=['text'])

for url in urls:
    driver = webdriver.Chrome(service=s)
    driver.get(url)

    questions = driver.find_elements(By.TAG_NAME, value='p')

    for question in questions:
        # store the url and text content of each element in the dataframe
        df = df.append({'text': question.text}, ignore_index=True)

    driver.quit()

# export the dataframe to a CSV file
df.to_csv('VolgordeFinal.csv', index=False)



