


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

# create a list of URLs to scrape
urls = [
        'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Cleaning%20Data%20in%20Python/Chapter%201%20-Exploring%20your%20data.py',
        'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Cleaning%20Data%20in%20Python/Chapter%202%20-%20Tidying%20data%20for%20analysis.py',
        'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Cleaning%20Data%20in%20Python/Chapter%203%20-%20Combining%20data%20for%20analysis.py',
        'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Cleaning%20Data%20in%20Python/Chapter%204%20-%20Cleaning%20data%20for%20analysis.py',
        'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Deep%20Learning%20in%20Python/Chapter%201%20-Basics%20of%20deep%20learning%20and%20neural%20networks.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Deep%20Learning%20in%20Python/Chapter%202%20-Optimizing%20a%20neural%20network%20with%20backward%20propagation.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Deep%20Learning%20in%20Python/Chapter%203%20-Building%20deep%20learning%20models%20with%20keras.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Deep%20Learning%20in%20Python/Chapter%204%20-%20Fine-tuning%20keras%20models.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Importing%20Data%20in%20Python%20pt1/Chapter%201%20-%20Introduction%20and%20flat%20files.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Importing%20Data%20in%20Python%20pt1/Chapter%202%20-%20Importing%20data%20from%20other%20file%20types.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Importing%20Data%20in%20Python%20pt1/Chapter%203%20-%20Working%20with%20relational%20databases%20in%20Python.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Importing%20Data%20in%20Python%20pt2/Chapter%201%20-%20Importing%20data%20from%20the%20Internet.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Importing%20Data%20in%20Python%20pt2/Chapter%202%20-%20Interacting%20with%20APIs%20to%20import%20data%20from%20the%20web.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Importing%20Data%20in%20Python%20pt2/Chapter%203%20-%20Diving%20deep%20into%20the%20Twitter%20API.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Interactive%20Data%20Visualization%20with%20Bokeh/Chapter%201%20-%20Basic%20plotting%20with%20Bokeh.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Interactive%20Data%20Visualization%20with%20Bokeh/Chapter%202%20-%20Layouts%2C%20Interactions%2C%20and%20Annotations.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Interactive%20Data%20Visualization%20with%20Bokeh/Chapter%203%20-Building%20interactive%20apps%20with%20Bokeh.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Interactive%20Data%20Visualization%20with%20Bokeh/Chapter%204%20-Putting%20It%20All%20Together!%20A%20Case%20Study.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Intermediate%20Python%20for%20Data%20Science/Chapter%201-Matplotlib.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Intermediate%20Python%20for%20Data%20Science/Chapter%202%20-%20Dictionaries%20%26%20Pandas.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Intermediate%20Python%20for%20Data%20Science/Chapter%203%20-%20Logic%2C%20Control%20Flow%20and%20Filtering.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Intermediate%20Python%20for%20Data%20Science/Chapter%204-Loops.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Intermediate%20Python%20for%20Data%20Science/Chapter%205%20-%20Case%20Study%20Hacker%20Statistics.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Intro%20to%20Python%20for%20Data%20Science/Python%20Lists%20-%20Chapter1.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Intro%20to%20Python%20for%20Data%20Science/Python%20Basics%20-%20Chapter2.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Intro%20to%20Python%20for%20Data%20Science/Chapter%203%20-%20Functions%20and%20Packages%20.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Intro%20to%20Python%20for%20Data%20Science/NumPy%20-%20Chapter%204.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Introduction%20to%20Data%20Visualizaion%20with%20Python/Chapter%201%20-Customizing%20plots.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Introduction%20to%20Data%20Visualizaion%20with%20Python/Chapter%202%20-%20Plotting%202D%20arrays.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Introduction%20to%20Data%20Visualizaion%20with%20Python/Chapter%203%20-%20Statistical%20plots%20with%20Seaborn.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Introduction%20to%20Data%20Visualizaion%20with%20Python/Chapter%204%20-Analyzing%20time%20series%20and%20images.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Machine%20Learning%20with%20Experts-School%20Budgets/Chapter%201%20-%20Exploring%20the%20raw%20data.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Machine%20Learning%20with%20Experts-School%20Budgets/Chapter%202%20-%20Exploring%20the%20raw%20data.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Machine%20Learning%20with%20Experts-School%20Budgets/Chapter%203%20-%20Improving%20your%20model.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Machine%20Learning%20with%20Experts-School%20Budgets/Chapter%204%20-%20Learning%20from%20the%20experts.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Merging%20DataFrames%20with%20pandas/Chapter%201%20-%20Preparing%20data.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Merging%20DataFrames%20with%20pandas/Chapter%202%20-%20Concatenating%20data.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Merging%20DataFrames%20with%20pandas/Chapter%203%20-%20Merging%20data.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Merging%20DataFrames%20with%20pandas/Chapter%204%20-%20Case%20Study%20-%20Summer%20Olympics.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Natural%20Language%20Processing%20Fundamentals%20in%20Python/Chapter%201%20-%20Regular%20expressions%20%26%20word%20tokenization.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Natural%20Language%20Processing%20Fundamentals%20in%20Python/Chapter%202%20-Simple%20topic%20identification.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Natural%20Language%20Processing%20Fundamentals%20in%20Python/Chapter%203%20-Named-entity%20recognition.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Natural%20Language%20Processing%20Fundamentals%20in%20Python/Chapter%204%20-%20Building%20a%20%20fake%20news%20classifier.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Network%20Analysis%20in%20Python%20(Part%201)/Chapter%201%20-%20Introduction%20to%20networks.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Network%20Analysis%20in%20Python%20(Part%201)/Chapter%202%20-%20Important%20nodes.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Network%20Analysis%20in%20Python%20(Part%201)/Chapter%203%20-%20Structures.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Network%20Analysis%20in%20Python%20(Part%201)/Chapter%204%20-%20Bringing%20it%20all%20together.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Pandas%20Foundations/Chapter%201%20-%20Data%20ingestion%20%26%20inspection.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Pandas%20Foundations/Chapter%202%20-%20Exploratory%20data%20analysis.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Pandas%20Foundations/Chapter%203%20-%20Time%20series%20in%20pandas.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Pandas%20Foundations/Chapter%204%20-Case%20Study%20-%20Sunlight%20in%20Austin.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Python%20Data%20Science%20Toolbox%20pt1/Chapter%201%20-%20Writing%20your%20own%20functions.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Python%20Data%20Science%20Toolbox%20pt1/Chapter%202%20-%20Default%20arguments%2C%20variable-length%20arguments%20and%20scope.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Python%20Data%20Science%20Toolbox%20pt1/Chapter%203-%20Lambda%20functions%20and%20error-handling.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Python%20Data%20Science%20Toolbox%20pt2/Chapter%201%20-Using%20iterators%20in%20PythonLand.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Python%20Data%20Science%20Toolbox%20pt2/Chapter%202%20-List%20comprehensions%20and%20generators.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Python%20Data%20Science%20Toolbox%20pt2/Chapter%203%20-%20Bringing%20it%20all%20together!.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Statistical%20Thinking%20in%20Python%20(Part%202)/Chapter%201%20-%20Parameter%20estimation%20by%20optimization.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Statistical%20Thinking%20in%20Python%20(Part%202)/Chapter%202%20-%20Bootstrap%20confidence%20intervals.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Statistical%20Thinking%20in%20Python%20(Part%202)/Chapter%203%20-Introduction%20to%20hypothesis%20testing.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Statistical%20Thinking%20in%20Python%20(Part%202)/Chapter%204%20-Hypothesis%20test%20examples.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Statistical%20Thinking%20in%20Python%20(Part%202)/Chapter%205%20-%20Putting%20it%20all%20together%20-%20a%20case%20study.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Python%20Data%20Science%20Toolbox%20pt1/Chapter%201%20-%20Writing%20your%20own%20functions.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Python%20Data%20Science%20Toolbox%20pt1/Chapter%202%20-%20Default%20arguments%2C%20variable-length%20arguments%20and%20scope.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Python%20Data%20Science%20Toolbox%20pt1/Chapter%203-%20Lambda%20functions%20and%20error-handling.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Supervised%20Learning%20with%20scikit-learn/Chapter%201%20-%20Classification.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Supervised%20Learning%20with%20scikit-learn/Chapter%202%20-%20Regression.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Supervised%20Learning%20with%20scikit-learn/Chapter%203%20-%20Fine-tuning%20your%20model.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Supervised%20Learning%20with%20scikit-learn/Chapter%204%20-%20Preprocessing%20and%20pipelines.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Unsupervised%20Learning%20in%20Python/Chapter%201%20-%20Clustering%20for%20dataset%20exploration.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Unsupervised%20Learning%20in%20Python/Chapter%202%20-%20Visualization%20with%20hierarchical%20clustering%20and%20t-SNE.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Unsupervised%20Learning%20in%20Python/Chapter%203%20-%20Decorrelating%20your%20data%20and%20dimension%20reduction.py',
'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Unsupervised%20Learning%20in%20Python/Chapter%204%20-%20Discovering%20interpretable%20features.py'

    
        ]

s = Service(r"C:/Users/1948NM/Documents/Information Management/Thesis/Code/chromedriver.exe")

# create an empty dataframe to store the scraped data
df = pd.DataFrame(columns=['answer'])

for url in urls:
    driver = webdriver.Chrome(service=s)
    driver.get(url)

    questions = driver.find_elements(By.TAG_NAME, value='tr')

    for answer in questions:
        # store the url and text content of each element in the dataframe
        df = df.append({'answer': answer.text}, ignore_index=True)

    driver.quit()

# export the dataframe to a CSV file
df.to_csv('VolgordeAntwoordenVersieFinal4.csv', index=False)



