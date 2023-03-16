from deta import Deta

DEV_KEY = "b0lyegbralh_q6Uvw4eVUMhMgRNUKNRHDwRrnTFbP9C4"

deta = Deta(DEV_KEY)

en_versions = deta.Base("en_versions")
fr_versions = deta.Base("fr_versions")
ar_versions = deta.Base("ar_versions")

en_features = deta.Base("en_features")
fr_features = deta.Base("fr_features")
ar_features = deta.Base("ar_features")

en_questions = deta.Base("en_questions")
fr_questions = deta.Base("fr_questions")
ar_questions = deta.Base("ar_questions")

en_answers = deta.Base("en_answers")
fr_answers = deta.Base("fr_answers")
ar_answers = deta.Base("ar_answers")

locals = deta.Base("locals")
localized_strings_dict = deta.Base("localizedStringsDict")
contributors = deta.Base("contributors")

import random

first_names = ['Adam', 'Ben', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hannah', 'Isabelle', 'John', 'Kate', 'Liam', 'Mia', 'Nathan', 'Olivia', 'Peter', 'Quinn', 'Rachel', 'Samantha', 'Tyler']
last_names = ['Anderson', 'Baker', 'Carter', 'Davis', 'Evans', 'Ford', 'Garcia', 'Hernandez', 'Jackson', 'Khan', 'Lee', 'Martinez', 'Nguyen', 'Patel', 'Reyes', 'Smith', 'Taylor', 'Walker', 'Xu', 'Young']

for i in range(20):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    full_name = f"{first_name} {last_name}"

    contributors.put(
        {
            "key": f'34567{i}',
            "name": full_name,
            "src": "https://picsum.photos/200/300",
            "url": "https://github.com/afrcvn"
        }
    )