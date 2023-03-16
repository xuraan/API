from deta import Deta

from helper.constants import DEV_KEY

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


# driver

avatars = deta.Drive("avatars")
demos = deta.Drive("demos")
