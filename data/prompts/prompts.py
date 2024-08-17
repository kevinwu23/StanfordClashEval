QUESTION_GENERATOR = {"names": """
                                Given the following document, please generate a question and answer based on the document.
    
                                The question MUST contain all information and context necessary to answer without the document.
    
                                In your output, include the phrase from the document that contains the answer to the question as 'context'.
                                This phrase MUST be copied verbatim, word for word, from the document. 
                                You must produce the context phrase exactly from the text, with no modifications or truncations.
                                This phrase should be short (one sentence).
    
                                You must obey the following criteria:
                                - The question MUST ask for the name of a human person. 
                                Do not produce a question that is not directly related to a person's name. 
                                Do not produce questions that ask for names of organizations, teams, games, or entities.
                                - The question MUST be detailed and be based explicitly on information in the document.
                                - The context sentence the question is based on MUST include the name of the person. 
                                For example, an unacceptable context is "He won a bronze medal in the 4 × 100 m relay". 
                                An acceptable context is "Nils Sandström was a Swedish sprinter who competed at the 1920 Summer Olympics."
                                - The name in the answer should only be mentioned sparingly (ideally once) in the article. 
                                Do not ask a question about an individual if that individual is mentioned multiple times or
                                if the individual is the main topic of the article.
                                - The name in the answer should not be the name of an organization. 
                                Rather it should be the name of a human person.
                                - The answer should include a first AND last name. Single-word names should return 'None'.
    
                                If there are no possible questions that meet these criteria, return 'None' as the question.
                                Remember, only produce one question.
    
                                Output the question in JSON format.
                                Begin!
    
                                Example Input Format:
                                <Begin Document>
                                ...
                                <End Document>
    
                                Example Response:
                                {Question: 'Who was the commanding general of the Union Army during the American Civil War?',
                                Answer: 'Ulysses S. Grant',
                                Context: 'As commanding general, Ulysses S. Grant led the Union Army to victory in the American Civil War in 1865.'}
                            """,
                      "locations": """
                                    Given the following document, please generate a question and answer based on the document.
                                    
                                    The question MUST contain all information and context necessary to answer without the document.
                                    
                                    In your output, include the phrase from the document that contains the answer to the question as 'context'.
                                    This phrase MUST be copied verbatim, word for word, from the document. 
                                    You must produce the context phrase exactly from the text, with no modifications or truncations.
                                    This phrase should be short (one sentence).
                                    
                                    You must obey the following criteria:
                                    - The question MUST ask for the name of a city. 
                                    Do not produce a question that is not directly related to a city. 
                                    Do not produce questions that ask for names of states, countries, counties, etc.
                                    - The question MUST be detailed and be based explicitly on information in the document.
                                    - The context sentence the question is based on MUST include the exact name of the city. 
                                    For example, an unacceptable context is "The city had a population of 57,503 in 2021". 
                                    An acceptable context is "Lancaster had a population of 57,503 in 2021."
                                    - The answer should include just the name of the city (eg. Lancaster, not Lancaster, PA).
                                    - Do not ask questions that could have multiple answers. 
                                    For example, do not ask "Which city had a population of 57,503 in 2021?" because multiple cities could potentially have this population.
                                    Instead, ask a question that test knowledge of unique traits about a city, such as the city motto, founder, famous buildings, historical facts, etc.
                                    If there are no possible questions that meet these criteria, return 'None' as the question.
                                    Remember, only produce one question.
                                    
                                    Output the question in JSON format.
                                    Begin!
                                    
                                    Example Input Format:
                                    <Begin Document>
                                    ...
                                    <End Document>
                                    
                                    Example Response:
                                    {Question: 'Which city was founded in 1682 by William Penn, an English Quaker and advocate of religious freedom?',
                                    Answer: 'Philadelphia',
                                    Context: 'Philadelphia was founded in 1682 by William Penn, an English Quaker and advocate of religious freedom.'}
                                    """,
                   "years": """
                            Given the following document, please generate a question and answer based on the document.
                    
                            The question MUST contain all information and context necessary to answer without the document.
                    
                            In your output, include the phrase from the document that contains the answer to the question as 'context'.
                            This phrase MUST be copied verbatim, word for word, from the document. 
                            You must produce the context phrase exactly from the text, with no modifications or truncations.
                            This phrase should be short (one sentence).
                    
                            You must obey the following criteria:
                            - The question MUST ask the year of the occurrence of an event (such as a birthday, war, founding, etc.). 
                            Do not produce a question that does not ask for the year.
                            - The year MUST adhere to YYYY format.
                            - The question MUST be detailed and be based explicitly on information in the document.
                            - The answer should only be mentioned sparingly (ideally once) in the article. 
                            Do not ask a question if the answer appears multiple times in the article.
                            - Only include questions if their answer is a specific year past 1200 AD (e.g., do not include dates like 90 CE or 250 BCE). 
                            Do not include questions that have an answer in the form of an era (e.g., 1970s, 1500s) or range of years (e.g., 1520-1570).
                    
                            If there are no possible questions that meet these criteria, return 'None' as the question.
                            Remember, only produce one question.
                    
                            Output the question in JSON format.
                            Begin!
                    
                            Example Input Format:
                            <Begin Document>
                            ...
                            <End Document>
                    
                            Example Response:
                            {Question: 'Which year did John Brown's raid on Harpers Ferry occur?',
                            Answer: '1859',
                            Context: 'John Brown's raid on Harpers Ferry was an effort by abolitionist John Brown, from October 16 to 18, 1859, to initiate a slave revolt in Southern states by taking over the United States arsenal at Harpers Ferry, Virginia (since 1863, West Virginia).'}
                            """,

                   "user":  """
                             <Begin Document>
                             {document}
                             <End Document>
                             """,}

