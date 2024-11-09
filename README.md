# HDBSCAN-LLMs
#install streamlit and depedencies

#Run streamlit app on localhost

~streamlit run .\cluster_euproject.py

Harnessing the Power of Large Language Models and Traditional Machine Learning: A Hybrid Approach for Next-Gen AI Solutions
It's super cool to have a GenAI solution for your organization but is GenAI solely the best solution? 

In the world of AI, it’s tempting to default to Generative AI (GenAI) as the go-to approach. But is it truly the optimal solution for every scenario? To make informed, effective, and cost-efficient design choices, we need to understand the strengths and limitations of Large Language Models (LLMs) to ensure they’re delivering genuine business value.

LLM Strengths: Large Language Models bring powerful capabilities to the table, particularly in areas where natural language understanding is critical. Key strengths include:

Content Generation: Capable of creating coherent, high-quality text for a wide range of applications, from marketing copy to conversational agents.
Context Understanding and Summarization: LLMs can interpret and distill meaning from complex text, making them useful for summarization and classification tasks.
Semantic Classification: Effective in grouping related concepts, labeling content, and categorizing documents based on nuanced language similarities.
Conversational Context Retention: Good at maintaining conversational flow and context over shorter sessions, enhancing user engagement in chat and support applications.

LLM Limitations: While LLMs offer impressive capabilities, they also come with certain limitations that may impact their effectiveness for specific use cases:

Processing Latency: Although parallel processing is possible, API requests for LLMs can still introduce significant delays, particularly at scale.
Non-Deterministic Responses: LLMs can produce varied results for the same input, which may be unsuitable for applications requiring consistency.
Opaque Logic (Black-Box Nature): LLMs lack interpretability, often failing to provide confidence scores or explanations for their responses, making them harder to trust in critical decision-making contexts.
Token Limitations and Data Distribution Awareness: With token constraints, LLMs cannot process extensive datasets in a single request, nor do they inherently understand the underlying distribution of data.
Limited Real-Time Adaptability: LLMs struggle with evolving information or real-time clustering, as they process requests independently without awareness of ongoing trends or patterns in the data.
Cost Limitation of LLMs: LLMs can be expensive to use, especially at scale. The cost per token may seem low, but with large datasets or frequent usage, these expenses quickly add up, making it challenging to maintain cost-efficiency, particularly for businesses with budget constraints or high data volume requirements.

A Real-world Use Case: LLM Limitations in Dynamic Text Clustering Needs

LLMs may not be ideal for tasks that involve dynamic text clustering, such as Call Center Logs analysis where we do not know the number of clusters in advance. For example, analyzing a few years call logs data (over 300,000 transcripts annually) to identify emerging issues using real time filters (e.g. within a specific timeframe) is challenging due to the following:

Response Latency: Processing a large volume of transcripts can be slow with LLM APIs, especially if near-instantaneous results are needed.
Inconsistent Clustering: LLMs generate clusters independently with each request, leading to inconsistent or redundant cluster names as there’s no connection between numerous consecutive calls.
Lack of Data Distribution Awareness: Without an understanding of data distribution, LLMs struggle to create meaningful, consistent clusters over time.

A Hybrid Approach: Combining LLMs with Traditional ML for Optimal Results 

Given these limitations, combining LLMs with traditional machine learning methods (e.g. HDBSCAN) can offer a more robust solution. 

Without HDBSCAN and parallel processing

Using LLMs to analyze 36,000 transcripts (about one month of data) would take approximately 36,000 seconds (~10 hours). At an average transcript length of 100 tokens using GPT-4o, this process would cost around $10 per run.

Without LLMs, how will HDBSCAN clusters look like?

As public Call Center Logs data is not available, for demo purpose, I have built a Streamlit app analyzing European project open data (http://data.europa.eu/88u/dataset/eu-results-projects).


HDBSCAN with dynamic clustering.
Setting specific filters, 3 dynamic clusters based on a few thousands of records are generated in just a couple of seconds and with Zero API request cost. But what is missing from here? We only have frequent keywords in each clusters and will need data scientists to interpret the results before communicate to business managers!!!

Yes, your thinking is correct, this is when LLMs can help and is proved to be very efficient. Here you go with simple Prompting:

I have a text clustering output from European projects with popular terms and frequencies below, give me the Cluster name or topic in one sentence with less than 10 words.
This is the output with LLMs as cluster interpreter:

HDBSCAN clusters with LLM as cluster intepreter.
Now we can automatically generate summary for the detected clusters:

![image](https://github.com/user-attachments/assets/7f2dd07b-857d-4905-9592-64accadfdcda)


European project for strong, sustainable local development.
European project encourages farmers to innovate and strengthen environmentally friendly practices.
