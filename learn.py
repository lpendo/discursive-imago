import streamlit as st

# MagePath = st.selectbox(
#     "What is your Path?",
#     ("Acanthus", "Moros", "Mastigos", "Obrimos", "Thyrsus"),
#     placeholder="Path?"
# )


# Arcana = st.selectbox(
#     "Arcana of spell?",
#     ("Death", "Fate", "Forces", "Life", "Matter", "Mind", "Prime",
#      "Space", "Spirit", "Time"),
#     placeholder="Arcana?" 
# )


EffectsL = ( "Inflict Damage", "Perform Healing", "Impose a Condition/Tilt",
            "Provide a Bonus/Penalty to a Trait", "Add a dice poll efffect", 
            "Protect something", "Hide something" )
Effects = st.selectbox("What is your spell going to do?",EffectsL)

PracticesL = (
    ( "●Compelling", "●Knowing", "●Unvieling", ),
    ( "●●Ruling", "●●Shielding", "●●Veiling", ),
    ( "●●●Fraying", "●●●Perfecting", "●●●Weaving", ),
    ("●●●●Patterning", "●●●●Unraveling", ),
    ("●●●●●Making", "●●●●●Unmaking" ),
)
# Practice = st.selectbox("Which practice?",PracticesL)


# RankL = ( "Initiate(●)", "Apprentice(●●)", "Disciple(●●●)", "Adept(●●●●)",
#          "Master(●●●●●)" )
# Rank = st.selectbox("What rank?",RankL)


# st.write("Path:", MagePath)
# st.write("Arcana:", Arcana)

if Effects == EffectsL[0]:
    DamageKind = ("Bashing", "Lethal", "Aggravated")
    DamageType = st.selectbox("Damage type?", DamageKind)

    if DamageType == DamageKind[0]:
        Practice = PracticesL[2][0]
    if DamageType == DamageKind[1]:
        Practice = PracticesL[3][1]
    if DamageType == DamageKind[2]:
        Practice = PracticesL[4][1]

    

st.write("Effect:", Effects)
st.write("Effect:", Practice)