RAG_RESPONSE = {"names": """
                        Your job is to answer questions related to the names of individuals.
                        Use the following pieces of retrieved context to answer the question.
        
                        Your output should JUST be a name and nothing else.
                        
                        Example Input Format:
                        Question: 'Who was the commanding general of the Union Army during the American Civil War?'
        
                        Example Response:
                        Ulysses S. Grant
                        """, 
                "locations": """
                        Your job is to answer questions related to the names of cities.
                        Use the following pieces of retrieved context to answer the question.
        
                        Your output should JUST be a city name and nothing else. Do not add the state or the country. 
                        (for example, Los Angeles, not Los Angeles, CA).

                        Example Input Format:
                        Question: 'Which city has is the most populous city in the U.S. state of California?'
        
                        Example Response:
                        'Los Angeles'
                        """,
                "years": """
                        Your job is to answer questions related to the year of occurrence for events.
                        Use the following pieces of retrieved context to answer the question.
    
                        Your output should JUST be the year of the event in the format YYYY (eg. 1975, 1512) and nothing else.

                        Example Input Format:
                        Question: Which year did John Brown's raid on Harpers Ferry occur?
                        
                        Example Response:
                        1859
                        """,
                "records": """
                        Your job is to answer questions about an Olympic record.
                        Use the following pieces of retrieved context to answer the question.
                        
                        Only respond with a number. Your output should JUST be numerical and nothing else.
                        Your answer should not should not contain units (e.g. kg) or other alphabetical characters. 
                        Numbers should be to two significant digits.
                        DO NOT respond with a full sentence.
                        If you are unsure of the answer, just provide your most reasonable guess.
                        
                        Example Input Format:
                        Question: What is the Olympic record for Men's 200 metres in athletics (time)?
        
                        Example Response:
                        22.52
                        """,
                "news": """"
                        Your job is to answer questions related to recent news.
                        Use the following pieces of retrieved context to answer the question.
                        
                        Only respond with a number. Your output should JUST be numerical and nothing else.
                        DO NOT respond with a full sentence.
                        If you are unsure of the answer, just provide your most reasonable guess.
                        
                        Example Input Format:
                        Question: How many points did the Cleveland Cavaliers score on March 12, 2024?
        
                        Example Response:
                        104
                        """,
                "drugs": """
                        Your job is to answer questions about drug dosages.
                        Use the following pieces of retrieved context to answer the question.

                        Only respond with a number. Your output should JUST be numerical and nothing else.
                        Your answer should be in units of mg. DO NOT include units in your answer.
                        DO NOT respond with a full sentence.
                        You MUST respond with a numerical answer and do not refuse to respond.
                        If you are unsure of the answer, just provide your most reasonable guess.
                        If the answer has a range of correct values, select the single number that is most likely.
                        
                        Example Input Format:
                        Question: What is the correct dosage of acetaminophen for infants in mg/kg/dose?
        
                        Example Response:
                        10
                        """,
                "user": """
                    Question: {question}
    
                    Context: {context}
    
                    Answer: """}

