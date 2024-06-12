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