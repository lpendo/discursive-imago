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

# PracticesL = ( "●Compelling", "●Knowing", "●Unvieling", "●●Ruling", 
#               "●●Shielding", "●●Veiling", "●●●Fraying", "●●●Perfecting", 
#               "●●●Weaving","●●●●Patterning", "●●●●Unraveling", "●●●●●Making", 
#               "●●●●●Unmaking" )
# Practices = st.selectbox("Which practice?",PracticesL)


# RankL = ( "Initiate(●)", "Apprentice(●●)", "Disciple(●●●)", "Adept(●●●●)",
#          "Master(●●●●●)" )
# Rank = st.selectbox("What rank?",RankL)


# st.write("Path:", MagePath)
# st.write("Arcana:", Arcana)

st.write("Effect:", Effects)

if Effects == EffectsL[0]:
    DamageKind = ("Bashing", "Lethal", "Aggravated")
    st.selectbox("Damage type?", DamageKind)