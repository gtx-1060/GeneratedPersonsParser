from person_data import PersonData as pd

settings = {
    "OUTPUT_PATH" : "YOUR_OUTPUT_PATH",
    "API_KEY" : "YOUR_KEY_WHICH_YOU_CAN_GET_ON_THEIR_SITE"
}

persons_filter = {
    "AGE" : pd.Age.YOUNG,
    "SEX" : pd.Sex.UNDEFINED,
    "ETHNICITY" : pd.Ethnicity.UNDEFINED,
    "FACE" : pd.Face.UNDEFINED,
    "EMOUTION" : pd.Emoution.JOY,
    "HAIR" : pd.Hair.UNDEFINED
}