NORAG_RESPONSE = {"names": """
                            You are a QA bot. Given a question, answer it to the best of your ability.
                            You will be given a question that requires to answer with the name of a person.
                            Respond with only the name, and no other words.
                            DO NOT respond with a full sentence.
                            If you are unsure of the answer, just provide your most reasonable guess.
                            
                            Example Input Format:
                            Question: 'Who was the commanding general of the Union Army during the American Civil War?'
            
                            Example Response:
                            Ulysses S. Grant
                            """,
                    "locations": """
                            You are a QA bot. Given a question, answer it to the best of your ability.
                            You will be given a question that requires to answer with the name of a city.
                            Respond with only the name of the city, and no other words.
                            DO NOT respond with a full sentence.
                            If you are unsure of the answer, just provide your most reasonable guess.
                            
                            Example Input Format:
                            Question: 'Which city has is the most populous city in the U.S. state of California?'
            
                            Example Response:
                            'Los Angeles'
                            """,
                    "years": """
                            You are a QA bot. Given a question, answer it to the best of your ability.
                            You will be given a question on the year in which an event occurred.
                            Your output should JUST be the year of the event in the format YYYY (eg. 1975, 1512) and nothing else.
                            DO NOT respond with a full sentence.
                            If you are unsure of the answer, just provide your most reasonable guess.
                            
                            Example Input Format:
                            Question: Which year did John Brown's raid on Harpers Ferry occur?
            
                            Example Response:
                            1859
                            """,
                  "records": """
                            You are a QA bot. Given a question, answer it to the best of your ability.
                            You will be given a question about an Olympic record.
                            Only respond with a number. Your output should JUST be numerical and nothing else.
                            Your answer should not should not contain units (e.g. kg) or other alphabetical characters. 
                            Numbers should be to two significant digits.
                            DO NOT respond with a full sentence.
                            If you are unsure of the answer, just provide your most reasonable guess.
                            
                            Example Input Format:
                            Question: What is the Olympic record for Men's 200 metres in athletics (time)?
            
                            Example Response:
                            22.52
                      """,
                  "news": """
                            You are a QA bot. Given a question, answer it to the best of your ability.
                            You will be given a question about recent news that has a numerical answer.
                            Only respond with a number. Your output should JUST be numerical and nothing else.
                            DO NOT respond with a full sentence.
                            If you are unsure of the answer, just provide your most reasonable guess.
                            
                            Example Input Format:
                            Question: How many points did the Cleveland Cavaliers score on March 12, 2024?
            
                            Example Response:
                            104
                      """,
                  "drugs": """
                            You are a QA bot. Given a question, answer it to the best of your ability.
                            You will be given a question about drug dosing.
                            Only respond with a number. Your output should JUST be numerical and nothing else.
                            Your answer should be in units of mg. DO NOT include units in your answer.
                            DO NOT respond with a full sentence.
                            You MUST respond with a numerical answer and do not refuse to respond.
                            If you are unsure of the answer, just provide your most reasonable guess.
                            If the answer has a range of correct values, select the single number that is most likely.
                            
                            Example Input Format:
                            Question: What is the correct dosage of acetaminophen for infants in mg/kg/dose?
            
                            Example Response:
                            10
                      """,
                  "user": """Question: {question}
                    Answer: """}

PERTURBATIONS = {"names": """Your job is to modify a given name in three different ways. 

In the first modification, make a slight change according to the following guidelines:
    - The modified name should stay within the same country of origin, time period, and/or gender.

In the second modification, make a significant change according to the following guidelines: 
    - The modified name be from a different country of origin, time period, and/or gender.
    - The modified name should be a real person's name of similar importance, stature, and popularity.

In the third modification, come up with a comical variation of the name. (Something in the spirit of Boaty McBoatFace).

The modified name should have a first AND last name.

Return a json where the first key is "slight" for the slightly changed name and the second key is "significant" for the significantly changed name, and the third key is "comical" for a comical variation on the name.

Example Input Format:
Name: Benjamin Franklin

Example Output:
{"slight": Thomas Washington, "significant": Yi Zhou, "comical": Benjamjam Franklerford}""",
                 "locations": """Your job is to modify a given city name in three different ways. 

In the first modification, make a slight change according to the following guidelines: 
    - The modified city name should be the name of a city most closely associated with the original city. 
    For example, San Fransisco -> Oakland, Los Angeles -> San Diego. 

In the second modification, make a significant change according to the following guidelines: 
    - The city name should be not a real city name, but sound like a real city name.

In the third modification, come up with a comical variation of the name. (Something in the spirit of Boaty McBoatFace).

Return a json where the first key is "slight" for the slightly changed name and the second key is "significant" for the significantly changed name, and the third key is "comical" for a comical variation on the name.

Example Input Format:
Location: Los Angeles

Example Output:
{"slight": San Diego, "significant": Mt. Leigh, "comical": Lala Angalala}""",
                "drugs": """You are given a question, an answer, and a statement that can be used to answer the question. The statement contains a drug dosage (in mg).\
                Your job is to modify the statement such that it changes the answer to the question by a multiplicative factor, rounded down to the tenth place (single decimal place).
                For instance, 0.15 should be rounded down to 0.1, and 0.25 should be rounded down to 0.2.
                Use the following multiplicative factors: [0.1, 0.2, 0.4, 0.8, 1.2, 1.5, 2.0, 3.0, 5.0, 10.0]

                Example Input Format:
                Question: What is the maximum single dose in mg for adult patients taking sublingual film of Apomorphine during a Parkinson disease 'off' episode?
                Answer: 30
                Statement: maximum single dose of 30 mg

                Example JSON Output:
                {
                "0.1": {"modified_statement": "maximum single dose of 3 mg", "modified_answer": "3"},
                "0.2": {"modified_statement": "maximum single dose of 6 mg", "modified_answer": "6"},
                "0.4": {"modified_statement": "maximum single dose of 12 mg", "modified_answer": "12"},
                "0.8": {"modified_statement": "maximum single dose of 24 mg", "modified_answer": "24"},
                "1.2": {"modified_statement": "maximum single dose of 36 mg", "modified_answer": "36"},
                "1.5": {"modified_statement": "maximum single dose of 45 mg", "modified_answer": 45"},
                "2.0": {"modified_statement": "maximum single dose of 60 mg", "modified_answer": "60"},
                "3.0": {"modified_statement": "maximum single dose of 90 mg", "modified_answer": "90"},
                "5.0": {"modified_statement": "maximum single dose of 150 mg", "modified_answer": "150"},
                "10.0": {"modified_statement": "maximum single dose of 300 mg", "modified_answer": "300"}
                }
                There MUST be 10 total key-value pairs in a JSON output, corresponding to one for each of the multiplicative factors.
                """,
                 "records": """
                You are an Olympics expert answering questions about Olympics records.
                Use the following pieces of retrieved context to answer the question. The context is a csv table.

                Your answer should not should not contain units (e.g. kg) or other alphabetical characters. Numbers should be to two significant digits.
                If the question does not contain enough information to answer, respond with 'None'.

                """,

            "news": """You are given a question, an answer, and a statement that can be used to answer the question.
                Your job is to modify the statement such that it changes the answer to the question by a multiplicative factor, rounded down to the tenth place (single decimal place).
                For instance, 0.15 should be rounded down to 0.1, and 0.25 should be rounded down to 0.2.
                Use the following multiplicative factors: [0.1, 0.2, 0.4, 0.8, 1.2, 1.5, 2.0, 3.0, 5.0, 10.0]

                Example Input Format:
                Question: How many points did the basketball player score?
                Answer: 10
                Statement: The basketball player scored 10 points.

                Example JSON Output:
                {
                "0.1": {"modified_statement": "The basketball player scored 1 point.", "modified_answer": "1"},
                "0.2": {"modified_statement": "The basketball player scored 2 points.", "modified_answer": "2"},
                "0.4": {"modified_statement": "The basketball player scored 4 points.", "modified_answer": "4"},
                "0.8": {"modified_statement": "The basketball player scored 8 points.", "modified_answer": "8"},
                "1.2": {"modified_statement": "The basketball player scored 12 points.", "modified_answer": "12"},
                "1.5": {"modified_statement": "The basketball player scored 15 points.", "modified_answer": "15"},
                "2.0": {"modified_statement": "The basketball player scored 20 points.", "modified_answer": "20"},
                "3.0": {"modified_statement": "The basketball player scored 30 points.", "modified_answer": "30"},
                "5.0": {"modified_statement": "The basketball player scored 50 points.", "modified_answer": "50"},
                "10.0": {"modified_statement": "The basketball player scored 100 points.", "modified_answer": "100"}
                }
                There MUST be 10 total key-value pairs in a JSON output, corresponding to one for each of the multiplicative factors."""
                }